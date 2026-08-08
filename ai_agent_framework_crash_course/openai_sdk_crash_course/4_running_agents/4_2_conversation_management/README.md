# Conversation Management / 对话管理

Demonstrates manual conversation threading with `to_input_list()` and automatic management with Sessions.
演示如何使用 `to_input_list()` 手动维护对话线程，以及如何使用 Session 自动管理对话。

## 🎯 What This Demonstrates / 本示例演示

- **Manual Threading**: Using `result.to_input_list()` for conversation history
  **手动维护对话线程**：使用 `result.to_input_list()` 管理对话历史
- **Automatic Sessions**: Using `SQLiteSession` for memory management
  **自动会话管理**：使用 `SQLiteSession` 管理会话记忆
- **Conversation Context**: Maintaining state across multiple turns
  **对话上下文**：在多轮交互中保持状态
- **Thread Management**: Different approaches to conversation flow
  **线程管理**：了解不同的对话流程管理方式

## 🚀 Quick Start / 快速开始

1. **Install OpenAI Agents SDK / 安装 OpenAI Agents SDK**:
   ```bash
   pip install openai-agents
   ```

2. **Set up environment / 配置环境**:
   ```bash
   cp ../env.example .env
   # Edit .env and add your OpenAI API key
   ```

3. **Run the agent / 运行 Agent**:
   ```python
   import asyncio
   from agent import manual_conversation_example, session_conversation_example
   
   # Test manual conversation management
   asyncio.run(manual_conversation_example())
   ```

## 💡 Key Concepts / 核心概念

- **to_input_list()**: Manual conversation history management
  **to_input_list()**：手动管理对话历史
- **SQLiteSession**: Automatic conversation persistence
  **SQLiteSession**：自动持久化对话内容
- **Context Preservation**: Maintaining conversation state
  **上下文保持**：在多轮对话中保留状态
- **Session Storage**: In-memory vs persistent storage
  **会话存储**：内存存储与持久化存储的区别

## 🔗 Next Steps / 后续步骤

- [Execution Methods](../4_1_execution_methods/README.md) - Basic execution patterns
  [执行方式](../4_1_execution_methods/README.md)：基础执行模式
- [Streaming Events](../4_4_streaming_events/) - Real-time processing
  [流式事件](../4_4_streaming_events/)：实时处理
