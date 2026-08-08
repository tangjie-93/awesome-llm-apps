from agents import Agent, Runner, RunConfig

# Create an agent for demonstrating run configuration
# 创建用于演示单次运行配置的 Agent

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
    name="Configuration Demo Agent",
    instructions="You are a helpful assistant that demonstrates run configuration options."
)

# Example 1: Basic run configuration with model settings
# 示例 1：通过 RunConfig 覆盖模型和运行参数
async def model_config_example():
    """Demonstrates run configuration with model overrides and settings"""
    
    run_config = RunConfig(
        # Override agent's default model
        # 覆盖 Agent 的默认模型
        model="gpt-5.5",
        model_settings={
            # Low temperature for consistent responses
            # 较低温度有助于获得稳定响应
            "temperature": 0.1,
            "top_p": 0.9
        },
        # Limit conversation turns
        # 限制最多执行轮数
        max_turns=5,
        # For tracing
        # 用于追踪标识
        workflow_name="demo_workflow",
        trace_metadata={"experiment": "config_demo"}
    )
    
    result = await Runner.run(
        root_agent, 
        "Explain the weather in exactly 3 sentences.",
        run_config=run_config
    )
    
    return result.final_output

# Example 2: Run configuration with tracing settings
# 示例 2：通过 RunConfig 配置追踪行为
async def tracing_config_example():
    """Demonstrates run configuration with tracing options"""
    
    run_config = RunConfig(
        # Enable tracing
        # 启用追踪
        tracing_disabled=False,
        # Exclude sensitive data
        # 不记录敏感数据
        trace_include_sensitive_data=False,
        workflow_name="production_workflow",
        # Link multiple runs
        # 将多次运行关联到同一组
        group_id="user_session_456",
        trace_metadata={
            "user_id": "user_123",
            "feature": "chat_assistance"
        }
    )
    
    result = await Runner.run(
        root_agent,
        "What are the benefits of structured logging?",
        run_config=run_config
    )
    
    return result.final_output
