# Function Tools Agent
# 函数工具 Agent

Demonstrates custom function tools creation using the `@function_tool` decorator.

演示如何使用 `@function_tool` 装饰器创建自定义函数工具。

## What This Demonstrates
## 本示例演示的内容

- **Custom Function Tools**: Creating tools with `@function_tool` decorator
- **自定义函数工具**：使用 `@function_tool` 装饰器创建工具
- **Tool Descriptions**: Providing clear docstrings for LLM understanding
- **工具描述**：提供清晰的 docstring，帮助 LLM 理解工具用途
- **Parameter Handling**: Type hints and default parameters
- **参数处理**：使用类型提示和默认参数
- **Error Handling**: Graceful tool failure management
- **错误处理**：优雅地处理工具执行失败的情况

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

3. **Run the agent / 运行 Agent**

   ```python
   from agents import Runner
   from agent import root_agent

   result = Runner.run_sync(root_agent, "What time is it in New York?")
   print(result.final_output)
   ```

4. **Run the complete demo / 运行完整 demo**

   ```bash
   python agent.py
   ```

## Key Concepts
## 核心概念

- **@function_tool Decorator / @function_tool 装饰器**: Converting Python functions to agent tools / 将 Python 函数转换为 Agent 工具
- **Tool Docstrings / 工具 docstring**: Helping the LLM decide when to use tools / 帮助 LLM 判断何时使用工具
- **Type Hints / 类型提示**: Parameter validation and documentation / 用于参数校验和文档说明
- **Tool Registration / 工具注册**: Adding tools to agent configuration / 将工具添加到 Agent 配置中

## Available Tools
## 可用工具

### `get_current_time(timezone: str = "UTC")`

- Returns the current time in the specified timezone.
- 返回指定时区的当前时间。
- Handles timezone validation and error cases.
- 处理时区校验和错误情况。

### `greet_user(name: str)`

- Simple greeting tool demonstrating basic tool usage.
- 用于演示基础工具调用方式的简单问候工具。
- Shows parameter passing from the LLM to the tool.
- 展示如何将参数从 LLM 传递给工具。

## Next Steps
## 下一步

- [Built-in Tools / 内置工具](../3_2_builtin_tools/README.md) - Using WebSearch and CodeInterpreter / 使用 WebSearch 和 CodeInterpreter
- [Agents as Tools / Agent 作为工具](../3_3_agents_as_tools/README.md) - Advanced agent orchestration / 高级 Agent 编排
