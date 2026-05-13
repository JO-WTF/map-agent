# Frontend Workbench Scaffold

已实现：
- `/workbench` 页面骨架
- SSE 客户端（POST `/api/chat/stream` + ReadableStream）
- Zustand 状态层（chat/agentRun/task/result）
- 事件解析与分发（`parseSseEvent` + `handleAgentEvent`）

建议初始化 Next.js：
```bash
cd frontend
npx create-next-app@latest . --ts --tailwind --app
npm i zustand
```
