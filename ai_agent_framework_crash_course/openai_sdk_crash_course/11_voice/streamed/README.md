# 🌊 Streaming Voice Agent
# 🌊 流式语音 Agent

A streaming voice agent that continuously processes audio and returns partial output as the conversation progresses.<br>
这是一个流式语音 Agent，可持续处理音频，并在对话进行过程中返回部分输出。

## 🎯 What This Demonstrates
## 🎯 本示例演示的内容

- Continuous audio input and incremental speech processing.<br>
  连续音频输入和增量语音处理。
- Streaming Agent output, tool execution, language switching, and session management.<br>
  流式 Agent 输出、工具执行、语言切换和会话管理。
- Lifecycle events and monitoring for a long-running voice interaction.<br>
  用于长时间语音交互的生命周期事件和监控。

## 🧠 Core Concept: Streaming Voice Pipeline
## 🧠 核心概念：流式语音流水线

Audio is processed in chunks instead of waiting for one complete request, allowing the application to surface results earlier.<br>
音频按片段处理，而不是等待单个完整请求完成，因此应用可以更早显示结果。

Streaming improves responsiveness and supports natural interruptions, but requires careful session and event management.<br>
流式处理能提升响应速度并支持自然打断，但需要谨慎管理会话和事件。

## 🚀 Quick Start
## 🚀 快速开始

1. Install dependencies.<br>
   安装依赖。

   ```bash
   pip install -r requirements.txt
   ```

2. Copy `env.example` to `.env` and configure `OPENAI_API_KEY`.<br>
   将 `env.example` 复制为 `.env`，并配置 `OPENAI_API_KEY`。

3. Run the streaming demo.<br>
   运行流式示例。

   ```bash
   python agent.py
   ```

## 🎯 Example Interactions
## 🎯 交互示例

- Ask follow-up questions without restarting the whole session.<br>
  无需重新启动整个会话即可继续追问。
- Interrupt the response and change the task or language.<br>
  打断当前回答，并切换任务或语言。
- Request live calculations or tool-assisted information.<br>
  请求实时计算或借助工具获取信息。

## 🔧 Key Implementation Patterns
## 🔧 关键实现模式

- Stream microphone data into the input pipeline and consume output events as they arrive.<br>
  将麦克风数据流式输入处理流水线，并在输出事件到达时立即消费。
- Keep a session alive so conversation context persists across turns.<br>
  保持会话存活，让对话上下文跨轮次保留。
- Handle interruption, completion, error, and tool events explicitly.<br>
  显式处理打断、完成、错误和工具事件。
- Apply activity detection to identify when the user starts and stops speaking.<br>
  使用活动检测识别用户何时开始和停止说话。

## 📊 When to Use It
## 📊 适用场景

Use streaming voice for voice chat, live assistants, coaching, and scenarios where perceived latency matters.<br>
流式语音适用于语音聊天、实时助手、辅导，以及重视感知延迟的场景。

## 🚨 Requirements and Considerations
## 🚨 运行要求与注意事项

- Python 3.9+, microphone access, audio output, and the dependencies in `requirements.txt`.<br>
  Python 3.9+、麦克风权限、音频输出，以及 `requirements.txt` 中的依赖。
- Manage network failures and reconnect sessions when a long-lived stream is interrupted.<br>
  长时间流连接中断时，需要处理网络失败并重连会话。
- Avoid blocking event handlers; slow handlers increase response latency.<br>
  避免阻塞事件处理器，缓慢的处理器会增加响应延迟。

## 🔗 Related Examples
## 🔗 相关示例

- [Static Voice Agent](../static/README.md) / [静态语音 Agent](../static/README.md)
- [Realtime Voice Agent](../realtime/README.md) / [实时语音 Agent](../realtime/README.md)
