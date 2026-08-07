# Agents as Tools
# Agent 作为工具

Demonstrates advanced orchestration patterns where agents are used as tools by other agents.

演示如何将一个 Agent 作为另一个 Agent 的工具，实现高级 Agent 编排。

## What This Demonstrates
## 本示例演示的内容

- **Agent.as_tool()**: Converting agents to tools for orchestration
- **Agent.as_tool()**：将 Agent 转换为工具，用于编排其他 Agent
- **Custom Agent Tools**: Using `@function_tool` with `Runner.run()`
- **自定义 Agent 工具**：结合 `@function_tool` 和 `Runner.run()` 创建自定义工具
- **Multi-Agent Workflows**: Coordinating multiple specialized agents
- **多 Agent 工作流**：协调多个专业 Agent 协同完成任务
- **Custom Configuration**: Per-agent settings like max_turns and run_config
- **自定义配置**：为每个 Agent 设置 `max_turns`、`run_config` 等参数

## Quick Start
## 快速开始

1. **Install OpenAI Agents SDK / 安装 OpenAI Agents SDK**

   ```bash
   pip install openai-agents
   ```

2. **Set up environment / 配置运行环境**

   ```bash
   cp ../env.example .env
   # Edit .env and add your OpenAI API key
   # 编辑 .env，填入你的 OpenAI API key
   ```

3. **Run basic orchestration / 运行基础编排示例**

   ```python
   from agents import Runner
   from agent import root_agent

   result = Runner.run_sync(root_agent, "Say 'Hello, how are you?' in Spanish.")
   print(result.final_output)
   ```

4. **Try advanced orchestration / 尝试高级编排示例**

   ```python
   from advanced_agent import advanced_orchestrator

   result = Runner.run_sync(advanced_orchestrator, "Research the benefits of AI in healthcare.")
   print(result.final_output)
   ```

## Key Concepts
## 核心概念

### Basic Agent Tools (`agent.py`)
### 基础 Agent 工具（`agent.py`）

- **Agent.as_tool()**: Simple agent-to-tool conversion
- **Agent.as_tool()**：将一个 Agent 简单转换为工具
- **Translation Orchestration**: Multiple language agents coordinated
- **翻译编排**：协调多个语言 Agent 完成翻译任务
- **Tool Naming**: Custom tool names and descriptions
- **工具命名**：自定义工具名称和描述

### Advanced Agent Tools (`advanced_agent.py`)
### 高级 Agent 工具（`advanced_agent.py`）

- **@function_tool with Runner.run()**: Custom agent tool implementations
- **@function_tool 与 Runner.run()**：实现自定义 Agent 工具
- **Custom Configuration**: Per-run settings (max_turns, temperature)
- **自定义配置**：为每次运行设置 `max_turns`、`temperature` 等参数
- **Research-Writing Pipeline**: Complex multi-stage workflows
- **研究与写作流水线**：实现复杂的多阶段工作流

## Available Patterns
## 可用模式

### Basic Orchestration
### 基础编排

- Spanish translation agent
- 西班牙语翻译 Agent
- French translation agent
- 法语翻译 Agent
- Orchestrator coordinates language tasks
- 编排 Agent 协调不同语言任务

### Advanced Orchestration
### 高级编排

- Research agent for information gathering
- 用于收集信息的研究 Agent
- Writing agent for content creation
- 用于生成内容的写作 Agent
- Custom tool functions with Runner configuration
- 结合 Runner 配置使用自定义工具函数

## Next Steps
## 下一步

- [Function Tools / 函数工具](../3_1_function_tools/README.md) - Custom function tools / 自定义函数工具
- [Built-in Tools / 内置工具](../3_2_builtin_tools/README.md) - SDK-provided tools / SDK 提供的工具
- [Tutorial 4: Running Agents / 教程 4：运行 Agent](../../4_running_agents/README.md) - Advanced execution patterns / 高级执行模式
