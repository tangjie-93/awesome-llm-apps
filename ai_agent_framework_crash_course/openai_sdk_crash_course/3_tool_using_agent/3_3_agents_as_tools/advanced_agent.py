from agents import Agent, Runner, function_tool

# 定义专用研究 Agent

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

# 研究 Agent 负责收集和分析主题信息
research_agent = Agent(
    name="Research Specialist",
    instructions="""
    You are a research specialist. Provide detailed, well-researched information
    on any topic with proper analysis and insights.
    """
)

# 写作 Agent 负责将研究结果整理成结构化内容
writing_agent = Agent(
    name="Writing Specialist", 
    instructions="""
    You are a professional writer. Take research information and create
    well-structured, engaging content with proper formatting.
    """
)

@function_tool
async def run_research_agent(topic: str) -> str:
    """使用专用研究 Agent 调研主题，并应用自定义运行配置。"""
    
    result = await Runner.run(
        research_agent,
        input=f"Research this topic thoroughly: {topic}",
        max_turns=3  # 限制最多执行 3 轮，避免研究过程无限延伸
    )
    
    return str(result.final_output)

@function_tool  
async def run_writing_agent(content: str, style: str = "professional") -> str:
    """使用指定风格的写作 Agent 改写内容。"""
    
    prompt = f"Rewrite this content in a {style} style: {content}"
    
    result = await Runner.run(
        writing_agent,
        input=prompt,
        max_turns=2  # 写作任务最多执行 2 轮
    )
    
    return str(result.final_output)

# 创建内容生产编排 Agent，并注册研究和写作工具
advanced_orchestrator = Agent(
    name="Content Creation Orchestrator",
    instructions="""
    You are a content creation orchestrator that combines research and writing expertise.
    
    You have access to:
    - Research agent: For in-depth topic research
    - Writing agent: For professional content creation
    
    When users request content:
    1. First use the research agent to gather information
    2. Then use the writing agent to create polished content
    3. You can specify writing styles (professional, casual, academic, etc.)
    
    Coordinate both agents to create comprehensive, well-written content.
    """,
    tools=[run_research_agent, run_writing_agent]
)
