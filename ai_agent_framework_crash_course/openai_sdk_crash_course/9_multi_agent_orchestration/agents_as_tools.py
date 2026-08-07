from agents import Agent, Runner, function_tool
import asyncio

# Define specialized research agent
# 定义专门负责研究分析的 Agent

from pathlib import Path
import sys

# 定位 openai_sdk_crash_course 根目录，方便导入共享配置。
_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

# 在创建和运行 Agent 前，先完成 OpenAI 客户端配置。
configure_openai_client()

# 研究 Agent：负责围绕主题收集信息、分析要点和输出洞察。
research_agent = Agent(
    name="Research Specialist",
    instructions="""
    You are a research specialist. Provide detailed, well-researched information
    on any topic with proper analysis and insights. Focus on factual accuracy
    and comprehensive coverage.
    """
)

# Define specialized writing agent
# 定义专门负责写作成文的 Agent。
writing_agent = Agent(
    name="Writing Specialist", 
    instructions="""
    You are a professional writer. Take research information and create
    well-structured, engaging content with proper formatting and flow.
    Make content accessible and compelling for readers.
    """
)

# Define editing agent
# 定义专门负责润色和编辑的 Agent。
editing_agent = Agent(
    name="Editing Specialist",
    instructions="""
    You are a professional editor. Review written content for:
    - Grammar and spelling errors
    - Clarity and readability
    - Structure and flow
    - Consistency and tone
    
    Provide the improved version of the content.
    """
)

# Create function tools from agents
# 把研究 Agent 包装成 function_tool，供编排 Agent 调用。
@function_tool
async def research_tool(topic: str) -> str:
    """使用研究 Agent 深入研究指定主题，并返回关键洞察。"""
    
    # max_turns=3 允许研究 Agent 进行更深入的多轮推理。
    result = await Runner.run(
        research_agent,
        input=f"Research this topic thoroughly and provide key insights: {topic}",
        max_turns=3  # Allow deeper research
    )
    
    return str(result.final_output)

# 把写作 Agent 包装成 function_tool，支持传入不同写作风格。
@function_tool  
async def writing_tool(content: str, style: str = "professional") -> str:
    """使用写作 Agent 将研究内容改写成指定风格的正文。"""
    
    # 将研究结果和目标风格组合成写作 Agent 的输入。
    prompt = f"Write engaging {style} content based on this research: {content}"
    
    result = await Runner.run(
        writing_agent,
        input=prompt,
        max_turns=2
    )
    
    return str(result.final_output)

# 把编辑 Agent 包装成 function_tool，用于最终润色内容。
@function_tool
async def editing_tool(content: str) -> str:
    """使用编辑 Agent 对内容进行语法、结构和表达优化。"""
    
    result = await Runner.run(
        editing_agent,
        input=f"Edit and improve this content for clarity, grammar, and engagement: {content}"
    )
    
    return str(result.final_output)

# Create orchestrator agent that uses other agents as tools
# 创建总控 Agent：它不直接完成所有工作，而是按需调用其他 Agent 工具。
content_orchestrator = Agent(
    name="Content Creation Orchestrator",
    instructions="""
    You are a content creation orchestrator that coordinates research, writing, and editing.
    
    You have access to:
    - research_tool: For in-depth topic research and insights
    - writing_tool: For professional content creation (specify style: professional, casual, academic, etc.)
    - editing_tool: For content review and improvement
    
    When users request content:
    1. First use research_tool to gather comprehensive information
    2. Then use writing_tool to create well-structured content
    3. Finally use editing_tool to polish and improve the final piece
    
    Coordinate all three tools to create high-quality, well-researched content.
    """,
    tools=[research_tool, writing_tool, editing_tool]
)

# Example 1: Basic content creation workflow
async def basic_content_workflow():
    """演示把多个 Agent 当作工具使用的基础内容生产流程。"""
    
    print("=== Basic Content Creation Workflow ===")
    
    # 编排 Agent 会根据指令自动依次调用 research_tool、writing_tool 和 editing_tool。
    result = await Runner.run(
        content_orchestrator,
        """Create a comprehensive article about the benefits of renewable energy. 
        I need it to be professional and well-researched, suitable for a business audience."""
    )
    
    print(f"Final article: {result.final_output}")
    
    return result

# Example 2: Custom workflow with specific requirements
async def custom_workflow_example():
    """演示编排 Agent 如何处理更具体的内容要求。"""
    
    print("\n=== Custom Workflow with Specific Requirements ===")
    
    # 这个请求包含主题、受众、内容范围和字数限制，用于测试编排能力。
    result = await Runner.run(
        content_orchestrator,
        """I need content about artificial intelligence in healthcare for a technical blog.
        Make sure to:
        1. Research current AI applications in medical diagnosis
        2. Write in an accessible but technical style
        3. Include both benefits and challenges
        4. Keep it under 500 words
        
        Please go through the full research -> write -> edit process."""
    )
    
    print(f"Technical blog post: {result.final_output}")
    
    return result

# Example 3: Comparison with direct agent orchestration
async def direct_orchestration_comparison():
    """对比手动串联 Agent 和自动使用 Agent 工具的编排方式。"""
    
    print("\n=== Direct Orchestration (Manual) ===")
    topic = "The future of remote work"
    
    # Manual orchestration - calling agents directly
    # 手动编排第 1 步：直接调用研究 Agent。
    print("Step 1: Research...")
    research_result = await Runner.run(
        research_agent,
        f"Research trends and predictions about: {topic}"
    )
    
    # 手动编排第 2 步：把研究结果传给写作 Agent。
    print("Step 2: Writing...")
    writing_result = await Runner.run(
        writing_agent,
        f"Write a professional article based on this research: {research_result.final_output}"
    )
    
    # 手动编排第 3 步：把写作结果传给编辑 Agent。
    print("Step 3: Editing...")
    editing_result = await Runner.run(
        editing_agent,
        f"Edit and improve this article: {writing_result.final_output}"
    )
    
    print(f"Manual orchestration result: {editing_result.final_output}")
    
    print("\n=== Agents-as-Tools Orchestration (Automatic) ===")
    
    # Automatic orchestration using orchestrator agent
    # 自动编排：只把目标交给 content_orchestrator，由它决定何时调用各个工具。
    orchestrated_result = await Runner.run(
        content_orchestrator,
        f"Create a professional article about: {topic}. Go through research, writing, and editing."
    )
    
    print(f"Automatic orchestration result: {orchestrated_result.final_output}")
    
    return editing_result, orchestrated_result

# Example 4: Advanced orchestrator with conditional logic
async def advanced_orchestrator_example():
    """演示带条件判断的高级 Agent 工具编排逻辑。"""
    
    print("\n=== Advanced Orchestrator with Conditional Logic ===")
    
    # Create advanced orchestrator with conditional workflows
    # 高级编排 Agent 会根据任务类型选择不同工作流。
    advanced_orchestrator = Agent(
        name="Advanced Content Orchestrator",
        instructions="""
        You are an intelligent content orchestrator that adapts workflows based on requirements.
        
        Available tools:
        - research_tool: For topic research
        - writing_tool: For content creation (styles: professional, casual, academic, creative)
        - editing_tool: For content improvement
        
        Workflow decisions:
        - For complex/technical topics: Do extra research first
        - For creative content: Use creative writing style
        - For short content: Skip detailed research
        - For business content: Always edit for professionalism
        - Always explain your workflow decisions
        
        Adapt your approach based on the specific request.
        """,
        tools=[research_tool, writing_tool, editing_tool]
    )
    
    # Test with different content types
    # 用三类不同请求测试高级编排 Agent 的条件判断能力。
    requests = [
        "Write a quick social media post about coffee benefits",
        "Create a detailed technical whitepaper on blockchain security",
        "Write a creative story about a robot learning to paint"
    ]
    
    for i, request in enumerate(requests, 1):
        # 每个请求都交给同一个高级编排 Agent，由它自行决定调用哪些工具。
        print(f"\nRequest {i}: {request}")
        result = await Runner.run(advanced_orchestrator, request)
        print(f"Result: {result.final_output}")
        print("-" * 50)
    
    return requests

# Main execution
async def main():
    """依次运行所有 Agent 作为工具的编排示例。"""
    print("🔧 OpenAI Agents SDK - Agents as Tools Orchestration")
    print("=" * 60)
    
    # 基础三步内容生产：研究、写作、编辑。
    await basic_content_workflow()
    # 带具体要求的内容生产。
    await custom_workflow_example()
    # 手动编排和自动编排的对比。
    await direct_orchestration_comparison()
    # 根据任务类型动态选择工作流的高级编排。
    await advanced_orchestrator_example()
    
    print("\n✅ Agents as tools tutorial complete!")
    print("Agents as tools enable sophisticated workflow orchestration with intelligent coordination")

if __name__ == "__main__":
    asyncio.run(main())
