# 🚀 OpenAI Agents SDK Crash Course
# 🚀 OpenAI Agents SDK 速成课程

A comprehensive tutorial series for learning OpenAI's Agents SDK from basics to advanced concepts. This crash course is designed to take you from zero to hero in building AI agents with the OpenAI Agents SDK.

这是一套从基础到进阶学习 OpenAI `Agents SDK` 的完整教程。它会带你从零开始，逐步掌握如何使用 `OpenAI Agents SDK` 构建 `AI agent`。

## 📚 What is OpenAI Agents SDK?
## 📚 什么是 OpenAI Agents SDK？

OpenAI Agents SDK is a powerful framework for **developing and deploying AI agents**. It provides:

OpenAI `Agents SDK` 是一个用于**开发和部署 AI agent** 的强大框架。它提供：

### Key Features:
### 主要特性：
- **Agent Orchestration**: Create and manage intelligent AI agents

  **Agent 编排**：创建和管理智能 `AI agent`

- **Tool Integration**: Extend agents with custom and built-in tools

  **工具集成**：使用自定义工具和内置工具扩展 `agent`

- **Structured Outputs**: Type-safe responses using Pydantic models

  **结构化输出**：使用 `Pydantic` 模型返回类型安全的结果

- **Multi-Agent Workflows**: Coordinate multiple agents with handoffs

  **多 Agent 工作流**：通过 `handoff` 协调多个 `agent`

- **Real-time Execution**: Sync, async, and streaming execution methods

  **实时执行**：支持同步、异步和流式执行方式

- **Voice Integration**: Static, streaming, and realtime voice capabilities

  **语音集成**：支持静态、流式和实时语音能力

- **Session Management**: Automatic conversation memory and history

  **会话管理**：自动维护对话记忆和历史记录

- **Production Ready**: Built-in tracing, guardrails, and monitoring

  **可用于生产**：内置 `tracing`、`guardrails` 和监控能力

## 🎯 Learning Path
## 🎯 学习路径

This crash course covers the essential concepts of OpenAI Agents SDK through hands-on tutorials:

本速成课程通过动手教程覆盖 `OpenAI Agents SDK` 的核心概念：

### 📚 **Tutorials**
### 📚 **教程**

#### **🌱 Foundation Layer**
#### **🌱 基础层**

1. **[1_starter_agent](./1_starter_agent/README.md)** - Your first OpenAI agent

   **[1_starter_agent](./1_starter_agent/README.md)**：你的第一个 OpenAI agent

   - Basic agent creation and configuration

     基础 `agent` 创建与配置

   - Understanding different execution methods

     理解不同的执行方式

   - Simple text processing and responses

     简单文本处理与响应

2. **[2_structured_output_agent](./2_structured_output_agent/README.md)** - Type-safe responses

   **[2_structured_output_agent](./2_structured_output_agent/README.md)**：类型安全的响应

   - **Support Ticket Agent** - Convert complaints to structured tickets

     **支持工单 Agent**：将投诉转换为结构化工单

   - **Product Review Agent** - Extract structured data from reviews

     **产品评论 Agent**：从评论中提取结构化数据

   - Pydantic models and validation

     `Pydantic` 模型与校验

#### **🔧 Core Capabilities Layer**
#### **🔧 核心能力层**

3. **[3_tool_using_agent](./3_tool_using_agent/README.md)** - Agent tools & functions

   **[3_tool_using_agent](./3_tool_using_agent/README.md)**：Agent 工具与函数

   - Custom function tools with `@function_tool`

     使用 `@function_tool` 编写自定义函数工具

   - Built-in tools (WebSearch, CodeInterpreter, FileSearch)

     内置工具（`WebSearch`、`CodeInterpreter`、`FileSearch`）

   - Tool integration and execution patterns

     工具集成与执行模式

4. **[4_running_agents](./4_running_agents/README.md)** - Running & execution mastery

   **[4_running_agents](./4_running_agents/README.md)**：运行与执行掌握

   - The agent loop: LLM calls, tool execution, handoffs

     `agent loop`：`LLM` 调用、工具执行、`handoff`

   - Sync, async, and streaming execution methods

     同步、异步和流式执行方式

   - Advanced streaming events and exception handling

     高级流式事件与异常处理

   - Run configuration and conversation management

     运行配置与对话管理

5. **[5_context_management](./5_context_management/README.md)** - State & context handling

   **[5_context_management](./5_context_management/README.md)**：状态与上下文处理

   - Context passing between runs

     在多次运行之间传递上下文

   - State persistence and management

     状态持久化与管理

   - Conversation flow control

     对话流程控制

#### **🧠 Advanced Features Layer**
#### **🧠 进阶特性层**

6. **[6_guardrails_validation](./6_guardrails_validation/README.md)** - Safety & validation

   **[6_guardrails_validation](./6_guardrails_validation/README.md)**：安全与校验

   - Input guardrails for user validation

     用于用户输入校验的输入 `guardrails`

   - Output guardrails for response filtering

     用于响应过滤的输出 `guardrails`

   - Custom business rule validation

     自定义业务规则校验

7. **[7_sessions](./7_sessions/README.md)** - Sessions & memory management

   **[7_sessions](./7_sessions/README.md)**：会话与记忆管理

   - Automatic conversation history with SQLiteSession

     使用 `SQLiteSession` 自动保存对话历史

   - Memory operations and conversation corrections

     记忆操作与对话修正

   - Multiple session management and organization

     多会话管理与组织

#### **🤝 Multi-Agent Layer**
#### **🤝 多 Agent 层**

8. **[8_handoffs_delegation](./8_handoffs_delegation/README.md)** - Agent handoffs & delegation

   **[8_handoffs_delegation](./8_handoffs_delegation/README.md)**：Agent 转交与委派

   - Agent-to-agent task delegation

     `agent` 与 `agent` 之间的任务委派

   - Triage systems and smart routing

     分诊系统与智能路由

   - Advanced handoff configuration with callbacks

     带回调的高级 `handoff` 配置

9. **[9_multi_agent_orchestration](./9_multi_agent_orchestration/README.md)** - Complex workflows

   **[9_multi_agent_orchestration](./9_multi_agent_orchestration/README.md)**：复杂工作流

   - Parallel agent execution with `asyncio.gather()`

     使用 `asyncio.gather()` 并行执行多个 `agent`

   - Agents as tools orchestration patterns

     将 `agent` 作为工具的编排模式

   - Multi-stage workflow coordination

     多阶段工作流协调

#### **🔍 Production Layer**
#### **🔍 生产层**

10. **[10_tracing_observability](./10_tracing_observability/README.md)** - Monitoring & debugging

    **[10_tracing_observability](./10_tracing_observability/README.md)**：监控与调试

    - Built-in tracing and execution visualization

      内置 `tracing` 与执行可视化

    - Custom traces and spans for complex workflows

      面向复杂工作流的自定义 `trace` 和 `span`

    - Performance monitoring and optimization

      性能监控与优化

#### **🎙️ Voice & Advanced Features**
#### **🎙️ 语音与进阶特性**

11. **[11_voice](./11_voice/README.md)** - Voice agents & real-time conversation

    **[11_voice](./11_voice/README.md)**：语音 agent 与实时对话

    - Static voice processing (turn-based interaction)

      静态语音处理（轮次式交互）

    - Streaming voice processing (real-time conversation)

      流式语音处理（实时对话）

    - Realtime voice agents (ultra-low latency with WebSocket)

      实时语音 `agent`（基于 `WebSocket` 的超低延迟）

    - Speech-to-text, text-to-speech, and voice pipelines

      语音转文本、文本转语音和语音管线

## 🛠️ Prerequisites
## 🛠️ 前置条件

Before starting this crash course, ensure you have:

开始之前，请确认你已经具备：

- **Python 3.8+** installed (Python 3.9+ required for voice features)

  已安装 **Python 3.8+**（语音功能需要 `Python 3.9+`）

- **OpenAI API Key** from [OpenAI Platform](https://platform.openai.com/api-keys)

  来自 [OpenAI Platform](https://platform.openai.com/api-keys) 的 **OpenAI API Key**

- Basic understanding of Python and APIs

  对 `Python` 和 `API` 的基础了解

- Familiarity with async/await concepts (helpful but not required)

  熟悉 `async/await` 概念（有帮助，但不是必须）

- **For voice tutorials**: Microphone and speakers/headphones

  **语音教程所需**：麦克风和扬声器/耳机

## 📖 How to Use This Course
## 📖 如何使用本课程

Each tutorial follows a consistent structure:

每个教程都遵循一致的结构：

- **README.md**: Concept explanation and learning objectives

  **README.md**：概念说明与学习目标

- **Python files**: Contains the agent implementations and examples

  **Python 文件**：包含 `agent` 实现与示例

- **Interactive interfaces**: Streamlit web apps for hands-on testing

  **交互界面**：用于动手测试的 `Streamlit` Web 应用

- **Submodules**: Organized examples for different concepts

  **子模块**：按不同概念组织的示例

- **requirements.txt**: Dependencies for the tutorial

  **requirements.txt**：该教程的依赖

- **env.example**: Environment variable template

  **env.example**：环境变量模板

### Learning Approach:
### 学习方式：
1. **Read the README** to understand the concept

   **阅读 README**，先理解概念

2. **Examine the code** to see the implementation

   **查看代码**，理解实现方式

3. **Run the examples** to see agents in action

   **运行示例**，观察 `agent` 实际工作

4. **Experiment** by modifying the code

   **自行实验**，修改代码观察效果

5. **Use interactive interfaces** for hands-on testing

   **使用交互界面**，进行动手测试

6. **Try voice features** (tutorial 11) with your microphone

   **尝试语音功能**（教程 11），配合麦克风使用

7. **Move to the next tutorial** when ready

   **准备好后**，进入下一个教程

## 🎯 Tutorial Features
## 🎯 教程特性

Each tutorial includes:

每个教程都包含：

- ✅ **Clear concept explanation**

  ✅ **清晰的概念说明**

- ✅ **Minimal, working code examples**

  ✅ **精简且可运行的代码示例**

- ✅ **Real-world use cases**

  ✅ **真实场景的使用案例**

- ✅ **Step-by-step instructions**

  ✅ **逐步操作说明**

- ✅ **Interactive web interfaces**

  ✅ **交互式 Web 界面**

- ✅ **Best practices and tips**

  ✅ **最佳实践与提示**

## 🚀 Quick Start
## 🚀 快速开始

1. **Clone the repository** and navigate to this directory

   **克隆仓库**并进入当前目录

2. **Choose a tutorial** from the list above

   从上面的列表中**选择一个教程**

3. **Follow the README** instructions for that tutorial

   按照该教程的 `README` 指引操作

4. **Install dependencies**: `pip install -r requirements.txt`

   **安装依赖**：`pip install -r requirements.txt`

5. **Set up environment**: Copy `env.example` to `.env` and add your API key

   **配置环境**：将 `env.example` 复制为 `.env`，并填入你的 API Key

6. **Run the examples** and start learning!

   **运行示例**，开始学习！

## 🔧 Environment Setup
## 🔧 环境配置

Each tutorial requires an OpenAI API key. Create a `.env` file in each tutorial directory:

每个教程都需要一个 OpenAI API Key。请在对应教程目录下创建 `.env` 文件：

```bash
OPENAI_API_KEY=sk-your_openai_key_here
```

Get your API key from: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

你的 API Key 可以从这里获取：[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

## 💡 Learning Tips
## 💡 学习建议

- **Start Sequential**: Follow tutorials in order for best learning experience

  **按顺序学习**：按照教程顺序学习，效果最好

- **Experiment Freely**: Modify code and see what happens

  **大胆实验**：修改代码并观察结果

- **Use Web Interfaces**: Interactive apps make learning more engaging

  **使用 Web 界面**：交互式应用会让学习更直观

- **Read Error Messages**: They often contain helpful guidance

  **阅读错误信息**：它们通常包含有用提示

- **Join Community**: Engage with other learners and share experiences

  **参与社区**：与其他学习者交流经验

## 🚨 Common Issues
## 🚨 常见问题

### API Key Problems
### API Key 问题
- Make sure your `.env` file is in the tutorial directory

  确保 `.env` 文件位于教程目录中

- Verify your API key is valid and has sufficient credits

  确认你的 API Key 有效且额度充足

- Check for typos in the environment variable name

  检查环境变量名是否拼写正确

### Import Errors
### 导入错误
- Ensure you've installed requirements: `pip install -r requirements.txt`

  确保已经安装依赖：`pip install -r requirements.txt`

- Check that you're using Python 3.8 or higher

  确认你使用的是 `Python 3.8` 或更高版本

- Try creating a virtual environment if you have conflicts

  如果有依赖冲突，尝试创建虚拟环境

### Rate Limiting
### 速率限制
- OpenAI has rate limits based on your plan

  `OpenAI` 会根据你的套餐设置速率限制

- If you hit limits, wait a moment before trying again

  如果触发限制，稍等片刻再重试

- Consider upgrading your OpenAI plan for higher limits

  可以考虑升级 `OpenAI` 套餐以获得更高限制

## 📚 Additional Resources
## 📚 额外资源

- [OpenAI Agents SDK Documentation](https://openai.github.io/openai-agents-python/)

  [OpenAI Agents SDK 文档](https://openai.github.io/openai-agents-python/)

- [OpenAI Platform](https://platform.openai.com/)

  [OpenAI Platform](https://platform.openai.com/)

- [Pydantic Documentation](https://docs.pydantic.dev/)

  [Pydantic 文档](https://docs.pydantic.dev/)

- [Streamlit Documentation](https://docs.streamlit.io/)

  [Streamlit 文档](https://docs.streamlit.io/)

## 🤝 Contributing
## 🤝 贡献

Feel free to contribute improvements, bug fixes, or additional tutorials. Each tutorial should:

欢迎贡献改进、修复 bug 或补充教程。每个教程都应：

- Be self-contained and runnable

  保持自包含且可运行

- Include clear documentation

  包含清晰文档

- Follow the established structure

  遵循既定结构

- Use minimal, understandable code

  使用精简且易懂的代码

## 📊 Progress Tracking
## 📊 进度跟踪

Track your progress through the course:

跟踪你在课程中的学习进度：

- [ ] **Tutorial 1**: Basic agent creation ✨  
  **教程 1**：基础 `agent` 创建 ✨

- [ ] **Tutorial 2**: Structured outputs with `Pydantic`  
  **教程 2**：使用 `Pydantic` 的结构化输出

- [ ] **Tutorial 3**: Tool integration and custom functions  
  **教程 3**：工具集成与自定义函数

- [ ] **Tutorial 4**: Execution methods mastery  
  **教程 4**：执行方式掌握

- [ ] **Tutorial 5**: Context and state management  
  **教程 5**：上下文与状态管理

- [ ] **Tutorial 6**: Guardrails and validation  
  **教程 6**：`guardrails` 与校验

- [ ] **Tutorial 7**: Sessions and memory management  
  **教程 7**：会话与记忆管理

- [ ] **Tutorial 8**: Agent handoffs and delegation  
  **教程 8**：`agent` 转交与委派

- [ ] **Tutorial 9**: Multi-agent orchestration  
  **教程 9**：多 `agent` 编排

- [ ] **Tutorial 10**: Tracing and observability  
  **教程 10**：`tracing` 与可观测性

- [ ] **Tutorial 11**: Voice agents and real-time conversation 🎯  
  **教程 11**：语音 `agent` 与实时对话 🎯

Happy learning! 🚀

祝你学习顺利！🚀
