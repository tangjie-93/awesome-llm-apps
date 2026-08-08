# Execution Methods / 执行方式

Demonstrates the three execution methods available in the OpenAI Agents SDK: sync, async, and streaming.
演示 OpenAI Agents SDK 提供的三种执行方式：同步、异步和流式执行。

## 🎯 What This Demonstrates / 本示例演示

- **Runner.run()**: Asynchronous execution for non-blocking operations
  **Runner.run()**：用于非阻塞操作的异步执行
- **Runner.run_sync()**: Synchronous execution for simple blocking calls
  **Runner.run_sync()**：用于简单阻塞调用的同步执行
- **Runner.run_streamed()**: Streaming execution for real-time responses
  **Runner.run_streamed()**：用于实时响应的流式执行
- **Performance Comparison**: When to use each method
  **性能对比**：了解不同场景下应选择哪种执行方式

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
   from agents import Runner
   from agent import root_agent
   
   # Test sync execution
   result = root_agent.sync_execution_example()
   print(result)
   ```

## 💡 Key Concepts / 核心概念

- **Sync Execution**: Blocks until completion, simple to use
  **同步执行**：阻塞等待任务完成，使用简单
- **Async Execution**: Non-blocking, enables concurrency
  **异步执行**：不会阻塞当前流程，可支持并发
- **Streaming Execution**: Real-time response processing
  **流式执行**：实时处理模型返回的响应
- **Use Case Selection**: Choose based on application needs
  **场景选择**：根据应用需求选择合适的执行方式

## 🔗 Next Steps / 后续步骤

- [Conversation Management](../4_2_conversation_management/README.md) - Threading and sessions
  [对话管理](../4_2_conversation_management/README.md)：对话线程与会话管理
- [Run Configuration](../4_3_run_configuration/) - Advanced settings
  [运行配置](../4_3_run_configuration/)：高级配置
