# 📊 AI VC Due Diligence Agent Team
# 📊 `AI VC` 尽职调查代理团队

A multi-agent AI pipeline for startup investment analysis, built with [Google ADK](https://google.github.io/adk-docs/), Gemini 3 Pro, Gemini 3 Flash and Nano Banana Pro.
一个用于初创公司投资分析的多代理 `AI` 流水线，基于 [Google ADK](https://google.github.io/adk-docs/)、`Gemini 3 Pro`、`Gemini 3 Flash` 和 `Nano Banana Pro` 构建。

**Works with any startup** - from early-stage unknowns to well-funded companies. Just provide a company name, website URL, or both.
**适用于任何初创公司** - 从早期不知名公司到资金充足的公司都可以。只需提供公司名称、网站 `URL`，或两者都提供。

## Features
## 功能

- 🔍 **Live Research** - Real-time web search for company and market data
- 🔍 **实时研究** - 实时网页搜索公司和市场数据
- 🌐 **URL Support** - Analyze any startup by their website URL
- 🌐 **`URL` 支持** - 通过网站 `URL` 分析任何初创公司
- 📈 **Revenue Charts** - Bear/Base/Bull projection charts with matplotlib
- 📈 **收入图表** - 使用 `matplotlib` 生成熊市/基准/牛市预测图表
- 🧠 **Deep Risk Analysis** - Comprehensive risk assessment across 5 categories
- 🧠 **深度风险分析** - 覆盖 `5` 个类别的综合风险评估
- 📄 **Professional Reports** - McKinsey-style HTML investment reports
- 📄 **专业报告** - `McKinsey` 风格的 `HTML` 投资报告
- 🎨 **Visual TL;DR** - AI-generated infographic summary for quick review
- 🎨 **可视化 `TL;DR`** - `AI` 生成的信息图摘要，便于快速审阅

## What It Does
## 它能做什么

Given a startup name or URL, the pipeline automatically:
给定初创公司名称或 `URL` 后，流水线会自动：

1. **Researches the company** - Founders, funding, product, traction
1. **研究公司** - 创始人、融资、产品、增长势头
2. **Analyzes the market** - TAM/SAM, competitors, positioning
2. **分析市场** - `TAM/SAM`、竞争对手、定位
3. **Builds financial models** - Revenue projections, unit economics
3. **构建财务模型** - 收入预测、单位经济模型
4. **Assesses risks** - Market, execution, financial, regulatory, exit
4. **评估风险** - 市场、执行、财务、监管、退出
5. **Generates investor memo** - Structured investment thesis
5. **生成投资人备忘录** - 结构化投资论点
6. **Creates HTML report** - Professional due diligence document
6. **创建 `HTML` 报告** - 专业尽职调查文档
7. **Generates infographic** - Visual summary for quick review
7. **生成信息图** - 便于快速审阅的可视化摘要

## Quick Start
## 快速开始

### 1. Clone & Navigate
### 1. 克隆并进入目录
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/advanced_ai_agents/multi_agent_apps/agent_teams/ai_vc_due_diligence_agent_team
```

### 2. Set Environment
### 2. 设置环境
```bash
export GOOGLE_API_KEY=your_api_key
# Or create .env file:
echo "GOOGLE_API_KEY=your_api_key" > .env
```

### 3. Install & Run
### 3. 安装并运行
```bash
pip install -r requirements.txt
adk web
```

### 4. Try It
### 4. 试用

Works with company names, URLs, or both:
支持公司名称、`URLs`，或两者同时使用：

Open `http://localhost:8000` and try:
打开 `http://localhost:8000` 并尝试：

- *"Analyze https://agno.com for Series A investment of $30-50M"*
- *“分析 `https://agno.com`，评估 `$30-50M` 的 `Series A` 投资”*
- *"Research Genspark AI for its next funding round"*
- *“研究 `Genspark AI` 的下一轮融资”*
- *"Analyze Lovable for Series C funding opportunities"*
- *“分析 `Lovable` 的 `Series C` 融资机会”*
- *"Research emergent.sh for Series B funding in the $40-60M range"*
- *“研究 `emergent.sh` 在 `$40-60M` 区间的 `Series B` 融资”*


## Pipeline Architecture
## 流水线架构

```
User Query: "Analyze https://agno.com for Series A"
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│              DueDiligencePipeline (SequentialAgent)             │
│                                                                 │
│  ┌─────────────┐    ┌────────────────┐    ┌──────────────────┐  │
│  │  Stage 1    │    │    Stage 2     │    │     Stage 3      │  │
│  │  Company    │───▶│    Market      │───▶│    Financial     │  │
│  │  Research   │    │    Analysis    │    │    Modeling      │  │
│  └─────────────┘    └────────────────┘    └──────────────────┘  │
│         │                   │                      │            │
│         ▼                   ▼                      ▼            │
│  ┌─────────────┐    ┌────────────────┐    ┌──────────────────┐  │
│  │  Stage 4    │    │    Stage 5     │    │     Stage 6      │  │
│  │    Risk     │───▶│   Investor     │───▶│     Report       │  │
│  │ Assessment  │    │     Memo       │    │    Generator     │  │
│  └─────────────┘    └────────────────┘    └──────────────────┘  │
│                                                    │            │
│                                                    ▼            │
│                                          ┌──────────────────┐   │
│                                          │     Stage 7      │   │
│                                          │   Infographic    │   │
│                                          │    Generator     │   │
│                                          └──────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
Artifacts: revenue_chart.png, investment_report.html, infographic.png
```

---

## Agent Details
## 代理详情

### Stage 1: Company Research Agent
### 阶段 1：公司研究代理

**Purpose:** Gathers comprehensive company information through web search.
**目的：** 通过网页搜索收集全面的公司信息。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-flash-preview` |
| Tools<br>工具 | `google_search` |
| Output Key<br>输出键 | `company_info` |

**What it researches:**
**研究内容：**

- **Company Basics** - What they do, founding date, HQ location, team size
- **公司基础信息** - 业务内容、成立日期、总部位置、团队规模
- **Founders & Team** - Key people, backgrounds, LinkedIn profiles
- **创始人与团队** - 关键人物、背景、`LinkedIn` 资料
- **Product/Technology** - Core offering, how it works, target customers
- **产品/技术** - 核心产品、工作方式、目标客户
- **Funding History** - Rounds raised, investors, amounts
- **融资历史** - 已完成轮次、投资方、金额
- **Traction** - Customers, partnerships, growth signals
- **增长势头** - 客户、合作伙伴、增长信号
- **Recent News** - Press coverage, product launches, announcements
- **近期新闻** - 媒体报道、产品发布、公告

**For early-stage startups:** Checks website, LinkedIn, Crunchbase, AngelList, founder interviews, and notes when information is limited.
**对于早期初创公司：** 检查网站、`LinkedIn`、`Crunchbase`、`AngelList`、创始人访谈，并在信息有限时注明。

---

### Stage 2: Market Analysis Agent
### 阶段 2：市场分析代理

**Purpose:** Analyzes market size, competition, and positioning.
**目的：** 分析市场规模、竞争和定位。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-flash-preview` |
| Tools<br>工具 | `google_search` |
| Input<br>输入 | `{company_info}` |
| Output Key<br>输出键 | `market_analysis` |

**What it analyzes:**
**分析内容：**

- **Market Size** - TAM, SAM, growth rate from industry reports
- **市场规模** - 来自行业报告的 `TAM`、`SAM`、增长率
- **Competitors** - Who else is in the space, their funding/traction
- **竞争对手** - 该领域还有哪些公司，以及它们的融资和增长势头
- **Positioning** - How the company differentiates
- **定位** - 公司如何实现差异化
- **Trends** - Market drivers, emerging tech, regulatory changes
- **趋势** - 市场驱动因素、新兴技术、监管变化

**For early-stage:** Focuses on broader market category, identifies well-funded competitors, looks for market validation signals.
**对于早期公司：** 聚焦更广泛的市场类别，识别资金充足的竞争对手，并寻找市场验证信号。

---

### Stage 3: Financial Modeling Agent
### 阶段 3：财务建模代理

**Purpose:** Builds revenue projections and generates financial charts.
**目的：** 构建收入预测并生成财务图表。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-pro-preview` |
| Tools<br>工具 | `generate_financial_chart` |
| Input<br>输入 | `{company_info}`, `{market_analysis}` |
| Output Key<br>输出键 | `financial_model` |

**What it calculates:**
**计算内容：**

- **Current Metrics** - Estimated ARR, growth stage
- **当前指标** - 估算 `ARR`、增长阶段
- **Growth Scenarios** (5-year projections):
- **增长情景**（`5` 年预测）：
  - Bear Case: Conservative growth rates
  - 熊市情景：保守增长率
  - Base Case: Expected trajectory
  - 基准情景：预期轨迹
  - Bull Case: Optimistic scenario
  - 牛市情景：乐观情景
- **Return Analysis** - Exit valuations, MOIC, IRR estimates
- **回报分析** - 退出估值、`MOIC`、`IRR` 估算

**Stage benchmarks:**
**阶段基准：**

- Seed: $0.1-0.5M ARR, 3-5x growth
- 种子轮：`$0.1-0.5M ARR`，`3-5x` 增长
- Series A: $1-3M ARR, 2-3x growth
- `Series A`：`$1-3M ARR`，`2-3x` 增长
- Series B: $5-15M ARR, 1.5-2x growth
- `Series B`：`$5-15M ARR`，`1.5-2x` 增长

**Artifact:** Saves `revenue_chart_TIMESTAMP.png` with Bear/Base/Bull projections.
**制品：** 保存包含熊市/基准/牛市预测的 `revenue_chart_TIMESTAMP.png`。

---

### Stage 4: Risk Assessment Agent
### 阶段 4：风险评估代理

**Purpose:** Conducts deep risk analysis across multiple categories.
**目的：** 跨多个类别开展深度风险分析。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-pro-preview` |
| Tools<br>工具 | None<br>无（扩展推理） |
| Input<br>输入 | `{company_info}`, `{market_analysis}`, `{financial_model}` |
| Output Key<br>输出键 | `risk_assessment` |

**Risk categories analyzed:**
**分析的风险类别：**

1. **Market Risk** - Competition, timing, adoption barriers
1. **市场风险** - 竞争、时机、采用障碍
2. **Execution Risk** - Team gaps, technology challenges, scaling
2. **执行风险** - 团队短板、技术挑战、扩张
3. **Financial Risk** - Burn rate, fundraising, unit economics
3. **财务风险** - 烧钱速度、融资、单位经济模型
4. **Regulatory Risk** - Compliance, legal, geopolitical
4. **监管风险** - 合规、法律、地缘政治
5. **Exit Risk** - Acquirer landscape, IPO viability
5. **退出风险** - 潜在收购方格局、`IPO` 可行性

**For each risk provides:**
**每项风险提供：**

- Severity (Low/Medium/High/Critical)
- 严重程度（低/中/高/关键）
- Description with evidence
- 带证据的描述
- Mitigation strategy
- 缓解策略

**Final output:**
**最终输出：**

- Overall Risk Score (1-10)
- 总体风险分数（`1-10`）
- Top 3 risks that could kill the investment
- 可能使投资失败的前 `3` 大风险
- Recommended protective terms
- 推荐保护性条款

---

### Stage 5: Investor Memo Agent
### 阶段 5：投资人备忘录代理

**Purpose:** Synthesizes all findings into a structured investment memo.
**目的：** 将所有发现综合为结构化投资备忘录。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-pro-preview` |
| Tools<br>工具 | None<br>无 |
| Input<br>输入 | All previous stages<br>所有前置阶段 |
| Output Key<br>输出键 | `investor_memo` |

**Memo structure:**
**备忘录结构：**

1. **Executive Summary** - Company one-liner, recommendation, key highlights
1. **执行摘要** - 公司一句话介绍、建议、关键亮点
2. **Company Overview** - What they do, team, product/technology
2. **公司概览** - 业务内容、团队、产品/技术
3. **Funding & Valuation** - History, estimated valuation range
3. **融资与估值** - 历史、估算估值范围
4. **Market Opportunity** - Size, growth, competitors, differentiation
4. **市场机会** - 规模、增长、竞争对手、差异化
5. **Financial Analysis** - Revenue, unit economics, runway
5. **财务分析** - 收入、单位经济模型、现金 runway
6. **Risk Analysis** - Top risks with severity, overall score
6. **风险分析** - 主要风险及严重程度、总体分数
7. **Investment Thesis** - Why invest, concerns, return scenarios
7. **投资论点** - 投资理由、顾虑、回报情景
8. **Recommendation** - Final verdict, suggested next steps
8. **建议** - 最终判断、建议的下一步

**Recommendations:** Strong Buy / Buy / Hold / Pass
**建议类型：** `Strong Buy` / `Buy` / `Hold` / `Pass`

---

### Stage 6: Report Generator Agent
### 阶段 6：报告生成代理

**Purpose:** Creates a professional HTML investment report.
**目的：** 创建专业的 `HTML` 投资报告。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-flash-preview` |
| Tools<br>工具 | `generate_html_report` |
| Input<br>输入 | `{investor_memo}` |
| Output Key<br>输出键 | `html_report_result` |

**Report features:**
**报告特性：**

- McKinsey/Goldman Sachs styling
- `McKinsey`/`Goldman Sachs` 风格
- Dark blue (#1a365d) and gold (#d4af37) color scheme
- 深蓝色（`#1a365d`）和金色（`#d4af37`）配色方案
- Executive summary at top
- 顶部包含执行摘要
- Clear section headers with professional typography
- 使用专业字体排版的清晰章节标题
- Data tables for metrics
- 用于指标的数据表格
- Print-friendly layout
- 适合打印的布局

**Artifact:** Saves `investment_report_TIMESTAMP.html` viewable in any browser.
**制品：** 保存可在任意浏览器查看的 `investment_report_TIMESTAMP.html`。

---

### Stage 7: Infographic Generator Agent
### 阶段 7：信息图生成代理

**Purpose:** Creates a visual summary infographic using AI image generation.
**目的：** 使用 `AI` 图像生成创建可视化摘要信息图。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-flash-preview` |
| Tools<br>工具 | `generate_infographic`（uses `gemini-3-pro-image-preview`） |
| Input<br>输入 | `{investor_memo}` |
| Output Key<br>输出键 | `infographic_result` |

**Infographic includes:**
**信息图包含：**

- Company name prominently displayed
- 突出显示公司名称
- Key metrics in large, bold numbers
- 用大号粗体数字展示关键指标
- Market size visualization
- 市场规模可视化
- Risk score indicator (1-10 scale)
- 风险分数指示器（`1-10` 分）
- Investment recommendation badge
- 投资建议徽章
- Professional investment banking aesthetic
- 专业投行审美风格

**Artifact:** Saves `infographic_TIMESTAMP.png` for quick visual review.
**制品：** 保存用于快速视觉审阅的 `infographic_TIMESTAMP.png`。

---

## Project Structure
## 项目结构

```
ai_due_diligence_agent/
├── __init__.py        # Exports root_agent
├── agent.py           # All 7 agents + pipeline defined here
├── tools.py           # Custom tools (chart, report, infographic)
├── outputs/           # Generated artifacts saved here
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Generated Artifacts
## 生成的制品

All artifacts are saved to the **Artifacts tab** in ADK web and the **`outputs/`** folder:
所有制品都会保存到 `ADK web` 中的 **Artifacts tab** 和 **`outputs/`** 文件夹：

```
outputs/
├── revenue_chart_20260104_143030.png       # Financial projections
├── investment_report_20260104_143052.html  # Full HTML report
└── infographic_20260104_143105.png         # Visual TL;DR
```

| Artifact<br>制品 | Format<br>格式 | Description<br>描述 |
|----------|--------|-------------|
| Revenue Chart<br>收入图表 | PNG | Bear/Base/Bull 5-year projections<br>熊市/基准/牛市 `5` 年预测 |
| Investment Report<br>投资报告 | HTML | Full due diligence document<br>完整尽职调查文档 |
| Infographic<br>信息图 | PNG/JPG | Visual summary one-pager<br>单页可视化摘要 |

---

## ADK Features Demonstrated
## 演示的 `ADK` 功能

| Feature<br>功能 | Usage<br>用法 |
|---------|-------|
| **SequentialAgent**<br>**`SequentialAgent`** | 7-stage pipeline orchestration<br>`7` 阶段流水线编排 |
| **LlmAgent**<br>**`LlmAgent`** | All specialized agents<br>所有专业代理 |
| **google_search**<br>**`google_search`** | Real-time company/market research<br>实时公司/市场研究 |
| **Custom Tools**<br>**自定义工具** | Chart generation, HTML reports, infographics<br>图表生成、`HTML` 报告、信息图 |
| **Artifacts**<br>**制品** | Saving and versioning generated files<br>保存并版本化生成文件 |
| **State Management**<br>**状态管理** | Passing data between pipeline stages via `output_key`<br>通过 `output_key` 在流水线阶段之间传递数据 |
| **Multi-modal Output**<br>**多模态输出** | Text analysis + image generation<br>文本分析 + 图像生成 |

## Models Used
## 使用的模型

| Agent<br>代理 | Model<br>模型 | Why<br>原因 |
|-------|-------|-----|
| CompanyResearch<br>公司研究 | `gemini-3-flash-preview` | Fast web search<br>快速网页搜索 |
| MarketAnalysis<br>市场分析 | `gemini-3-flash-preview` | Fast web search<br>快速网页搜索 |
| FinancialModeling<br>财务建模 | `gemini-3-pro-preview` | Complex calculations<br>复杂计算 |
| RiskAssessment<br>风险评估 | `gemini-3-pro-preview` | Deep reasoning<br>深度推理 |
| InvestorMemo<br>投资人备忘录 | `gemini-3-pro-preview` | Synthesis quality<br>综合质量 |
| ReportGenerator<br>报告生成 | `gemini-3-flash-preview` | Fast HTML generation<br>快速 `HTML` 生成 |
| InfographicGenerator<br>信息图生成 | `gemini-3-flash-preview` | Orchestration<br>编排 |
| Infographic Tool<br>信息图工具 | `gemini-3-pro-image-preview` | Image generation<br>图像生成 |

---

## Learn More
## 了解更多

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK 文档](https://google.github.io/adk-docs/)
- [Multi Agent Patterns in ADK](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [`ADK` 中的多代理模式](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [Gemini API](https://ai.google.dev/gemini-api/docs)
- [`Gemini API`](https://ai.google.dev/gemini-api/docs)
- [Gemini Image Generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [`Gemini` 图像生成](https://ai.google.dev/gemini-api/docs/image-generation)
