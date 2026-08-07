# Personal Assistant Agent

# 个人助理 Agent

This example shows how to create a basic personal assistant with the OpenAI Agents SDK. It focuses on the smallest useful agent setup: name, instructions, and simple execution with `Runner`.

本示例演示如何使用 OpenAI Agents SDK 创建一个基础个人助理。它聚焦于最小可用的 Agent 配置：名称、指令，以及通过 `Runner` 进行简单执行。

## What You'll Learn

## 你将学到什么

- **Basic Agent Definition**: Create an agent with `Agent()`

  **基础 Agent 定义**：使用 `Agent()` 创建一个 Agent

- **Instruction Design**: Guide the assistant's role and behavior with natural language

  **指令设计**：用自然语言约束助理的角色和行为

- **Runner Usage**: Execute the agent and read the final output

  **Runner 使用方式**：运行 Agent 并读取最终输出

- **Starter Workflow**: Set up the API key, import the agent, and test a prompt

  **入门工作流**：配置 API Key、导入 Agent，并测试提示词

## Core Concept: A Minimal Personal Assistant

## 核心概念：最小个人助理

The personal assistant agent is a simple conversational helper. Its instructions tell it to answer clearly, provide practical advice, stay professional, and keep responses concise.

个人助理 Agent 是一个简单的对话助手。它的指令要求它清晰回答问题、提供实用建议、保持专业，并让回复简洁但有信息量。

```python
from agents import Agent

root_agent = Agent(
    name="Personal Assistant Agent",
    instructions="You are a helpful personal assistant."
)
```

## Key Components

## 关键组件

### 1. Agent Definition

### 1. Agent 定义

`root_agent` is the reusable agent object imported by other examples or scripts.

`root_agent` 是可复用的 Agent 对象，可被其他示例或脚本导入使用。

### 2. Instructions

### 2. 指令

The instruction block defines what the assistant should do:

指令块定义了助理应该做什么：

- Answer questions clearly and concisely

  清晰、简洁地回答问题

- Provide helpful information and advice

  提供有帮助的信息和建议

- Explain complex topics in simple terms

  用简单语言解释复杂主题

- Offer follow-up suggestions when appropriate

  在合适时给出后续建议

### 3. Runner Execution

### 3. Runner 执行

Use `Runner.run_sync()` for a simple blocking call:

使用 `Runner.run_sync()` 进行简单的同步调用：

```python
from agents import Runner
from agent import root_agent

result = Runner.run_sync(root_agent, "Hello, introduce yourself!")
print(result.final_output)
```

## Project Structure

## 项目结构

```text
1_personal_assistant_agent/
├── README.md       # This file - personal assistant guide
├── agent.py        # Personal assistant agent definition
├── env.example     # Environment variable template
└── __init__.py     # Package marker
```

```text
1_personal_assistant_agent/
├── README.md       # 当前文件 - 个人助理说明
├── agent.py        # 个人助理 Agent 定义
├── env.example     # 环境变量模板
└── __init__.py     # Python 包标记
```

## Quick Start

## 快速开始

1. **Install OpenAI Agents SDK**:

   **安装 OpenAI Agents SDK**：

   ```bash
   pip install openai-agents
   ```

2. **Set up environment variables**:

   **设置环境变量**：

   ```bash
   cp env.example .env
   # Edit .env and add your OpenAI API key
   # 编辑 .env 并添加你的 OpenAI API Key
   # OPENAI_API_KEY=sk-your_openai_key_here
   ```

3. **Run a quick test**:

   **运行快速测试**：

   ```python
   from agents import Runner
   from agent import root_agent

   result = Runner.run_sync(root_agent, "How can I plan my day more effectively?")
   print(result.final_output)
   ```

## Example Prompts

## 示例提示词

- **Daily Planning**: "Help me plan a focused workday."

  **日程规划**："Help me plan a focused workday."

- **Explanations**: "Explain APIs in simple terms."

  **解释说明**："Explain APIs in simple terms."

- **Advice**: "How can I improve my productivity?"

  **建议咨询**："How can I improve my productivity?"

- **Writing Help**: "Draft a polite follow-up email."

  **写作辅助**："Draft a polite follow-up email."

## Learning Objectives

## 学习目标

After completing this example, you'll understand:

完成本示例后，你将理解：

- How to define a simple OpenAI Agent

  如何定义一个简单的 OpenAI Agent

- How instructions shape agent behavior

  指令如何影响 Agent 行为

- How to execute an agent with `Runner.run_sync()`

  如何使用 `Runner.run_sync()` 执行 Agent

- How to reuse `root_agent` in other scripts

  如何在其他脚本中复用 `root_agent`

## Next Steps

## 下一步

- **[Tutorial 1 Overview](../README.md)** - Learn the starter agent concepts and execution patterns

  **[教程 1 总览](../README.md)** - 学习 Starter Agent 的概念和执行模式

- **[Tutorial 2: Structured Output Agent](../../2_structured_output_agent/README.md)** - Create type-safe structured responses

  **[教程 2：结构化输出 Agent](../../2_structured_output_agent/README.md)** - 创建类型安全的结构化响应

- **[Tutorial 3: Tool Using Agent](../../3_tool_using_agent/README.md)** - Add custom tools and functions to agents

  **[教程 3：工具调用 Agent](../../3_tool_using_agent/README.md)** - 为 Agent 添加自定义工具和函数

## Troubleshooting

## 常见问题

- **API Key Issues**: Make sure `.env` contains a valid `OPENAI_API_KEY`

  **API Key 问题**：确保 `.env` 包含有效的 `OPENAI_API_KEY`

- **Import Errors**: Run the script from this directory or ensure the module path includes this folder

  **导入错误**：请从当前目录运行脚本，或确保模块路径包含当前文件夹

- **Dependency Issues**: Install the SDK with `pip install openai-agents`

  **依赖问题**：使用 `pip install openai-agents` 安装 SDK
