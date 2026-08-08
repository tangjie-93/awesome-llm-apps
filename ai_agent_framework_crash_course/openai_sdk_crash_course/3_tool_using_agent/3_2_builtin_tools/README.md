# Built-in Tools Agent
# 内置工具 Agent

Demonstrates using OpenAI Agents SDK built-in tools like WebSearchTool and CodeInterpreterTool.

演示如何使用 OpenAI Agents SDK 提供的内置工具，例如 WebSearchTool 和 CodeInterpreterTool。

## What This Demonstrates
## 本示例演示的内容

- **WebSearchTool**: Real-time web search capabilities
- **WebSearchTool**：实时网页搜索能力
- **CodeInterpreterTool**: Code execution and mathematical computation
- **CodeInterpreterTool**：代码执行和数学计算能力
- **Built-in Tool Integration**: Using pre-configured SDK tools
- **内置工具集成**：使用 SDK 中预配置的工具
- **Tool Combination**: Leveraging multiple tools in one agent
- **工具组合**：在一个 Agent 中组合使用多个工具

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

   result = Runner.run_sync(root_agent, "What's the latest news about AI and calculate 15% of 200?")
   print(result.final_output)
   ```

4. **Run the complete demo / 运行完整 demo**

   ```bash
   python agent.py
   ```

## Key Concepts
## 核心概念

- **WebSearchTool()**: Search the web for current information / 搜索互联网中的最新信息
- **CodeInterpreterTool()**: Execute Python code and calculations / 执行 Python 代码和计算任务
- **Tool Instantiation**: Creating tool instances with default configurations / 使用默认配置创建工具实例
- **Multi-tool Agents**: Combining different tool types / 组合使用不同类型的工具

## Available Tools
## 可用工具

### WebSearchTool

- Search for current information on the internet.
- 在互联网上搜索最新信息。
- Useful for factual questions requiring recent data.
- 适用于需要近期数据的事实类问题。
- Automatically formats search results for agent use.
- 自动整理搜索结果，供 Agent 使用。

### CodeInterpreterTool

- Execute Python code in a secure environment.
- 在安全环境中执行 Python 代码。
- Perfect for mathematical calculations.
- 适合执行数学计算。
- Can handle data analysis and complex computations.
- 可以处理数据分析和复杂计算。

## Next Steps
## 下一步

- [Function Tools / 函数工具](../3_1_function_tools/README.md) - Custom function tools / 自定义函数工具
- [Agents as Tools / Agent 作为工具](../3_3_agents_as_tools/README.md) - Advanced orchestration patterns / 高级编排模式
