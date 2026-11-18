#!/usr/bin/env python3
"""WikiSQL modern LLM baseline: E1/E2/E3/E4 with dynamic 5-shot retrieval."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import math
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import run_experiment as base


EXPERIMENTS = {
    "E1": {"few_shot": 0, "thinking": False, "effort": "none"},
    "E2": {"few_shot": 0, "thinking": True, "effort": "high"},
    "E3": {"few_shot": 5, "thinking": False, "effort": "none"},
    "E4": {"few_shot": 5, "thinking": True, "effort": "high"},
}
PROMPT_VERSION = "wikisql-modern-schema-aware-v3-lossless-shots"
INPUT_PRICE_PER_MILLION = 4.0
OUTPUT_PRICE_PER_MILLION = 20.0
TOKEN_RE = re.compile(r"[a-z0-9]+")
STOPWORDS = {
    "a", "an", "and", "are", "at", "be", "by", "did", "do", "for", "from",
    "how", "in", "is", "it", "of", "on", "or", "the", "that", "to", "was", "what",
    "which", "who", "with", "would",
}


def tokens(text: str) -> list[str]:
    return [token for token in TOKEN_RE.findall(str(text).lower()) if token not in STOPWORDS]


def question_structure(question: str) -> tuple[str, int]:
    q = question.lower()
    if re.search(r"\bhow many\b|\bnumber of\b|\bcount\b", q):
        agg = "COUNT"
    elif re.search(r"\bhighest\b|\bmaximum\b|max\b", q):
        agg = "MAX"
    elif re.search(r"\blowest\b|\bminimum\b|min\b", q):
        agg = "MIN"
    elif re.search(r"\btotal\b|\bsum\b", q):
        agg = "SUM"
    elif re.search(r"\baverage\b|\bmean\b", q):
        agg = "AVG"
    else:
        agg = ""
    conjunctions = len(re.findall(r"\band\b|\balso\b", q))
    condition_hint = conjunctions + (1 if re.search(r"\b(where|whose|that|with|for|in|from|number|year)\b", q) else 0)
    return agg, condition_hint


class TrainRetriever:
    """Deterministic lexical + question-structure retriever over Train only."""

    def __init__(self, train: list[dict[str, Any]], tables: dict[str, dict[str, Any]]):
        self.items: list[dict[str, Any]] = []
        self.postings: dict[str, list[int]] = defaultdict(list)
        self.df: Counter[str] = Counter()
        for index, example in enumerate(train):
            table = tables[example["table_id"]]
            text = example["question"] + " " + " ".join(table["header"])
            term_set = set(tokens(text))
            item = {
                "index": index,
                "example": example,
                "table": table,
                "tokens": Counter(tokens(text)),
                "terms": term_set,
                "agg": base.AGG_OPS[example["sql"].get("agg", 0)],
                "cond_count": len(example["sql"].get("conds", [])),
            }
            self.items.append(item)
            for term in term_set:
                self.postings[term].append(index)
                self.df[term] += 1
        self.doc_count = max(1, len(self.items))
        self.norms = [self._norm(item["tokens"]) for item in self.items]

    def _idf(self, term: str) -> float:
        return math.log((self.doc_count + 1) / (self.df.get(term, 0) + 1)) + 1.0

    def _norm(self, counts: Counter[str]) -> float:
        return math.sqrt(sum((count * self._idf(term)) ** 2 for term, count in counts.items())) or 1.0

    def retrieve(self, question: str, table: dict[str, Any], k: int = 5) -> list[dict[str, Any]]:
        query_counts = Counter(tokens(question + " " + " ".join(table["header"])))
        query_terms = set(query_counts)
        candidate_ids: set[int] = set()
        for term in query_terms:
            candidate_ids.update(self.postings.get(term, []))
        if not candidate_ids:
            candidate_ids = set(range(len(self.items)))
        query_norm = self._norm(query_counts)
        target_agg, target_conds = question_structure(question)
        target_headers = set(tokens(" ".join(table["header"])))
        scored = []
        for index in candidate_ids:
            item = self.items[index]
            dot = sum(
                query_counts[term] * item["tokens"].get(term, 0) * self._idf(term) ** 2
                for term in query_terms
            )
            lexical = dot / (query_norm * self.norms[index])
            structure = 0.5 * (1.0 if item["agg"] == target_agg else 0.0)
            structure += 0.5 * (1.0 / (1.0 + abs(item["cond_count"] - target_conds)))
            header_overlap = len(target_headers & set(tokens(" ".join(item["table"]["header"])))) / max(1, len(target_headers))
            score = 0.65 * lexical + 0.25 * structure + 0.10 * header_overlap
            scored.append((score, -item["index"], item))
        scored.sort(reverse=True, key=lambda value: (value[0], value[1]))
        selected = []
        for rank, (score, _, item) in enumerate(scored[:k], 1):
            selected.append({
                "train_index": item["index"],
                "example_id": f"train:{item['index']}:{item['example']['table_id']}",
                "score": round(score, 8),
                "rank": rank,
                "question": item["example"]["question"],
                "table_id": item["example"]["table_id"],
                "sql": item["example"]["sql"],
            })
        return selected


def compact_table(table: dict[str, Any], max_rows: int | None, columns: list[int] | None = None) -> str:
    """Compact table encoding; target tables are lossless, shot rows are projected to used columns."""
    selected = list(range(len(table["header"]))) if columns is None else columns
    types = table.get("types") or [None] * len(table["header"])
    headers = [[index, table["header"][index], types[index]] for index in selected]
    source_rows = table["rows"] if max_rows is None else table["rows"][:max_rows]
    rows = [[row[index] for index in selected] for row in source_rows]
    result: dict[str, Any] = {"C": headers, "R": rows}
    if max_rows is not None and len(table["rows"]) > max_rows:
        result["TRUNCATED_ROWS"] = len(table["rows"]) - max_rows
    return json.dumps(result, ensure_ascii=False, separators=(",", ":"))


def build_prompt(
    example: dict[str, Any], table: dict[str, Any], retrieved: list[dict[str, Any]],
    train_tables: dict[str, dict[str, Any]], config: dict[str, Any], example_max_rows: int | None,
) -> tuple[str, str]:
    schema_guide = "\n".join([
        "You are solving WikiSQL Text-to-SQL with schema-aware reasoning.",
        "Internally perform these checks: understand the question; match requested fields to column indices; identify aggregation; identify every WHERE condition and operator; then validate the JSON.",
        "Do not reveal chain-of-thought. Return only the final JSON object.",
        "sel is zero-based selected column index. agg: 0=NONE, 1=MAX, 2=MIN, 3=COUNT, 4=SUM, 5=AVG.",
        "Each cond is [zero-based column index, integer operator, value]. Operator: 0='=', 1='>', 2='<', 3='OP'.",
        "Use integer operators, not symbols. Preserve values from the table/question.",
    ])
    shots = []
    for shot in retrieved:
        shot_example = next(item for item in train_tables[shot["table_id"]]["examples"] if item["index"] == shot["train_index"])
        shot_table = train_tables[shot["table_id"]]["table"]
        sql = shot_example["example"]["sql"]
        relevant_columns = sorted({sql["sel"], *[condition[0] for condition in sql.get("conds", [])]})
        shots.append({
            "retrieval_rank": shot["rank"],
            "retrieval_score": shot["score"],
            "question": shot_example["example"]["question"],
            "table": compact_table(shot_table, example_max_rows, relevant_columns),
            "sql": sql,
        })
    dynamic_examples = ""
    if shots:
        dynamic_examples = "\nRetrieved WikiSQL training demonstrations (use as guidance, not as new facts):\n"
        for index, shot in enumerate(shots, 1):
            dynamic_examples += f"\nExample {index}:\n{json.dumps(shot, ensure_ascii=False, separators=(',', ':'))}\n"
    user = (
        dynamic_examples + "\nTarget question:\n" + example["question"] + "\n\nTarget table (compact lossless JSON; C=[original_index,header,type], R=rows):\n" +
        compact_table(table, None)
    )
    return schema_guide, user


def make_request(model: str, system: str, user: str, effort: str, cache_key: str, cache_enabled: bool = True) -> dict[str, Any]:
    request = {
        "model": model,
        "reasoning": {"effort": effort},
        "input": [
            {"role": "developer", "content": [{"type": "input_text", "text": system}]},
            {"role": "user", "content": [{"type": "input_text", "text": user}]},
        ],
        "text": {"format": {"type": "json_schema", "name": "wikisql_sql", "strict": True, "schema": base.SCHEMA}},
        "max_output_tokens": 384 if effort == "high" else 256,
    }
    if cache_enabled:
        request["prompt_cache_key"] = cache_key
        request["prompt_cache_options"] = {"mode": "implicit", "ttl": "30m"}
    return request


def process_item(item: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    cfg = context["experiment_config"]
    retrieved = context["retriever"].retrieve(item["example"]["question"], item["table"], cfg["few_shot"])
    system, user = build_prompt(
        item["example"], item["table"], retrieved, context["train_tables"], cfg,
        context["example_max_rows"],
    )
    request = make_request(context["model"], system, user, cfg["effort"], context["cache_key"], context["cache_enabled"])
    base_record = {
        "example_id": item["example_id"], "split": context["split"], "experiment": context["experiment"],
        "index": item["index"], "table_id": item["example"]["table_id"],
        "question": item["example"]["question"], "gold_sql": item["example"]["sql"],
        "prompt_version": PROMPT_VERSION, "few_shot": cfg["few_shot"],
        "thinking": cfg["thinking"], "reasoning_effort": cfg["effort"],
        "retrieved_examples": retrieved, "request": {"model": context["model"], "reasoning": request["reasoning"], "max_output_tokens": request["max_output_tokens"], "prompt_cache_key": request.get("prompt_cache_key")},
        "recorded_at": base.now(),
    }
    try:
        response, attempts, latency = base.api_call(
            context["url"], context["key"], request, context["timeout"], context["retries"]
        )
        text = base.output_text(response)
        if response.get("status") == "incomplete" or not text.strip():
            fallback_request = dict(request)
            fallback_request["max_output_tokens"] = 768
            response2, attempts2, latency2 = base.api_call(
                context["url"], context["key"], fallback_request, context["timeout"], context["retries"]
            )
            response, attempts, latency = response2, attempts + attempts2, latency + latency2
            text = base.output_text(response)
        prediction, parse_error = None, None
        try:
            prediction = base.parse_prediction(text)
        except Exception as exc:
            parse_error = str(exc)
        structural_valid, validation_errors = base.validate_sql(prediction, len(item["table"]["header"]))
        return {**base_record, "api_success": True, "raw_response": response, "response_id": response.get("id"),
                "output_text": text, "prediction_sql": prediction, "json_valid": prediction is not None,
                "parse_error": parse_error, "structural_valid": structural_valid,
                "validation_errors": validation_errors, "usage": base.usage(response),
                "latency_ms": latency, "attempts": attempts, "error": None}
    except Exception as exc:
        body = getattr(exc, "body", None)
        attempts = getattr(exc, "attempts", [])
        return {**base_record, "api_success": False, "raw_response": body, "response_id": None,
                "output_text": None, "prediction_sql": None, "json_valid": False,
                "parse_error": None, "structural_valid": False, "validation_errors": [],
                "usage": base.usage(body), "latency_ms": sum(x.get("latency_ms", 0) for x in attempts) or None,
                "attempts": attempts, "error": {"type": type(exc).__name__, "message": str(exc),
                                                  "status": getattr(exc, "status", None), "response_body": body}}


def evaluate(records: list[dict[str, Any]], selected: list[dict[str, Any]], engine: base.WikiSqlEngine, out_dir: Path, experiment: str) -> dict[str, Any]:
    evaluated, predictions = [], []
    for item, record in zip(selected, records):
        gold = engine.execute(item["example"]["table_id"], item["example"]["sql"])
        pred_result, execution_error = None, None
        if record.get("structural_valid"):
            try:
                pred_result = engine.execute(item["example"]["table_id"], record["prediction_sql"])
            except Exception as exc:
                execution_error = str(exc)
        lf = bool(record.get("structural_valid") and base.lf_equal(record["prediction_sql"], item["example"]["sql"]))
        ex = pred_result is not None and pred_result == gold
        evaluated.append({**record, "lf_correct": lf, "ex_correct": ex, "executable": pred_result is not None, "execution_error": execution_error})
        predictions.append({"query": record["prediction_sql"]} if record.get("structural_valid") else {"error": (record.get("error") or {}).get("message") or record.get("parse_error")})
    (out_dir / "evaluated.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in evaluated), encoding="utf-8")
    (out_dir / "predictions.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in predictions), encoding="utf-8")
    total = len(evaluated)
    count = lambda key: sum(bool(row.get(key)) for row in evaluated)
    valid_json = count("json_valid")
    valid_sql = count("structural_valid")
    executable = count("executable")
    execution_success_rate = executable / valid_sql if valid_sql else 0.0
    latencies = sorted(x["latency_ms"] for x in evaluated if isinstance(x.get("latency_ms"), (int, float)))
    usage = {key: sum(x.get("usage", {}).get(key) or 0 for x in evaluated) for key in ("input_tokens", "output_tokens", "total_tokens")}
    usage["cached_input_tokens"] = sum((x.get("usage", {}).get("input_tokens_details") or {}).get("cached_tokens") or 0 for x in evaluated)
    usage["cache_write_tokens"] = sum((x.get("usage", {}).get("input_tokens_details") or {}).get("cache_write_tokens") or 0 for x in evaluated)
    if not any(x.get("usage", {}).get("total_tokens") is not None for x in evaluated):
        usage = {key: None for key in usage}
    def pct(p):
        return latencies[min(len(latencies) - 1, max(0, math.ceil(len(latencies) * p) - 1))] if latencies else None
    semantic_samples = [{"example_id": x["example_id"], "question": x["question"], "prediction_sql": x.get("prediction_sql"), "gold_sql": x["gold_sql"], "manual_label": None} for x in evaluated[: min(20, len(evaluated))]]
    (out_dir / "semantic_samples.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in semantic_samples), encoding="utf-8")
    error_rows = [x for x in evaluated if not x.get("ex_correct")]
    (out_dir / "error_cases.md").write_text("# Error cases\n\n" + "\n".join(
        f"## {x['example_id']}\n\n- Question: {x['question']}\n- Gold: `{json.dumps(x['gold_sql'], ensure_ascii=False)}`\n- Prediction: `{json.dumps(x.get('prediction_sql'), ensure_ascii=False)}`\n- Error: {x.get('execution_error') or x.get('parse_error') or (x.get('error') or {}).get('message') or 'logical-form mismatch'}\n" for x in error_rows
    ), encoding="utf-8")
    summary = {
        "experiment": experiment, "total": total, "api_success_count": count("api_success"),
        "json_validity_count": valid_json, "sql_validity_count": valid_sql, "execution_success_count": executable,
        "logical_form_correct_count": count("lf_correct"), "execution_correct_count": count("ex_correct"),
        "api_success_rate": count("api_success") / total, "json_validity": valid_json / total,
        "sql_validity": valid_sql / total, "execution_success_rate": execution_success_rate,
        "logical_form_accuracy": count("lf_correct") / total, "execution_accuracy": count("ex_correct") / total,
        "semantic_accuracy": None, "usage": usage,
        "estimated_api_cost_usd": ((max(0, (usage["input_tokens"] or 0) - (usage["cached_input_tokens"] or 0)) / 1_000_000 * INPUT_PRICE_PER_MILLION) + ((usage["cached_input_tokens"] or 0) / 1_000_000 * INPUT_PRICE_PER_MILLION * 0.5) + ((usage["output_tokens"] or 0) / 1_000_000 * OUTPUT_PRICE_PER_MILLION)) if usage["input_tokens"] is not None and usage["output_tokens"] is not None else None,
        "latency_ms": {"mean": sum(latencies) / len(latencies) if latencies else None, "p50": pct(.5), "p95": pct(.95), "max": latencies[-1] if latencies else None},
        "generated_at": base.now(),
    }
    base.write_json(out_dir / "metrics.json", summary)
    (out_dir / "metrics.md").write_text("# Modern WikiSQL baseline\n\n" + "\n".join(f"- {key}: {value}" for key, value in summary.items() if key not in ("usage", "latency_ms")) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="WikiSQL E1/E2/E3/E4 modern baseline")
    parser.add_argument("--experiment", choices=[*EXPERIMENTS, "all"], default="E4")
    parser.add_argument("--split", choices=("dev", "test"), default="dev")
    parser.add_argument("--limit", type=base.limit_value, default=2, metavar="N|all")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=180.0)
    parser.add_argument(
        "--run-root",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results" / "formal_test",
    )
    parser.add_argument("--env-file", type=Path, default=Path(__file__).resolve().parent.parents[2] / ".env")
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent.parent / "data")
    parser.add_argument("--example-max-rows", type=base.limit_value, default=None, metavar="N|all", help="Optional shot-row cap; default all rows to preserve semantics")
    parser.add_argument("--ablation-limit", type=int, default=1000, help="Test examples per E1-E3 when --limit all")
    parser.add_argument("--allow-full-run", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-existing-errors", action="store_true")
    parser.add_argument("--disable-prompt-cache", action="store_true")
    args = parser.parse_args()
    if args.limit is None and not args.allow_full_run:
        parser.error("full run locked: add --allow-full-run after approval")
    if (args.example_max_rows is not None and args.example_max_rows < 1) or args.ablation_limit < 1:
        parser.error("example-max-rows and ablation-limit must be positive")
    env = base.load_env(args.env_file.resolve())
    data_dir = args.data_dir.resolve()
    paths = {split: data_dir / f"{split}.jsonl" for split in ("train", "dev", "test")}
    table_paths = {split: data_dir / f"{split}.tables.jsonl" for split in ("train", "dev", "test")}
    db_path = data_dir / f"{args.split}.db"
    for path in (*paths.values(), *table_paths.values(), db_path):
        if not path.exists():
            raise FileNotFoundError(path)
    train = base.read_jsonl(paths["train"])
    train_tables_raw = {x["id"]: x for x in base.read_jsonl(table_paths["train"])}
    target_examples = base.read_jsonl(paths[args.split])
    target_tables = {x["id"]: x for x in base.read_jsonl(table_paths[args.split])}
    end = len(target_examples) if args.limit is None else min(len(target_examples), args.offset + args.limit)
    if args.offset >= len(target_examples):
        raise ValueError("offset exceeds split size")
    selected = [{"index": i, "example": target_examples[i], "table": target_tables[target_examples[i]["table_id"]], "example_id": f"{args.split}:{i}:{target_examples[i]['table_id']}"} for i in range(args.offset, end)]
    train_tables: dict[str, dict[str, Any]] = {}
    grouped = defaultdict(list)
    for i, example in enumerate(train):
        grouped[example["table_id"]].append({"index": i, "example": example})
    for table_id, table in train_tables_raw.items():
        train_tables[table_id] = {"table": table, "examples": grouped[table_id]}
    retriever = TrainRetriever(train, train_tables_raw)
    prompt_hash = base.object_hash({"version": PROMPT_VERSION, "experiments": EXPERIMENTS, "schema": base.SCHEMA, "system": "fixed-developer-prefix-v2-dynamic-user-demos", "example_max_rows": args.example_max_rows, "cache": not args.disable_prompt_cache})
    run_root = args.run_root.resolve()
    run_root.mkdir(parents=True, exist_ok=True)
    freeze_path = run_root / "prompt_freeze.json"
    freeze = {"prompt_version": PROMPT_VERSION, "prompt_hash": prompt_hash, "created_at": base.now(), "retrieval": "question lexical cosine + heuristic SQL structure + header overlap", "train_only": True, "example_max_rows": args.example_max_rows, "lossless_target_table": True, "shot_rows_projected_to_sql_columns": True, "prompt_cache": not args.disable_prompt_cache}
    if freeze_path.exists():
        old = json.loads(freeze_path.read_text(encoding="utf-8"))
        if old.get("prompt_hash") != prompt_hash:
            raise ValueError("Prompt freeze hash mismatch; do not mix prompt versions")
    elif args.split == "test":
        raise ValueError("Test requires a frozen Prompt from a completed Dev run")
    else:
        base.write_json(freeze_path, freeze)
    experiments = list(EXPERIMENTS) if args.experiment == "all" else [args.experiment]
    summaries = []
    for experiment in experiments:
        cfg = EXPERIMENTS[experiment]
        experiment_selected = selected
        if args.split == "test" and args.limit is None and experiment != "E4":
            experiment_selected = selected[: args.ablation_limit]
        out_dir = run_root / args.split / experiment
        out_dir.mkdir(parents=True, exist_ok=True)
        manifest = {"experiment": experiment, "split": args.split, "model": env["model"], "thinking": cfg["thinking"], "reasoning_effort": cfg["effort"], "few_shot": cfg["few_shot"], "retrieval_source": "train", "prompt_freeze": str(freeze_path), "prompt_hash": prompt_hash, "selected_count": len(experiment_selected), "offset": args.offset, "limit": args.limit if experiment == "E4" or args.limit is not None else args.ablation_limit, "ablation": experiment != "E4" and args.split == "test" and args.limit is None, "prompt_cache_enabled": not args.disable_prompt_cache, "data_sha256": {"train": base.file_hash(paths["train"]), "target": base.file_hash(paths[args.split])}, "created_at": base.now()}
        base.write_json(out_dir / "manifest.json", manifest)
        engine = base.WikiSqlEngine(db_path)
        try:
            for item in experiment_selected:
                engine.execute(item["example"]["table_id"], item["example"]["sql"])
            result_path = out_dir / "responses.jsonl"
            existing = base.latest_records(result_path)
            pending = [x for x in experiment_selected if x["example_id"] not in existing or (not existing[x["example_id"]].get("api_success") and not args.skip_existing_errors)]
            print(f"{experiment}: validated {len(experiment_selected)} {args.split}; skipped={len(experiment_selected)-len(pending)} pending={len(pending)}")
            if not args.dry_run:
                context = {"experiment": experiment, "experiment_config": cfg, "retriever": retriever, "train_tables": train_tables, "example_max_rows": args.example_max_rows, "model": env["model"], "url": base.endpoint(env["base_url"]), "key": env["api_key"], "split": args.split, "timeout": args.timeout, "retries": args.max_retries, "cache_key": f"wikisql-modern:{env['model']}:{experiment}:{prompt_hash}", "cache_enabled": not args.disable_prompt_cache}
                with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
                    futures = {pool.submit(process_item, item, context): item for item in pending}
                    for done, future in enumerate(concurrent.futures.as_completed(futures), 1):
                        record = future.result()
                        base.append_record(result_path, record)
                        print(f"{experiment} [{done}/{len(pending)}] index={record['index']} {'ok' if record['api_success'] else 'error'}", flush=True)
                records = base.latest_records(result_path)
                ordered = [records[x["example_id"]] for x in experiment_selected]
                summaries.append(evaluate(ordered, experiment_selected, engine, out_dir, experiment))
        finally:
            engine.close()
    if summaries:
        comparison = run_root / args.split / "comparison.json"
        base.write_json(comparison, {"split": args.split, "experiments": summaries, "generated_at": base.now()})
        lines = [f"# WikiSQL modern baseline comparison ({args.split})\n", "\n| Experiment | Few-shot | Thinking | LFA | EX | SQL Validity | JSON Validity | Exec Success | Cost USD |\n|---|---:|:---:|---:|---:|---:|---:|---:|---:|\n"]
        for row in summaries:
            cfg = EXPERIMENTS[row["experiment"]]
            lines.append(f"| {row['experiment']} | {cfg['few_shot']} | {'On' if cfg['thinking'] else 'Off'} | {row['logical_form_accuracy']:.4f} | {row['execution_accuracy']:.4f} | {row['sql_validity']:.4f} | {row['json_validity']:.4f} | {row['execution_success_rate']:.4f} | {row['estimated_api_cost_usd']} |\n")
        (run_root / args.split / "comparison.md").write_text("".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(1)
