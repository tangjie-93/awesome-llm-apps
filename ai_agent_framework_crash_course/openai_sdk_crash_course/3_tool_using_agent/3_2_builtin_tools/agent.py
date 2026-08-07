from agents import Agent
# 导入 OpenAI Agents SDK 提供的内置工具，无需自行编写工具函数。
from agents.tools import WebSearchTool, CodeInterpreterTool

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
