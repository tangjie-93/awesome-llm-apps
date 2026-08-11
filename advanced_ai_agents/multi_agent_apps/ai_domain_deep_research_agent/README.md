# 🔍 AI Domain Deep Research Agent
# 🔍 `AI` 领域深度研究代理

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-domain-deep-research-agent) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-domain-deep-research-agent)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

An advanced AI research agent built using the Agno Agent framework, Together AI's Qwen model, and Composio tools. This agent helps users conduct comprehensive research on any topic by generating research questions, finding answers through multiple search engines, and compiling professional reports with Google Docs integration.
一个高级 `AI` 研究代理，使用 `Agno Agent` 框架、`Together AI` 的 `Qwen` 模型和 `Composio` 工具构建。该代理通过生成研究问题、借助多个搜索引擎查找答案，并结合 `Google Docs` 集成编写专业报告，帮助用户对任何主题开展全面研究。

## Features
## 功能

- 🧠 **Intelligent Question Generation**:
- 🧠 **智能问题生成**：

  - Automatically generates 5 specific research questions about your topic
  - 自动围绕你的主题生成 `5` 个具体研究问题
  - Tailors questions to your specified domain
  - 根据你指定的领域定制问题
  - Focuses on creating yes/no questions for clear research outcomes
  - 重点创建是/否问题，以获得清晰的研究结果
- 🔎 **Multi-Source Research**:
- 🔎 **多来源研究**：

  - Uses Tavily Search for comprehensive web results
  - 使用 `Tavily Search` 获取全面的网页结果
  - Leverages Perplexity AI for deeper analysis
  - 利用 `Perplexity AI` 进行更深入分析
  - Combines multiple sources for thorough research
  - 结合多个来源进行充分研究
- 📊 **Professional Report Generation**:
- 📊 **专业报告生成**：

  - Compiles research findings into a McKinsey-style report
  - 将研究发现汇编成 `McKinsey` 风格报告
  - Structures content with executive summary, analysis, and conclusion
  - 使用执行摘要、分析和结论来组织内容
  - Creates a Google Doc with the complete report
  - 创建包含完整报告的 `Google Doc`
- 🖥️ **User-Friendly Interface**:
- 🖥️ **用户友好界面**：

  - Clean Streamlit UI with intuitive workflow
  - 提供简洁的 `Streamlit UI` 和直观工作流
  - Real-time progress tracking
  - 实时进度跟踪
  - Expandable sections to view detailed results
  - 可展开区域用于查看详细结果

## How to Run
## 运行方法

1. **Setup Environment**
1. **设置环境**

   ```bash
   # Clone the repository
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/single_agent_apps/ai_domain_deep_research_agent

   # Install dependencies
   pip install -r requirements.txt

   composio add googledocs
   composio add perplexityai
   ```
2. **Configure API Keys**
2. **配置 `API Keys`**

   - Get Together AI API key from [Together AI](https://together.ai)
   - 从 [Together AI](https://together.ai) 获取 `Together AI API key`
   - Get Composio API key from [Composio](https://composio.ai)
   - 从 [Composio](https://composio.ai) 获取 `Composio API key`
   - Add these to a `.env` file or enter them in the app sidebar
   - 将这些密钥添加到 `.env` 文件，或在应用侧边栏中输入
3. **Run the Application**
3. **运行应用**

   ```bash
   streamlit run ai_domain_deep_research_agent.py
   ```

## Usage
## 使用方法

1. Launch the application using the command above
1. 使用上面的命令启动应用
2. Enter your Together AI and Composio API keys in the sidebar
2. 在侧边栏输入你的 `Together AI` 和 `Composio API keys`
3. Input your research topic and domain in the main interface
3. 在主界面输入研究主题和领域
4. Click "Generate Research Questions" to create specific questions
4. 点击 "Generate Research Questions" 创建具体问题
5. Review the questions and click "Start Research" to begin the research process
5. 查看问题后点击 "Start Research" 开始研究流程
6. Once research is complete, click "Compile Final Report" to generate a professional report
6. 研究完成后，点击 "Compile Final Report" 生成专业报告
7. View the report in the app and access it in Google Docs
7. 在应用中查看报告，并在 `Google Docs` 中访问它

## Technical Details
## 技术细节

- **Agno Framework**: Used for creating and orchestrating AI agents
- **`Agno Framework`**：用于创建和编排 `AI agents`
- **Together AI**: Provides the Qwen 3 235B model for advanced language processing
- **`Together AI`**：提供用于高级语言处理的 `Qwen 3 235B` 模型
- **Composio Tools**: Integrates search engines and Google Docs functionality
- **`Composio Tools`**：集成搜索引擎和 `Google Docs` 功能
- **Streamlit**: Powers the user interface with interactive elements
- **`Streamlit`**：通过交互元素驱动用户界面

## Example Use Cases
## 示例用例

- **Academic Research**: Quickly gather information on academic topics across various disciplines
- **学术研究**：快速收集跨学科主题的学术信息
- **Market Analysis**: Research market trends, competitors, and industry developments
- **市场分析**：研究市场趋势、竞争对手和行业发展
- **Policy Research**: Analyze policy implications and historical context
- **政策研究**：分析政策影响和历史背景
- **Technology Evaluation**: Research emerging technologies and their potential impact
- **技术评估**：研究新兴技术及其潜在影响

## Dependencies
## 依赖

- agno
- `agno` 库
- composio_agno
- `composio_agno` 库
- streamlit
- `streamlit` 库
- python-dotenv
- `python-dotenv` 库

## License
## 许可证

This project is part of the awesome-llm-apps collection and is available under the MIT License.
该项目是 `awesome-llm-apps` 集合的一部分，并基于 `MIT License` 提供。
