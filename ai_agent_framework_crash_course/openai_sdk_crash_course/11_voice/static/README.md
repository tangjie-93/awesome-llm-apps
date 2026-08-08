# 🎙️ Static Voice Agent
# 🎙️ 静态语音 Agent

A turn-based voice agent that records an audio clip, transcribes it, runs an agent, and synthesizes the reply as audio.<br>
这是一个轮次式语音 Agent：录制一段音频，转写为文本，运行 Agent，再将回答合成为音频。

## 🎯 What This Demonstrates
## 🎯 本示例演示的内容

- Static voice pipeline: audio input, transcription, Agent reasoning, and speech output.<br>
  静态语音流水线：音频输入、语音转写、Agent 推理和语音输出。
- Multi-language responses, function tools, handoffs, and audio utility functions.<br>
  多语言响应、函数工具、Agent 交接和音频工具函数。
- Workflow callbacks for observing each processing stage.<br>
  用于观察各处理阶段的工作流回调。

## 🧠 Core Concept: Static Voice Pipeline
## 🧠 核心概念：静态语音流水线

The pipeline completes one request at a time: record audio, convert speech to text, generate a response, then convert the response to speech.<br>
该流水线一次完成一个请求：录制音频、将语音转换为文本、生成回答，再将回答转换为语音。

This approach is simple and reliable, but the user waits for the full processing cycle before hearing the response.<br>
这种方式简单可靠，但用户需要等待整个处理周期完成后才能听到回答。

## 🚀 Quick Start
## 🚀 快速开始

1. Install dependencies.<br>
   安装依赖。

   ```bash
   pip install -r requirements.txt
   ```

2. Copy `env.example` to `.env` and configure `OPENAI_API_KEY`.<br>
   将 `env.example` 复制为 `.env`，并配置 `OPENAI_API_KEY`。

3. Run the example.<br>
   运行示例。

   ```bash
   python agent.py
   ```

## 🎯 Example Interactions
## 🎯 交互示例

- “What is the weather in Paris?” / “巴黎天气怎么样？”
- “Translate this to Spanish.” / “把这句话翻译成西班牙语。”
- “Help me schedule an appointment tomorrow.” / “帮我预约明天的时间。”

## 🔧 Key Implementation Patterns
## 🔧 关键实现模式

- Use an audio input component to capture a complete utterance.<br>
  使用音频输入组件捕获一段完整话语。
- Send the recording to speech-to-text before calling `Runner`.<br>
  调用 `Runner` 前，先将录音发送至语音转文字服务。
- Convert `result.final_output` to speech and play or save the generated audio.<br>
  将 `result.final_output` 转换为语音，并播放或保存生成的音频。
- Delegate language-specific tasks to specialized agents when needed.<br>
  需要时将特定语言任务委派给专用 Agent。

## 📊 When to Use It
## 📊 适用场景

Use static voice processing for voice forms, short commands, accessibility controls, and simple assistant interactions.<br>
静态语音处理适用于语音表单、短指令、无障碍控制和简单助手交互。

## 🚨 Requirements
## 🚨 运行要求

- Python 3.9+ and the dependencies listed in `requirements.txt`.<br>
  Python 3.9+，以及 `requirements.txt` 中列出的依赖。
- A working microphone and audio output device.<br>
  可用的麦克风和音频输出设备。
- An OpenAI API key with access to the required voice models.<br>
  有权访问所需语音模型的 OpenAI API Key。

## 🔗 Related Examples
## 🔗 相关示例

- [Streaming Voice Agent](../streamed/README.md) / [流式语音 Agent](../streamed/README.md)
- [Realtime Voice Agent](../realtime/README.md) / [实时语音 Agent](../realtime/README.md)
