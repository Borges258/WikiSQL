# Single-table Agent framework

This first vertical slice is an executable atomic data agent, not a WikiSQL prompt experiment.
It uses a structured query-plan strategy: the model returns a constrained intent object, Java
validates it against live metadata and compiles a parameterized `SELECT`. The model never emits
executable SQL. The agent executes against exactly one configured table and returns rows plus SQL
and bound parameters.

## Runtime flow

`POST /api/agent/single-table/query` with `{"question":"..."}`

1. Read only the configured table's column names, types, and up to 10 distinct non-null sample values per column.
2. Ask the configured OpenAI Chat Completions-compatible endpoint for a JSON query plan.
3. Validate every selected, filtered, and sorted column against the metadata.
4. Compile a MySQL `SELECT` with parameter placeholders and a capped `LIMIT`.
5. Execute with JDBC query timeout and return an `AgentResult`.

The shared `Agent` / `AgentTask` / `AgentResult` contract is the delegation boundary. The first
Agent is deliberately independent of the existing FlowEngine. `AgentOrganizationCoordinator`
now executes client-specified Agent DAGs through that contract.

## Agent organization API

- `GET /api/agent/organization/agents` lists registered Agents and their descriptors.
- `POST /api/agent/organization/execute` validates and executes an organization graph.

Each node has a unique `nodeId`, a registered `agentId`, an optional node-specific `question`
(otherwise the organization-level question is used), and `dependsOn` node IDs. Nodes without
dependencies run first. Independent nodes in the same layer run concurrently (up to four at once).
Each dependent Agent receives its completed dependency results in
`task.context.upstreamResults`. A failed dependency causes its dependent node to be skipped;
inspect `subResults` for node-level status and errors. The `sql-validator` consumes upstream SQL
candidates and selects the highest-confidence valid read-only SELECT. At organization level,
successful terminal candidates use the same highest-confidence policy; ties preserve input order.
The chosen candidate is promoted into top-level `sql`, `parameters`, and `rows`, with every result
retained in `subResults`.

Example 1-1 (pipeline):

```json
{
  "question": "Find the relevant records and summarize them",
  "nodes": [
    {"nodeId": "inspect", "agentId": "single-table-data-agent"},
    {"nodeId": "summarize", "agentId": "single-table-data-agent", "dependsOn": ["inspect"]}
  ]
}
```

Registered roles include `schema-linker`, `sql-planner`, and `sql-validator` (plus the direct
`single-table-data-agent` entry point). The planner delegates to the validated single-table flow;
the validator is a deterministic candidate selector, not another LLM call. Example 1-N (fan-out)
and N-N use the same shape. For N-N, define multiple roots, then make a merge node depend on all
required parents:

```json
{
  "question": "Compare the independently retrieved evidence",
  "nodes": [
    {"nodeId": "source-a", "agentId": "single-table-data-agent"},
    {"nodeId": "source-b", "agentId": "single-table-data-agent"},
    {"nodeId": "merge", "agentId": "sql-validator", "dependsOn": ["source-a", "source-b"]}
  ]
}
```

The coordinator rejects unknown Agents/dependencies, duplicate or unsafe node IDs, cycles, empty
questions, graphs larger than 16 nodes, and depth greater than 8 before calling any Agent. Each
node has a 15-second timeout and an organization has a 60-second budget; unfinished same-layer
siblings are cancelled after a failure or timeout. The graph is explicit: this version does not
automatically discover Agents, choose a topology, or guarantee semantic/database join behavior.
Single-root diamonds are classified as `CUSTOM_DAG`, not 1-1.

## Required runtime configuration

Supply these values through the process environment or Spring configuration (never commit secrets):

- `AGENT_LLM_BASE_URL`: OpenAI-compatible API base URL, optionally ending in `/chat/completions`.
- `AGENT_LLM_API_KEY`: API credential.
- `AGENT_LLM_MODEL`: model identifier.
- Optional `AGENT_LLM_REASONING_EFFORT` (default `high`; provider/model must support it).
- `AGENT_SINGLE_TABLE_NAME`: one approved MySQL table, optionally `database.table`.
- Optional `AGENT_SINGLE_TABLE_MAX_ROWS` (default 100, hard cap 1000).
- Optional `AGENT_SINGLE_TABLE_QUERY_TIMEOUT_SECONDS` (default 10).

The endpoint is not ready for business traffic until a real table is selected and configured.
The SQL compiler supports one selected column, DISTINCT, optional aggregation, AND filters, ordering,
and a bounded result limit. `GROUP BY` is not supported and must be clarified/rejected. LIKE binds
the pattern but `%` and `_` retain SQL wildcard meaning; escape them for literal matching. `IN`
accepts 1–100 bound values; larger lists are rejected. Results include returned-row count and a
truncation flag based on fetching one extra row beyond the limit.

## Security and next validation

Use a database account that is itself read-only and scoped to the configured table; the program
cannot prove grants of an externally configured account. `application-test.yaml` now uses local
defaults and environment variables rather than embedded credentials. Any previously committed
credentials must be rotated separately; this change does not rewrite Git history. Keep the model
API key outside source control. The runtime only creates `SELECT` statements and binds filter values;
column and table identifiers are resolved from server-side metadata/configuration. Before production,
the MariaDB4j end-to-end smoke test runs with a stub planner and no external service. Offline
WikiSQL regression/acceptance fixtures and per-request JSONL telemetry remain to be implemented.
Real WikiSQL/API evaluation is intentionally not run here; wait for code audit and explicit approval
before starting it.
