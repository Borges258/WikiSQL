#!/usr/bin/env python3
"""WikiSQL zero-shot baseline using an OpenAI-compatible Responses API."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import random
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROMPT_VERSION = "wikisql-zero-shot-python-v1"
AGG_OPS = ("", "MAX", "MIN", "COUNT", "SUM", "AVG")
COND_OPS = ("=", ">", "<", "OP")
SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["sel", "agg", "conds"],
    "properties": {
        "sel": {"type": "integer", "minimum": 0},
        "agg": {"type": "integer", "minimum": 0, "maximum": 5},
        "conds": {
            "type": "array",
            "items": {
                "type": "array",
                "minItems": 3,
                "maxItems": 3,
                "prefixItems": [
                    {"type": "integer", "minimum": 0},
                    {"type": "integer", "minimum": 0, "maximum": 3},
                    {"type": ["string", "number"]},
                ],
                # Required by the configured OpenAI-compatible gateway.
                "items": {"type": ["integer", "string", "number"]},
            },
        },
    },
}
SYSTEM_PROMPT = "\n".join(
    [
        "Translate one WikiSQL question into canonical WikiSQL SQL JSON.",
        "Return only an object with keys sel, agg, conds.",
        "sel is the zero-based selected column index.",
        "agg: 0=NONE, 1=MAX, 2=MIN, 3=COUNT, 4=SUM, 5=AVG.",
        "Each condition is [zero-based column index, integer operator, value].",
        "Integer operator: 0='=', 1='>', 2='<', 3='OP'. Never output an operator symbol.",
        "Use only the question and table. Preserve condition values. Do not explain.",
    ]
)


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def limit_value(text: str) -> int | None:
    if text.lower() == "all":
        return None
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("limit must be positive or 'all'")
    return value


def arguments() -> argparse.Namespace:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="WikiSQL zero-shot baseline; defaults to 5 Dev rows")
    parser.add_argument("--split", choices=("dev", "test"), default="dev")
    parser.add_argument("--limit", type=limit_value, default=5, metavar="N|all")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--concurrency", type=int, default=3)
    parser.add_argument("--max-retries", type=int, default=5)
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--data-dir", type=Path, default=root.parent / "data")
    parser.add_argument("--env-file", type=Path, default=root.parents[2] / ".env")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-existing-errors", action="store_true")
    parser.add_argument("--allow-full-run", action="store_true")
    args = parser.parse_args()
    if args.offset < 0 or args.concurrency < 1 or args.max_retries < 0 or args.timeout <= 0:
        parser.error("offset/concurrency/retries/timeout values are invalid")
    if args.limit is None and not args.allow_full_run:
        parser.error("full run locked: add --allow-full-run only after explicit approval")
    if args.output_dir is None:
        suffix = "full" if args.limit is None else f"sample_{args.offset}_{args.limit}"
        args.output_dir = root / "results" / f"{args.split}_{suffix}_python"
    for name in ("output_dir", "data_dir", "env_file"):
        setattr(args, name, getattr(args, name).resolve())
    return args


def load_env(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip()
        if len(value) > 1 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        result[key.strip().lower()] = value
    for key in ("base_url", "api_key", "model"):
        if not result.get(key):
            raise ValueError(f"Missing {key} in {path}")
    return result


def endpoint(base_url: str) -> str:
    url = base_url.rstrip("/")
    if url.lower().endswith("/responses"):
        return url
    return f"{url}/responses" if url.lower().endswith("/v1") else f"{url}/v1/responses"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as stream:
        for line_no, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL {path}:{line_no}: {exc}") from exc
    return rows


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def object_hash(value: Any) -> str:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()


def build_request(model: str, example: dict[str, Any], table: dict[str, Any]) -> dict[str, Any]:
    types = table.get("types") or [None] * len(table["header"])
    table_data = {
        "id": table["id"],
        "page_title": table.get("page_title"),
        "section_title": table.get("section_title"),
        "caption": table.get("caption"),
        "columns": [
            {"index": i, "name": name, "type": types[i]}
            for i, name in enumerate(table["header"])
        ],
        "rows": table["rows"],
    }
    user_text = (
        f"Question:\n{example['question']}\n\nTable (JSON):\n"
        + json.dumps(table_data, ensure_ascii=False, separators=(",", ":"))
    )
    return {
        "model": model,
        "reasoning": {"effort": "none"},
        "input": [
            {"role": "system", "content": [{"type": "input_text", "text": SYSTEM_PROMPT}]},
            {"role": "user", "content": [{"type": "input_text", "text": user_text}]},
        ],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "wikisql_sql",
                "strict": True,
                "schema": SCHEMA,
            }
        },
        "max_output_tokens": 512,
    }


def output_text(response: dict[str, Any]) -> str:
    if isinstance(response.get("output_text"), str):
        return response["output_text"]
    chunks = []
    for item in response.get("output", []):
        for content in item.get("content", []):
            if content.get("type") in ("output_text", "text") and isinstance(content.get("text"), str):
                chunks.append(content["text"])
    return "".join(chunks)


def parse_prediction(text: str) -> dict[str, Any]:
    candidate = text.strip()
    match = re.fullmatch(r"```(?:json)?\s*([\s\S]*?)\s*```", candidate, re.I)
    if match:
        candidate = match.group(1)
    value = json.loads(candidate)
    if not isinstance(value, dict):
        raise ValueError("prediction must be a JSON object")
    return value


def integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def validate_sql(sql: Any, columns: int) -> tuple[bool, list[str]]:
    errors = []
    if not isinstance(sql, dict):
        return False, ["SQL must be an object"]
    if not integer(sql.get("sel")) or not 0 <= sql["sel"] < columns:
        errors.append("invalid sel")
    if not integer(sql.get("agg")) or not 0 <= sql["agg"] < len(AGG_OPS):
        errors.append("invalid agg")
    if not isinstance(sql.get("conds"), list):
        errors.append("invalid conds")
    else:
        for index, cond in enumerate(sql["conds"]):
            if not isinstance(cond, list) or len(cond) != 3:
                errors.append(f"conds[{index}] must contain three values")
                continue
            if not integer(cond[0]) or not 0 <= cond[0] < columns:
                errors.append(f"invalid conds[{index}] column")
            if not integer(cond[1]) or not 0 <= cond[1] < len(COND_OPS):
                errors.append(f"invalid conds[{index}] operator")
            if isinstance(cond[2], bool) or not isinstance(cond[2], (str, int, float)):
                errors.append(f"invalid conds[{index}] value")
    return not errors, errors


def normalized_condition(cond: list[Any]) -> str:
    return json.dumps([cond[0], cond[1], str(cond[2]).lower()], ensure_ascii=False)


def lf_equal(pred: dict[str, Any], gold: dict[str, Any]) -> bool:
    return (
        pred.get("sel") == gold.get("sel")
        and pred.get("agg") == gold.get("agg")
        and {normalized_condition(x) for x in pred.get("conds", [])}
        == {normalized_condition(x) for x in gold.get("conds", [])}
    )


def wiki_number(value: Any) -> int | float:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value
    text = str(value).strip().replace(",", "")
    try:
        number = float(text)
    except ValueError:
        match = re.search(r"[-+]?\d*\.?\d+", text)
        if not match:
            raise ValueError(f"Cannot parse numeric value {value!r}")
        number = float(match.group())
    return int(number) if number.is_integer() else number


class WikiSqlEngine:
    def __init__(self, db_path: Path):
        self.db = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
        self.cache: dict[str, list[str]] = {}

    @staticmethod
    def table_name(table_id: str) -> str:
        return table_id if table_id.startswith("table") else "table_" + table_id.replace("-", "_")

    @staticmethod
    def quote(value: str) -> str:
        return '"' + value.replace('"', '""') + '"'

    def schema(self, table_id: str) -> list[str]:
        name = self.table_name(table_id)
        if name not in self.cache:
            rows = self.db.execute(f"PRAGMA table_info({self.quote(name)})").fetchall()
            if not rows:
                raise ValueError(f"missing database table {name}")
            self.cache[name] = [str(row[2]).lower() for row in rows]
        return self.cache[name]

    def execute(self, table_id: str, sql: dict[str, Any]) -> list[Any]:
        schema = self.schema(table_id)
        valid, errors = validate_sql(sql, len(schema))
        if not valid:
            raise ValueError("; ".join(errors))
        agg = AGG_OPS[sql["agg"]]
        column = f"col{sql['sel']}"
        selection = f"{agg}({column})" if agg else column
        clauses, values = [], []
        for col, op, raw in sql["conds"]:
            operator = COND_OPS[op]
            if operator == "OP":
                raise ValueError("operator 3 is not executable")
            value = wiki_number(raw) if schema[col] == "real" else str(raw).lower()
            clauses.append(f"col{col} {operator} ?")
            values.append(value)
        where = " WHERE " + " AND ".join(clauses) if clauses else ""
        name = self.quote(self.table_name(table_id))
        return [row[0] for row in self.db.execute(f"SELECT {selection} FROM {name}{where}", values)]

    def close(self) -> None:
        self.db.close()


class ApiError(Exception):
    def __init__(self, message: str, status: int | None = None, body: Any = None):
        super().__init__(message)
        self.status, self.body, self.attempts = status, body, []


def decode(raw: bytes) -> Any:
    text = raw.decode("utf-8", errors="replace")
    try:
        return json.loads(text) if text else {}
    except json.JSONDecodeError:
        return {"unparsed_body": text}


def retryable(error: ApiError) -> bool:
    if error.status is None or error.status in (408, 409, 429, 500, 502, 503, 504):
        return True
    detail = error.body.get("error", {}) if isinstance(error.body, dict) else {}
    return error.status == 400 and detail.get("message") == "Upstream request failed"


def api_call(url: str, key: str, body: dict[str, Any], timeout: float, retries: int):
    encoded = json.dumps(body, ensure_ascii=False).encode()
    attempts = []
    for attempt in range(retries + 1):
        started = time.perf_counter()
        try:
            request = urllib.request.Request(
                url, data=encoded, method="POST",
                headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                result = decode(response.read())
                latency = round((time.perf_counter() - started) * 1000)
                attempts.append({"attempt": attempt + 1, "status": response.status, "latency_ms": latency})
                return result, attempts, sum(x["latency_ms"] for x in attempts)
        except urllib.error.HTTPError as exc:
            latency = round((time.perf_counter() - started) * 1000)
            error = ApiError(f"HTTP {exc.code}", exc.code, decode(exc.read()))
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            latency = round((time.perf_counter() - started) * 1000)
            error = ApiError(f"request failed: {exc}")
        attempts.append({
            "attempt": attempt + 1, "status": error.status, "latency_ms": latency,
            "error": str(error), "response_body": error.body,
        })
        if attempt >= retries or not retryable(error):
            error.attempts = attempts
            raise error
        time.sleep(min(30, 2**attempt) + random.random() * 0.4)
    raise RuntimeError("unreachable")


def usage(response: Any) -> dict[str, Any]:
    data = response.get("usage", {}) if isinstance(response, dict) else {}
    return {
        "input_tokens": data.get("input_tokens", data.get("prompt_tokens")),
        "output_tokens": data.get("output_tokens", data.get("completion_tokens")),
        "total_tokens": data.get("total_tokens"),
        "input_tokens_details": data.get("input_tokens_details"),
        "output_tokens_details": data.get("output_tokens_details"),
    }


def process(item: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    example, table = item["example"], item["table"]
    request = build_request(config["model"], example, table)
    base = {
        "example_id": item["id"], "split": config["split"], "index": item["index"],
        "table_id": example["table_id"], "question": example["question"],
        "gold_sql": example["sql"], "prompt_version": PROMPT_VERSION,
        "request": {"model": request["model"], "reasoning": request["reasoning"]},
        "recorded_at": now(),
    }
    try:
        response, attempts, latency = api_call(
            config["url"], config["key"], request, config["timeout"], config["retries"]
        )
        text = output_text(response)
        prediction, parse_error = None, None
        try:
            prediction = parse_prediction(text)
        except Exception as exc:
            parse_error = str(exc)
        valid, errors = validate_sql(prediction, len(table["header"]))
        return {
            **base, "api_success": True, "response_id": response.get("id"),
            "raw_response": response, "output_text": text, "prediction_sql": prediction,
            "parse_error": parse_error, "structural_valid": valid, "validation_errors": errors,
            "usage": usage(response), "latency_ms": latency, "attempts": attempts, "error": None,
        }
    except Exception as exc:
        body = getattr(exc, "body", None)
        attempts = getattr(exc, "attempts", [])
        return {
            **base, "api_success": False, "raw_response": body, "output_text": None,
            "prediction_sql": None, "parse_error": None, "structural_valid": False,
            "validation_errors": [], "usage": usage(body),
            "latency_ms": sum(x.get("latency_ms", 0) for x in attempts) or None,
            "attempts": attempts,
            "error": {"type": type(exc).__name__, "message": str(exc),
                      "status": getattr(exc, "status", None), "response_body": body},
        }


def latest_records(path: Path) -> dict[str, dict[str, Any]]:
    return {row["example_id"]: row for row in read_jsonl(path)} if path.exists() else {}


def write_json(path: Path, value: Any) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def append_record(path: Path, value: Any) -> None:
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


def evaluate(selected, latest, engine, output_dir: Path, split: str) -> dict[str, Any]:
    rows, predictions = [], []
    for item in selected:
        record = latest.get(item["id"], {
            "example_id": item["id"], "api_success": False, "prediction_sql": None,
            "structural_valid": False, "usage": {}, "error": {"message": "missing result"},
        })
        example = item["example"]
        gold_result = engine.execute(example["table_id"], example["sql"])
        pred_result, execution_error = None, None
        if record.get("prediction_sql") is not None and record.get("structural_valid"):
            try:
                pred_result = engine.execute(example["table_id"], record["prediction_sql"])
            except Exception as exc:
                execution_error = str(exc)
        lf = bool(record.get("structural_valid") and lf_equal(record["prediction_sql"], example["sql"]))
        ex = pred_result is not None and pred_result == gold_result
        rows.append({**record, "lf_correct": lf, "ex_correct": ex,
                     "executable": pred_result is not None, "execution_error": execution_error})
        predictions.append(
            {"query": record["prediction_sql"]} if record.get("structural_valid")
            else {"error": (record.get("error") or {}).get("message") or record.get("parse_error")}
        )
    for name, data in (("evaluated.jsonl", rows), ("predictions.jsonl", predictions)):
        (output_dir / name).write_text(
            "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in data), encoding="utf-8"
        )
    total = len(rows)
    count = lambda key: sum(bool(row.get(key)) for row in rows)
    token_sum = lambda key: sum(
        row.get("usage", {}).get(key) or 0 for row in rows
    ) if any(row.get("usage", {}).get(key) is not None for row in rows) else None
    latencies = sorted(row["latency_ms"] for row in rows if isinstance(row.get("latency_ms"), (int, float)))
    percentile = lambda p: latencies[min(len(latencies) - 1, max(0, int(len(latencies) * p + .999) - 1))] if latencies else None
    summary = {
        "metric_standard": "Salesforce WikiSQL-compatible LF and denotation execution comparison",
        "split": split, "total": total, "completed": len(rows),
        "api_success_count": count("api_success"),
        "parse_success_count": sum(row.get("prediction_sql") is not None for row in rows),
        "structural_valid_count": count("structural_valid"),
        "executable_count": count("executable"),
        "logical_form_correct_count": count("lf_correct"),
        "execution_correct_count": count("ex_correct"),
        "api_success_rate": count("api_success") / total,
        "parse_success_rate": sum(row.get("prediction_sql") is not None for row in rows) / total,
        "structural_sql_validity": count("structural_valid") / total,
        "sql_validity": count("executable") / total,
        "logical_form_accuracy": count("lf_correct") / total,
        "execution_accuracy": count("ex_correct") / total,
        "usage": {key: token_sum(key) for key in ("input_tokens", "output_tokens", "total_tokens")},
        "latency_ms": {"mean": sum(latencies) / len(latencies) if latencies else None,
                       "p50": percentile(.5), "p95": percentile(.95),
                       "max": latencies[-1] if latencies else None},
        "generated_at": now(),
    }
    write_json(output_dir / "metrics.json", summary)
    (output_dir / "metrics.md").write_text(
        "# WikiSQL zero-shot results\n\n"
        f"- Split: {split}\n- Evaluated: {total}\n- Model: see manifest.json\n"
        f"- Logical Form Accuracy: {summary['logical_form_accuracy']:.6f} "
        f"({summary['logical_form_correct_count']}/{total})\n"
        f"- Execution Accuracy: {summary['execution_accuracy']:.6f} "
        f"({summary['execution_correct_count']}/{total})\n"
        f"- SQL Validity: {summary['sql_validity']:.6f} ({summary['executable_count']}/{total})\n"
        f"- Structural SQL Validity: {summary['structural_sql_validity']:.6f} "
        f"({summary['structural_valid_count']}/{total})\n",
        encoding="utf-8",
    )
    return summary


def main() -> int:
    args, env = arguments(), None
    env = load_env(args.env_file)
    paths = {kind: args.data_dir / f"{args.split}.{suffix}" for kind, suffix in (
        ("questions", "jsonl"), ("tables", "tables.jsonl"), ("database", "db")
    )}
    for path in paths.values():
        if not path.exists():
            raise FileNotFoundError(path)
    questions = read_jsonl(paths["questions"])
    tables = {table["id"]: table for table in read_jsonl(paths["tables"])}
    if args.offset >= len(questions):
        raise ValueError("offset exceeds split size")
    end = len(questions) if args.limit is None else min(len(questions), args.offset + args.limit)
    selected = []
    for index in range(args.offset, end):
        example = questions[index]
        table = tables.get(example["table_id"])
        if table is None:
            raise ValueError(f"missing table {example['table_id']}")
        selected.append({"index": index, "example": example, "table": table,
                         "id": f"{args.split}:{index}:{example['table_id']}"})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result_path = args.output_dir / "responses.jsonl"
    manifest = {
        "experiment": "WikiSQL Zero-shot Baseline", "implementation": "Python standard library",
        "prompt_version": PROMPT_VERSION,
        "prompt_sha256": object_hash({"system": SYSTEM_PROMPT, "schema": SCHEMA}),
        "model": env["model"], "api_format": "OpenAI Responses API",
        "reasoning": {"effort": "none"}, "structured_output": SCHEMA, "zero_shot": True,
        "split": args.split, "split_size": len(questions), "offset": args.offset,
        "limit": args.limit, "selected_count": len(selected), "concurrency": args.concurrency,
        "max_retries": args.max_retries, "timeout_seconds": args.timeout,
        "endpoint": endpoint(env["base_url"]),
        "data_files": {name: {"path": str(path), "sha256": file_hash(path)} for name, path in paths.items()},
        "runtime": {"python": sys.version, "executable": sys.executable, "platform": sys.platform},
        "created_at": now(),
    }
    manifest_path = args.output_dir / "manifest.json"
    if manifest_path.exists():
        old = json.loads(manifest_path.read_text(encoding="utf-8"))
        for key in ("prompt_sha256", "model", "split", "offset", "limit", "selected_count"):
            if old.get(key) != manifest.get(key):
                raise ValueError(f"resume configuration mismatch for {key}")
        manifest["created_at"], manifest["resumed_at"] = old["created_at"], now()
    write_json(manifest_path, manifest)
    engine = WikiSqlEngine(paths["database"])
    try:
        for item in selected:
            engine.execute(item["example"]["table_id"], item["example"]["sql"])
        print(f"Validated {len(selected)} {args.split} examples, tables, gold SQL, and SQLite database.")
        print(f"Model: {env['model']}; reasoning.effort=none; Python: {sys.version.split()[0]}")
        print(f"Output: {args.output_dir}")
        if args.dry_run:
            print("Dry run complete. No API requests were sent.")
            return 0
        latest = latest_records(result_path)
        pending = [item for item in selected if item["id"] not in latest or
                   (not latest[item["id"]].get("api_success") and not args.skip_existing_errors)]
        print(f"Resume state: {len(selected) - len(pending)} skipped, {len(pending)} pending.")
        config = {"model": env["model"], "key": env["api_key"], "url": endpoint(env["base_url"]),
                  "split": args.split, "timeout": args.timeout, "retries": args.max_retries}
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
            futures = {pool.submit(process, item, config): item for item in pending}
            for done, future in enumerate(concurrent.futures.as_completed(futures), 1):
                record = future.result()
                append_record(result_path, record)
                print(f"[{done}/{len(pending)}] index={record['index']} "
                      f"{'ok' if record['api_success'] else 'error'}", flush=True)
        summary = evaluate(selected, latest_records(result_path), engine, args.output_dir, args.split)
        print(json.dumps({key: summary[key] for key in
                          ("logical_form_accuracy", "execution_accuracy", "sql_validity")}, indent=2))
        print(f"total_tokens: {summary['usage']['total_tokens']}")
        return 0
    finally:
        engine.close()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Interrupted; completed records remain resumable.", file=sys.stderr)
        raise SystemExit(130)
    except Exception as error:
        print(f"{type(error).__name__}: {error}", file=sys.stderr)
        raise SystemExit(1)
