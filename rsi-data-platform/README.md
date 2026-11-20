# RSI Data Platform

基于 Next.js App Router 的数据平台前端。当前应用入口为登录页，主要页面代码位于 `src/xpages`；平台通过本地 workspace 包 `node_horsecoder/@horsecoder/flow` 集成流程可视化能力。

## 环境要求

- Node.js（建议使用当前 LTS）
- pnpm（仓库包含 `pnpm-lock.yaml` 和 `pnpm-workspace.yaml`）

## 本地开发

在项目根目录运行：

```bash
pnpm install --frozen-lockfile
pnpm dev
```

打开 <http://localhost:3000>。登录页入口是 `app/page.tsx`，页面组件与样式位于 `src`。

常用命令：

```bash
pnpm lint
pnpm build
pnpm start
```

## 项目协作

平台使用 `@horsecoder/flow` 本地 workspace 包。修改该包时，依赖路径和 workspace 配置都在本仓库内；安装依赖时优先使用 pnpm，避免与 npm/yarn lockfile 混用。

独立可视化核心包 `@horsecoder/visual-core` 的构建、打包产物和外部项目引用方法，见 [rsi-data-visual README](../rsi-data-visual/Readme.md)。后端 Spring Boot 服务的启动配置及 Agent API 见 [rsi-data-spring-boot README](../rsi-data-spring-boot/README.md) 和 [Agent 框架说明](../rsi-data-spring-boot/AGENT_FRAMEWORK.md)。

## 技术栈

Next.js、React、TypeScript、Ant Design、Redux Toolkit 和 Tailwind CSS。具体版本以 `package.json` 为准。
