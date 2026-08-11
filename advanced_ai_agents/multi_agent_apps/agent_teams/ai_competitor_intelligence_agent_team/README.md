# 🧲 AI Competitor Intelligence Agent Team
# 🧲 `AI` 竞品情报智能体团队

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-competitor-intelligence-agent-team) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-competitor-intelligence-agent-team)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

The AI Competitor Intelligence Agent Team is a powerful competitor analysis tool powered by Firecrawl and Agno's AI Agent framework. This app helps businesses analyze their competitors by extracting structured data from competitor websites and generating actionable insights using AI.
`AI` 竞品情报智能体团队是一个强大的竞品分析工具，由 `Firecrawl` 和 `Agno` 的 `AI Agent` 框架驱动。该应用通过从竞品网站提取结构化数据，并使用 `AI` 生成可执行洞察，帮助企业分析竞争对手。

## Features
## 功能

- **Multi-Agent System**
- **多智能体系统**
    - **Firecrawl Agent**: Specializes in crawling and summarizing competitor websites
    - **`Firecrawl Agent`**：专门负责抓取和总结竞品网站
    - **Analysis Agent**: Generates detailed competitive analysis reports
    - **`Analysis Agent`**：生成详细的竞争分析报告
    - **Comparison Agent**: Creates structured comparisons between competitors
    - **`Comparison Agent`**：创建竞品之间的结构化比较

- **Competitor Discovery**:
- **竞品发现**：
  - Finds similar companies using URL matching with Exa AI
  - 使用 `Exa AI` 通过 `URL` 匹配寻找相似公司
  - Discovers competitors based on business descriptions
  - 根据业务描述发现竞争对手
  - Automatically extracts relevant competitor URLs
  - 自动提取相关竞品 `URLs`

- **Comprehensive Analysis**:
- **综合分析**：
  - Provides structured analysis reports with:
  - 提供包含以下内容的结构化分析报告：
    - Market gaps and opportunities
    - 市场缺口与机会
    - Competitor weaknesses
    - 竞争对手弱点
    - Recommended features
    - 推荐功能
    - Pricing strategies
    - 定价策略
    - Growth opportunities
    - 增长机会
    - Actionable recommendations
    - 可执行建议

- **Interactive Analysis**: Users can input either their company URL or description for analysis
- **交互式分析**：用户可以输入公司 `URL` 或公司描述进行分析

## Requirements
## 要求

The application requires the following Python libraries:
该应用需要以下 `Python` 库：

- `agno`
- `agno` 库
- `exa-py`
- `exa-py` 库
- `streamlit`
- `streamlit` 库
- `pandas`
- `pandas` 库
- `firecrawl-py`
- `firecrawl-py` 库

You'll also need API keys for:
你还需要以下服务的 `API keys`：

- OpenAI
- `OpenAI` 服务
- Firecrawl
- `Firecrawl` 服务
- Exa
- `Exa` 服务

## How to Run
## 如何运行

Follow these steps to set up and run the application:
按照以下步骤设置并运行该应用：

1. **Clone the Repository**:
1. **克隆仓库**：

   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_competitor_intelligence_agent_team
   ```

2. **Install the dependencies**:
2. **安装依赖**：

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API keys**:
3. **设置你的 `API keys`**：

    - Get an OpenAI API key from: https://platform.openai.com/api-keys
    - 从 https://platform.openai.com/api-keys 获取 `OpenAI API key`
    - Get a Firecrawl API key from: [Firecrawl website](https://www.firecrawl.dev/app/api-keys)
    - 从 [Firecrawl website](https://www.firecrawl.dev/app/api-keys) 获取 `Firecrawl API key`
    - Get an Exa API key from: [Exa website](https://dashboard.exa.ai/api-keys)
    - 从 [Exa website](https://dashboard.exa.ai/api-keys) 获取 `Exa API key`

4. **Run the Streamlit app**:
4. **运行 `Streamlit` 应用**：

    ```bash
    streamlit run ai_competitor_analyser.py
    ```

## Usage
## 使用方式

1. Enter your API keys in the sidebar
1. 在侧边栏输入你的 `API keys`
2. Input either:
2. 输入以下任一内容：
   - Your company's website URL
   - 你的公司网站 `URL`
   - A description of your company
   - 你的公司描述
3. Click "Analyze Competitors" to generate:
3. 点击 `Analyze Competitors` 以生成：
   - Competitor comparison table
   - 竞品比较表
   - Detailed analysis report
   - 详细分析报告
   - Strategic recommendations
   - 战略建议
