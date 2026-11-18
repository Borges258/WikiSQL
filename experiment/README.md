# WikiSQL Modern LLM Baseline（Python）

`run_modern_baseline.py` 实现四组统一评价的 WikiSQL Text-to-SQL 实验：

| 实验 | Few-shot | Thinking / effort |
|---|---:|---|
| E1 | 0-shot | Off / `none` |
| E2 | 0-shot | On / `high` |
| E3 | 5-shot | Off / `none` |
| E4 | 5-shot | On / `high` |

E4 是主 Baseline，E1–E3 是消融实验。模型、API Key 和 Base URL 从仓库根目录 `.env` 读取；请求使用 OpenAI Responses API 格式和严格 JSON Schema。

## Prompt 与检索策略

- Prompt 使用 Schema-aware Reasoning checklist：问题理解、字段匹配、聚合识别、条件识别、JSON 校验。
- 不要求输出链式思考，只输出最终 SQL JSON。
- E3/E4 的示例只从 `train.jsonl` 检索，绝不从 Dev/Test 检索。
- 动态检索分数结合问题/表头 TF-IDF 余弦相似度、启发式 SQL 聚合/条件结构相似度、表头重合度。
- Dev 首次运行会生成 `prompt_freeze.json`；Test 运行强制校验冻结哈希。

## Token 优化约束

- 目标表使用无损紧凑编码：保留所有列索引、列名、类型和所有行，只压缩 JSON 键名；因此不会删减目标表语义。
- Few-shot 示例保留问题、原始列索引、类型、SQL 及 SQL 使用列的全部证据行；不携带页面标题等与 SQL 无关的元数据。默认不删行，避免改变示例语义。
- 固定 Schema-aware developer 前缀，动态示例和目标表放在 user 段，使用稳定 `prompt_cache_key` 和隐式 Prompt Caching。
- 非 Thinking 组输出上限为 256，Thinking 组为 384；若出现截断，应在正式运行前调高上限，不自动改变 SQL 评价逻辑。
- 正式 Test 全量时 E4 运行全部 Test；E1–E3 默认各运行前 1000 条，可通过 `--ablation-limit` 调整。Train 和 Dev 仅本地检索/调试，不进行全量 API 调用。

## Dev 小范围调试

先做离线检查：

```powershell
$python = 'C:\Users\Borges\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $python .\dataset\WikiSQL\experiment\run_modern_baseline.py `
  --experiment all --split dev --limit 2 --dry-run `
  --run-root .\dataset\WikiSQL\archive\dev_and_smoke_tests\dev_current
```

运行四组各 2 条真实 API 小测：

```powershell
& $python .\dataset\WikiSQL\experiment\run_modern_baseline.py `
  --experiment all --split dev --limit 2 --concurrency 2 `
  --run-root .\dataset\WikiSQL\archive\dev_and_smoke_tests\dev_current
```

## 正式 Test 实验

获得人工批准后，才使用 `--limit all --allow-full-run`。建议先完成 Dev 调试并确认 `prompt_freeze.json` 后运行：

```powershell
& $python .\dataset\WikiSQL\experiment\run_modern_baseline.py `
  --experiment all --split test --limit all --allow-full-run `
  --ablation-limit 1000 --concurrency 3 `
  --run-root .\dataset\WikiSQL\results\formal_test
```

缺少 `--allow-full-run` 时会在任何 API 请求前退出；Test 还要求已有 Dev 生成的 Prompt 冻结清单。

## 输出

每组目录包含 `manifest.json`、`responses.jsonl`、`evaluated.jsonl`、`predictions.jsonl`、`metrics.json`、`metrics.md`、`error_cases.md` 和 `semantic_samples.jsonl`。上层 split 目录包含 `comparison.json`、`comparison.md`；运行根目录包含 `prompt_freeze.json`。

指标包括 Logical Form Accuracy、Execution Accuracy、SQL Validity、JSON Validity、Execution Success Rate、延迟、Token 和估算 API 成本。`semantic_accuracy` 保留为人工抽样标注字段，需在 `semantic_samples.jsonl` 填写 `manual_label` 后再汇总。
