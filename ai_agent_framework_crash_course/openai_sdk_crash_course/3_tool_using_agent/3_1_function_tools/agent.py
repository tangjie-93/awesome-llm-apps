from agents import Agent
from .tools import add_numbers, multiply_numbers, get_weather, convert_temperature

# Create an agent with custom function tools

from pathlib import Path
import sys

_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

configure_openai_client()

root_agent = Agent(
    name="Function Tools Agent",
    instructions="""
    You are a helpful assistant with access to various tools.
    
    Available tools:
    - add_numbers: Add two numbers together
    - multiply_numbers: Multiply two numbers together  
    - get_weather: Get weather information for a city
    - convert_temperature: Convert between Celsius and Fahrenheit
    
    When users ask for calculations or information:
    1. Use the appropriate tool for the task
    2. Explain what you're doing
    3. Show the result clearly
    
    Always use the provided tools rather than doing calculations yourself.
    """,
    tools=[add_numbers, multiply_numbers, get_weather, convert_temperature]
)
