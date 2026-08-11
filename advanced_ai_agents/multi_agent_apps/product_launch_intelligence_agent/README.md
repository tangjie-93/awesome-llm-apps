# 🚀 AI Product Launch Intelligence Agent
# 🚀 `AI` 产品发布情报智能体

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-multi-agent-product-launch-intelligence-app) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-multi-agent-product-launch-intelligence-app)，通过详细代码讲解、说明和最佳实践学习如何从零构建该应用。**

A **streamlined intelligence hub** for Go-To-Market (GTM) & Product-Marketing teams.
面向 `Go-To-Market`（`GTM`）和产品营销团队的**精简情报中心**。
Built with **Streamlit + Agno (GPT-4o) + Firecrawl**, the app turns scattered public-web data into concise, actionable launch insights.
该应用使用 **`Streamlit` + `Agno`（`GPT-4o`）+ `Firecrawl`** 构建，可将分散的公开网络数据转化为简洁、可执行的发布洞察。

## 3 Specialized Agents in Coordinated Team
## 协同团队中的 `3` 个专门智能体

| Tab<br>标签页 | What You Get<br>你将获得 |
|-----|--------------|
| **Competitor Analysis Agent**<br>**竞品分析智能体** | Evidence-backed breakdown of a rival's latest launches – positioning, differentiators, pricing cues & channel mix<br>基于证据拆解竞争对手的最新发布，包括定位、差异化因素、定价线索和渠道组合 |
| **Market Sentiment Agent**<br>**市场情绪智能体** | Consolidated social chatter & review themes split by 🚀 *positive* / ⚠️ *negative* drivers<br>汇总社交讨论和评论主题，并按 🚀 *正向* / ⚠️ *负向* 驱动因素拆分 |
| **Launch Metrics Agent**<br>**发布指标智能体** | Publicly available KPIs – adoption numbers, press coverage, qualitative "buzz" signals<br>公开可用的 `KPI`，包括采用数据、媒体报道和定性“热度”信号 |

Additional goodies:
其他亮点：

* 🔑 **Sidebar key input** – enter OpenAI & Firecrawl keys securely (type="password")
* 🔑 **侧边栏密钥输入** — 安全输入 `OpenAI` 和 `Firecrawl` 密钥（`type="password"`）
* 🧠 **Coordinated multi-agent team** – three expert agents work together for richer insight
* 🧠 **协同多智能体团队** — 三个专家智能体协作，提供更丰富的洞察
  * 🔍 Product Launch Analyst (GTM strategist)
  * 🔍 产品发布分析师（`GTM` 策略师）
  * 💬 Market Sentiment Specialist (consumer-perception guru)
  * 💬 市场情绪专家（消费者感知专家）
  * 📈 Launch Metrics Specialist (performance analyst)
  * 📈 发布指标专家（绩效分析师）
* ⚡ **Quick actions** – press **J/K/L** to trigger the three analyses without touching the UI
* ⚡ **快捷操作** — 按 **`J/K/L`** 即可触发三种分析，无需操作 `UI`
* 📑 **Auto-formatted Markdown reports** – bullet summary first, then expanded deep-dive
* 📑 **自动格式化的 `Markdown` 报告** — 先给出要点摘要，再展开深度分析
* 🛠️ **Sources section** – every report ends with the URLs that were crawled or searched
* 🛠️ **来源部分** — 每份报告末尾都会列出已抓取或搜索过的 `URL`

## 🛠️ Tech Stack
## 🛠️ 技术栈

| Layer<br>层级 | Details<br>详情 |
|-------|---------|
| Data<br>数据 | **Firecrawl** async search + crawl API<br>**`Firecrawl`** 异步搜索 + 抓取 `API` |
| Agents<br>智能体 | **Agno Team** (GPT-4o) with FirecrawlTools<br>使用 `FirecrawlTools` 的 **`Agno Team`**（`GPT-4o`） |
| UI<br>`UI` | **Streamlit** wide-layout, tabbed workflow<br>**`Streamlit`** 宽布局、标签页工作流 |
| LLM<br>`LLM` | **OpenAI GPT-4o**<br>**`OpenAI GPT-4o`** |

## 🚀 Quick Start
## 🚀 快速开始

1. **Clone** the repository
1. **克隆**仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/multi_agent_apps/product_launch_intelligence_agent
```

2. **Install** dependencies
2. **安装**依赖

```bash
pip install -r requirements.txt
```

3. **Provide API keys** (choose either option)
3. **提供 `API key`**（任选一种方式）

   • **Environment variables** – create a `.env` file:
   • **环境变量** — 创建 `.env` 文件：
   ```ini
   OPENAI_API_KEY=sk-************************
   FIRECRAWL_API_KEY=fc-************************
   ```
   • **In-app sidebar** – paste the keys into the secure text inputs
   • **应用内侧边栏** — 将密钥粘贴到安全文本输入框中

4. **Run the app**
4. **运行应用**

```bash
streamlit run product_launch_intelligence_agent.py
```

5. **Browse** to <http://localhost:8501> – you should see three analysis tabs.
5. **浏览** <http://localhost:8501>，你应该会看到三个分析标签页。

## 🕹️ Using the Application
## 🕹️ 使用应用

1. Enter **API keys** in the sidebar (or ensure they are in your environment).
1. 在侧边栏输入 **`API key`**（或确保它们已存在于你的环境中）。
2. Type a **company / product / hashtag** in the main input box.
2. 在主输入框中输入**公司 / 产品 / 话题标签**。
3. Pick a tab and hit the corresponding **Analyze** button – a spinner will appear while the coordinated team works.
3. 选择一个标签页并点击对应的 **Analyze** 按钮，协同团队工作时会显示加载指示器。
4. Review the two-part analysis:
4. 查看由两部分组成的分析：
   * Bullet list of key findings
   * 关键发现的项目符号列表
   * Expanded, richly-formatted report (tables, call-outs, recommendations)
   * 展开的丰富格式报告（表格、重点提示、建议）

## 🤖 How the Coordinated Team Works
## 🤖 协同团队如何工作

The application uses a **coordinated team approach** where three specialized agents work together:
该应用采用**协同团队方式**，由三个专门智能体共同工作：

- **Product Launch Analyst**: Evaluates competitive positioning, launch strategies, strengths, and weaknesses
- **产品发布分析师**：评估竞争定位、发布策略、优势和劣势
- **Market Sentiment Specialist**: Analyzes social media sentiment, customer feedback, and brand perception
- **市场情绪专家**：分析社交媒体情绪、客户反馈和品牌感知
- **Launch Metrics Specialist**: Tracks KPIs, adoption rates, press coverage, and performance indicators
- **发布指标专家**：跟踪 `KPI`、采用率、媒体报道和绩效指标

The team coordinates based on the analysis type requested, ensuring the most appropriate agent handles each task while maintaining consistency and comprehensive coverage across all analysis types.
团队会根据请求的分析类型进行协调，确保最合适的智能体处理每项任务，同时在所有分析类型中保持一致性和全面覆盖。
