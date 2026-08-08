"""通过本地语音识别和语音合成接入 DeepSeek 的语音 Agent 示例。"""

import json
import os
from datetime import datetime
from pathlib import Path

# Hugging Face 会在导入时读取 HF_ENDPOINT，因此必须先加载 .env。
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"), override=True)

import numpy as np
import pyttsx3
import sounddevice as sd
from faster_whisper import WhisperModel
from openai import OpenAI

SAMPLE_RATE = 16_000
RECORD_SECONDS = float(os.getenv("RECORD_SECONDS", "5"))


def get_weather(city: str) -> str:
    """返回演示用天气数据，便于展示 DeepSeek 的工具调用流程。"""
    weather_by_city = {
        "北京": "晴，18 摄氏度",
        "上海": "多云，21 摄氏度",
        "paris": "小雨，14 摄氏度",
    }
    return weather_by_city.get(city.lower(), f"{city}：晴，20 摄氏度（演示数据）")


def get_current_time() -> str:
    """返回本机当前时间。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M")


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的天气。",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string", "description": "城市名称"}},
                "required": ["city"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "查询当前本机时间。",
            "parameters": {"type": "object", "properties": {}, "additionalProperties": False},
        },
    },
]

TOOL_HANDLERS = {"get_weather": get_weather, "get_current_time": get_current_time}


def record_audio() -> np.ndarray:
    """从默认麦克风录制单声道 PCM 音频。"""
    frames = int(SAMPLE_RATE * RECORD_SECONDS)
    print(f"正在录音 {RECORD_SECONDS:g} 秒，请说话...")
    audio = sd.rec(frames, samplerate=SAMPLE_RATE, channels=1, dtype="float32")
    sd.wait()
    return audio.reshape(-1)


def transcribe(model: WhisperModel, audio: np.ndarray) -> str:
    """使用本地 Whisper 模型将录音转换为文本。"""
    segments, _ = model.transcribe(audio, language="zh", vad_filter=True)
    return "".join(segment.text for segment in segments).strip()


def load_whisper_model() -> WhisperModel | None:
    """加载本地 Whisper 模型，首次运行时会从 Hugging Face 下载。"""
    model_name = os.getenv("WHISPER_MODEL", "base")
    try:
        print(f"正在加载本地语音识别模型：{model_name}")
        return WhisperModel(model_name, device="auto", compute_type="int8")
    except Exception as error:
        print(f"无法加载语音识别模型：{error}")
        print("请检查网络或代理；首次运行需要下载 faster-whisper 模型。")
        print("若使用自建 Hugging Face Hub，请在 .env 中设置 HF_ENDPOINT=https://你的端点。")
        return None


def run_agent(client: OpenAI, model: str, history: list[dict], user_text: str) -> str:
    """调用 DeepSeek，并循环处理模型提出的本地工具调用。"""
    messages = [
        {
            "role": "system",
            "content": "你是简洁、自然的中文语音助手。回答适合朗读；需要天气或时间时使用工具。",
        },
        *history,
        {"role": "user", "content": user_text},
    ]

    while True:
        response = client.chat.completions.create(model=model, messages=messages, tools=TOOLS)
        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            answer = message.content or "抱歉，我暂时没有生成回答。"
            history.extend([{"role": "user", "content": user_text}, {"role": "assistant", "content": answer}])
            return answer

        for tool_call in message.tool_calls:
            arguments = json.loads(tool_call.function.arguments)
            handler = TOOL_HANDLERS.get(tool_call.function.name)
            result = handler(**arguments) if handler else "未找到该工具。"
            print(f"调用工具 {tool_call.function.name}: {result}")
            messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": result})


def speak(engine: pyttsx3.Engine, text: str) -> None:
    """使用操作系统已安装的默认语音朗读回答。"""
    engine.say(text)
    engine.runAndWait()


def main() -> None:
    """初始化组件，并执行按键触发的多轮语音对话。"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("未配置 DEEPSEEK_API_KEY。请将 env.example 复制为 .env 后填写密钥。")
        return

    client = OpenAI(api_key=api_key, base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    whisper_model = load_whisper_model()
    if whisper_model is None:
        return
    tts_engine = pyttsx3.init()
    history: list[dict] = []

    print("DeepSeek 本地语音 Agent")
    print("按 Enter 录音；输入 q 后按 Enter 退出。")
    while True:
        if input("\n准备开始：").strip().lower() == "q":
            break
        try:
            text = transcribe(whisper_model, record_audio())
            if not text:
                print("没有识别到有效语音，请重试。")
                continue
            print(f"你：{text}")
            answer = run_agent(client, os.getenv("DEEPSEEK_MODEL", "deepseek-chat"), history, text)
            print(f"助手：{answer}")
            speak(tts_engine, answer)
        except KeyboardInterrupt:
            break
        except Exception as error:
            print(f"语音 Agent 运行失败：{error}")


if __name__ == "__main__":
    main()
