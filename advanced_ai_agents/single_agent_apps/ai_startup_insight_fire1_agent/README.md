# 🔥 AI Startup Insight with Firecrawl FIRE-1 Agent
# 🔥 使用 `Firecrawl FIRE-1 Agent` 的 `AI` 初创公司洞察

An advanced web extraction and analysis tool built using Firecrawl's FIRE-1 agent + extract v1 endpoint and the Agno Agent framework to get details of a new startup instantly! This application automatically extracts structured data from startup websites and provides AI-powered business analysis, making it easy to gather insights about companies without manual research.
这是一个高级网页提取和分析工具，使用 `Firecrawl` 的 `FIRE-1 agent` + `extract v1 endpoint` 以及 `Agno Agent` 框架，可即时获取新初创公司的详细信息。该应用会从初创公司网站自动提取结构化数据，并提供由 `AI` 驱动的商业分析，让你无需手动研究即可轻松获得公司洞察。

## Features
## 功能

- 🌐 **Intelligent Web Extraction**:
- 🌐 **智能网页提取**：

  - Extract structured data from any company website
  - 从任意公司网站提取结构化数据
  - Automatically identify company information, mission, and product features
  - 自动识别公司信息、使命和产品功能
  - Process multiple websites in sequence
  - 按顺序处理多个网站
- 🔍 **Advanced Web Navigation**:
- 🔍 **高级网页导航**：

  - Interact with buttons, links, and dynamic elements
  - 与按钮、链接和动态元素交互
  - Handle pagination and multi-step processes
  - 处理分页和多步骤流程
  - Access information across multiple pages
  - 跨多个页面访问信息
- 🧠 **AI Business Analysis**:
- 🧠 **`AI` 商业分析**：

  - Generate insightful summaries of extracted company data
  - 为提取出的公司数据生成有洞察力的摘要
  - Identify unique value propositions and market opportunities
  - 识别独特价值主张和市场机会
  - Provide actionable business intelligence
  - 提供可执行的商业情报
- 📊 **Structured Data Output**:
- 📊 **结构化数据输出**：

  - Organize information in a consistent JSON schema
  - 使用一致的 `JSON schema` 组织信息
  - Extract company name, description, mission, and product features
  - 提取公司名称、描述、使命和产品功能
  - Standardize output for further processing
  - 标准化输出以便进一步处理
- 🎯 **Interactive UI**:
- 🎯 **交互式 `UI`**：

  - User-friendly Streamlit interface
  - 用户友好的 `Streamlit` 界面
  - Process multiple URLs in parallel
  - 并行处理多个 `URL`
  - Clear presentation of extracted data and analysis
  - 清晰展示提取出的数据和分析

## How to Run
## 如何运行

1. **Setup Environment**
   **设置环境**

   ```bash
   # Clone the repository

   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/single_agent_apps/ai_startup_insight_fire1_agent
   ```

   # Install dependencies
   # 安装依赖


   ```
   pip install -r requirements.txt

   ```
2. **Configure API Keys**
   **配置 `API Keys`**

   - Get Firecrawl API key from [Firecrawl](https://firecrawl.dev)
   - 从 [Firecrawl](https://firecrawl.dev) 获取 `Firecrawl API key`
   - Get OpenAI API key from [OpenAI Platform](https://platform.openai.com)
   - 从 [OpenAI Platform](https://platform.openai.com) 获取 `OpenAI API key`
3. **Run the Application**
   **运行应用**

   ```bash
   streamlit run ai_startup_insight_fire1_agent.py
   ```

## Usage
## 使用方法

1. Launch the application using the command above
   使用上方命令启动应用
2. Provide your Firecrawl and OpenAI API keys in the sidebar
   在侧边栏中提供你的 `Firecrawl` 和 `OpenAI API keys`
3. Enter one or more company website URLs in the text area (one per line)
   在文本区域输入一个或多个公司网站 `URL`（每行一个）
4. Click "🚀 Start Analysis" to begin the extraction and analysis process
   点击 “🚀 Start Analysis” 开始提取和分析流程
5. View the structured data and AI analysis for each website in the tabbed interface
   在标签页界面中查看每个网站的结构化数据和 `AI` 分析

## Example Websites to Try
## 可尝试的示例网站

- https://www.spurtest.com
- https://cluely.com
- https://www.harvey.ai

## Technologies Used
## 使用的技术

- **Firecrawl FIRE-1**: Advanced web extraction agent
- **Firecrawl FIRE-1**：高级网页提取智能体
- **Agno Agent Framework**: For AI analysis capabilities
- **Agno Agent Framework**：用于 `AI` 分析能力
- **OpenAI GPT Models**: For business insight generation
- **OpenAI GPT Models**：用于生成商业洞察
- **Streamlit**: For the interactive web interface
- **Streamlit**：用于交互式网页界面

## Requirements
## 要求

- Python 3.8+
- `Python 3.8+` 或更高版本
- Firecrawl API key
- `Firecrawl API key` 密钥
- OpenAI API key
- `OpenAI API key` 密钥
- Internet connection for web extraction
- 用于网页提取的互联网连接
