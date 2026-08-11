# Deep Research Agent with OpenAI Agents SDK and Firecrawl
# 使用 `OpenAI Agents SDK` 和 `Firecrawl` 的 `Deep Research Agent`

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-deep-research-agent-with-openai-agents-sdk-and-firecrawl) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整的分步教程](https://www.theunwindai.com/p/build-a-deep-research-agent-with-openai-agents-sdk-and-firecrawl)，学习如何从零开始构建此项目，包括详细的代码讲解、说明和最佳实践。**

A powerful research assistant that leverages OpenAI's Agents SDK and Firecrawl's deep research capabilities to perform comprehensive web research on any topic and any question.
一个强大的研究助手，利用 `OpenAI Agents SDK` 和 `Firecrawl` 的深度研究能力，对任何主题和问题执行全面的网页研究。

## Features
## 功能

- **Deep Web Research**: Automatically searches the web, extracts content, and synthesizes findings
  **深度网页研究**：自动搜索网络、提取内容并综合研究发现
- **Enhanced Analysis**: Uses OpenAI's Agents SDK to elaborate on research findings with additional context and insights
  **增强分析**：使用 `OpenAI Agents SDK` 对研究发现进行扩展说明，并补充上下文和洞察
- **Interactive UI**: Clean Streamlit interface for easy interaction
  **交互式 `UI`**：简洁的 `Streamlit` 界面，便于交互
- **Downloadable Reports**: Export research findings as markdown files
  **可下载报告**：将研究发现导出为 `Markdown` 文件

## How It Works
## 工作原理

1. **Input Phase**: User provides a research topic and API credentials
   **输入阶段**：用户提供研究主题和 `API` 凭据
2. **Research Phase**: The tool uses Firecrawl to search the web and extract relevant information
   **研究阶段**：该工具使用 `Firecrawl` 搜索网络并提取相关信息
3. **Analysis Phase**: An initial research report is generated based on the findings
   **分析阶段**：基于研究发现生成初始研究报告
4. **Enhancement Phase**: A second agent elaborates on the initial report, adding depth and context
   **增强阶段**：第二个智能体对初始报告进行扩展说明，增加深度和上下文
5. **Output Phase**: The enhanced report is presented to the user and available for download
   **输出阶段**：向用户展示增强后的报告，并支持下载

## Requirements
## 要求

- Python 3.8+
  `Python 3.8+` 环境
- OpenAI API key
  `OpenAI API key` 密钥
- Firecrawl API key
  `Firecrawl API key` 密钥
- Required Python packages (see `requirements.txt`)
  所需 `Python` 包（见 `requirements.txt`）

## Installation
## 安装

1. Clone this repository:
   克隆此仓库：
   ```bash
   git clone  https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/single_agent_apps/ai_deep_research_agent
   ```

2. Install the required packages:
   安装所需包：
   ```bash
   pip install -r requirements.txt
   ```

## Usage
## 使用方法

1. Run the Streamlit app:
   运行 `Streamlit` 应用：
   ```bash
   streamlit run deep_research_openai.py
   ```

2. Enter your API keys in the sidebar:
   在侧边栏输入你的 `API key`：
   - OpenAI API key
     `OpenAI API key` 密钥
   - Firecrawl API key
     `Firecrawl API key` 密钥

3. Enter your research topic in the main input field
   在主输入框中输入你的研究主题

4. Click "Start Research" and wait for the process to complete
   点击 “Start Research” 并等待流程完成

5. View and download your enhanced research report
   查看并下载增强后的研究报告

## Example Research Topics
## 示例研究主题

- "Latest developments in quantum computing"
  “量子计算的最新发展”
- "Impact of climate change on marine ecosystems"
  “气候变化对海洋生态系统的影响”
- "Advancements in renewable energy storage"
  “可再生能源存储的进展”
- "Ethical considerations in artificial intelligence"
  “人工智能中的伦理考量”
- "Emerging trends in remote work technologies"
  “远程办公技术的新兴趋势”

## Technical Details
## 技术细节

The application uses two specialized agents:
该应用使用两个专用智能体：

1. **Research Agent**: Utilizes Firecrawl's deep research endpoint to gather comprehensive information from multiple web sources.
   **`Research Agent`**：利用 `Firecrawl` 的深度研究端点，从多个网页来源收集全面信息。

2. **Elaboration Agent**: Enhances the initial research by adding detailed explanations, examples, case studies, and practical implications.
   **`Elaboration Agent`**：通过添加详细说明、示例、案例研究和实际意义来增强初始研究。

The Firecrawl deep research tool performs multiple iterations of web searches, content extraction, and analysis to provide thorough coverage of the topic.
`Firecrawl` 深度研究工具会执行多轮网页搜索、内容提取和分析，从而对主题进行全面覆盖。
