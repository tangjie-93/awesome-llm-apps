# Basic Sessions
# 基础会话

Demonstrates fundamental session memory management with `SQLiteSession` for automatic conversation history.

演示如何使用 `SQLiteSession` 管理基础会话记忆，并自动保存对话历史。

## What This Demonstrates
## 本示例演示的内容

- **In-Memory Sessions**: Temporary session storage for development
- **内存会话**：用于开发阶段的临时会话存储
- **Persistent Sessions**: File-based session storage for production
- **持久化会话**：用于生产环境的文件型会话存储
- **Multi-Turn Conversations**: Automatic context preservation
- **多轮对话**：自动保留上下文
- **Session Memory**: Eliminating manual `.to_input_list()` handling
- **会话记忆**：不再需要手动处理 `.to_input_list()`

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
   import asyncio
   from agent import in_memory_session_example, persistent_session_example

   # Test in-memory sessions
   # 测试内存会话
   asyncio.run(in_memory_session_example())

   # Test persistent sessions
   # 测试持久化会话
   asyncio.run(persistent_session_example())
   ```

## Key Concepts
## 核心概念

- **SQLiteSession / SQLiteSession 会话**: Automatic conversation memory management / 自动管理对话记忆
- **In-Memory vs Persistent / 内存会话与持久化会话**: Choose storage based on use case / 根据使用场景选择存储方式
- **Session IDs / 会话 ID**: Organizing conversations by unique identifiers / 使用唯一标识组织对话
- **Automatic Context / 自动上下文**: No manual conversation threading required / 不需要手动串联对话历史

## Available Examples
## 可用示例

### In-Memory Sessions
### 内存会话

- Temporary conversation storage
- 临时保存对话内容
- Lost when process ends
- 进程结束后数据会丢失
- Perfect for development and testing
- 适合开发和测试场景

### Persistent Sessions
### 持久化会话

- File-based conversation storage
- 基于文件保存对话内容
- Survives application restarts
- 应用重启后仍可保留数据
- Essential for production applications
- 适合生产应用

### Multi-Turn Conversations
### 多轮对话

- Extended conversation flows
- 支持连续的对话流程
- Automatic context preservation
- 自动保留上下文
- Natural conversation progression
- 让对话可以自然延续

### Session Comparison
### 会话对比

- Shows the difference between using sessions and not using sessions
- 展示使用会话与不使用会话的区别
- Highlights how `SQLiteSession` removes manual history handling
- 强调 `SQLiteSession` 如何省去手动维护历史记录的步骤

## Next Steps
## 下一步

- [Memory Operations / 记忆操作](../7_2_memory_operations/README.md) - Advanced memory manipulation / 高级记忆管理
- [Multi Sessions / 多会话](../7_3_multi_sessions/README.md) - Managing multiple conversations / 管理多个对话
