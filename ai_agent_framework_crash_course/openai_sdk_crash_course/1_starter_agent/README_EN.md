# 🎯 Tutorial 1: Your First OpenAI Agent

# 🎯 教程 1：你的第一个 OpenAI Agent

Welcome to your first step in the OpenAI Agents SDK journey! This tutorial introduces you to the fundamental concept of creating a simple AI agent using OpenAI's Agents SDK.

欢迎来到 OpenAI Agents SDK 学习之旅的第一步！本教程将介绍如何使用 OpenAI Agents SDK 创建一个简单 AI Agent 的基础概念。

## 🎯 What You'll Learn

## 🎯 你将学到什么

- **Basic Agent Creation**: How to create your first OpenAI agent

  **基础 Agent 创建**：如何创建你的第一个 OpenAI Agent

- **OpenAI SDK Workflow**: Understanding the agent lifecycle

  **OpenAI SDK 工作流**：理解 Agent 的生命周期

- **Simple Text Processing**: Basic input/output handling

  **简单文本处理**：基础输入与输出处理

- **Agent Configuration**: Essential parameters and settings

  **Agent 配置**：核心参数与设置

## 🧠 Core Concept: What is an OpenAI Agent?

## 🧠 核心概念：什么是 OpenAI Agent？

An OpenAI agent is a **programmable AI assistant** that can:

OpenAI Agent 是一个**可编程的 AI 助手**，它可以：

- Process user inputs (text, voice, etc.)

  处理用户输入（文本、语音等）

- Use AI models (like GPT-4o) to understand and respond

  使用 AI 模型（如 GPT-4o）理解并回复

- Perform specific tasks based on your instructions

  根据你的指令执行特定任务

- Return structured or unstructured responses

  返回结构化或非结构化响应

Think of it as creating a **smart function** that uses AI to handle complex tasks.

你可以把它理解为创建了一个使用 AI 处理复杂任务的**智能函数**。

## 🔧 Key Components

## 🔧 关键组件

### 1. **Agent Class**

### 1. **Agent 类**

The main building block for creating AI agents in OpenAI SDK:

这是在 OpenAI SDK 中创建 AI Agent 的主要构建块：

```python
from agents import Agent
```

### 2. **Essential Parameters**

### 2. **核心参数**

- `name`: Unique identifier for your agent

  `name`：Agent 的唯一标识

- `instructions`: How your agent should behave

  `instructions`：定义 Agent 应该如何行动

- `model`: The AI model to use (defaults to "gpt-4o")

  `model`：要使用的 AI 模型（默认是 "gpt-4o"）

### 3. **Basic Workflow**

### 3. **基础工作流**

1. **Input**: User sends a message

   **输入**：用户发送消息

2. **Processing**: Agent uses AI model to understand and respond

   **处理**：Agent 使用 AI 模型理解并生成回复

3. **Output**: Agent returns a response

   **输出**：Agent 返回响应

## 🚀 Tutorial Overview

## 🚀 教程概览

This tutorial includes **two focused agent examples**:

本教程包含**两个聚焦的 Agent 示例**：

### **1. Personal Assistant Agent** (`personal_assistant_agent/`)

### **1. 个人助理 Agent**（`personal_assistant_agent/`）

- Basic agent creation and configuration

  基础 Agent 创建与配置

- Simple instructions and role definition

  简单指令与角色定义

- Core Agent class usage

  Agent 核心类的使用方式

### **2. Execution Demo Agent** (`execution_demo_agent/`)

### **2. 执行方式演示 Agent**（`execution_demo_agent/`）

- Demonstrates different execution methods

  演示不同的执行方式

- Sync, async, and streaming patterns

  同步、异步和流式响应模式

- Runner class usage examples

  Runner 类的使用示例

## 📁 Project Structure

## 📁 项目结构

```text
1_starter_agent/
├── README.md                    # This file - concept explanation
├── requirements.txt             # Dependencies
├── personal_assistant_agent/    # Basic agent creation
│   ├── __init__.py
│   └── agent.py                # Simple agent definition (20 lines)
├── execution_demo_agent/        # Execution methods demonstration
│   ├── __init__.py
│   └── agent.py                # Sync, async, streaming examples
├── app.py                      # Streamlit web interface (optional)
└── env.example                 # Environment variables template
```

```text
1_starter_agent/
├── README.md                    # 当前文件 - 概念说明
├── requirements.txt             # 依赖项
├── personal_assistant_agent/    # 基础 Agent 创建
│   ├── __init__.py
│   └── agent.py                # 简单 Agent 定义（20 行）
├── execution_demo_agent/        # 执行方式演示
│   ├── __init__.py
│   └── agent.py                # 同步、异步、流式响应示例
├── app.py                      # Streamlit Web 界面（可选）
└── env.example                 # 环境变量模板
```

## 🎯 Learning Objectives

## 🎯 学习目标

By the end of this tutorial, you'll understand:

完成本教程后，你将理解：

- ✅ How to create a basic OpenAI agent

  ✅ 如何创建一个基础 OpenAI Agent

- ✅ Essential agent parameters and their purpose

  ✅ Agent 核心参数及其用途

- ✅ How to run agents synchronously and asynchronously

  ✅ 如何以同步和异步方式运行 Agent

- ✅ Basic OpenAI SDK workflow and lifecycle

  ✅ OpenAI SDK 的基础工作流和生命周期

- ✅ How to use streaming responses

  ✅ 如何使用流式响应

## 🚀 Getting Started

## 🚀 开始使用

1. **Set up your environment**:

   **设置你的环境**：

   ```bash
   # Make sure you have your OpenAI API key
   # 确保你已经拥有 OpenAI API Key
   # Get your API key from: https://platform.openai.com/api-keys
   # 你可以从这里获取 API Key：https://platform.openai.com/api-keys
   ```

2. **Install OpenAI Agents SDK**:

   **安装 OpenAI Agents SDK**：

   ```bash
   pip install openai-agents
   ```

3. **Install dependencies**:

   **安装依赖**：

   ```bash
   # Install required packages
   # 安装所需包
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   **设置环境变量**：

   ```bash
   # Copy the example environment file
   # 复制环境变量示例文件
   cp env.example .env

   # Edit .env and add your OpenAI API key
   # 编辑 .env 并添加你的 OpenAI API Key
   # OPENAI_API_KEY=sk-your_openai_key_here
   ```

5. **Test the agent**:

   **测试 Agent**：

   ```bash
   # Run the agent directly
   # 直接运行 Agent
   python agent.py

   # Or run the Streamlit web interface
   # 或运行 Streamlit Web 界面
   streamlit run app.py
   ```

6. **Try different execution methods**:

   **尝试不同的执行方式**：

   - Test synchronous execution: "What's the weather like today?"

     测试同步执行："What's the weather like today?"

   - Test asynchronous execution: "Tell me a story about AI"

     测试异步执行："Tell me a story about AI"

   - Test streaming responses: "Explain machine learning in detail"

     测试流式响应："Explain machine learning in detail"

## 🧪 Sample Prompts to Try

## 🧪 可尝试的示例提示词

- **General Questions**: "What's the capital of France?"

  **通用问题**："What's the capital of France?"

- **Creative Tasks**: "Write a short poem about technology"

  **创意任务**："Write a short poem about technology"

- **Problem Solving**: "How can I improve my productivity?"

  **问题解决**："How can I improve my productivity?"

- **Explanations**: "Explain quantum computing in simple terms"

  **解释说明**："Explain quantum computing in simple terms"

## 🔗 Next Steps

## 🔗 下一步

After completing this tutorial, you'll be ready for:

完成本教程后，你可以继续学习：

- **[Tutorial 2: Structured Output Agent](../2_structured_output_agent/README.md)** - Learn to create type-safe, structured responses

  **[教程 2：结构化输出 Agent](../2_structured_output_agent/README.md)** - 学习创建类型安全的结构化响应

- **[Tutorial 3: Tool Using Agent](../3_tool_using_agent/README.md)** - Add custom tools and functions to your agent

  **[教程 3：工具调用 Agent](../3_tool_using_agent/README.md)** - 为 Agent 添加自定义工具和函数

- **[Tutorial 4: Runner Execution Methods](../4_running_agents/README.md)** - Master different execution patterns

  **[教程 4：Runner 执行方式](../4_running_agents/README.md)** - 掌握不同的执行模式

## 💡 Pro Tips

## 💡 实用建议

- **Start Simple**: Begin with basic functionality and add complexity gradually

  **从简单开始**：先实现基础功能，再逐步增加复杂度

- **Test Often**: Try different prompts to understand agent behavior

  **经常测试**：尝试不同提示词，理解 Agent 的行为

- **Read Instructions**: Clear instructions lead to better agent behavior

  **重视指令**：清晰的指令会带来更好的 Agent 行为

- **Experiment**: Try different execution methods to see the differences

  **动手实验**：尝试不同执行方式，观察它们的差异

## 🚨 Troubleshooting

## 🚨 常见问题

- **API Key Issues**: Make sure your `.env` file contains a valid `OPENAI_API_KEY`

  **API Key 问题**：确保 `.env` 文件包含有效的 `OPENAI_API_KEY`

- **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`

  **导入错误**：确保已通过 `pip install -r requirements.txt` 安装所有依赖

- **Rate Limits**: If you hit rate limits, wait a moment before trying again

  **限流问题**：如果触发限流，请等待一会儿再重试
