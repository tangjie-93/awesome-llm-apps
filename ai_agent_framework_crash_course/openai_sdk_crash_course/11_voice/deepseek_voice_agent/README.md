# DeepSeek Local Voice Agent / DeepSeek 本地语音 Agent

这个示例将本地语音识别、DeepSeek 文本 Agent 和本地语音合成组合为多轮语音对话。

This example combines local speech recognition, a DeepSeek text agent, and local text-to-speech into a multi-turn voice conversation.

## Architecture / 架构

`Microphone -> faster-whisper (STT) -> DeepSeek Chat Completions + tools -> pyttsx3 (TTS) -> Speaker`

`麦克风 -> faster-whisper（语音识别）-> DeepSeek Chat Completions + 工具 -> pyttsx3（语音合成）-> 扬声器`

DeepSeek 不提供与 OpenAI Realtime API 兼容的双向实时音频 WebSocket，因此本示例不使用 `agents.realtime`。

DeepSeek does not provide a bidirectional realtime-audio WebSocket compatible with the OpenAI Realtime API, so this example does not use `agents.realtime`.

## Setup / 配置

在此目录创建虚拟环境并安装依赖。

Create a virtual environment in this directory and install dependencies.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item env.example .env
```

在 `.env` 中填写 `DEEPSEEK_API_KEY`。

Set `DEEPSEEK_API_KEY` in `.env`.

首次启动时，`faster-whisper` 会下载 `WHISPER_MODEL` 指定的本地识别模型；默认 `base` 在准确率和资源占用之间较平衡。

On first launch, `faster-whisper` downloads the local model selected by `WHISPER_MODEL`; the default `base` balances accuracy and resource use.

若 Hugging Face 无法直连，请配置系统网络代理，或在 `.env` 中设置组织提供的 `HF_ENDPOINT`。该变量需要在程序启动前设置，示例代码会优先加载当前目录的 `.env`。

If Hugging Face is unreachable, configure a system proxy or set your organization's `HF_ENDPOINT` in `.env`. The variable must be set before startup; the example loads this directory's `.env` first.

## Run / 运行

```powershell
python agent.py
```

按 Enter 后程序录音 `RECORD_SECONDS` 秒，随后完成转写、工具调用和语音播放；输入 `q` 退出。

After pressing Enter, the program records for `RECORD_SECONDS`, then transcribes, invokes tools, and plays the response; enter `q` to quit.

## Notes / 注意事项

天气工具返回的是演示数据，时间工具读取本机时间。

The weather tool returns demo data, while the time tool reads the local system time.

语音合成使用 Windows 或系统默认语音；如未安装中文语音包，中文朗读效果可能有限。

Text-to-speech uses the Windows or system default voice; Chinese speech quality may be limited when no Chinese voice pack is installed.
