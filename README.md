# Awesome LLM Apps

> 精选 LLM 应用合集

**100+ open-source AI agents, agent skills, and RAG apps. Hand-built, tested end-to-end, Apache-2.0.**

> **100 多个开源 AI Agent、Agent Skill 和 RAG 应用。所有项目均经人工构建和端到端测试，采用 Apache-2.0 许可证。**

Clone it, ship it, sell it - 100% free and open-source.

> 可克隆、交付或商业化使用，完全免费且开源。

Works with Claude, Gemini, GPT, DeepSeek, Llama, Qwen and other open-source models.

> 支持 Claude、Gemini、GPT、DeepSeek、Llama、Qwen 及其他开源模型。

[Step-by-step tutorials on Unwind AI](https://www.theunwindai.com) · [Quick start](#-run-one-now) · [Browse all templates](#-browse-all-templates)

> [Unwind AI 分步教程](https://www.theunwindai.com) · [快速开始](#-run-one-now) · [浏览全部模板](#-browse-all-templates)

## 🚀 Run one now

> ## 🚀 立即运行一个项目

Give your coding agent a new skill in 10 seconds:

> 10 秒钟为你的编码 Agent 添加一个新 Skill：

```bash
npx skills add https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/project-graveyard
```

Then ask it: *"why do I never finish my side projects?"*

> 然后问它：*“为什么我总是无法完成自己的副项目？”*

Or clone and run any agent in 30 seconds:

> 或者在 30 秒内克隆并运行任意一个 Agent：

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/starter_ai_agents/ai_travel_agent
pip install -r requirements.txt
streamlit run travel_agent.py
```

> New templates drop weekly.

> 每周都会发布新模板。

## 📂 Browse all templates

> ## 📂 浏览全部模板

### 🧩 Agent Skills

> ### 🧩 Agent Skills（可安装的能力包）

Give your coding agent new abilities. One command to install, plain English to use. Every skill ships real code and passes a security + eval CI gate.

> 为编码 Agent 添加新能力。一条命令即可安装，用自然语言即可使用。每个 Skill 都包含真实代码，并通过安全与评估 CI 检查。

- [⚰️ Project Graveyard](agent_skills/project-graveyard/) - Finds every side project you abandoned, tells you why each one died, and helps you finish the one worth going back to.

  > 找出你放弃过的副项目，说明每个项目失败的原因，并帮助你完成最值得继续的一个。

- [♾️ Self-Improving Agent Skills](agent_skills/self-improving-agent-skills/) - Automatically optimize agent skills using Gemini and ADK.

  > 使用 Gemini 与 ADK 自动优化 Agent Skills。

### 🌱 Starter AI Agents

> ### 🌱 入门 AI Agent

Single-file agents that run with just an API key - a great place to start.

> 只需 API Key 就能运行的单文件 Agent，适合作为入门项目。

- [🎙️ AI Blog to Podcast Agent](starter_ai_agents/ai_blog_to_podcast_agent/) - Turn any blog URL into a narrated podcast episode.

  > 将任意博客 URL 转换成带旁白的播客节目。

- [📊 AI Data Analysis Agent](starter_ai_agents/ai_data_analysis_agent/) - Ask questions of any CSV or Excel file in plain English.

  > 用自然语言询问任意 CSV 或 Excel 文件中的数据。

- [😂 AI Meme Generator Agent](starter_ai_agents/ai_meme_generator_agent_browseruse/) - Makes memes by driving a real browser, not an image API.

  > 通过操控真实浏览器而不是图片 API 来生成表情包。

- [🎵 AI Music Generator Agent](starter_ai_agents/ai_music_generator_agent/) - Prompt in, MP3 track out.

  > 输入提示词，输出 MP3 音轨。

- [🛫 AI Travel Agent](starter_ai_agents/ai_travel_agent/) - Personalized day-by-day travel itineraries.

  > 生成个性化的逐日旅行行程。

- [✨ Gemini Multimodal Agent](starter_ai_agents/multimodal_ai_agent/) - Video analysis plus web search in one agent.

  > 在一个 Agent 中结合视频分析和网页搜索。

- [🔄 Mixture of Agents](starter_ai_agents/mixture_of_agents/) - Multiple LLMs answer, one aggregates the best response.

  > 多个 LLM 分别回答，再由一个模型汇总最佳答案。

- [🔍 OpenAI Research Agent](starter_ai_agents/openai_research_agent/) - Multi-agent topic research with the OpenAI Agents SDK.

  > 基于 OpenAI Agents SDK 的多 Agent 主题研究。

### 🚀 Advanced AI Agents

> ### 🚀 高级 AI Agent

Production-style agents with tools, memory, and multi-step reasoning.

> 具备工具、记忆和多步骤推理能力的生产型 Agent。

- [🔍 AI Deep Research Agent](advanced_ai_agents/single_agent_apps/ai_deep_research_agent/) - Comprehensive web research with the OpenAI Agents SDK and Firecrawl.

  > 使用 OpenAI Agents SDK 和 Firecrawl 进行综合网页研究。

- [📊 AI VC Due Diligence Agent Team](advanced_ai_agents/multi_agent_apps/agent_teams/ai_vc_due_diligence_agent_team/) - Multi-agent startup investment analysis with Gemini 3.

  > 使用 Gemini 3 进行多 Agent 创业公司投资尽调分析。

- [🤝 AI Consultant Agent](advanced_ai_agents/single_agent_apps/ai_consultant_agent/) - Market analysis and strategy recommendations with live web research.

  > 结合实时网页研究的市场分析与战略建议。

- [🏗️ AI System Architect Agent](advanced_ai_agents/single_agent_apps/ai_system_architect_r1/) - Architecture reviews using DeepSeek R1 reasoning plus Claude.

  > 使用 DeepSeek R1 推理与 Claude 进行架构评审。

- [💰 AI Financial Coach Agent](advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent/) - Personalized budget, debt, and savings analysis.

  > 提供个性化预算、债务和储蓄分析。

- [🎬 AI Movie Production Agent](advanced_ai_agents/single_agent_apps/ai_movie_production_agent/) - Script drafts and casting ideas from a one-line movie concept.

  > 从一句电影概念生成剧本草稿和选角创意。

- [🏋️‍♂️ AI Health & Fitness Agent](advanced_ai_agents/single_agent_apps/ai_health_fitness_agent/) - Tailored diet and workout plans from your goals.

  > 根据你的目标制定饮食与锻炼计划。

### 🤝 Multi-agent Teams

> ### 🤝 多 Agent 团队

Multiple agents collaborating to accomplish complex, cross-domain tasks.

> 多个 Agent 协同完成复杂的跨领域任务。

- [🧲 AI Competitor Intelligence Agent Team](advanced_ai_agents/multi_agent_apps/agent_teams/ai_competitor_intelligence_agent_team/) - Structured competitor teardowns built from their own websites.

  > 基于竞争对手自身网站生成结构化拆解报告。

- [💲 AI Finance Agent Team](advanced_ai_agents/multi_agent_apps/agent_teams/ai_finance_agent_team/) - A financial analyst team in 20 lines of Python.

  > 仅用 20 行 Python 构建的金融分析师团队。

- [👨‍⚖️ AI Legal Agent Team](advanced_ai_agents/multi_agent_apps/agent_teams/ai_legal_agent_team/) - Research, contract analysis, and strategy from a full legal bench.

  > 提供研究、合同分析和策略建议的完整法律 Agent 团队。

- [👨‍🏫 AI Teaching Agent Team](advanced_ai_agents/multi_agent_apps/agent_teams/ai_teaching_agent_team/) - A faculty of agents that builds your complete learning path.

  > 由多个教学 Agent 组成，为你构建完整学习路径。

### 🗣️ Voice AI Agents

> ### 🗣️ 语音 AI Agent

Speech-in, speech-out agents using real-time voice APIs.

> 使用实时语音 API，实现语音输入和输出的 Agent。

- [🗣️ AI Audio Tour Agent](voice_ai_agents/ai_audio_tour_agent/) - Self-guided audio tours from your location, interests, and pace.

  > 根据位置、兴趣和节奏生成自助语音导览。

- [📞 Customer Support Voice Agent](voice_ai_agents/customer_support_voice_agent/) - Voice answers grounded in your own docs.

  > 基于你自己的文档提供有依据的语音客服回答。

- [🔊 Voice RAG Agent](voice_ai_agents/voice_rag_openaisdk/) - Ask your PDFs questions, hear the answers.

  > 向 PDF 提问，并以语音听取回答。

### ♾️ MCP AI Agents

> ### ♾️ MCP AI Agent

Agents that connect to external tools and data via Model Context Protocol.

> 通过模型上下文协议（MCP）连接外部工具和数据的 Agent。

- [♾️ Browser MCP Agent](mcp_ai_agents/browser_mcp_agent/) - Drive a real browser with natural language over MCP.

  > 通过 MCP 用自然语言操控真实浏览器。

- [🐙 GitHub MCP Agent](mcp_ai_agents/github_mcp_agent/) - Explore and analyze any repo in plain English.

  > 用自然语言探索和分析任意仓库。

- [📑 Notion MCP Agent](mcp_ai_agents/notion_mcp_agent/) - Talk to your Notion pages from the terminal.

  > 在终端中与 Notion 页面交互。

### 📀 RAG (Retrieval Augmented Generation)

> ### 📀 RAG（检索增强生成）

Retrieval pipelines, from simple chains to agentic and multi-source.

> 从简单链式流程到 Agent 化、多数据源流程的检索管道。

- [🔥 Agentic RAG with Embedding Gemma](rag_tutorials/agentic_rag_embedding_gemma/) - Fully local agentic RAG with EmbeddingGemma and Llama 3.2.

  > 使用 EmbeddingGemma 和 Llama 3.2 的完全本地化 Agentic RAG。

- [🧐 Agentic RAG with Reasoning](rag_tutorials/agentic_rag_with_reasoning/) - Watch the agent's step-by-step reasoning as it retrieves.

  > 观察 Agent 在检索时的逐步推理过程。

- [🔍 Autonomous RAG](rag_tutorials/autonomous_rag/) - GPT-4o answers from your PDFs, falls back to web search.

  > GPT-4o 基于 PDF 回答问题，必要时回退到网页搜索。

- [🔄 Corrective RAG](rag_tutorials/corrective_rag/) - Retrieval that grades itself and retries before answering.

  > 能自我评分，并在回答前重试的检索流程。

- [🦙 Local RAG Agent](rag_tutorials/local_rag_agent/) - Llama 3.2 and Qdrant, no API keys required.

  > 使用 Llama 3.2 与 Qdrant，无需 API Key。

- [🧩 RAG-as-a-Service](rag_tutorials/rag-as-a-service/) - A production RAG service in under 50 lines.

  > 不到 50 行代码实现一个生产级 RAG 服务。

### 💬 Chat with X

> ### 💬 与任意数据源对话

Turn any data source into a chat interface.

> 将任意数据源转换为聊天界面。

- [💬 Chat with GitHub](advanced_llm_apps/chat_with_X_tutorials/chat_with_github/) - Any repo, answered in 30 lines of RAG.

  > 用 30 行 RAG 代码实现任意仓库问答。

- [📨 Chat with Gmail](advanced_llm_apps/chat_with_X_tutorials/chat_with_gmail/) - Ask your inbox questions.

  > 向自己的收件箱提问。

- [📄 Chat with PDF](advanced_llm_apps/chat_with_X_tutorials/chat_with_pdf/) - The classic, in 30 lines of Python.

  > 经典的 PDF 问答，用 30 行 Python 实现。

### 🧑‍🏫 AI Agent Framework Crash Courses

> ### 🧑‍🏫 AI Agent 框架速成课程

Deep-dive tutorials on the major agent frameworks.

> 主流 Agent 框架的深入教程。

- [Google ADK Crash Course](ai_agent_framework_crash_course/google_adk_crash_course/) - Starter agent, structured outputs, tools, memory, callbacks, plugins, and multi-agent patterns. Model-agnostic.

  > Google ADK 的入门、结构化输出、工具、记忆、回调、插件和多 Agent 模式教程；不绑定特定模型。

- [OpenAI Agents SDK Crash Course](ai_agent_framework_crash_course/openai_sdk_crash_course/) - Starter agent, function calling, structured outputs, tools, memory, evaluation, handoffs, swarm orchestration, and routing logic.

  > OpenAI Agents SDK 的入门、函数调用、结构化输出、工具、记忆、评估、交接、群体编排和路由逻辑教程。

---

⭐ [Star the repo](https://github.com/Shubhamsaboo/awesome-llm-apps/stargazers) to get notified when new templates drop.

> ⭐ [给仓库加星](https://github.com/Shubhamsaboo/awesome-llm-apps/stargazers)，以便在发布新模板时收到通知。

Apache-2.0 · See [LICENSE](LICENSE) · Fork it, ship it, sell it.

> Apache-2.0 · 查看 [许可证](LICENSE) · 可以 Fork、交付或商业化使用。
