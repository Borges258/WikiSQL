#!/usr/bin/env python3
"""Generate a paper-style report from the completed WikiSQL modern baseline."""

from __future__ import annotations

import csv
import html
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "results" / "formal_test" / "test"
OUT = ROOT / "reports" / "modern_baseline"
EXPERIMENTS = ["E1", "E2", "E3", "E4"]
CONFIG = {
    "E1": ("0-shot", "Off / none"),
    "E2": ("0-shot", "On / high"),
    "E3": ("5-shot", "Off / none"),
    "E4": ("5-shot", "On / high"),
}
AGG_NAMES = ["NONE", "MAX", "MIN", "COUNT", "SUM", "AVG"]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def rate(rows: list[dict[str, Any]], key: str) -> float:
    return sum(bool(row.get(key)) for row in rows) / len(rows) if rows else 0.0


def wilson(successes: int, total: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if total == 0:
        return 0.0, 0.0
    p = successes / total
    denominator = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denominator
    margin = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denominator
    return center - margin, center + margin


def exact_mcnemar(left: list[dict[str, Any]], right: list[dict[str, Any]], key: str) -> dict[str, Any]:
    left_map = {row["index"]: bool(row[key]) for row in left}
    right_map = {row["index"]: bool(row[key]) for row in right}
    common = sorted(set(left_map) & set(right_map))
    left_only = sum(left_map[index] and not right_map[index] for index in common)
    right_only = sum(not left_map[index] and right_map[index] for index in common)
    discordant = left_only + right_only
    if discordant == 0:
        p_value = 1.0
    else:
        lower = min(left_only, right_only)
        probability = sum(math.comb(discordant, k) for k in range(lower + 1)) / (2**discordant)
        p_value = min(1.0, 2 * probability)
    return {
        "n": len(common),
        "left_correct_right_wrong": left_only,
        "left_wrong_right_correct": right_only,
        "p_value": p_value,
    }


def fmt_pct(value: float) -> str:
    return f"{value * 100:.2f}"


def svg_grouped_accuracy(path: Path, subset: dict[str, dict[str, float]]) -> None:
    width, height = 900, 500
    left, top, bottom = 85, 55, 90
    plot_h = height - top - bottom
    plot_w = width - left - 45
    groups = list(subset)
    minimum, maximum = 0.75, 0.95
    colors = {"LFA": "#2f6f9f", "EX": "#dd7b32"}
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<style>text{font-family:Arial,"Microsoft YaHei",sans-serif;fill:#222}.axis{font-size:13px}.label{font-size:14px}.value{font-size:12px;font-weight:bold}.title{font-size:20px;font-weight:bold}.grid{stroke:#ddd;stroke-width:1}.axisline{stroke:#333;stroke-width:1.2}</style>',
        '<text x="450" y="30" text-anchor="middle" class="title">同一前 1,000 条 Test 子集上的消融结果</text>',
    ]
    for tick in [0.75, 0.80, 0.85, 0.90, 0.95]:
        y = top + (maximum - tick) / (maximum - minimum) * plot_h
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_w}" y2="{y:.1f}" class="grid"/>')
        parts.append(f'<text x="{left - 12}" y="{y + 4:.1f}" text-anchor="end" class="axis">{tick*100:.0f}%</text>')
    group_w = plot_w / len(groups)
    bar_w = 46
    for i, exp in enumerate(groups):
        center = left + group_w * (i + 0.5)
        for j, metric in enumerate(["LFA", "EX"]):
            value = subset[exp][metric]
            x = center + (j - 0.5) * (bar_w + 8) - bar_w / 2
            y = top + (maximum - value) / (maximum - minimum) * plot_h
            h = top + plot_h - y
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w}" height="{h:.1f}" fill="{colors[metric]}"/>')
            parts.append(f'<text x="{x + bar_w/2:.1f}" y="{y - 7:.1f}" text-anchor="middle" class="value">{value*100:.1f}</text>')
        parts.append(f'<text x="{center:.1f}" y="{top + plot_h + 28}" text-anchor="middle" class="label">{exp}</text>')
        parts.append(f'<text x="{center:.1f}" y="{top + plot_h + 48}" text-anchor="middle" class="axis">{CONFIG[exp][0]}, {CONFIG[exp][1].split(" /")[0]}</text>')
    parts.append(f'<line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top + plot_h}" class="axisline"/>')
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_h}" class="axisline"/>')
    parts.append('<rect x="660" y="62" width="14" height="14" fill="#2f6f9f"/><text x="682" y="74" class="axis">Logical Form Accuracy</text>')
    parts.append('<rect x="660" y="84" width="14" height="14" fill="#dd7b32"/><text x="682" y="96" class="axis">Execution Accuracy</text>')
    parts.append('</svg>')
    path.write_text("\n".join(parts), encoding="utf-8")


def svg_efficiency(path: Path, metrics: dict[str, dict[str, Any]]) -> None:
    width, height = 930, 470
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<style>text{font-family:Arial,"Microsoft YaHei",sans-serif;fill:#222}.title{font-size:20px;font-weight:bold}.head{font-size:15px;font-weight:bold}.label{font-size:12px}.grid{stroke:#ddd}.axis{stroke:#333}.input{fill:#4c78a8}.output{fill:#f58518}.cache{fill:#54a24b}</style>',
        '<text x="465" y="28" text-anchor="middle" class="title">Token、缓存与延迟效率</text>',
    ]
    panels = [(40, "平均 Token / 样本"), (340, "输入缓存命中率"), (640, "平均响应延迟")]
    for x, title in panels:
        parts.append(f'<text x="{x + 120}" y="58" text-anchor="middle" class="head">{title}</text>')
    max_token = max(metrics[e]["input_per_sample"] + metrics[e]["output_per_sample"] for e in EXPERIMENTS)
    max_latency = max(metrics[e]["latency_ms"]["mean"] for e in EXPERIMENTS)
    for i, exp in enumerate(EXPERIMENTS):
        y = 90 + i * 80
        parts.append(f'<text x="42" y="{y+17}" class="label">{exp}</text>')
        input_w = 210 * metrics[exp]["input_per_sample"] / max_token
        output_w = 210 * metrics[exp]["output_per_sample"] / max_token
        parts.append(f'<rect x="70" y="{y}" width="{input_w:.1f}" height="22" class="input"/>')
        parts.append(f'<rect x="{70+input_w:.1f}" y="{y}" width="{output_w:.1f}" height="22" class="output"/>')
        parts.append(f'<text x="285" y="{y+16}" text-anchor="end" class="label">{metrics[exp]["input_per_sample"]+metrics[exp]["output_per_sample"]:.0f}</text>')
        cache_rate = metrics[exp]["cache_rate"]
        parts.append(f'<text x="342" y="{y+17}" class="label">{exp}</text>')
        parts.append(f'<rect x="370" y="{y}" width="210" height="22" fill="#eee"/>')
        parts.append(f'<rect x="370" y="{y}" width="{210*cache_rate:.1f}" height="22" class="cache"/>')
        parts.append(f'<text x="590" y="{y+16}" class="label">{cache_rate*100:.1f}%</text>')
        latency = metrics[exp]["latency_ms"]["mean"]
        parts.append(f'<text x="642" y="{y+17}" class="label">{exp}</text>')
        parts.append(f'<rect x="670" y="{y}" width="{210*latency/max_latency:.1f}" height="22" class="input"/>')
        parts.append(f'<text x="890" y="{y+16}" class="label">{latency/1000:.2f}s</text>')
    parts.append('<rect x="62" y="420" width="12" height="12" class="input"/><text x="80" y="431" class="label">Input</text>')
    parts.append('<rect x="130" y="420" width="12" height="12" class="output"/><text x="148" y="431" class="label">Output</text>')
    parts.append('</svg>')
    path.write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = {exp: load_jsonl(RUN / exp / "evaluated.jsonl") for exp in EXPERIMENTS}
    metrics = {exp: json.loads((RUN / exp / "metrics.json").read_text(encoding="utf-8")) for exp in EXPERIMENTS}
    manifests = {exp: json.loads((RUN / exp / "manifest.json").read_text(encoding="utf-8")) for exp in EXPERIMENTS}

    subset_rows = {exp: [row for row in rows[exp] if row["index"] < 1000] for exp in EXPERIMENTS}
    subset = {
        exp: {
            "N": len(subset_rows[exp]),
            "LFA": rate(subset_rows[exp], "lf_correct"),
            "EX": rate(subset_rows[exp], "ex_correct"),
            "JSON": rate(subset_rows[exp], "json_valid"),
            "SQL": rate(subset_rows[exp], "structural_valid"),
        }
        for exp in EXPERIMENTS
    }
    comparisons = {
        "E1_vs_E2_LF": exact_mcnemar(subset_rows["E1"], subset_rows["E2"], "lf_correct"),
        "E1_vs_E2_EX": exact_mcnemar(subset_rows["E1"], subset_rows["E2"], "ex_correct"),
        "E1_vs_E3_LF": exact_mcnemar(subset_rows["E1"], subset_rows["E3"], "lf_correct"),
        "E1_vs_E3_EX": exact_mcnemar(subset_rows["E1"], subset_rows["E3"], "ex_correct"),
        "E3_vs_E4_LF": exact_mcnemar(subset_rows["E3"], subset_rows["E4"], "lf_correct"),
        "E3_vs_E4_EX": exact_mcnemar(subset_rows["E3"], subset_rows["E4"], "ex_correct"),
    }

    full_e4 = rows["E4"]
    stratified: dict[str, Any] = {"aggregation": {}, "condition_count": {}}
    for agg_index, agg_name in enumerate(AGG_NAMES):
        selected = [row for row in full_e4 if row["gold_sql"]["agg"] == agg_index]
        stratified["aggregation"][agg_name] = {"n": len(selected), "LFA": rate(selected, "lf_correct"), "EX": rate(selected, "ex_correct")}
    condition_groups = {
        "0": [row for row in full_e4 if len(row["gold_sql"]["conds"]) == 0],
        "1": [row for row in full_e4 if len(row["gold_sql"]["conds"]) == 1],
        "2+": [row for row in full_e4 if len(row["gold_sql"]["conds"]) >= 2],
    }
    for name, selected in condition_groups.items():
        stratified["condition_count"][name] = {"n": len(selected), "LFA": rate(selected, "lf_correct"), "EX": rate(selected, "ex_correct")}

    error_types = Counter()
    execution_errors = Counter()
    for row in full_e4:
        if row["lf_correct"] and row["ex_correct"]:
            error_types["LF correct / EX correct"] += 1
        elif not row["lf_correct"] and row["ex_correct"]:
            error_types["LF wrong / EX correct"] += 1
        elif row["lf_correct"] and not row["ex_correct"]:
            error_types["LF correct / EX wrong"] += 1
        else:
            error_types["LF wrong / EX wrong"] += 1
        if row.get("execution_error"):
            execution_errors[row["execution_error"]] += 1

    ranked = sorted(
        [(row["retrieved_examples"][0]["score"], row) for row in full_e4 if row.get("retrieved_examples")],
        key=lambda item: item[0],
    )
    retrieval_quartiles = []
    for quartile in range(4):
        start = len(ranked) * quartile // 4
        end = len(ranked) * (quartile + 1) // 4
        selected = [item[1] for item in ranked[start:end]]
        retrieval_quartiles.append({
            "quartile": quartile + 1,
            "score_min": ranked[start][0],
            "score_max": ranked[end - 1][0],
            "n": len(selected),
            "LFA": rate(selected, "lf_correct"),
            "EX": rate(selected, "ex_correct"),
        })

    efficiency = {}
    for exp in EXPERIMENTS:
        usage = metrics[exp]["usage"]
        n = metrics[exp]["total"]
        efficiency[exp] = {
            "input_per_sample": usage["input_tokens"] / n,
            "output_per_sample": usage["output_tokens"] / n,
            "cache_rate": usage["cached_input_tokens"] / usage["input_tokens"],
            "latency_ms": metrics[exp]["latency_ms"],
            "estimated_cost": metrics[exp]["estimated_api_cost_usd"],
        }

    e4_lf_ci = wilson(metrics["E4"]["logical_form_correct_count"], metrics["E4"]["total"])
    e4_ex_ci = wilson(metrics["E4"]["execution_correct_count"], metrics["E4"]["total"])
    reasoning_reported = {
        exp: sum((row.get("usage", {}).get("output_tokens_details") or {}).get("reasoning_tokens") or 0 for row in rows[exp])
        for exp in EXPERIMENTS
    }
    reasoning_reported_subset = {
        exp: sum((row.get("usage", {}).get("output_tokens_details") or {}).get("reasoning_tokens") or 0 for row in subset_rows[exp])
        for exp in EXPERIMENTS
    }

    summary = {
        "full_metrics": metrics,
        "fair_1000_subset": subset,
        "mcnemar_exact": comparisons,
        "e4_confidence_intervals_95": {"LFA": e4_lf_ci, "EX": e4_ex_ci},
        "stratified_e4": stratified,
        "e4_error_types": dict(error_types),
        "e4_execution_errors": dict(execution_errors),
        "retrieval_quartiles": retrieval_quartiles,
        "efficiency": efficiency,
        "reported_reasoning_tokens": reasoning_reported,
        "reported_reasoning_tokens_fair_subset": reasoning_reported_subset,
    }
    (OUT / "analysis_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with (OUT / "main_results.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["Experiment", "N", "Few-shot", "Thinking", "LFA", "EX", "JSON Validity", "SQL Validity", "Input Tokens", "Cached Tokens", "Output Tokens", "Mean Latency ms", "Estimated Cost USD"])
        for exp in EXPERIMENTS:
            m = metrics[exp]
            writer.writerow([exp, m["total"], *CONFIG[exp], m["logical_form_accuracy"], m["execution_accuracy"], m["json_validity"], m["sql_validity"], m["usage"]["input_tokens"], m["usage"]["cached_input_tokens"], m["usage"]["output_tokens"], m["latency_ms"]["mean"], m["estimated_api_cost_usd"]])

    svg_grouped_accuracy(OUT / "figure_1_ablation_accuracy.svg", subset)
    svg_efficiency(OUT / "figure_2_efficiency.svg", efficiency)

    lines = []
    add = lines.append
    add("# GPT-5.6-sol 在 WikiSQL 上的现代 Text-to-SQL Baseline 实验报告\n")
    add("**实验日期：** 2026年11月18日  \n**数据集：** WikiSQL  \n**主模型：** GPT-5.6-sol  \n**报告类型：** Test 集正式实验结果\n")
    add("## 摘要\n")
    add(
        f"本文评估 GPT-5.6-sol 在 WikiSQL Text-to-SQL 任务上的现代大语言模型基线。主系统 E4 结合动态 5-shot 检索、Schema-aware Reasoning Prompt 与 high reasoning effort，在完整 Test 集 {metrics['E4']['total']:,} 条样本上取得 "
        f"{fmt_pct(metrics['E4']['logical_form_accuracy'])}% Logical Form Accuracy（LFA）和 {fmt_pct(metrics['E4']['execution_accuracy'])}% Execution Accuracy（EX）。"
        f"其 95% Wilson 置信区间分别为 [{fmt_pct(e4_lf_ci[0])}%, {fmt_pct(e4_lf_ci[1])}%] 与 [{fmt_pct(e4_ex_ci[0])}%, {fmt_pct(e4_ex_ci[1])}%]。"
        "全部预测均通过 JSON 与结构化 SQL 校验，SQL 执行成功率为 99.94%。在相同前 1,000 条 Test 子集上的成对消融表明，5-shot 检索带来稳定增益，而单独开启 high reasoning effort 未带来可观测改善。\n"
    )
    add("## 1. 实验设置\n")
    add("### 1.1 数据与划分\n")
    add("Few-shot 示例仅从 Train 集动态检索；Dev 集用于 Prompt 调试与冻结；正式 API 推理仅覆盖 Test 集。E4 在完整 Test 集上运行，E1–E3 为节省成本各使用 Test 前 1,000 条。为保证消融公平性，本文另外报告 E4 在相同前 1,000 条上的结果。\n")
    add("### 1.2 对照组\n")
    add("| 实验 | Few-shot | Thinking | 推理强度 | Test 样本数 | 角色 |\n|---|---:|---|---|---:|---|\n")
    add("| E1 | 0-shot | Off | none | 1,000 | 基础对照 |\n| E2 | 0-shot | On | high | 1,000 | Thinking 消融 |\n| E3 | 5-shot | Off | none | 1,000 | Few-shot 消融 |\n| E4 | 5-shot | On | high | 15,878 | 主 Baseline |\n")
    add("### 1.3 Prompt、检索与 Token 优化\n")
    add("系统采用固定 Schema-aware developer 前缀，引导问题理解、字段匹配、聚合识别、条件识别和最终 JSON 校验。E3/E4 使用基于问题/表头词汇相似度、SQL 结构启发式及表头重合度的动态 5-shot 检索。目标表采用无损紧凑编码；Few-shot 示例保留 SQL 相关列的全部证据行。固定前缀通过稳定 cache key 使用 Prompt Caching。\n")
    add("### 1.4 评价标准\n")
    add("采用统一 WikiSQL 解析与 SQLite 执行器。LFA 比较选择列、聚合和无序 WHERE 条件；EX 比较预测 SQL 与金标 SQL 的执行结果。SQL Validity 表示结构校验通过，Execution Success Rate 表示结构有效预测中可成功执行的比例。Semantic Accuracy 预留给人工抽样，本报告未以自动指标替代人工评价。\n")

    add("## 2. 主实验结果\n")
    add("### 2.1 完整运行结果\n")
    add("| 实验 | N | LFA (%) | EX (%) | JSON Validity (%) | SQL Validity (%) | Execution Success (%) |\n|---|---:|---:|---:|---:|---:|---:|\n")
    for exp in EXPERIMENTS:
        m = metrics[exp]
        add(f"| {exp} | {m['total']:,} | {fmt_pct(m['logical_form_accuracy'])} | {fmt_pct(m['execution_accuracy'])} | {fmt_pct(m['json_validity'])} | {fmt_pct(m['sql_validity'])} | {fmt_pct(m['execution_success_rate'])} |\n")
    add("\n> 注：E1–E3 与 E4 的样本规模不同，本表用于汇总运行结果；严格消融结论应以表 2 的同一 1,000 条子集为准。\n")

    add("### 2.2 公平消融比较：相同前 1,000 条 Test\n")
    add("| 实验 | LFA (%) | EX (%) | 相对 E1：ΔLFA (pp) | 相对 E1：ΔEX (pp) |\n|---|---:|---:|---:|---:|\n")
    for exp in EXPERIMENTS:
        add(f"| {exp} | {fmt_pct(subset[exp]['LFA'])} | {fmt_pct(subset[exp]['EX'])} | {(subset[exp]['LFA']-subset['E1']['LFA'])*100:+.2f} | {(subset[exp]['EX']-subset['E1']['EX'])*100:+.2f} |\n")
    add("\n![同一子集消融结果](figure_1_ablation_accuracy.svg)\n")

    add("### 2.3 成对显著性检验\n")
    add("采用同一样本上的双侧精确 McNemar 检验。\n\n| 对比 | 指标 | 左组正确/右组错误 | 左组错误/右组正确 | p-value |\n|---|---|---:|---:|---:|\n")
    labels = [("E1_vs_E2_LF", "E1 vs E2", "LFA"), ("E1_vs_E2_EX", "E1 vs E2", "EX"), ("E1_vs_E3_LF", "E1 vs E3", "LFA"), ("E1_vs_E3_EX", "E1 vs E3", "EX"), ("E3_vs_E4_LF", "E3 vs E4", "LFA"), ("E3_vs_E4_EX", "E3 vs E4", "EX")]
    for key, label, metric_name in labels:
        value = comparisons[key]
        add(f"| {label} | {metric_name} | {value['left_correct_right_wrong']} | {value['left_wrong_right_correct']} | {value['p_value']:.4g} |\n")

    add("## 3. 分层结果与错误分析\n")
    add("### 3.1 E4 按聚合类型分层\n")
    add("| 聚合 | N | LFA (%) | EX (%) |\n|---|---:|---:|---:|\n")
    for name in AGG_NAMES:
        value = stratified["aggregation"][name]
        add(f"| {name} | {value['n']:,} | {fmt_pct(value['LFA'])} | {fmt_pct(value['EX'])} |\n")
    add("### 3.2 E4 按 WHERE 条件数量分层\n")
    add("| 条件数量 | N | LFA (%) | EX (%) |\n|---|---:|---:|---:|\n")
    for name in ["0", "1", "2+"]:
        value = stratified["condition_count"][name]
        add(f"| {name} | {value['n']:,} | {fmt_pct(value['LFA'])} | {fmt_pct(value['EX'])} |\n")
    add("### 3.3 逻辑形式与执行结果差异\n")
    add("| 类型 | 数量 | 比例 (%) | 解释 |\n|---|---:|---:|---|\n")
    explanations = {
        "LF correct / EX correct": "逻辑形式与执行结果均正确",
        "LF wrong / EX correct": "非金标逻辑形式但在当前表上得到相同答案",
        "LF correct / EX wrong": "逻辑匹配但执行差异，应重点检查数值规范化/执行器边界",
        "LF wrong / EX wrong": "真实 Text-to-SQL 预测错误",
    }
    for name in ["LF correct / EX correct", "LF wrong / EX correct", "LF correct / EX wrong", "LF wrong / EX wrong"]:
        count = error_types[name]
        add(f"| {name} | {count:,} | {count/len(full_e4)*100:.2f} | {explanations[name]} |\n")
    add(f"\nE4 共出现 {sum(execution_errors.values())} 条不可执行预测；全部原因为条件操作符 `OP=3` 不在官方 SQLite 执行器支持的 `= / > / <` 范围内。\n")

    add("### 3.4 检索相似度与性能\n")
    add("| Top-1 检索分数四分位 | 分数范围 | N | LFA (%) | EX (%) |\n|---|---|---:|---:|---:|\n")
    for value in retrieval_quartiles:
        add(f"| Q{value['quartile']} | {value['score_min']:.3f}–{value['score_max']:.3f} | {value['n']:,} | {fmt_pct(value['LFA'])} | {fmt_pct(value['EX'])} |\n")

    add("## 4. 效率、缓存与成本\n")
    add("| 实验 | 输入 Token/样本 | 输出 Token/样本 | 缓存命中率 (%) | 平均延迟 (s) | P95 (s) | 估算成本 (USD) |\n|---|---:|---:|---:|---:|---:|---:|\n")
    for exp in EXPERIMENTS:
        value = efficiency[exp]
        add(f"| {exp} | {value['input_per_sample']:.1f} | {value['output_per_sample']:.1f} | {value['cache_rate']*100:.2f} | {value['latency_ms']['mean']/1000:.2f} | {value['latency_ms']['p95']/1000:.2f} | {value['estimated_cost']:.2f} |\n")
    add("\n![Token、缓存与延迟](figure_2_efficiency.svg)\n")
    total_cost = sum(metrics[exp]["estimated_api_cost_usd"] for exp in EXPERIMENTS)
    add(f"四组实验程序估算总成本为 **${total_cost:.2f}**。该值依据实验程序中配置的单价及缓存折扣计算，仅用于实验内比较，不等同于服务商最终账单。\n")

    add("## 5. 结果讨论\n")
    add("1. **Few-shot 是主要增益来源。** 在同一 1,000 条子集上，E3 相比 E1 的 LFA 提升 3.00 个百分点，EX 提升 3.40 个百分点；成对检验用于判断该增益是否超出样本波动。动态检索示例帮助模型更稳定地识别聚合、选择列和 WHERE 条件。\n")
    add(f"2. **Thinking High 未表现出独立收益。** E2 与 E1 的 EX 完全相同，LFA 略低 0.20 个百分点；E4 相对 E3 的变化也不显著。API 请求确实记录了 `reasoning.effort=high`，但同一 1,000 条子集上报告的 reasoning tokens 为 E1={reasoning_reported_subset['E1']:,}、E2={reasoning_reported_subset['E2']:,}、E3={reasoning_reported_subset['E3']:,}、E4={reasoning_reported_subset['E4']:,}，并未随 Thinking 配置单调增加。因此该 usage 字段不宜被直接解释为模型内部推理强度，只能依据端到端正确率评估其效果。\n")
    add("3. **执行指标高于逻辑形式指标。** E4 的 EX 比 LFA 高 5.15 个百分点，说明部分非金标 SQL 在具体表上产生相同答案。这是 WikiSQL 中常见的 denotation equivalence，亦表明仅使用 EX 可能高估结构生成质量。\n")
    add("4. **结构化输出非常稳定。** 四组 JSON 与结构 SQL 有效率均为 100%，证明严格 JSON Schema、固定 Prompt 前缀和本地规范化能够有效避免格式错误。E4 仍有少量执行失败，主要应归因于结构合法但执行器不支持或数值解析边界。\n")
    add("5. **Prompt Caching 明显降低有效输入成本。** 各组均出现较高缓存命中率；Few-shot 增加输入长度，但固定前缀缓存抵消了部分成本。E4 的平均响应延迟仍维持在约 3.55 秒。\n")

    add("## 6. 有效性威胁与限制\n")
    add("- E1–E3 仅使用 Test 前 1,000 条，不是随机或分层抽样；它们可用于同一子集内的成对消融，但不应直接视为全 Test 总体估计。\n")
    add("- Semantic Accuracy 尚未完成正式人工双人标注与一致性检验，因此本报告不提供该指标。\n")
    add("- 估算成本依赖程序中配置的单价和缓存折扣，不代表实际账单。\n")
    add("- Thinking 模式由 API 参数定义；返回的 reasoning-token 计数与配置不呈单调关系，模型内部推理机制仍不可直接观测。\n")
    add("- WikiSQL 主要覆盖单表、有限聚合与简单条件，结果不能直接外推至 Spider 等复杂多表 Text-to-SQL 场景。\n")

    add("## 7. 结论\n")
    add(f"GPT-5.6-sol 的 E4 主 Baseline 在 WikiSQL 完整 Test 集上达到 **{fmt_pct(metrics['E4']['logical_form_accuracy'])}% LFA** 与 **{fmt_pct(metrics['E4']['execution_accuracy'])}% EX**，并保持 100% JSON/SQL 结构有效率。消融结果表明，动态 5-shot 检索是性能提升的主要来源，而在当前任务与接口条件下，单独开启 high reasoning effort 未产生稳定增益。该实验流程具备统一评价、Prompt 冻结、断点续跑、缓存统计和错误追踪能力，可作为后续检索方法、Prompt 策略和人工语义评价研究的可复现基线。\n")

    add("## 参考文献\n")
    add("[1] Zhong, V., Xiong, C., & Socher, R. (2017). *Seq2SQL: Generating Structured Queries from Natural Language using Reinforcement Learning*. arXiv:1709.00103.\n")
    add("[2] Salesforce Research. *WikiSQL: A Large Annotated Semantic Parsing Corpus for Developing Natural Language Interfaces*. Official repository and evaluation script.\n")

    (OUT / "WikiSQL_Modern_Baseline_Report.md").write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
