# 🔍 AI SEO Audit Team
# 🔍 AI SEO 审计团队

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-seo-audit-team-with-gemini) and learn how to build this AI SEO Audit Team from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-seo-audit-team-with-gemini)，通过详细代码讲解、说明和最佳实践，学习如何从零构建这个 `AI SEO Audit Team`。**

The **AI SEO Audit Team** is an autonomous, multi-agent workflow built with Google ADK.
**`AI SEO Audit Team`** 是一个基于 `Google ADK` 构建的自主多智能体工作流。

It takes a webpage URL, crawls the live page, researches real-time SERP competition, and produces a polished, prioritized SEO optimization report.
它接收网页 `URL`，抓取实时页面，研究实时 `SERP` 竞争情况，并生成一份完善且按优先级排列的 `SEO` 优化报告。

The app uses **Firecrawl via MCP (Model Context Protocol)** for accurate page scraping and Google's Gemini 2.5 Flash for analysis and reporting.
该应用使用 **通过 `MCP`（`Model Context Protocol`）调用的 `Firecrawl`** 进行准确页面抓取，并使用 `Google Gemini 2.5 Flash` 进行分析和报告生成。

## Features
## 功能

- **End-to-End On-Page SEO Evaluation**
- **端到端页面内 SEO 评估**
  - Automated crawl of any public URL (Firecrawl MCP)
  - 自动抓取任意公开 `URL`（`Firecrawl MCP`）
  - Structured audit of titles, headings, content depth, internal/external links, and technical signals
  - 对标题、页面标题层级、内容深度、内部/外部链接和技术信号进行结构化审计
- **Competitive SERP Intelligence**
- **竞争性 SERP 情报**
  - Google Search research for the inferred primary keyword
  - 针对推断出的主关键词进行 `Google Search` 研究
  - Analysis of top competitors, content formats, title patterns, and common questions
  - 分析主要竞争对手、内容格式、标题模式和常见问题
- **Actionable Recommendations**
- **可执行建议**
  - Prioritized optimization roadmap with rationale and expected impact
  - 带理由和预期影响的优先级优化路线图
  - Keyword strategy, schema opportunities, internal linking ideas, and measurement plan
  - 关键词策略、`schema` 机会、内链想法和衡量计划
  - Clean Markdown report ready for stakeholders or ticket creation
  - 可直接面向利益相关者或用于创建工单的清晰 `Markdown` 报告
- **ADK Dev UI Integration**
- **ADK Dev UI 集成**
  - Trace view of each agent step (crawl → SERP → report)
  - 每个智能体步骤的 `Trace` 视图（抓取 → `SERP` → 报告）
  - Easy environment variable management through `.env`
  - 通过 `.env` 轻松管理环境变量

## Agent Workflow
## 智能体工作流

| Step<br>步骤 | Agent<br>智能体 | Responsibilities<br>职责 |
| --- | --- | --- |
| 1<br>`1` | **Page Auditor Agent**<br>**页面审计智能体** | Calls `firecrawl_scrape`, inspects page structure, summarizes technical/content signals, and infers target keywords.<br>调用 `firecrawl_scrape`，检查页面结构，总结技术/内容信号，并推断目标关键词。 |
| 2<br>`2` | **Serp Analyst Agent**<br>**SERP 分析智能体** | Consumes the SERP data, extracts patterns, opportunities, PAA questions, and differentiation angles.<br>使用 `SERP` 数据，提取模式、机会、`PAA` 问题和差异化角度。 |
| 3<br>`3` | **Optimization Advisor Agent**<br>**优化顾问智能体** | Combines audit + SERP insights into a Markdown report with clear priorities and next steps.<br>将审计和 `SERP` 洞察合并为一份 `Markdown` 报告，其中包含清晰优先级和后续步骤。 |

All agents run sequentially using ADK’s `SequentialAgent`, passing state between stages via the shared session.
所有智能体都使用 `ADK` 的 `SequentialAgent` 顺序运行，并通过共享会话在阶段之间传递状态。

## Requirements
## 要求

### System Requirements
### 系统要求

- **Python 3.10+** for Google ADK
- **Python 3.10+** 用于 `Google ADK`
- **Node.js** (for Firecrawl MCP server via npx)
- **Node.js**（用于通过 `npx` 运行 `Firecrawl MCP server`）

### Python Dependencies
### Python 依赖

Install the Python dependencies:
安装 `Python` 依赖：

```bash
pip install -r requirements.txt
```

### API Keys
### API 密钥

You will need valid API keys:
你需要有效的 `API` 密钥：

- `GOOGLE_API_KEY` – Gemini (Google AI Studio) for LLM + Google Search
- `GOOGLE_API_KEY` – 用于 `LLM` + `Google Search` 的 `Gemini`（`Google AI Studio`）
- `FIRECRAWL_API_KEY` – Firecrawl MCP server ([get one here](https://firecrawl.dev/app/api-keys))
- `FIRECRAWL_API_KEY` – `Firecrawl MCP server`（[在这里获取](https://firecrawl.dev/app/api-keys)）

Set your environment variables (e.g., add to your shell profile or `export` in your terminal):
设置你的环境变量（例如添加到 shell 配置文件，或在终端中使用 `export`）：

```bash
export GOOGLE_API_KEY=your_gemini_key
export FIRECRAWL_API_KEY=your_firecrawl_key
```

Alternatively, you can put these in a `.env` file if you prefer.
或者，如果你愿意，也可以把这些变量放入 `.env` 文件。

## Running the App with ADK Dev UI
## 使用 ADK Dev UI 运行应用

1. **Activate your environment** (optional but recommended):
1. **激活你的环境**（可选但推荐）：
   ```bash
   cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_seo_audit_team
   ```

2. **Install dependencies** (if not already):
2. **安装依赖**（如果尚未安装）：
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the ADK web UI** from the project root:
3. 从项目根目录**启动 ADK web UI**：
   ```bash
   adk web
   ```

4. In the UI:
4. 在 `UI` 中：
   - Select the `ai_seo_audit_team` app.
   - 选择 `ai_seo_audit_team` 应用。
   - Provide the target URL when prompted.
   - 出现提示时提供目标 `URL`。
   - Watch the agents execute in the **Trace** panel (Firecrawl → Google Search → Report).
   - 在 **Trace** 面板中观察智能体执行（`Firecrawl` → `Google Search` → 报告）。

## Usage Tips
## 使用提示

- Ensure the target URL is publicly accessible without auth requirements.
- 确保目标 `URL` 可公开访问，且无需认证。
- The workflow is optimized for a single URL per run; start a new session for each distinct audit.
- 该工作流针对每次运行一个 `URL` 进行了优化；每次不同审计请启动一个新会话。
- The final report can be copied directly into docs, tickets, or shared with stakeholders.
- 最终报告可以直接复制到文档、工单中，或分享给利益相关者。

## Folder Structure
## 文件夹结构

```
ai_seo_audit_team/
├── agent.py          # Multi-agent workflow definitions
├── requirements.txt  # Minimal dependencies
├── __init__.py       # Module initialization
└── README.md         # You are here
```

## Next Steps & Extensibility
## 后续步骤与可扩展性

- Add automated evaluations via ADK Eval Sets for regression testing.
- 通过 `ADK Eval Sets` 添加自动化评估，用于回归测试。
- Hook the Markdown report into Slack/email connectors or ticketing systems.
- 将 `Markdown` 报告接入 `Slack`/邮件连接器或工单系统。
- Swap in alternative SERP providers (Serper, Tavily) if you prefer non-Google search APIs.
- 如果你更偏好非 `Google Search API`，可以替换为其他 `SERP` 提供商（`Serper`、`Tavily`）。
- Extend the workflow with additional agents (e.g., content brief generator, schema builder) using the shared session state.
- 使用共享会话状态，通过额外智能体扩展工作流（例如内容简报生成器、`schema builder`）。

Happy auditing! 🚀
审计愉快！🚀
