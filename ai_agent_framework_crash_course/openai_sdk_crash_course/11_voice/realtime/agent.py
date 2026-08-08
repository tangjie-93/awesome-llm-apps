import asyncio
import os

import websockets
from agents import function_tool
# 导入实时 Agent、运行器和用于切换专用 Agent 的交接工具。
from agents.realtime import RealtimeAgent, RealtimeRunner, realtime_handoff
from dotenv import load_dotenv

from pathlib import Path
import sys

# 将课程根目录加入模块搜索路径，以便复用公共客户端配置。
_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

# 优先加载当前示例目录的 .env，避免公共配置模块找不到此处的 API Key。
load_dotenv(Path(__file__).with_name(".env"), override=True)
# 配置本项目使用的 OpenAI 客户端和模型。
configure_openai_client()

"""
使用 OpenAI Realtime API 的基础实时语音 Agent 示例。
通过 python agent.py 启动。

This demonstrates the core realtime components from the official guide:
https://openai.github.io/openai-agents-python/realtime/guide/

核心组件：
1. RealtimeAgent：包含指令、工具和交接关系的 Agent
2. RealtimeRunner：管理模型配置和会话生命周期
3. RealtimeSession：单次实时对话会话
4. 事件处理：处理音频、转写结果和工具调用
"""

# 基础函数工具：@function_tool 会将普通函数注册为实时 Agent 可调用的工具。
@function_tool
def get_weather(city: str) -> str:
    """Get current weather for a city.

    获取指定城市的当前天气。
    """
    print(f"[debug] get_weather called with city: {city}")
    return f"The weather in {city} is sunny, 72°F"

@function_tool
def book_appointment(date: str, time: str, service: str) -> str:
    """Book an appointment.

    根据日期、时间和服务类型预约服务。
    """
    print(f"[debug] book_appointment called: {service} on {date} at {time}")
    return f"Appointment booked for {service} on {date} at {time}"

# 专用账单 Agent：主 Agent 遇到支付或账单问题时会交接给它处理。
billing_agent = RealtimeAgent(
    name="Billing Support",
    instructions="You specialize in billing and payment issues.",
)

# 主实时语音 Agent：负责一般对话、工具调用和账单问题的交接。
agent = RealtimeAgent(
    name="Assistant",
    instructions="You are a helpful voice assistant. Keep responses brief and conversational.",
    tools=[get_weather, book_appointment],
    handoffs=[
        realtime_handoff(
            billing_agent,
            # 覆盖交接工具描述，帮助模型理解何时转交账单问题。
            tool_description_override="Transfer to billing support",
        )
    ]
)

async def main():
    """Basic realtime session example.

    基础实时语音会话示例。
    """
    
    if not os.getenv("OPENAI_API_KEY"):
        print("未找到 OPENAI_API_KEY，请在 realtime/.env 中配置后重试。")
        return

    realtime_url = os.getenv("OPENAI_REALTIME_URL")
    base_url = os.getenv("OPENAI_BASE_URL")
    if base_url and "api.openai.com" not in base_url and not realtime_url:
        print("检测到自定义 OPENAI_BASE_URL，但未配置实时 WebSocket 端点。")
        print("请在 realtime/.env 中设置 OPENAI_REALTIME_URL=wss://<服务地址>/...。")
        print("该地址必须由服务商明确支持 OpenAI Realtime WebSocket API。")
        return

    print("🎙️ Basic Realtime Voice Agent")
    print("=" * 40)
    
    # Set up the runner with basic configuration
    # 使用基础配置创建实时运行器
    runner = RealtimeRunner(
        starting_agent=agent,
        config={
            "model_settings": {
                # Realtime 模型、语音音色和输入/输出模态。
                "model_name": "gpt-4o-realtime-preview",
                "voice": "alloy",
                "modalities": ["text", "audio"],
                # 将用户音频转写为文本，便于在事件循环中显示。
                "input_audio_transcription": {
                    "model": "whisper-1"
                },
                # 服务器端 VAD 检测用户何时说完一轮话。
                "turn_detection": {
                    "type": "server_vad",
                    "threshold": 0.5,
                    "silence_duration_ms": 200
                }
            }
        }
    )
    
    # Start the session
    # 启动实时会话
    print("Connecting to realtime session...")
    # 传入自定义 WebSocket 地址时，SDK 仍会使用 OPENAI_API_KEY 作为 Bearer 认证。
    model_config = {"api_key": os.environ["OPENAI_API_KEY"]}
    if realtime_url:
        model_config["url"] = realtime_url
    session = await runner.run(model_config=model_config)
    
    # Handle session events
    # 处理会话中的音频、转写、工具调用和错误事件
    try:
        async with session:
            print("Session connected! Speak naturally - agent will respond in real-time.")
            print("Try: 'What's the weather in Paris?' or 'Book appointment tomorrow at 2pm'")
            print("Press Ctrl+C to end")
            print("-" * 40)

            try:
                async for event in session:
                    # 根据事件类型输出助手回复、用户转写或工具调用信息。
                    if event.type == "response.audio_transcript.done":
                        # 助手语音回复的最终转写文本。
                        print(f"🤖 Assistant: {event.transcript}")

                    elif event.type == "conversation.item.input_audio_transcription.completed":
                        # 用户输入语音完成转写。
                        print(f"👤 User: {event.transcript}")

                    elif event.type == "response.function_call_arguments.done":
                        # 模型已生成完整工具参数，即将执行对应工具。
                        print(f"🔧 Tool called: {event.name}")

                    elif event.type == "error":
                        # 遇到不可恢复的会话错误时退出事件循环。
                        print(f"❌ Error: {event.error}")
                        break

            except KeyboardInterrupt:
                print("\n⏹️ Session ended")
    except TimeoutError:
        print("❌ Realtime WebSocket 握手超时。")
        print("请检查 OPENAI_REALTIME_URL、网络代理和服务商是否支持 Realtime WebSocket API。")
    except websockets.exceptions.InvalidStatus as error:
        print(f"❌ Realtime WebSocket 被服务端拒绝：HTTP {error.response.status_code}。")
        print("请使用服务商提供的 Realtime WebSocket 地址；当前普通中转路径不支持该接口。")

if __name__ == "__main__":
    asyncio.run(main())
