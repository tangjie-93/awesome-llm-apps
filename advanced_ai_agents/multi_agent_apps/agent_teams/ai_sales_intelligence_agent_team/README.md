# 👨🏻‍💼 AI Sales Intelligence Agent Team
# 👨🏻‍💼 AI 销售情报智能体团队

A multi-agent AI pipeline that generates competitive sales battle cards in real-time, built with [Google ADK](https://google.github.io/adk-docs/) and Gemini 3.
一个多智能体 `AI` 流水线，可实时生成竞争销售作战卡，基于 [Google ADK](https://google.github.io/adk-docs/) 和 `Gemini 3` 构建。

**Give it a competitor + your product** → Get a complete battle card with positioning strategies, objection handling scripts, and visual comparisons.
**输入一个竞争对手 + 你的产品** → 获取一份完整作战卡，其中包含定位策略、异议处理话术和可视化对比。

## Features
## 功能

- 🔍 **Live Research** - Real-time web search for competitor intelligence
- 🔍 **实时研究** - 通过实时网页搜索获取竞争对手情报
- 📊 **Feature Analysis** - Deep dive into competitor product capabilities
- 📊 **功能分析** - 深入分析竞争对手的产品能力
- 🎯 **Positioning Intel** - Uncover how competitors position against you
- 🎯 **定位情报** - 揭示竞争对手如何相对于你进行定位
- ⚖️ **SWOT Analysis** - Honest strengths/weaknesses comparison
- ⚖️ **SWOT 分析** - 真实比较优势与劣势
- 💬 **Objection Scripts** - Ready-to-use responses for sales calls
- 💬 **异议话术** - 可直接用于销售电话的回应
- 📄 **Battle Card** - Professional HTML battle card for reps
- 📄 **作战卡** - 面向销售代表的专业 `HTML` 作战卡
- 📈 **Comparison Infographic** - AI-generated visual comparison (Gemini image)
- 📈 **对比信息图** - `AI` 生成的可视化对比（`Gemini` 图像）

## What It Does
## 它能做什么

Given a competitor and your product, the pipeline automatically:
给定竞争对手和你的产品后，该流水线会自动：

1. **Researches the competitor** - Company, funding, customers, reviews
1. **研究竞争对手** - 公司、融资、客户、评价
2. **Analyzes their features** - Capabilities, integrations, pricing
2. **分析其功能** - 能力、集成、定价
3. **Uncovers positioning** - Their messaging, personas, analyst coverage
3. **揭示定位** - 其信息表达、目标角色、分析师覆盖
4. **Creates SWOT analysis** - Where you win, where they win
4. **创建 SWOT 分析** - 你胜出的地方，以及对方胜出的地方
5. **Generates objection scripts** - Top 10 objections with responses
5. **生成异议话术** - 前 `10` 个异议及回应
6. **Builds battle card** - Professional HTML for sales reps
6. **构建作战卡** - 面向销售代表的专业 `HTML`
7. **Creates comparison chart** - Visual feature-by-feature comparison
7. **创建对比图表** - 按功能逐项进行可视化对比

## Quick Start
## 快速开始

### 1. Navigate to Project
### 1. 进入项目

```bash
cd awesome-llm-apps/advanced_ai_agents/multi_agent_apps/agent_team/ai_sales_intelligence_team
```

### 2. Set Environment
### 2. 设置环境

```bash
export GOOGLE_API_KEY=your_api_key
```

### 3. Install & Run
### 3. 安装并运行

```bash
pip install -r requirements.txt
adk web
```

### 4. Try It
### 4. 试用

Open `http://localhost:8000` and try:
打开 `http://localhost:8000` 并尝试：

- *"Create a battle card for Salesforce. We sell HubSpot."*
- *“为 `Salesforce` 创建一份作战卡。我们销售 `HubSpot`。”*
- *"Battle card against Slack - we're selling Microsoft Teams"*
- *“针对 `Slack` 的作战卡 - 我们销售 `Microsoft Teams`。”*
- *"Help me compete against Zendesk, I sell Freshdesk"*
- *“帮我与 `Zendesk` 竞争，我销售 `Freshdesk`。”*

## Example Prompts
## 示例提示词

| Your Product<br>你的产品 | Competitor<br>竞争对手 | Prompt<br>提示词 |
|--------------|------------|--------|
| HubSpot<br>`HubSpot` | Salesforce<br>`Salesforce` | "Create a battle card for Salesforce. We sell HubSpot."<br>“为 `Salesforce` 创建一份作战卡。我们销售 `HubSpot`。” |
| Asana<br>`Asana` | Monday.com<br>`Monday.com` | "Battle card against Monday.com, I sell Asana"<br>“针对 `Monday.com` 的作战卡，我销售 `Asana`。” |
| Zoom<br>`Zoom` | Microsoft Teams<br>`Microsoft Teams` | "Competitive analysis: Zoom vs our product Teams"<br>“竞争分析：`Zoom` 对比我们的产品 `Teams`。” |
| Notion<br>`Notion` | Confluence<br>`Confluence` | "Help me compete against Confluence, we're Notion"<br>“帮我与 `Confluence` 竞争，我们是 `Notion`。” |

---

## Pipeline Architecture
## 流水线架构

```
User Query: "Battle card for Salesforce. We sell HubSpot."
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│               BattleCardPipeline (SequentialAgent)              │
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │    Stage 1      │    │    Stage 2      │    │   Stage 3   │  │
│  │   Competitor    │───▶│    Product      │───▶│ Positioning │  │
│  │   Research      │    │    Features     │    │  Analyzer   │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
│           │                     │                     │         │
│           ▼                     ▼                     ▼         │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │    Stage 4      │    │    Stage 5      │    │   Stage 6   │  │
│  │      SWOT       │───▶│   Objection     │───▶│ Battle Card │  │
│  │    Analysis     │    │    Handler      │    │  Generator  │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
│                                                       │         │
│                                                       ▼         │
│                                              ┌─────────────┐    │
│                                              │   Stage 7   │    │
│                                              │ Comparison  │    │
│                                              │    Chart    │    │
│                                              └─────────────┘    │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
Artifacts: battle_card.html, comparison_chart.png
```

---

## Agent Details
## 智能体详情

### Stage 1: Competitor Research Agent
### 阶段 1：竞争对手研究智能体

**Purpose:** Gathers comprehensive competitor intelligence through web search.
**目的：** 通过网页搜索收集全面的竞争对手情报。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-flash-preview` |
| Tools<br>工具 | `google_search` |
| Output Key<br>输出键 | `competitor_profile` |

**Researches:**
**研究内容：**

- Company overview (founded, HQ, size, funding)
- 公司概览（创立时间、总部、规模、融资）
- Target market and ideal customers
- 目标市场和理想客户
- Products and pricing tiers
- 产品和定价层级
- Recent news, launches, acquisitions
- 近期新闻、发布、收购
- Customer reviews (G2, Capterra, TrustRadius)
- 客户评价（`G2`、`Capterra`、`TrustRadius`）

---

### Stage 2: Product Feature Agent
### 阶段 2：产品功能智能体

**Purpose:** Deep analysis of competitor product capabilities.
**目的：** 深入分析竞争对手的产品能力。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-flash-preview` |
| Tools<br>工具 | `google_search` |
| Output Key<br>输出键 | `feature_analysis` |

**Analyzes:**
**分析内容：**

- Core features and capabilities
- 核心功能和能力
- Integrations and ecosystem
- 集成和生态系统
- Technical architecture (cloud, API, mobile)
- 技术架构（云、`API`、移动端）
- Pricing details and hidden costs
- 定价细节和隐藏成本
- Known limitations from reviews
- 从评论中发现的已知限制

---

### Stage 3: Positioning Analyzer Agent
### 阶段 3：定位分析智能体

**Purpose:** Uncovers competitor positioning and messaging strategy.
**目的：** 揭示竞争对手的定位和信息表达策略。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-pro-preview` |
| Tools<br>工具 | `google_search` |
| Output Key<br>输出键 | `positioning_intel` |

**Discovers:**
**发现内容：**

- Marketing messaging and taglines
- 市场信息表达和标语
- Target personas they focus on
- 其聚焦的目标角色
- How they position against YOUR product
- 他们如何相对于你的产品进行定位
- Analyst coverage (Gartner, Forrester, G2)
- 分析师覆盖（`Gartner`、`Forrester`、`G2`）
- Social proof and case studies
- 社会证明和案例研究

---

### Stage 4: SWOT Analysis Agent
### 阶段 4：SWOT 分析智能体

**Purpose:** Creates honest strengths/weaknesses analysis.
**目的：** 创建真实的优势/劣势分析。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-pro-preview` |
| Tools<br>工具 | None (synthesis)<br>无（综合） |
| Output Key<br>输出键 | `swot_analysis` |

**Produces:**
**产出：**

- Top 5 competitor strengths (with evidence)
- 竞争对手前 `5` 个优势（带证据）
- Top 5 competitor weaknesses
- 竞争对手前 `5` 个劣势
- Where YOU win against them
- 你相对他们胜出的地方
- Competitive landmines to set in deals
- 可在交易中设置的竞争陷阱点

---

### Stage 5: Objection Handler Agent
### 阶段 5：异议处理智能体

**Purpose:** Creates scripts for handling competitive objections.
**目的：** 创建处理竞争异议的话术。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-pro-preview` |
| Tools<br>工具 | None (synthesis)<br>无（综合） |
| Output Key<br>输出键 | `objection_scripts` |

**Creates:**
**创建内容：**

- Top 10 objections with scripted responses
- 前 `10` 个异议及成稿回应
- Proof points for each response
- 每个回应的证明点
- Killer questions to ask prospects
- 可向潜在客户提出的关键问题
- Trap-setting phrases for early in deals
- 交易早期可使用的铺垫式话术

---

### Stage 6: Battle Card Generator Agent
### 阶段 6：作战卡生成智能体

**Purpose:** Generates professional HTML battle card.
**目的：** 生成专业 `HTML` 作战卡。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-flash-preview` |
| Tools<br>工具 | `generate_battle_card_html` |
| Output Key<br>输出键 | `battle_card_result` |

**Battle Card Includes:**
**作战卡包含：**

- Quick stats header
- 快速统计标题区
- At-a-glance comparison (We Win / They Win / Toss-up)
- 一览式对比（我们胜出 / 他们胜出 / 难分胜负）
- Feature comparison table
- 功能对比表
- Objection handling cheat sheet
- 异议处理速查表
- Killer questions
- 关键问题
- Landmines to set
- 可设置的陷阱点

**Artifact:** `battle_card_TIMESTAMP.html`
**产物：** `battle_card_TIMESTAMP.html`

---

### Stage 7: Comparison Chart Agent
### 阶段 7：对比图表智能体

**Purpose:** Creates visual comparison infographic using Gemini image generation.
**目的：** 使用 `Gemini` 图像生成创建可视化对比信息图。

| Property<br>属性 | Value<br>值 |
|----------|-------|
| Model<br>模型 | `gemini-3-flash-preview` |
| Tools<br>工具 | `generate_comparison_chart` (uses `gemini-2.0-flash-exp`)<br>`generate_comparison_chart`（使用 `gemini-2.0-flash-exp`） |
| Output Key<br>输出键 | `chart_result` |

**Infographic Features:**
**信息图功能：**

- AI-generated professional comparison graphic
- `AI` 生成的专业对比图
- Side-by-side feature comparison visualization
- 并排功能对比可视化
- Color-coded scores (green = you, red = competitor)
- 颜色编码评分（绿色 = 你方，红色 = 竞争对手）
- Key differentiators highlighted
- 突出关键差异点
- Overall verdict badge
- 总体结论徽章

**Artifact:** `comparison_infographic_TIMESTAMP.png`
**产物：** `comparison_infographic_TIMESTAMP.png`

---

## Project Structure
## 项目结构

```
ai_battle_card_agent/
├── __init__.py        # Exports root_agent
├── agent.py           # All 7 agents + pipeline
├── tools.py           # Battle card HTML + comparison chart tools
├── outputs/           # Generated artifacts saved here
├── requirements.txt   # Dependencies
└── README.md          # This file
```

## Generated Artifacts
## 生成的产物

All artifacts are saved to the **Artifacts tab** in ADK web and the **`outputs/`** folder:
所有产物都会保存到 `ADK web` 的 **Artifacts tab** 和 **`outputs/`** 文件夹中：

```
outputs/
├── battle_card_20260104_143052.html         # Full battle card document
└── comparison_infographic_20260104_143105.png # AI-generated comparison visual
```

| Artifact<br>产物 | Format<br>格式 | Description<br>描述 |
|----------|--------|-------------|
| Battle Card<br>作战卡 | HTML<br>`HTML` | Sales-ready competitive battle card<br>可供销售使用的竞争作战卡 |
| Comparison Infographic<br>对比信息图 | PNG/JPG<br>`PNG`/`JPG` | AI-generated visual comparison (Gemini image)<br>`AI` 生成的可视化对比（`Gemini` 图像） |

---

## Battle Card Sections
## 作战卡章节

The generated HTML battle card includes:
生成的 `HTML` 作战卡包括：

1. **Header** - Competitor name, last updated date
1. **标题区** - 竞争对手名称、最后更新日期
2. **Quick Stats** - 5-6 one-liner facts
2. **快速统计** - `5-6` 条一句话事实
3. **At a Glance** - Three columns: We Win | They Win | Toss-up
3. **一览对比** - 三列：我们胜出 | 他们胜出 | 难分胜负
4. **Feature Comparison** - Table with checkmarks
4. **功能对比** - 带对勾的表格
5. **Their Strengths** - Red indicators (be honest!)
5. **他们的优势** - 红色指示（保持真实！）
6. **Their Weaknesses** - Green indicators (opportunities)
6. **他们的劣势** - 绿色指示（机会）
7. **Objection Handling** - Top 5 with quick responses
7. **异议处理** - 前 `5` 个异议及快速回应
8. **Killer Questions** - Questions to ask prospects
8. **关键问题** - 可向潜在客户提出的问题
9. **Landmines** - Traps to set in competitive deals
9. **陷阱点** - 在竞争交易中可设置的陷阱

---

## ADK Features Demonstrated
## 展示的 ADK 功能

| Feature<br>功能 | Usage<br>用途 |
|---------|-------|
| **SequentialAgent**<br>**SequentialAgent** | 7-stage pipeline orchestration<br>`7` 阶段流水线编排 |
| **google_search**<br>**google_search** | Real-time competitor research<br>实时竞争对手研究 |
| **Custom Tools**<br>**自定义工具** | HTML battle card, AI-generated infographics<br>`HTML` 作战卡、`AI` 生成的信息图 |
| **Image Generation**<br>**图像生成** | Gemini image model for comparison visuals<br>用于对比视觉内容的 `Gemini` 图像模型 |
| **Artifacts**<br>**产物** | Saving battle cards per session<br>按会话保存作战卡 |
| **State Management**<br>**状态管理** | Passing research between stages via `output_key`<br>通过 `output_key` 在阶段之间传递研究结果 |
| **Coordinator Pattern**<br>**协调器模式** | Root agent routes to pipeline<br>根智能体路由到流水线 |

## Models Used
## 使用的模型

| Agent<br>智能体 | Model<br>模型 | Why<br>原因 |
|-------|-------|-----|
| CompetitorResearch<br>`CompetitorResearch` | `gemini-3-flash-preview` | Fast web search<br>快速网页搜索 |
| ProductFeature<br>`ProductFeature` | `gemini-3-flash-preview` | Fast web search<br>快速网页搜索 |
| PositioningAnalyzer<br>`PositioningAnalyzer` | `gemini-3-pro-preview` | Strategic analysis<br>战略分析 |
| SWOT<br>`SWOT` | `gemini-3-pro-preview` | Deep synthesis<br>深度综合 |
| ObjectionHandler<br>`ObjectionHandler` | `gemini-3-pro-preview` | Script quality<br>话术质量 |
| BattleCardGenerator<br>`BattleCardGenerator` | `gemini-3-flash-preview` | HTML generation<br>`HTML` 生成 |
| ComparisonChart Agent<br>`ComparisonChart Agent` | `gemini-3-flash-preview` | Orchestration<br>编排 |
| Comparison Tool<br>`Comparison Tool` | `gemini-3-pro-image-preview` | Image generation<br>图像生成 |

---

## Learn More
## 了解更多

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK 文档](https://google.github.io/adk-docs/)
- [Multi-Agent Patterns in ADK](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [ADK 中的多智能体模式](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [Gemini API](https://ai.google.dev/gemini-api/docs)
- [Gemini API 文档](https://ai.google.dev/gemini-api/docs)
