# 🤝 AI Consultant Agent with Google ADK 
# 🤝 使用 `Google ADK` 的 `AI Consultant Agent`

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-consultant-agent-with-gemini-2-5-flash) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整的分步教程](https://www.theunwindai.com/p/build-an-ai-consultant-agent-with-gemini-2-5-flash)，学习如何从零开始构建此项目，包括详细的代码讲解、说明和最佳实践。**

A powerful business consultant powered by Google's Agent Development Kit that provides comprehensive market analysis, strategic planning, and actionable business recommendations with real-time web research.
一个由 `Google Agent Development Kit` 提供支持的强大商业顾问，可结合实时网页研究，提供全面的市场分析、战略规划和可执行的商业建议。


## Features
## 功能

- **Real-time Web Research**: Uses Perplexity AI search for current market data, trends, and competitor intelligence
  **实时网页研究**：使用 `Perplexity AI` 搜索当前市场数据、趋势和竞争对手情报
- **Market Analysis**: Leverages web search and AI insights to analyze market conditions and opportunities
  **市场分析**：利用网页搜索和 `AI` 洞察分析市场状况与机会
- **Strategic Recommendations**: Generates actionable business strategies with timelines and implementation plans
  **战略建议**：生成包含时间表和实施计划的可执行商业策略
- **Risk Assessment**: Identifies potential risks and provides mitigation strategies
  **风险评估**：识别潜在风险并提供缓解策略
- **Interactive UI**: Clean Google ADK web interface for easy consultation
  **交互式 `UI`**：简洁的 `Google ADK` 网页界面，便于咨询
- **Evaluation System**: Built-in evaluation and debugging capabilities with session tracking
  **评估系统**：内置评估与调试能力，并支持会话跟踪

## How It Works
## 工作原理

1. **Input Phase**: User provides business questions or consultation requests through the ADK web interface
   **输入阶段**：用户通过 `ADK` 网页界面提供商业问题或咨询请求
2. **Research Phase**: The agent conducts real-time web research using Perplexity AI to gather current market data
   **研究阶段**：智能体使用 `Perplexity AI` 进行实时网页研究，以收集当前市场数据
3. **Analysis Phase**: The agent uses market analysis tools to process the query and generate insights
   **分析阶段**：智能体使用市场分析工具处理查询并生成洞察
4. **Strategy Phase**: Strategic recommendations are generated based on the analysis and web research
   **策略阶段**：基于分析和网页研究生成战略建议
5. **Synthesis Phase**: The agent combines findings into a comprehensive consultation report with citations
   **综合阶段**：智能体将研究发现整合为带引用的综合咨询报告
6. **Output Phase**: Actionable recommendations with timelines and implementation steps are presented
   **输出阶段**：展示包含时间表和实施步骤的可执行建议

## Requirements
## 要求

- Python 3.8+
  `Python 3.8+`
- Google API key (for Gemini model)
  `Google API key`（用于 `Gemini` 模型）
- Perplexity API key (for real-time web search)
  `Perplexity API key`（用于实时网页搜索）
- Required Python packages (see `requirements.txt`)
  所需 `Python` 包（见 `requirements.txt`）

## Installation
## 安装

1. Clone this repository:
   克隆此仓库：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/single_agent_apps
   ```

2. Install the required packages:
   安装所需包：
   ```bash
   pip install -r requirements.txt
   ```

## Usage
## 使用方法

1. Set your API keys:
   设置你的 `API key`：
   ```bash
   export GOOGLE_API_KEY=your-google-api-key
   export PERPLEXITY_API_KEY=your-perplexity-api-key
   ```

2. Start the Google ADK web interface:
   启动 `Google ADK` 网页界面：
   ```bash
   adk web 
   ```

3. Open your browser and navigate to `http://localhost:8000`
   打开浏览器并访问 `http://localhost:8000`

4. Select "AI Business Consultant" from the available agents
   从可用智能体中选择 “AI Business Consultant”

5. Enter your business questions or consultation requests
   输入你的商业问题或咨询请求

6. Review the comprehensive analysis and strategic recommendations with real-time web data and citations
   查看包含实时网页数据和引用的综合分析与战略建议

7. Use the Eval tab to save and evaluate consultation sessions
   使用 `Eval` 标签页保存并评估咨询会话

## Example Consultation Topics
## 示例咨询主题

- "I want to launch a SaaS startup for small businesses"
  “我想为小型企业推出一个 `SaaS` 创业项目”
- "Should I expand my retail business to e-commerce?"
  “我是否应该将零售业务扩展到电子商务？”
- "What are the market opportunities in healthcare technology?"
  “医疗技术领域有哪些市场机会？”
- "How should I position my new fintech product?"
  “我应该如何定位新的金融科技产品？”
- "What are the risks of entering the renewable energy market?"
  “进入可再生能源市场有哪些风险？”

## Technical Details
## 技术细节

The application uses specialized analysis tools:
该应用使用专门的分析工具：

1. **Perplexity Search Tool**: Conducts real-time web research using Perplexity AI's "sonar" model to gather current market data, competitor information, and industry trends with citations.
   **`Perplexity Search Tool`**：使用 `Perplexity AI` 的 “sonar” 模型进行实时网页研究，收集当前市场数据、竞争对手信息和行业趋势，并附带引用。

2. **Market Analysis Tool**: Processes business queries and generates market insights, competitive analysis, and opportunity identification.
   **`Market Analysis Tool`**：处理商业查询，并生成市场洞察、竞争分析和机会识别。

3. **Strategic Recommendations Tool**: Creates actionable business strategies with priority levels, timelines, and implementation roadmaps.
   **`Strategic Recommendations Tool`**：创建包含优先级、时间表和实施路线图的可执行商业策略。

The agent is built on Google ADK's LlmAgent framework using the Gemini 2.5 Flash model, providing fast and accurate business consultation capabilities backed by real-time web research.
该智能体基于 `Google ADK` 的 `LlmAgent` 框架构建，并使用 `Gemini 2.5 Flash` 模型，在实时网页研究支持下提供快速且准确的商业咨询能力。

## Evaluation and Testing
## 评估与测试

The agent includes built-in evaluation features:
该智能体包含内置评估功能：

- **Session Management**: Track consultation history and progress
  **会话管理**：跟踪咨询历史和进展
- **Test Case Creation**: Save successful consultations as evaluation cases
  **测试用例创建**：将成功的咨询保存为评估用例
- **Performance Metrics**: Monitor tool usage and response quality
  **性能指标**：监控工具使用情况和响应质量
- **Custom Evaluation**: Configure metrics for specific business requirements
  **自定义评估**：针对特定业务需求配置指标
