# ⚡ Realtime Voice Agent
# ⚡ 实时语音 Agent

A low-latency voice agent built with OpenAI's Realtime API for natural, persistent audio conversations.<br>
这是一个基于 OpenAI Realtime API 构建的低延迟语音 Agent，用于自然且持续的音频对话。

## 🎯 What This Demonstrates
## 🎯 本示例演示的内容

- `RealtimeAgent`, `RealtimeRunner`, and `RealtimeSession` for live conversations.<br>
  使用 `RealtimeAgent`、`RealtimeRunner` 和 `RealtimeSession` 构建实时对话。
- Realtime tool calls, specialized-agent handoffs, and event handling.<br>
  实时工具调用、专用 Agent 交接和事件处理。
- Voice activity detection, audio configuration, guardrails, and production concerns.<br>
  语音活动检测、音频配置、护栏和生产环境注意事项。

## 🧠 Core Concept: Realtime Voice Processing
## 🧠 核心概念：实时语音处理

Realtime agents maintain a persistent connection so audio can be processed and answered with minimal delay.<br>
实时 Agent 会保持持久连接，以便快速处理音频并给出回答。

Unlike a static pipeline, the user can interrupt the Agent naturally while it is speaking.<br>
与静态流水线不同，用户可以在 Agent 讲话时自然地打断它。

## 🚀 Quick Start
## 🚀 快速开始

1. Install dependencies.<br>
   安装依赖。

   ```bash
   pip install -r requirements.txt
   ```

2. Copy `env.example` to `.env` and configure an API key with Realtime API access.<br>
   将 `env.example` 复制为 `.env`，并配置具有 Realtime API 访问权限的 API Key。

3. Run the realtime Agent.<br>
   运行实时 Agent。

   ```bash
   python agent.py
   ```

## 🎯 Example Voice Interactions
## 🎯 语音交互示例

- “What's the weather in Paris?” / “巴黎天气怎么样？”
- “Translate this into French.” / “把这句话翻译成法语。”
- “Stop, I want to ask something else.” / “停一下，我想问别的问题。”

## 🔧 Key Implementation Patterns
## 🔧 关键实现模式

- Create a `RealtimeAgent` with concise instructions and the required tools.<br>
  使用简洁指令和所需工具创建 `RealtimeAgent`。
- Start a `RealtimeRunner` session, then forward microphone input and play audio output events.<br>
  启动 `RealtimeRunner` 会话，然后转发麦克风输入并播放音频输出事件。
- Configure turn detection to control when the Agent treats speech as a completed turn.<br>
  配置轮次检测，控制 Agent 在何时将语音视为一个完成的轮次。
- Observe session events for transcription, audio deltas, tool calls, errors, and interruptions.<br>
  监听转写、音频增量、工具调用、错误和打断等会话事件。

## 📊 Realtime vs Traditional Voice
## 📊 实时语音与传统语音的对比

Realtime voice provides the most natural interaction and lowest perceived latency, while static and streamed pipelines are simpler to operate.<br>
实时语音能提供最自然的交互和最低的感知延迟；静态和流式流水线则更易于运行和维护。

Choose realtime voice for conversational assistants, live support, language practice, and hands-free interfaces.<br>
实时语音适用于对话助手、实时支持、语言练习和免手持交互界面。

## 🚨 Requirements and Production Considerations
## 🚨 运行要求与生产环境注意事项

- Python 3.9+, microphone and speaker access, and a Realtime API-enabled model.<br>
  Python 3.9+、麦克风和扬声器权限，以及支持 Realtime API 的模型。
- Use reconnection, timeout, and error-handling strategies for persistent sessions.<br>
  为持久会话提供重连、超时和错误处理策略。
- Monitor latency, interruption rate, tool failures, and audio quality in production.<br>
  在生产环境中监控延迟、打断率、工具失败和音频质量。
- Keep safety instructions and guardrails close to the Agent configuration.<br>
  将安全指令和护栏配置靠近 Agent 配置定义。

## 🔗 Related Examples
## 🔗 相关示例

- [Static Voice Agent](../static/README.md) / [静态语音 Agent](../static/README.md)
- [Streaming Voice Agent](../streamed/README.md) / [流式语音 Agent](../streamed/README.md)
