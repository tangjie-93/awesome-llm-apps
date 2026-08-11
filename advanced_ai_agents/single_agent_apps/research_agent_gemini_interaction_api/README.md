# 🔬 AI Research Planner & Executor Agent with Google's Interactions API
# 🔬 使用 `Google Interactions API` 的 `AI` 研究规划与执行智能体

A streamlined multi-phase research agent built with **Google's Interactions API** that demonstrates stateful conversations, model mixing, background execution, and automatic infographic generation.
一个使用 **`Google Interactions API`** 构建的精简多阶段研究智能体，展示有状态对话、模型混用、后台执行和自动信息图生成。

## 🌟 Features
## 🌟 功能

- **📋 Phase 1 - Research Planning**: Uses **Gemini 3 Flash** to create structured, actionable research plans
- **📋 阶段 1 - 研究规划**：使用 **`Gemini 3 Flash`** 创建结构化、可执行的研究计划
- **🔍 Phase 2 - Task Selection & Deep Research**: Select specific tasks and leverage **Deep Research Agent** with built-in web search
- **🔍 阶段 2 - 任务选择与深度研究**：选择特定任务，并利用内置网页搜索的 **`Deep Research Agent`**
- **📊 Phase 3 - Synthesis + TL;DR**: Uses **Gemini 3 Pro** for executive reports + **Gemini 3 Pro Image** for automatic infographic generation
- **📊 阶段 3 - 综合 + `TL;DR`**：使用 **`Gemini 3 Pro`** 生成高管报告，并使用 **`Gemini 3 Pro Image`** 自动生成信息图
- **🎨 Auto-Generated Infographics**: Creates whiteboard-style TL;DR summary at the top of every report
- **🎨 自动生成信息图**：在每份报告顶部创建白板风格的 `TL;DR` 摘要
- **🔄 Stateful Conversations**: Demonstrates `previous_interaction_id` for maintaining context across phases
- **🔄 有状态对话**：演示使用 `previous_interaction_id` 在多个阶段之间保持上下文
- **⚡ Background Execution**: Async research execution with progress tracking
- **⚡ 后台执行**：带进度跟踪的异步研究执行
- **📥 Export Reports**: Download comprehensive research reports as markdown files
- **📥 导出报告**：将综合研究报告下载为 `markdown` 文件

## 🎯 How It Works
## 🎯 工作原理

```
User Goal
    ↓
[Phase 1] Gemini 3 Flash → Research Plan
    ↓
[Phase 2] Select Tasks → Deep Research Agent → Research Results
    ↓
[Phase 3] Gemini 3 Pro → Executive Report
         + Gemini 3 Pro Image → TL;DR Infographic
```

### Phase 1: Planning
### 阶段 1：规划
1. Enter your research goal
   输入你的研究目标
2. **Gemini 3 Flash** creates a numbered research plan with 5-8 specific tasks
   **`Gemini 3 Flash`** 创建一个包含 `5-8` 个具体任务的编号研究计划
3. Plan is stored as an `Interaction` for stateful continuation
   计划会作为 `Interaction` 存储，以便进行有状态续接

### Phase 2: Select & Research
### 阶段 2：选择与研究
1. Review the research plan with checkboxes for each task
   查看研究计划，并通过每个任务的复选框进行确认
2. Select/deselect tasks to focus your research
   选择/取消选择任务，以聚焦你的研究
3. **Deep Research Agent** executes comprehensive web research using `previous_interaction_id`
   **`Deep Research Agent`** 使用 `previous_interaction_id` 执行综合网页研究

### Phase 3: Synthesis + Infographic
### 阶段 3：综合 + 信息图
1. **Gemini 3 Pro** synthesizes findings into an executive report
   **`Gemini 3 Pro`** 将发现综合成高管报告
2. **Gemini 3 Pro Image** automatically generates a whiteboard TL;DR infographic
   **`Gemini 3 Pro Image`** 自动生成白板风格的 `TL;DR` 信息图
3. Report displays with infographic at the top, followed by full text
   报告顶部显示信息图，后面跟随完整文本
4. Download as markdown
   下载为 `markdown`

## 🛠️ Tech Stack
## 🛠️ 技术栈

| Component<br>组件 | Technology<br>技术 |
|-----------|-----------|
| **Planning Model**<br>**规划模型** | `gemini-3-flash-preview` |
| **Research Agent**<br>**研究智能体** | `deep-research-pro-preview-12-2025` |
| **Synthesis Model**<br>**综合模型** | `gemini-3-pro-preview` |
| **Infographic Model**<br>**信息图模型** | `gemini-3-pro-image-preview` |
| **UI Framework**<br>**`UI` 框架** | Streamlit<br>`Streamlit` |
| **Python SDK**<br>**`Python SDK`** | `google-genai` |

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
   克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/single_agent_apps/research_agent_gemini_interaction_api
```

2. Install the required dependencies:
   安装所需依赖：

```bash
pip install -r requirements.txt
```

3. Get your Google API Key
   获取你的 `Google API Key`

- Sign up for a [Google AI Studio account](https://ai.google.dev/) and obtain your API key.
- 注册一个 [Google AI Studio account](https://ai.google.dev/)，并获取你的 `API key`。

4. Run the Streamlit App
   运行 `Streamlit App`

```bash
streamlit run research_planner_executor_agent.py
```

5. Open your browser at `http://localhost:8501`
   在浏览器中打开 `http://localhost:8501`

6. Enter your Google API key in the sidebar and start researching!
   在侧边栏输入你的 `Google API key` 并开始研究！

## 📝 Example Research Goals
## 📝 示例研究目标

- "Research the B2B HR SaaS market in Germany - key players, regulations, pricing models"
- “研究德国的 `B2B HR SaaS` 市场 - 关键参与者、法规、定价模型”
- "Analyze market opportunities for AI-powered customer support tools"
- “分析 `AI` 驱动的客户支持工具的市场机会”
- "Investigate the competitive landscape for sustainable packaging in e-commerce"
- “调查电子商务中可持续包装的竞争格局”
- "Research regulatory requirements for fintech products targeting Gen Z"
- “研究面向 `Gen Z` 的金融科技产品的监管要求”

## ⚠️ Notes
## ⚠️ 备注

- **Beta API**: The Interactions API is in Beta - features may change
- **Beta API**：`Interactions API` 处于 `Beta` 阶段 - 功能可能变化
- **Deep Research**: May take 2-5 minutes for comprehensive research
- **Deep Research**：综合研究可能需要 `2-5` 分钟
- **Agent vs Model**: Deep Research uses `agent` parameter, not `model`
- **Agent vs Model**：`Deep Research` 使用 `agent` 参数，而不是 `model`
- **Image Generation**: Infographic generation uses the standard `generate_content` API
- **Image Generation**：信息图生成使用标准 `generate_content` API

## 🔗 Resources
## 🔗 资源

- [Gemini Interactions API Docs](https://ai.google.dev/gemini-api/docs/interactions)
- [Gemini Interactions API 文档](https://ai.google.dev/gemini-api/docs/interactions)
- [Gemini Models](https://ai.google.dev/gemini-api/docs/models)
- [`Gemini` 模型](https://ai.google.dev/gemini-api/docs/models)
- [Google AI Studio](https://ai.google.dev/)
- [`Google AI Studio` 资源](https://ai.google.dev/)

## 📄 License
## 📄 许可证

Part of the [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) collection.
属于 [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) 集合的一部分。
