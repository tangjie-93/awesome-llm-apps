# OpenAI Research Agent
# OpenAI 研究代理

This project builds a structured research assistant with the OpenAI Agents SDK.
这个项目使用 OpenAI Agents SDK 构建结构化研究助手。

It combines triage, retrieval, and editor agents to produce a research report.
它结合分诊、检索和编辑 Agent，生成研究报告。

## Features
## 功能特性

- Ask a research question in natural language.
- 用自然语言提出研究问题。
- Route work through specialized agents.
- 通过专门的 Agent 分配任务。
- Collect and summarize supporting sources.
- 收集并总结支持性来源。
- Produce a structured final report.
- 输出结构化最终报告。

## Run
## 运行

1. Clone the repository.
1. 克隆仓库。
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd starter_ai_agents/openai_research_agent
   ```
2. Install dependencies.
2. 安装依赖。
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app.
3. 启动应用。
   ```bash
   streamlit run research_agent.py
   ```

## Notes
## 注意事项

Make sure your OpenAI API key is available before starting the workflow.
在启动流程前，请先准备好 OpenAI API Key。
