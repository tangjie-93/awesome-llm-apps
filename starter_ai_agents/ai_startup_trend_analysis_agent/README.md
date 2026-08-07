# AI Startup Trend Analysis Agent
# AI 创业趋势分析代理

This agent researches startup trends, market gaps, and growth opportunities.
这个 Agent 用于研究创业趋势、市场空缺和增长机会。

It combines DuckDuckGo, Newspaper4k, and Claude-based analysis.
它结合 DuckDuckGo、Newspaper4k 和基于 Claude 的分析能力。

## Features
## 功能特性

- Accept a startup sector or technology prompt.
- 接收创业赛道或技术方向的提示词。
- Gather recent news and market articles.
- 收集最新新闻和市场文章。
- Summarize verified information.
- 总结已验证的信息。
- Highlight emerging trends and opportunities.
- 提炼新兴趋势和机会。

## Setup
## 安装

1. Clone the repository.
1. 克隆仓库。
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/starter_ai_agents/ai_startup_trend_analysis_agent
   ```
2. Create and activate a virtual environment.
2. 创建并激活虚拟环境。
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies.
3. 安装依赖。
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app.
4. 运行应用。
   ```bash
   streamlit run startup_trends_agent.py
   ```

## Note
## 注意

You need an Anthropic API key for the Claude-based workflow.
基于 Claude 的流程需要 Anthropic API Key。
