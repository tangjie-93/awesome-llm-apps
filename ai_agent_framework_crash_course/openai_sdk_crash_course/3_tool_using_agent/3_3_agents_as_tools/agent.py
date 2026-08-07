from agents import Agent

# 定义多个专用翻译 Agent，每个 Agent 负责一种目标语言

from pathlib import Path
import sys

_OPENAI_SDK_ROOT = Path(__file__).resolve()
# 将课程根目录加入模块搜索路径，以便复用统一的客户端配置
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

configure_openai_client()

# 创建西班牙语、法语和德语翻译 Agent
spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You translate the user's message to Spanish"
)

french_agent = Agent(
    name="French Agent", 
    instructions="You translate the user's message to French"
)

german_agent = Agent(
    name="German Agent",
    instructions="You translate the user's message to German"
)

# 创建编排 Agent，并将专用翻译 Agent 暴露为可调用工具
root_agent = Agent(
    name="Translation Orchestrator",
    instructions="""
    You are a translation orchestrator agent. You coordinate specialized translation agents.
    
    You have access to translation agents for:
    - Spanish translations
    - French translations  
    - German translations
    
    When users request translations:
    1. Use the appropriate translation agent tool
    2. You can use multiple agents if asked for multiple translations
    3. Present the results clearly with language labels
    
    If asked for multiple translations, call the relevant tools for each language.
    """,
    tools=[
        # as_tool 将 Agent 封装为工具，编排 Agent 可按需调用
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish"
        ),
        french_agent.as_tool(
            tool_name="translate_to_french", 
            tool_description="Translate the user's message to French"
        ),
        german_agent.as_tool(
            tool_name="translate_to_german",
            tool_description="Translate the user's message to German"
        )
    ]
)
