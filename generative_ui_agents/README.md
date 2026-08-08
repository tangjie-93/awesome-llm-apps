# 🖼️ Generative UI and Agentic Frontends

**Agents that render UI — not just text.**

Generative UI (Gen UI) apps let an LLM emit rich, interactive frontend components instead of (or in addition to) plain chat messages. The model decides *what to show*, the frontend renders real components, and the user can click, edit, and respond — closing the loop between reasoning and interface.

This section collects self-contained templates for building Gen UI apps across the common stacks:

- **AG-UI / CopilotKit** — streaming agent ↔ UI protocol for React apps
- **Vercel AI SDK** — `streamUI` / React Server Components generative UI
- **LangChain / LangGraph UI** — structured tool calls rendered as components
- **Custom tool-call → component renderers** — minimal DIY patterns in any framework

## 中文对照

### 生成式 UI 与智能体前端

智能体不仅生成文本，也可以直接生成和操作界面。生成式 UI 应用允许大模型输出交互式前端组件，前端负责渲染真实组件，用户可以点击、编辑并反馈，从而形成完整的人机交互闭环。

本目录收集了基于 AG-UI/CopilotKit、Vercel AI SDK、LangChain/LangGraph 以及自定义工具调用渲染器的生成式 UI 示例。
