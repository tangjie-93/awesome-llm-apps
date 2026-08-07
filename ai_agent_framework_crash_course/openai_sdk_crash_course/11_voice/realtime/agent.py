import asyncio
from agents import function_tool
from agents.realtime import RealtimeAgent, RealtimeRunner, realtime_handoff

from pathlib import Path
import sys

_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

configure_openai_client()

"""
Basic realtime voice agent example using OpenAI's Realtime API.
Run it via: python agent.py

This demonstrates the core realtime components from the official guide:
https://openai.github.io/openai-agents-python/realtime/guide/

Core Components:
1. RealtimeAgent - Agent with instructions, tools, and handoffs
2. RealtimeRunner - Manages configuration and sessions
3. RealtimeSession - Single conversation session
4. Event handling - Process audio, transcripts, and tool calls
"""

# Basic function tool
@function_tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    print(f"[debug] get_weather called with city: {city}")
    return f"The weather in {city} is sunny, 72°F"

@function_tool
def book_appointment(date: str, time: str, service: str) -> str:
    """Book an appointment."""
    print(f"[debug] book_appointment called: {service} on {date} at {time}")
    return f"Appointment booked for {service} on {date} at {time}"

# Specialized agent for handoffs
billing_agent = RealtimeAgent(
    name="Billing Support",
    instructions="You specialize in billing and payment issues.",
)

# Main realtime agent
agent = RealtimeAgent(
    name="Assistant",
    instructions="You are a helpful voice assistant. Keep responses brief and conversational.",
    tools=[get_weather, book_appointment],
    handoffs=[
        realtime_handoff(billing_agent, tool_description="Transfer to billing support")
    ]
)

async def main():
    """Basic realtime session example"""
    
    print("🎙️ Basic Realtime Voice Agent")
    print("=" * 40)
    
    # Set up the runner with basic configuration
    runner = RealtimeRunner(
        starting_agent=agent,
        config={
            "model_settings": {
                "model_name": "gpt-4o-realtime-preview",
                "voice": "alloy",
                "modalities": ["text", "audio"],
                "input_audio_transcription": {
                    "model": "whisper-1"
                },
                "turn_detection": {
                    "type": "server_vad",
                    "threshold": 0.5,
                    "silence_duration_ms": 200
                }
            }
        }
    )
    
    # Start the session
    print("Starting realtime session...")
    session = await runner.run()
    
    print("Session started! Speak naturally - agent will respond in real-time.")
    print("Try: 'What's the weather in Paris?' or 'Book appointment tomorrow at 2pm'")
    print("Press Ctrl+C to end")
    print("-" * 40)
    
    # Handle session events
    async with session:
        try:
            async for event in session:
                # Handle key event types
                if event.type == "response.audio_transcript.done":
                    print(f"🤖 Assistant: {event.transcript}")
                    
                elif event.type == "conversation.item.input_audio_transcription.completed":
                    print(f"👤 User: {event.transcript}")
                    
                elif event.type == "response.function_call_arguments.done":
                    print(f"🔧 Tool called: {event.name}")
                    
                elif event.type == "error":
                    print(f"❌ Error: {event.error}")
                    break
                    
        except KeyboardInterrupt:
            print("\n⏹️ Session ended")

if __name__ == "__main__":
    asyncio.run(main())
