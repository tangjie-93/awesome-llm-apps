# AI Dashboard Canvas Agent

https://github.com/user-attachments/assets/9201d528-573f-43cc-9d31-571c362318a7

---

An agent that populates **live charts, metrics, and real-time data** into a Canvas dashboard instead of just streaming text. Built with [CopilotKit](https://github.com/CopilotKit/CopilotKit), [AG-UI](https://github.com/ag-ui-protocol/ag-ui), and Google's [ADK](https://google.github.io/adk-docs/).

**Gen UI concept — agentic canvas.** The chat is a thin sidebar; the real surface is a persistent Canvas the agent writes into. Charts, KPIs, and panels are addressable artifacts the agent can place, update, and rearrange across turns — closer to a collaborator using a whiteboard than a chatbot returning replies.

---

## 🔧 Quickstart

```bash
# from the awesome-llm-apps repo root
cd generative_ui_agents/ai-dashboard-canvas-agent

# install JS deps + agent
pnpm install        # or npm/yarn/bun

# install Python deps separately for the ADK agent
pnpm install:agent

# set your Google API key
cp .env.example .env
# edit .env and set GOOGLE_API_KEY=...

# start UI + agent together
pnpm run dev
```

### 📦 Prerequisites

- Node.js 18+
- Python 3.8+
- Google Makersuite API Key → get one [here](https://makersuite.google.com/)
- Any package manager (pnpm recommended)

💡 Lockfiles (`package-lock.json`, `yarn.lock`, etc.) are gitignored — each dev manages their own.

---

### 🛠 Available Scripts

- `dev` → Start UI + agent (default)
- `dev:debug` → Start with debug logging
- `dev:ui` → Run just the Next.js app
- `dev:agent` → Run just the ADK agent
- `build / start` → Production build + server
- `lint` → Run ESLint
- `install:agent` → Install Python deps inside `agent/.venv`

---

### 🎨 Customization

- **Main UI** → `src/app/page.tsx`
- Change theme/colors and sidebar appearance
- Add new visualization components
- Extend agent logic in `/agent`

---

### 📚 Docs

- [ADK](https://google.github.io/adk-docs/)
- [CopilotKit](https://github.com/CopilotKit/CopilotKit)
- [AG-UI](https://docs.ag-ui.com/introduction)

## 中文对照

### AI 仪表盘画布智能体

该项目让智能体将实时图表、指标和数据填充到 Canvas 仪表盘中，而不是只输出文本。聊天区域是侧边栏，持久化 Canvas 才是主要工作区；智能体可以跨轮次创建、更新和排列图表、KPI 与面板。

快速开始需要安装 Node.js、Python 和 Google API Key，然后安装依赖、配置 `.env`，最后运行 `pnpm run dev`。
