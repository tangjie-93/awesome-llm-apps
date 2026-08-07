# Self-Improving Agent Skills
# 自我改进的 Agent Skills

Automatically optimize your agent skills using a multi-agent system built with **Google ADK (Agent Development Kit)** and **Gemini**. Upload a skill, let the agents generate test scenarios and evaluation criteria, then watch as three specialized ADK agents collaborate to improve your skill through iterative optimization.

使用基于 **Google ADK（Agent Development Kit）** 和 **Gemini** 构建的多 Agent 系统，自动优化你的 agent skills。上传一个 skill，让 Agent 生成测试场景和评估标准，然后观察三个专用 ADK Agent 通过迭代优化协作改进你的 skill。

<img width="960" height="718" alt="Screenshot 2026-04-12 at 7 26 04 PM" src="https://github.com/user-attachments/assets/35a31f1a-398d-4797-a5d8-de538b4391e5" />

## How It Works
## 工作原理

This app implements an automated skill improvement loop inspired by Karpathy's autoresearch methodology, powered by a team of ADK agents:

该应用实现了一个自动化 skill 改进循环，灵感来自 Karpathy 的 autoresearch 方法，并由一组 ADK Agent 驱动：

1. **Upload**: Drop in your skill folder (following [agentskills.io](https://agentskills.io) spec)
1. **上传**：放入你的 skill 文件夹（遵循 [agentskills.io](https://agentskills.io) 规范）
2. **Configure**: The Executor agent generates test scenarios and evaluation criteria. Edit, add, or regenerate as needed
2. **配置**：Executor Agent 会生成测试场景和评估标准。你可以按需编辑、添加或重新生成
3. **Optimize**: Three ADK agents collaborate — one executes and scores, one diagnoses failures, one applies fixes
3. **优化**：三个 ADK Agent 协作工作，一个负责执行和打分，一个诊断失败原因，一个应用修复
4. **Results**: Download your improved skill with a detailed changelog
4. **结果**：下载改进后的 skill，并获得详细变更日志

### The ADK Agent Team
### ADK Agent 团队

| Agent | Role | What It Does |
|-------|------|-------------|
| **Executor** | Skill Runner & Scorer | Executes the skill against test scenarios, scores outputs against evaluation criteria, and generates initial test scenarios during analysis |
| **Executor** | Skill 运行器和评分器 | 使用测试场景执行 skill，根据评估标准给输出打分，并在分析阶段生成初始测试场景 |
| **Analyst** | Failure Diagnostician | Examines failed evaluations, identifies root causes, and recommends a mutation strategy. Uses Pydantic `output_schema` for guaranteed structured JSON |
| **Analyst** | 失败诊断器 | 检查失败评估，识别根因，并推荐变更策略。使用 Pydantic `output_schema` 保证结构化 JSON 输出 |
| **Mutator** | Prompt Editor | Makes exactly ONE targeted change to the skill prompt based on the analyst's diagnosis. Uses Pydantic `output_schema` for guaranteed structured JSON |
| **Mutator** | Prompt 编辑器 | 根据 Analyst 的诊断，对 skill prompt 进行一次精准修改。使用 Pydantic `output_schema` 保证结构化 JSON 输出 |

### The Optimization Loop
### 优化循环

- The **Executor** agent runs the skill against all test scenarios
- **Executor** Agent 会针对所有测试场景运行 skill
- The **Executor** then scores each output against binary yes/no evaluation criteria
- **Executor** 随后根据二元 yes/no 评估标准给每个输出打分
- The **Analyst** agent diagnoses failure patterns and picks a strategy (`add_example`, `add_constraint`, `restructure`, or `add_edge_case`)
- **Analyst** Agent 会诊断失败模式，并选择策略（`add_example`、`add_constraint`、`restructure` 或 `add_edge_case`）
- The **Mutator** agent applies ONE surgical fix to the skill prompt
- **Mutator** Agent 会对 skill prompt 应用一次外科手术式精准修复
- The **Executor** re-runs and re-scores the modified skill
- **Executor** 重新运行并重新评分修改后的 skill
- Changes are kept if the score improves, reverted if not
- 如果分数提升，则保留修改；否则回滚
- Repeats until the target pass rate is reached or max rounds hit
- 重复执行，直到达到目标通过率或触发最大轮数

## Architecture
## 架构

```text
self-improving-agent-skills/
├── backend/                 # FastAPI server + ADK optimization engine
│   ├── app.py              # REST API endpoints + SSE streaming
│   ├── adk_optimizer.py    # Multi-agent optimizer (Executor, Analyst, Mutator)
│   └── requirements.txt
├── frontend/               # Next.js + React + Tailwind
│   ├── src/
│   │   ├── app/            # Main page + layout
│   │   └── components/     # Upload, Config, Running, Results steps
│   ├── package.json
│   └── *.config.ts
│   ├── code-reviewer/
│   └── content-writer/
└── README.md
```

## Tech Stack
## 技术栈

- **Backend**: Python 3.10+, FastAPI, Google ADK, Pydantic
- **后端**：Python 3.10+、FastAPI、Google ADK、Pydantic
- **Frontend**: Next.js 15, React 19, Tailwind CSS v4, Recharts
- **前端**：Next.js 15、React 19、Tailwind CSS v4、Recharts
- **AI**: Google ADK multi-agent system with Gemini (`gemini-3-flash-preview`) — structured output via `output_schema` on Analyst and Mutator agents
- **AI**：使用 Gemini（`gemini-3-flash-preview`）的 Google ADK 多 Agent 系统，Analyst 和 Mutator Agent 通过 `output_schema` 输出结构化结果
- **Real-time**: Server-Sent Events (SSE) for live optimization progress
- **实时通信**：使用 Server-Sent Events（SSE）展示实时优化进度

## Quick Start
## 快速开始

### Backend Setup
### 后端配置

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment (optional — the app will prompt for your API key in the UI)
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# Run server
python app.py
# Server runs on http://localhost:8891
```

### Frontend Setup
### 前端配置

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
# App runs on http://localhost:3000
```

### Usage
### 使用方法

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)
1. 从 [Google AI Studio](https://aistudio.google.com/apikey) 获取 Gemini API Key
2. Open http://localhost:3000
2. 打开 http://localhost:3000
3. Upload a skill folder as a .zip file (or try an example)
3. 将 skill 文件夹以 .zip 文件形式上传（也可以试用示例）
4. Enter your Gemini API key
4. 输入你的 Gemini API Key
5. Review and edit the generated test scenarios and evaluation criteria
5. 查看并编辑生成的测试场景和评估标准
6. Click "Start Optimization" and watch the agents collaborate to improve your skill
6. 点击 "Start Optimization"，观察 Agent 协作改进你的 skill
7. Download your improved skill when complete
7. 完成后下载改进后的 skill

## Skill Format
## Skill 格式

Skills follow the [agentskills.io](https://agentskills.io) specification:

Skills 遵循 [agentskills.io](https://agentskills.io) 规范：

```text
my-skill/
├── SKILL.md           # Required: YAML frontmatter + instructions
├── scripts/           # Optional: executable code
├── references/        # Optional: additional docs
└── assets/            # Optional: templates, resources
```

Example SKILL.md:

示例 SKILL.md：

```markdown
---
name: my-skill
description: What this skill does and when to use it
license: MIT
metadata:
  author: your-name
  version: "1.0"
---

# My Skill

Your skill instructions here...
```

## Trying it
## 试用

Zip any skill folder and upload it — for instance this repo's own [project-graveyard](../project-graveyard/):

压缩任意 skill 文件夹并上传，例如本仓库自带的 [project-graveyard](../project-graveyard/)：

```bash
cd agent_skills
zip -r project-graveyard.zip project-graveyard/
```

The app's "examples" picker also lists sibling skills from this repo automatically — real skills, not toys.

应用中的 "examples" 选择器也会自动列出本仓库的同级 skills。这些是真实 skills，不是玩具示例。

## How the Multi-Agent Optimization Works
## 多 Agent 优化如何工作

### 1. Analysis Phase
### 1. 分析阶段

The **Executor** agent analyzes your skill and generates:

**Executor** Agent 会分析你的 skill 并生成：

- 3-4 diverse test scenarios
- 3-4 个多样化测试场景
- 4-6 binary evaluation criteria (yes/no questions)
- 4-6 个二元评估标准（yes/no 问题）

You can edit, add, or remove scenarios and criteria before optimization begins.

在优化开始前，你可以编辑、添加或删除测试场景和评估标准。

### 2. Baseline Run
### 2. 基线运行

The **Executor** agent runs the skill against all scenarios and scores each output against all evaluation criteria. This establishes the starting score.

**Executor** Agent 会针对所有场景运行 skill，并根据所有评估标准给每个输出打分。这会建立初始分数。

### 3. Optimization Loop
### 3. 优化循环

For each round, the three agents collaborate:

每一轮中，三个 Agent 会协作：

1. **Executor** runs the skill against all test scenarios and scores the outputs
1. **Executor** 针对所有测试场景运行 skill 并给输出打分
2. **Analyst** examines failures, identifies root cause, and selects a mutation strategy (returns structured JSON via `output_schema`)
2. **Analyst** 检查失败项，识别根因，并选择变更策略（通过 `output_schema` 返回结构化 JSON）
3. **Mutator** applies ONE specific change to improve the skill (returns structured JSON via `output_schema`)
3. **Mutator** 应用一个具体修改来改进 skill（通过 `output_schema` 返回结构化 JSON）
4. **Executor** re-runs and re-scores the modified skill
4. **Executor** 重新运行并重新评分修改后的 skill
5. Score is compared — keep the change if improved, revert if not
5. 比较分数，如果提升则保留修改，否则回滚
6. Repeat until target pass rate or max rounds reached
6. 重复执行，直到达到目标通过率或最大轮数

### 4. Output
### 4. 输出

- Improved SKILL.md with all successful changes applied
- 应用所有成功修改后的 SKILL.md
- Detailed changelog of what changed and why
- 详细变更日志，说明改了什么以及为什么改
- Performance comparison (baseline vs final)
- 性能对比（基线 vs 最终结果）

## API Endpoints
## API 端点

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/upload` | Upload skill zip file (max 10MB, text files only) |
| `POST` | `/api/upload` | 上传 skill zip 文件（最大 10MB，仅文本文件） |
| `POST` | `/api/upload-files` | Upload multiple files (folder upload) |
| `POST` | `/api/upload-files` | 上传多个文件（文件夹上传） |
| `POST` | `/api/analyze` | Generate scenarios and evals (requires Gemini API key) |
| `POST` | `/api/analyze` | 生成场景和评估标准（需要 Gemini API Key） |
| `POST` | `/api/regenerate` | Regenerate scenarios and evals |
| `POST` | `/api/regenerate` | 重新生成场景和评估标准 |
| `POST` | `/api/update-config` | Save user's selected/edited config |
| `POST` | `/api/update-config` | 保存用户选择或编辑后的配置 |
| `POST` | `/api/start/{session_id}` | Start optimization |
| `POST` | `/api/start/{session_id}` | 开始优化 |
| `GET` | `/api/stream/{session_id}` | SSE stream of optimization progress |
| `GET` | `/api/stream/{session_id}` | 优化进度的 SSE 流 |
| `POST` | `/api/stop/{session_id}` | Stop optimization |
| `POST` | `/api/stop/{session_id}` | 停止优化 |
| `GET` | `/api/download/{session_id}` | Download improved skill |
| `GET` | `/api/download/{session_id}` | 下载改进后的 skill |
| `GET` | `/api/examples` | List available example skills |
| `GET` | `/api/examples` | 列出可用示例 skills |
| `POST` | `/api/examples/{name}/load` | Load an example skill |
| `POST` | `/api/examples/{name}/load` | 加载示例 skill |
| `GET` | `/api/status/{session_id}` | Poll-based status endpoint |
| `GET` | `/api/status/{session_id}` | 基于轮询的状态端点 |
| `GET` | `/health` | Health check |
| `GET` | `/health` | 健康检查 |

## Configuration
## 配置

### Backend
### 后端

The Gemini API key is passed from the frontend with each request. Optionally set `GOOGLE_API_KEY` in `.env` for local development. Server runs on port **8891**.

Gemini API Key 会随每个请求从前端传给后端。本地开发时，也可以选择在 `.env` 中设置 `GOOGLE_API_KEY`。服务运行在 **8891** 端口。

Upload limits:

上传限制：

- **10MB** max total upload size
- 总上传大小最大 **10MB**
- **1MB** max per file
- 单个文件最大 **1MB**
- **50** max files per upload
- 每次最多上传 **50** 个文件
- Text files only (`.md`, `.txt`, `.json`, `.yaml`, `.py`, `.js`, `.ts`, etc.)
- 仅支持文本文件（`.md`、`.txt`、`.json`、`.yaml`、`.py`、`.js`、`.ts` 等）

Sessions expire after **1 hour** automatically.

Sessions 会在 **1 小时** 后自动过期。

### Frontend
### 前端

API key is entered in the UI, stored in component state (not persisted), and sent with each request. The key is passed to the backend which sets `GOOGLE_API_KEY` for ADK agent authentication.

API Key 在界面中输入，存储在组件状态中（不会持久化），并随每个请求发送。该 Key 会传给后端，由后端设置 `GOOGLE_API_KEY`，用于 ADK Agent 认证。

### Optimization Parameters
### 优化参数

In `RunningStep.tsx`, adjust `max_rounds` (capped at 50):

在 `RunningStep.tsx` 中调整 `max_rounds`（上限为 50）：

```typescript
body: JSON.stringify({
  max_rounds: 20,  // Default: 20, max: 50
}),
```

In `adk_optimizer.py`, adjust the model:

在 `adk_optimizer.py` 中调整模型：

```python
def __init__(self, api_key: str, model: str = "gemini-3-flash-preview"):
```

## Development
## 开发

### Backend Tests
### 后端测试

```bash
cd backend
python -c "from adk_optimizer import SkillOptimizer; print('OK')"
```

### Frontend Build
### 前端构建

```bash
cd frontend
npm run build
```

### Live Development
### 实时开发

Both servers support hot reload. Edit code and see changes immediately.

两个服务都支持热重载。修改代码后可以立即看到变化。

## Based on Karpathy's Autoresearch
## 基于 Karpathy 的 Autoresearch

This tool applies Andrej Karpathy's autoresearch methodology (using LLMs to iteratively improve their own prompts) to agent skills. The key insight: rather than manually tweaking prompts, define success criteria and let the AI optimize itself — now powered by a team of specialized ADK agents.

这个工具把 Andrej Karpathy 的 autoresearch 方法（使用 LLM 迭代改进自己的 prompts）应用到 agent skills 上。核心洞察是：与其手动调整 prompts，不如定义成功标准，让 AI 自我优化。现在，这个过程由一组专用 ADK Agent 驱动。

Original concept: [https://github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)

原始概念：[https://github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)
