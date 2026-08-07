import os

from agents import Agent, CodeInterpreterTool, Runner, WebSearchTool

# 导入 OpenAI Agents SDK 提供的内置工具，无需自行编写工具函数。

# 创建一个使用 OpenAI 内置工具的 Agent。

from pathlib import Path
import sys

# 将教程根目录加入模块搜索路径，以便导入公共的客户端配置模块。
_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

# 配置本项目使用的 OpenAI 客户端和模型。
configure_openai_client()

root_agent = Agent(
    name="Built-in Tools Agent",
    instructions="""
    You are a research and computation assistant with access to powerful built-in tools.
    
    Available tools:
    - WebSearchTool: Search the web for current information
    - CodeInterpreterTool: Execute Python code safely
    
    You can help with:
    - Finding current information and news
    - Performing complex calculations
    - Data analysis and visualization
    - Mathematical computations
    
    When users request information or calculations:
    1. Use web search for current information
    2. Use code execution for computations and analysis
    3. Provide clear explanations of results
    """,
    # WebSearchTool 获取实时网络信息，CodeInterpreterTool 执行代码和计算。
    # Agent 会根据用户问题和 instructions 自主选择是否调用这些工具。
    tools=[WebSearchTool(), CodeInterpreterTool()]
)


DEMO_PROMPT = "Use the code interpreter to calculate the compound interest on $5,000 at 3.5% annually for 8 years."


def main() -> None:
    """运行内置工具示例，并输出 Agent 的最终回答。"""
    if not os.getenv("OPENAI_API_KEY"):
        print("请在 .env 文件中配置 OPENAI_API_KEY 后再运行此示例。")
        return

    print("=== Built-in Tools Demo ===")
    print(f"Question: {DEMO_PROMPT}")
    result = Runner.run_sync(root_agent, DEMO_PROMPT)
    print(f"Answer: {result.final_output}")


if __name__ == "__main__":
    main()
