# RSI Data Spring Boot — Agent v0.01

This local v0.01 task result delivers the single-table Agent and explicit Agent-organization
framework. WikiSQL dataset evaluation, business-table evaluation, production deployment, and
per-request JSONL telemetry are outside this version. No real dataset/API run is part of this
release.

Java 8 / Spring Boot 2.1.9 multi-module backend for the RSI data platform. The repository contains shared core, data access, integration, Flow, web, and starter modules. The `core-starter` module is the runnable Spring Boot application.

## Build and test

Install a JDK 8 and Maven 3.x. If the project requires a private Maven mirror, configure it in your local Maven `settings.xml` (do not commit credentials or machine-specific settings).

From the repository root:

```bash
mvn -s /path/to/settings.xml -pl core-test -am test
```

The `core-test` suite includes a local MariaDB4j end-to-end check from schema inspection through
the REST controller. Its planner is a fixed stub; it does not call an LLM or connect to a business
database.

Omit `-s` when Maven is already configured. To package the runnable application:

```bash
mvn -s /path/to/settings.xml -pl core-starter -am package -DskipTests
```

## Agent API

The starter exposes a single-table data Agent and a DAG coordinator for explicit Agent organizations:

- `POST /api/agent/single-table/query` — run one natural-language query against the configured table.
- `GET /api/agent/organization/agents` — list registered Agent IDs and capabilities.
- `POST /api/agent/organization/execute` — execute a bounded 1-1, 1-N, N-N, or custom DAG.

The single-table Agent asks the model for a structured query plan; Java validates identifiers against database metadata and compiles a parameterized, read-only query. The registry includes schema-linker, sql-planner, and sql-validator roles. The coordinator passes dependency results downstream and selects the highest-confidence successful terminal SQL candidate (ties use request order); graph structure remains caller-supplied. See [AGENT_FRAMEWORK.md](AGENT_FRAMEWORK.md) for request examples, execution behavior, and security boundaries.

## Runtime configuration

`core-starter/src/main/resources/application.yaml` reads model and table settings from process environment variables. Configure these outside source control:

```text
AGENT_LLM_BASE_URL=<OpenAI-compatible endpoint>
AGENT_LLM_API_KEY=<secret>
AGENT_LLM_MODEL=<model id>
AGENT_LLM_REASONING_EFFORT=high
AGENT_SINGLE_TABLE_NAME=<approved table>
AGENT_SINGLE_TABLE_MAX_ROWS=100
AGENT_SINGLE_TABLE_QUERY_TIMEOUT_SECONDS=10
```

Spring Boot does not automatically load a plain `.env` file. Export the variables into the process environment or configure an explicit local environment loader before starting the application. Use a database account scoped to read-only access for the configured table; keep credentials out of tracked configuration files.

On PowerShell, a local launch after setting the required environment variables can use:

```powershell
$env:AGENT_LLM_BASE_URL = 'https://your-openai-compatible-endpoint/v1'
$env:AGENT_LLM_API_KEY = '...'
$env:AGENT_LLM_MODEL = '...'
$env:AGENT_SINGLE_TABLE_NAME = 'your_database.your_table'
mvn -pl core-starter -am spring-boot:run
```

No WikiSQL data/API run is part of build or startup. WikiSQL regression and acceptance harnesses
are not yet wired into this Java project; do not launch live dataset evaluation until the audit and
explicit approval.

## Related repositories

- [RSI Data Platform](../rsi-data-platform/README.md) — Next.js front end.
- [RSI Data Visual](../rsi-data-visual/Readme.md) — `@horsecoder/visual-core` component package and local consumption instructions.
