# Advanced LLM Apps

> 高级 `LLM` 应用合集

`advanced_llm_apps` collects practical `LLM` applications that go beyond starter examples: `RAG` chat apps, memory-enabled assistants, fine-tuning demos, optimization tools, multimodal search, and guided reasoning interfaces.

> `advanced_llm_apps` 汇集了比入门示例更完整的实用 `LLM` 应用：包括 `RAG` 聊天应用、带记忆的助手、微调示例、优化工具、多模态搜索，以及引导式推理界面。

Use this folder when you want a runnable reference for building richer `LLM` products with real inputs, state, retrieval, model routing, or cost/performance optimization.

> 当你需要构建更完整的 `LLM` 产品，并希望参考可运行的真实输入、状态管理、检索、模型路由或成本/性能优化示例时，可以从这个目录开始。

## Project Map

> ## 项目地图

### Chat With Data Sources

> ### 与数据源对话

Turn external content into a chat interface using `RAG`, embeddings, and lightweight app frameworks.

> 使用 `RAG`、嵌入模型和轻量应用框架，将外部内容转换为可对话的界面。

- [Chat with GitHub](chat_with_X_tutorials/chat_with_github/) - Ask questions about a `GitHub` repository with a compact `RAG` app.

  > [与 `GitHub` 对话](chat_with_X_tutorials/chat_with_github/) - 使用紧凑的 `RAG` 应用询问 `GitHub` 仓库内容。

- [Chat with Gmail](chat_with_X_tutorials/chat_with_gmail/) - Query your `Gmail` inbox through an `LLM` chat interface.

  > [与 `Gmail` 对话](chat_with_X_tutorials/chat_with_gmail/) - 通过 `LLM` 聊天界面查询你的 `Gmail` 收件箱。

- [Chat with PDF](chat_with_X_tutorials/chat_with_pdf/) - Upload a `PDF` and ask grounded questions about its content.

  > [与 `PDF` 对话](chat_with_X_tutorials/chat_with_pdf/) - 上传 `PDF`，并围绕文档内容进行有依据的问答。

- [Chat with Research Papers](chat_with_X_tutorials/chat_with_research_papers/) - Search and discuss `arXiv` papers with a research-focused assistant.

  > [与研究论文对话](chat_with_X_tutorials/chat_with_research_papers/) - 使用面向研究的助手检索并讨论 `arXiv` 论文。

- [Chat with Substack](chat_with_X_tutorials/chat_with_substack/) - Ask questions about a `Substack` newsletter using `OpenAI` and `Embedchain`.

  > [与 `Substack` 对话](chat_with_X_tutorials/chat_with_substack/) - 使用 `OpenAI` 和 `Embedchain` 针对 `Substack` Newsletter 提问。

- [Chat with YouTube Videos](chat_with_X_tutorials/chat_with_youtube_videos/) - Use transcripts and memory to chat with `YouTube` video content.

  > [与 `YouTube` 视频对话](chat_with_X_tutorials/chat_with_youtube_videos/) - 结合字幕和记忆能力，与 `YouTube` 视频内容对话。

- [Streaming AI Chatbot](chat_with_X_tutorials/streaming_ai_chatbot/) - Demonstrates real-time `AI` response streaming and conversation state management with `Motia`.

  > [流式 `AI` 聊天机器人](chat_with_X_tutorials/streaming_ai_chatbot/) - 展示如何使用 `Motia` 实现实时 `AI` 响应流和会话状态管理。

### Memory-Based LLM Apps

> ### 带记忆的 `LLM` 应用

Build assistants that remember user preferences, conversation history, or shared context across sessions.

> 构建能够跨会话记住用户偏好、对话历史或共享上下文的助手。

- [AI Arxiv Agent with Memory](llm_apps_with_memory_tutorials/ai_arxiv_agent_memory/) - Research assistant with `arXiv` search, user-interest memory, and web browsing.

  > [带记忆的 `AI arXiv` 研究助手](llm_apps_with_memory_tutorials/ai_arxiv_agent_memory/) - 结合 `arXiv` 检索、用户兴趣记忆和网页浏览的研究助手。

- [AI Travel Agent with Memory](llm_apps_with_memory_tutorials/ai_travel_agent_memory/) - Travel planning assistant that remembers preferences and past interactions.

  > [带记忆的 `AI` 旅行助手](llm_apps_with_memory_tutorials/ai_travel_agent_memory/) - 能记住用户偏好和历史互动的旅行规划助手。

- [LLM App with Personalized Memory](llm_apps_with_memory_tutorials/llm_app_personalized_memory/) - `OpenAI` chatbot with persistent user memory.

  > [带个性化记忆的 `LLM` 应用](llm_apps_with_memory_tutorials/llm_app_personalized_memory/) - 具备持久化用户记忆的 `OpenAI` 聊天机器人。

- [Local ChatGPT with Memory](llm_apps_with_memory_tutorials/local_chatgpt_with_memory/) - Fully local `Llama 3.1` chat app with local embeddings and vector storage.

  > [带记忆的本地 `ChatGPT` 克隆](llm_apps_with_memory_tutorials/local_chatgpt_with_memory/) - 基于本地 `Llama 3.1`、本地嵌入和向量存储的聊天应用。

- [Multi-LLM Shared Memory](llm_apps_with_memory_tutorials/multi_llm_memory/) - Shared memory layer for conversations across multiple `LLM` providers.

  > [多 `LLM` 共享记忆](llm_apps_with_memory_tutorials/multi_llm_memory/) - 面向多个 `LLM` Provider 的共享会话记忆层。

- [Llama 3 Stateful Chat](llm_apps_with_memory_tutorials/llama3_stateful_chat/) - Local stateful chat example for `Llama 3`.

  > [`Llama 3` 有状态聊天](llm_apps_with_memory_tutorials/llama3_stateful_chat/) - 面向 `Llama 3` 的本地有状态聊天示例。

### Fine-Tuning Tutorials

> ### 微调教程

Small, focused examples for adapting open models with `LoRA`, `4-bit` loading, and `Unsloth`.

> 使用 `LoRA`、`4-bit` 加载和 `Unsloth` 适配开源模型的小型聚焦示例。

- [Finetune Gemma 3](llm_finetuning_tutorials/gemma3_finetuning/) - Minimal `Gemma 3` fine-tuning workflow with `Unsloth`.

  > [微调 `Gemma 3`](llm_finetuning_tutorials/gemma3_finetuning/) - 使用 `Unsloth` 的最小化 `Gemma 3` 微调流程。

- [Finetune Llama 3.2](llm_finetuning_tutorials/llama3.2_finetuning/) - Compact `Llama 3.2` fine-tuning example designed for quick experimentation.

  > [微调 `Llama 3.2`](llm_finetuning_tutorials/llama3.2_finetuning/) - 面向快速实验的紧凑型 `Llama 3.2` 微调示例。

### Optimization Tools

> ### 优化工具

Explore techniques for reducing token usage, compressing context, and making `LLM` calls more efficient.

> 探索减少 Token 使用、压缩上下文，以及提升 `LLM` 调用效率的技术。

- [LLM Optimization Tools](llm_optimization_tools/) - Index for cost and performance optimization utilities.

  > [`LLM` 优化工具](llm_optimization_tools/) - 成本与性能优化工具索引。

- [Headroom Context Optimization](llm_optimization_tools/headroom_context_optimization/) - Compress redundant tool output while preserving useful context.

  > [`Headroom` 上下文优化](llm_optimization_tools/headroom_context_optimization/) - 压缩冗余工具输出，同时保留有用上下文。

- [Toonify Token Optimization](llm_optimization_tools/toonify_token_optimization/) - Use `TOON` notation to reduce structured-data token usage.

  > [`Toonify` Token 优化](llm_optimization_tools/toonify_token_optimization/) - 使用 `TOON` 表示法减少结构化数据的 Token 消耗。

### Multimodal And Product Demos

> ### 多模态与产品化示例

These projects show richer product patterns beyond basic chat: visual search, resume matching, critique loops, and guided thinking paths.

> 这些项目展示了基础聊天之外更完整的产品形态：视觉搜索、简历匹配、批判改进循环和引导式思考路径。

- [Multimodal Video Moment Finder](multimodal_video_moment_finder/) - Find video moments using image or text queries powered by `Gemini Embedding 2`.

  > [多模态视频片段查找器](multimodal_video_moment_finder/) - 使用 `Gemini Embedding 2` 基于图片或文字查询定位视频片段。

- [Resume & Job Matcher](resume_job_matcher/) - Compare a resume with a job description and generate fit analysis.

  > [简历与职位匹配器](resume_job_matcher/) - 对比简历和职位描述，并生成匹配度分析。

- [GPT-OSS Critique & Improvement Loop](gpt_oss_critique_improvement_loop/) - Demonstrates an automatic critique and revision pattern with `GPT-OSS` through `Groq`.

  > [`GPT-OSS` 批判与改进循环](gpt_oss_critique_improvement_loop/) - 展示通过 `Groq` 使用 `GPT-OSS` 实现自动批判和修订的模式。

- [ThinkPath Chatbot](thinkpath_chatbot_app/) - A guided-thinking chat interface that lets users control reasoning depth step by step.

  > [`ThinkPath` 聊天机器人](thinkpath_chatbot_app/) - 引导式思考聊天界面，让用户逐步控制推理深度。

- [The Magician IA Reader](chat-with-tarots/) - Combines `AI`, natural language input, and tarot-card meanings for interpretive readings.

  > [`The Magician IA Reader`](chat-with-tarots/) - 结合 `AI`、自然语言输入和塔罗牌含义，生成解读式反馈。

### Cursor AI Experiments

> ### `Cursor AI` 实验

Experimental scripts and small apps for local chat, model routing, web scraping, and multi-agent research.

> 面向本地聊天、模型路由、网页抓取和多 Agent 研究的小型实验脚本与应用。

- [Local ChatGPT Clone](cursor_ai_experiments/local_chatgpt_clone/) - Local `ChatGPT`-style app using `Llama 3` and `Streamlit`.

  > [本地 `ChatGPT` 克隆](cursor_ai_experiments/local_chatgpt_clone/) - 使用 `Llama 3` 和 `Streamlit` 构建的本地聊天应用。

- [RouteLLM Chat App](cursor_ai_experiments/llm_router_app/) - Routes prompts between language models based on task complexity.

  > [`RouteLLM` 聊天应用](cursor_ai_experiments/llm_router_app/) - 根据任务复杂度在不同语言模型之间路由 Prompt。

- [Standalone Experiments](cursor_ai_experiments/) - Includes `ai_web_scrapper.py`, `chatgpt_clone_llama3.py`, and `multi_agent_researcher.py`.

  > [独立实验脚本](cursor_ai_experiments/) - 包含 `ai_web_scrapper.py`、`chatgpt_clone_llama3.py` 和 `multi_agent_researcher.py`。

## How To Run

> ## 如何运行

Most `Python` projects in this folder follow the same pattern:

> 本目录中大多数 `Python` 项目都遵循相同运行方式：

```bash
cd advanced_llm_apps/<project-folder>
pip install -r requirements.txt
streamlit run <app-file>.py
```

For `JavaScript` or `TypeScript` projects, install dependencies and run the app script defined in `package.json`:

> 对于 `JavaScript` 或 `TypeScript` 项目，请安装依赖，并运行 `package.json` 中定义的应用脚本：

```bash
cd advanced_llm_apps/<project-folder>
npm install
npm run dev
```

Some examples require provider keys such as `OPENAI_API_KEY`, `GROQ_API_KEY`, or model-specific local runtimes. Check each project README before running.

> 部分示例需要 `OPENAI_API_KEY`、`GROQ_API_KEY` 等 Provider Key，或特定的本地模型运行环境。运行前请查看对应项目的 `README.md`。

## Documentation Convention

> ## 文档约定

This README uses a direct bilingual layout: each English section or bullet is followed by its matching Chinese translation in a blockquote.

> 本 `README.md` 使用直接中英对照布局：每个英文段落或列表项后，都紧跟对应中文翻译并以引用块展示。

Project names, commands, filenames, model names, providers, API keys, and framework names are formatted as inline code for easier scanning.

> 项目名、命令、文件名、模型名、Provider、API Key 和框架名会使用内联代码格式，便于快速浏览。
