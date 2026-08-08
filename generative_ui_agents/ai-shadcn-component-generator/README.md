# AI Shadcn Component Generator

> Ported from the upstream [CopilotKit/shadify](https://github.com/CopilotKit/shadify) repository.

Describe a UI in plain English. Get a live, interactive [shadcn/ui](https://ui.shadcn.com/) component back. Export it as clean React code.

https://github.com/user-attachments/assets/b14bebd6-527a-48bd-94f5-d27fea8808aa

**Gen UI concept — schema-driven component composition.** The full shadcn component schema is passed as agent context, so the model knows exactly which primitives exist, what props they take, and how they nest. The agent's "output" is a structured tree of those primitives — streamed to the browser, mounted as real React, exportable as code. The design system is the action space.

## Built With

- **[shadcn/ui](https://ui.shadcn.com/)** — The AI composes from real shadcn components (cards, charts, forms, menus, layouts). Every generated component is accessible, polished, and uses the same primitives you'd `npx shadcn add` into your own project.
- **[CopilotKit](https://github.com/CopilotKit/CopilotKit)** — Streams structured UI from the agent to the browser in real time. Passes the full component schema as agent context so the model knows exactly what it can build.
- **[AG-UI](https://github.com/ag-ui-protocol/ag-ui)** — The agent ↔ UI protocol that carries tool calls and component instructions between the LangGraph backend and the React frontend.
- **[LangGraph](https://www.langchain.com/langgraph)** — Powers the agent backend. Handles reasoning, tool use (web search, site extraction via Tavily), and conversation memory across turns.
- **[Render](https://render.com/)** — All three services deploy from a single `render.yaml` Blueprint. Render wires service URLs together automatically via `fromService` references — push to `main` and you're live.

## Architecture

Three services in a pnpm monorepo:

```
UI (React + Vite)  →  Runtime (Hono + CopilotKit)  →  Agent (FastAPI + LangGraph)
```

| Service | Path | What it does |
|---|---|---|
| `ui` | `apps/ui` | Chat interface, component rendering, code export |
| `runtime` | `apps/runtime` | CopilotKit runtime, routes messages to the agent |
| `agent` | `apps/agent` | LangGraph agent with search tools, returns structured UI |

## Quick Start

```bash
pnpm install
```

Add your keys:

```bash
# apps/runtime/.env
OPENAI_API_KEY=sk-...

# apps/agent/.env
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...
```

```bash
pnpm dev
```

UI runs at [localhost:5173](http://localhost:5173). Runtime on 4000, agent on 8123.

## Deploy

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

Or connect your repo — `render.yaml` defines everything.

## 中文对照

### AI Shadcn 组件生成器

用户可以用自然语言描述 UI，系统会生成可实时交互的 shadcn/ui 组件，并导出干净的 React 代码。智能体使用完整的组件 Schema 作为上下文，将结构化组件树流式传输到浏览器。

项目由 shadcn/ui、CopilotKit、AG-UI、LangGraph 和 Render 构成，采用 pnpm monorepo 结构，包含 UI、Runtime 和 Agent 三个服务。
