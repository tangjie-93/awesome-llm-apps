from agents import Agent, Runner, RunConfig

# Create an agent for demonstrating run configuration

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
async def model_config_example():
    """Demonstrates run configuration with model overrides and settings"""
    
    run_config = RunConfig(
        model="gpt-4o",  # Override agent's default model
        model_settings={
            "temperature": 0.1,  # Low temperature for consistent responses
            "top_p": 0.9
        },
        max_turns=5,  # Limit conversation turns
        workflow_name="demo_workflow",  # For tracing
        trace_metadata={"experiment": "config_demo"}
    )
    
    result = await Runner.run(
        root_agent, 
        "Explain the weather in exactly 3 sentences.",
        run_config=run_config
    )
    
    return result.final_output

# Example 2: Run configuration with tracing settings
async def tracing_config_example():
    """Demonstrates run configuration with tracing options"""
    
    run_config = RunConfig(
        tracing_disabled=False,  # Enable tracing
        trace_include_sensitive_data=False,  # Exclude sensitive data
        workflow_name="production_workflow",
        group_id="user_session_456",  # Link multiple runs
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
