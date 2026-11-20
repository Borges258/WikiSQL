# RSI Data Visual

`@horsecoder/visual-core` 是 React 流程图/数据可视化组件库。本仓库通过 Rollup 将 `src/index.ts` 构建为 CommonJS 包，供其他前端项目本地依赖使用。发布入口和类型声明分别由 `package.json` 的 `main`、`types` 字段定义。

## 本地引用打包产物（dist）

## 1. 构建本项目

在本项目根目录执行：

```bash
yarn install
yarn build
```

修改源码后动态调试可运行 `yarn build:lib --watch`，保持该命令运行即可持续更新 `dist`。构建产物 `dist` 与类型声明 `types` 是包的发布文件。

## 2. 在使用方项目添加本地依赖

在使用方项目的 `package.json` 中，将依赖路径设为**本项目根目录**（不是 `dist` 目录）：

```json
{
  "dependencies": {
    "@horsecoder/visual-core": "file:../rsi-data-visual"
  }
}
```

相对路径从使用方项目目录解析，也可改为本机绝对路径；示例假设两个仓库目录同级。保存后在使用方项目运行 `yarn install`，代码通过 `import VisualDiagram from '@horsecoder/visual-core'` 引用。

动态调试希望改动自动同步时，使用 `yarn link`（先在本项目运行 `yarn link`，再在使用方运行 `yarn link @horsecoder/visual-core`），并在本项目保持 `yarn build:lib --watch` 运行。使用方还需监听链接包的变化，并确保双方使用同一份 React。该包将 React 和 React DOM 声明为 peer dependency；请使用兼容版本，避免重复安装 React 导致 Hooks 或组件上下文异常。

## 相关项目

- [RSI Data Platform](../rsi-data-platform/README.md)：Next.js 平台前端。
- [RSI Data Spring Boot](../rsi-data-spring-boot/README.md)：后端服务及 Agent API。
