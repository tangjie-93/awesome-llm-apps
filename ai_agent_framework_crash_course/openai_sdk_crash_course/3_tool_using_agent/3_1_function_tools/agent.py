import os

from agents import Agent, Runner

try:
    # 支持通过 `python -m` 方式作为包运行。
    from .tools import add_numbers, convert_temperature, get_weather, multiply_numbers
except ImportError:
    # 支持在当前目录直接执行 `python agent.py`。
    from tools import add_numbers, convert_temperature, get_weather, multiply_numbers

# 创建一个使用自定义函数工具的 Agent。

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


DEMO_PROMPT = "What is 12.5 degrees Celsius in Fahrenheit?"


def main() -> None:
    """运行函数工具示例，并输出 Agent 的最终回答。"""
    if not os.getenv("OPENAI_API_KEY"):
        print("请在 .env 文件中配置 OPENAI_API_KEY 后再运行此示例。")
        return

    print("=== Function Tools Demo ===")
    print(f"Question: {DEMO_PROMPT}")
    result = Runner.run_sync(root_agent, DEMO_PROMPT)
    print(f"Answer: {result.final_output}")


if __name__ == "__main__":
    main()
