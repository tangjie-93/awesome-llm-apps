## 💲 AI Finance Agent Team with Web Access
## 💲 支持网页访问的 `AI` 金融智能体团队

This script demonstrates how to build a team of AI agents that work together as a financial analyst using GPT-4o in just 20 lines of Python code. The system combines web search capabilities with financial data analysis tools to provide comprehensive financial insights.
该脚本演示如何仅用 `20` 行 `Python` 代码，使用 `GPT-4o` 构建一个像金融分析师一样协作的 `AI` 智能体团队。系统将网页搜索能力与金融数据分析工具结合起来，提供全面的金融洞察。

### Features
### 功能

- Multi-agent system with specialized roles:
- 具备专门角色的多智能体系统：
    - Web Agent for general internet research
    - `Web Agent` 用于通用互联网研究
    - Finance Agent for detailed financial analysis
    - `Finance Agent` 用于详细金融分析
    - Team Agent for coordinating between agents
    - `Team Agent` 用于协调各智能体
- Real-time financial data access through YFinance
- 通过 `YFinance` 访问实时金融数据
- Web search capabilities using DuckDuckGo
- 使用 `DuckDuckGo` 提供网页搜索能力
- Persistent storage of agent interactions using SQLite
- 使用 `SQLite` 持久化存储智能体交互

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
1. 克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_finance_agent_team
```

2. Install the required dependencies:
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```

3. Get your OpenAI API Key
3. 获取你的 `OpenAI API Key`

- Sign up for an [OpenAI account](https://platform.openai.com/) (or the LLM provider of your choice) and obtain your API key.
- 注册 [OpenAI account](https://platform.openai.com/)（或你选择的 `LLM` 提供商），并获取你的 `API key`。
- Set your OpenAI API key as an environment variable:
- 将你的 `OpenAI API key` 设置为环境变量：

```bash
export OPENAI_API_KEY='your-api-key-here'
```

4. Run the team of AI Agents
4. 运行 `AI Agents` 团队

```bash
python3 finance_agent_team.py
```

5. Open your web browser and navigate to the URL provided in the console output to interact with the team of AI agents through the playground interface.
5. 打开网页浏览器，并导航到控制台输出中提供的 `URL`，通过 `playground` 界面与 `AI` 智能体团队交互。
