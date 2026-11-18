
"""
WikiSQL Dataset Basic Analysis
功能：
1. 统计 train/dev/test 数据集规模
2. 分析自然语言问题长度
3. 分析 SQL 结构分布
4. 分析表格规模与数据类型
5. 检查基础数据完整性
6. 导出 JSON 和 Markdown 报告

注意：
本脚本只进行客观统计和基础结构检查，
不提前判断数据集是否存在某类研究缺陷。
"""

import argparse
import json
import statistics
from pathlib import Path
from collections import Counter


# ============================================================
# 1. 配置区
# ============================================================

SPLITS = ["train", "dev", "test"]

# WikiSQL 官方常见 SQL 编码
AGG_OPS = {
    0: "NONE",
    1: "MAX",
    2: "MIN",
    3: "COUNT",
    4: "SUM",
    5: "AVG",
}

# 条件操作符编码。
# 第 3 号操作符在部分官方实现中记作 OP，
# 通常对应不等于操作；这里保留官方编码名称，避免误读。
COND_OPS = {
    0: "=",
    1: ">",
    2: "<",
    3: "OP",
}


# ============================================================
# 2. JSONL 文件读取
# ============================================================

def load_jsonl(file_path):
    """
    逐行读取 JSONL 文件。

    返回：
        records: 成功读取的 JSON 对象列表
        errors: 读取失败的行号及原因
    """
    records = []
    errors = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                errors.append({
                    "line": line_no,
                    "reason": "空白行"
                })
                continue

            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                errors.append({
                    "line": line_no,
                    "reason": str(e)
                })

    return records, errors


# ============================================================
# 3. 通用统计函数
# ============================================================

def describe(values):
    """
    对数值列表计算基础描述统计。

    空列表返回 None，避免统计函数报错。
    """
    if not values:
        return {
            "count": 0,
            "mean": None,
            "median": None,
            "min": None,
            "max": None
        }

    return {
        "count": len(values),
        "mean": round(statistics.mean(values), 4),
        "median": round(statistics.median(values), 4),
        "min": min(values),
        "max": max(values)
    }


def counter_to_dict(counter):
    """将 Counter 转换为按频次降序排列的字典。"""
    return dict(counter.most_common())


def get_question_length(question):
    """
    统计英文问题的空格分词长度。

    说明：
    这是简单词数统计，不等于模型实际使用的 tokenizer token 数。
    """
    if not isinstance(question, str):
        return 0

    return len(question.split())


# ============================================================
# 4. WikiSQL 分析器
# ============================================================

class WikiSQLAnalyzer:

    def __init__(self, data_dir, output_dir):
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.results = {}

    # --------------------------------------------------------
    # 4.1 寻找数据文件
    # --------------------------------------------------------

    def find_question_file(self, split):
        """寻找 train.jsonl / dev.jsonl / test.jsonl。"""

        candidates = [
            self.data_dir / f"{split}.jsonl",
            self.data_dir / split / f"{split}.jsonl"
        ]

        for path in candidates:
            if path.exists():
                return path

        raise FileNotFoundError(
            f"找不到 {split}.jsonl，请检查数据目录：{self.data_dir}"
        )

    def find_table_file(self, split):
        """
        寻找表格文件。

        优先使用 split 对应的 tables 文件；
        如果不存在，则尝试使用统一的 tables.jsonl。
        """

        candidates = [
            self.data_dir / f"{split}.tables.jsonl",
            self.data_dir / f"{split}_tables.jsonl",
            self.data_dir / "tables.jsonl",
            self.data_dir / "tables" / f"{split}.jsonl",
            self.data_dir / split / f"{split}.tables.jsonl"
        ]

        for path in candidates:
            if path.exists():
                return path

        return None

    # --------------------------------------------------------
    # 4.2 分析问题数据与 SQL 结构
    # --------------------------------------------------------

    def analyze_questions(self, questions):
        question_lengths = []

        agg_counter = Counter()
        cond_count_counter = Counter()
        cond_op_counter = Counter()

        missing_question = 0
        missing_table_id = 0
        missing_sql = 0
        invalid_sql = 0

        table_id_counter = Counter()

        for record in questions:

            question = record.get("question")

            if not isinstance(question, str) or not question.strip():
                missing_question += 1
            else:
                question_lengths.append(
                    get_question_length(question)
                )

            table_id = record.get("table_id")

            if not table_id:
                missing_table_id += 1
            else:
                table_id_counter[table_id] += 1

            sql = record.get("sql")

            if not isinstance(sql, dict):
                missing_sql += 1
                continue

            # SELECT 聚合操作
            agg = sql.get("agg")

            if isinstance(agg, int):
                agg_counter[
                    AGG_OPS.get(agg, f"UNKNOWN_{agg}")
                ] += 1
            else:
                invalid_sql += 1

            # WHERE 条件数量
            conds = sql.get("conds")

            if isinstance(conds, list):
                cond_count_counter[len(conds)] += 1

                for cond in conds:
                    if (
                        isinstance(cond, list)
                        and len(cond) >= 2
                        and isinstance(cond[1], int)
                    ):
                        op = cond[1]
                        cond_op_counter[
                            COND_OPS.get(op, f"UNKNOWN_{op}")
                        ] += 1
                    else:
                        invalid_sql += 1
            else:
                invalid_sql += 1

        duplicate_question_count = sum(
            count - 1
            for count in table_id_counter.values()
            if count > 1
        )

        return {
            "question_length": describe(question_lengths),

            "sql": {
                "aggregation_distribution": counter_to_dict(
                    agg_counter
                ),
                "where_condition_count_distribution": (
                    counter_to_dict(cond_count_counter)
                ),
                "condition_operator_distribution": (
                    counter_to_dict(cond_op_counter)
                )
            },

            "basic_integrity": {
                "missing_question": missing_question,
                "missing_table_id": missing_table_id,
                "missing_sql": missing_sql,
                "invalid_sql_structure": invalid_sql
            },

            "table_id": {
                "unique_count": len(table_id_counter),
                "repeated_reference_count": duplicate_question_count
            }
        }

    # --------------------------------------------------------
    # 4.3 分析表格数据
    # --------------------------------------------------------

    def analyze_tables(self, tables):
        row_counts = []
        column_counts = []
        cell_counts = []

        header_lengths = []
        cell_type_counter = Counter()

        empty_cell_count = 0
        malformed_rows = 0
        missing_header = 0
        duplicate_table_ids = 0

        table_ids = set()

        for table in tables:

            table_id = table.get("id")

            if table_id is not None:
                if table_id in table_ids:
                    duplicate_table_ids += 1
                else:
                    table_ids.add(table_id)

            headers = table.get("header", [])
            rows = table.get("rows", [])

            if not isinstance(headers, list):
                missing_header += 1
                headers = []

            if not isinstance(rows, list):
                rows = []

            column_count = len(headers)
            row_count = len(rows)

            row_counts.append(row_count)
            column_counts.append(column_count)
            cell_counts.append(row_count * column_count)

            for header in headers:
                header_lengths.append(
                    len(str(header).split())
                )

            for row in rows:

                if not isinstance(row, list):
                    malformed_rows += 1
                    continue

                if len(row) != column_count:
                    malformed_rows += 1

                for cell in row:

                    if cell is None or str(cell).strip() == "":
                        empty_cell_count += 1

                    if isinstance(cell, bool):
                        cell_type_counter["bool"] += 1
                    elif isinstance(cell, (int, float)):
                        cell_type_counter["number"] += 1
                    elif cell is None:
                        cell_type_counter["null"] += 1
                    else:
                        cell_type_counter["text"] += 1

        return {
            "table_count": len(tables),

            "row_count_per_table": describe(row_counts),
            "column_count_per_table": describe(column_counts),
            "cell_count_per_table": describe(cell_counts),
            "header_word_count": describe(header_lengths),

            "cell_type_distribution": counter_to_dict(
                cell_type_counter
            ),

            "basic_integrity": {
                "duplicate_table_ids": duplicate_table_ids,
                "missing_or_invalid_header": missing_header,
                "malformed_rows": malformed_rows,
                "empty_cells": empty_cell_count
            }
        }

    # --------------------------------------------------------
    # 4.4 检查问题与表格关联
    # --------------------------------------------------------

    def analyze_table_links(self, questions, tables):
        """
        检查每条问题能否关联到对应的 table_id。

        如果没有独立的表格文件，则返回未检查状态。
        """

        if tables is None:
            return {
                "checked": False,
                "reason": "没有找到对应的表格文件"
            }

        table_ids = {
            table.get("id")
            for table in tables
            if table.get("id") is not None
        }

        missing_links = 0

        for question in questions:
            table_id = question.get("table_id")

            if table_id not in table_ids:
                missing_links += 1

        return {
            "checked": True,
            "question_count": len(questions),
            "unique_table_count": len(table_ids),
            "missing_table_links": missing_links
        }

    # --------------------------------------------------------
    # 4.5 分析一个数据集 split
    # --------------------------------------------------------

    def analyze_split(self, split):

        print(f"\n正在分析 {split} 数据集...")

        question_path = self.find_question_file(split)
        questions, question_errors = load_jsonl(question_path)

        table_path = self.find_table_file(split)

        tables = None
        table_errors = []

        if table_path is not None:
            tables, table_errors = load_jsonl(table_path)

        question_result = self.analyze_questions(questions)

        if tables is not None:
            table_result = self.analyze_tables(tables)
        else:
            table_result = None

        link_result = self.analyze_table_links(
            questions,
            tables
        )

        result = {
            "split": split,

            "files": {
                "question_file": str(question_path),
                "table_file": (
                    str(table_path) if table_path else None
                )
            },

            "sample_count": len(questions),

            "question_analysis": question_result,

            "table_analysis": table_result,

            "table_link_analysis": link_result,

            "file_read_errors": {
                "question_file_errors": question_errors,
                "table_file_errors": table_errors
            }
        }

        self.results[split] = result

        print(f"{split} 样本数量：{len(questions)}")

        if tables is not None:
            print(f"{split} 表格数量：{len(tables)}")

        return result

    # --------------------------------------------------------
    # 4.6 运行全部分析
    # --------------------------------------------------------

    def run(self):

        for split in SPLITS:

            try:
                self.analyze_split(split)

            except FileNotFoundError as e:
                print(f"[跳过] {e}")

        if not self.results:
            raise RuntimeError(
                "没有成功分析任何数据集，请检查 data_dir。"
            )

        self.export_json()
        self.export_markdown()

        print("\n分析完成！")
        print(f"报告保存目录：{self.output_dir}")

    # --------------------------------------------------------
    # 4.7 导出 JSON
    # --------------------------------------------------------

    def export_json(self):

        output_path = self.output_dir / "analysis_report.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(
                self.results,
                f,
                ensure_ascii=False,
                indent=4
            )

        print(f"已生成：{output_path}")

    # --------------------------------------------------------
    # 4.8 导出 Markdown
    # --------------------------------------------------------

    def export_markdown(self):

        output_path = self.output_dir / "analysis_report.md"

        lines = []

        lines.append("# WikiSQL 数据集基础分析报告\n")

        lines.append(
            "> 本报告为描述性统计与基础完整性检查，"
            "不直接判定数据集缺陷。\n"
        )

        for split, result in self.results.items():

            lines.append(f"\n## {split.upper()} 数据集\n")

            lines.append(
                f"- 问题样本数量：{result['sample_count']}\n"
            )

            q = result["question_analysis"]

            lines.append("### 1. 自然语言问题长度\n")

            for key, value in q["question_length"].items():
                lines.append(f"- {key}：{value}\n")

            lines.append("\n### 2. SQL 聚合操作分布\n")

            for key, value in (
                q["sql"]["aggregation_distribution"].items()
            ):
                lines.append(f"- {key}：{value}\n")

            lines.append("\n### 3. WHERE 条件数量分布\n")

            for key, value in (
                q["sql"]["where_condition_count_distribution"].items()
            ):
                lines.append(f"- {key} 个条件：{value}\n")

            lines.append("\n### 4. WHERE 操作符分布\n")

            for key, value in (
                q["sql"]["condition_operator_distribution"].items()
            ):
                lines.append(f"- {key}：{value}\n")

            lines.append("\n### 5. 基础完整性检查\n")

            for key, value in q["basic_integrity"].items():
                lines.append(f"- {key}：{value}\n")

            table = result["table_analysis"]

            lines.append("\n### 6. 表格统计\n")

            if table is None:
                lines.append("- 未找到表格文件，无法统计\n")
            else:
                lines.append(
                    f"- 表格数量：{table['table_count']}\n"
                )

                for metric in [
                    "row_count_per_table",
                    "column_count_per_table",
                    "cell_count_per_table"
                ]:
                    lines.append(f"\n#### {metric}\n")

                    for key, value in table[metric].items():
                        lines.append(f"- {key}：{value}\n")

                lines.append("\n#### 表格完整性\n")

                for key, value in (
                    table["basic_integrity"].items()
                ):
                    lines.append(f"- {key}：{value}\n")

            lines.append("\n### 7. 问题与表格关联\n")

            for key, value in (
                result["table_link_analysis"].items()
            ):
                lines.append(f"- {key}：{value}\n")

            lines.append("\n---\n")

        with open(output_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        print(f"已生成：{output_path}")


# ============================================================
# 5. 命令行入口
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description="WikiSQL 数据集基础分析工具"
    )

    parser.add_argument(
        "--data_dir",
        type=str,
        required=True,
        help="WikiSQL 数据集所在目录"
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        default="./analysis_results",
        help="分析报告输出目录"
    )

    args = parser.parse_args()

    analyzer = WikiSQLAnalyzer(
        data_dir=args.data_dir,
        output_dir=args.output_dir
    )

    analyzer.run()


if __name__ == "__main__":
    main()
