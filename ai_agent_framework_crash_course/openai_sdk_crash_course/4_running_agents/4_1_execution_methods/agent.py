from agents import Agent, Runner
from agents.stream_events import RawResponsesStreamEvent
from openai.types.responses.response_text_delta_event import ResponseTextDeltaEvent
import asyncio

# Create a simple agent for demonstrating execution methods
# 创建一个用于演示不同执行方式的简单 Agent

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
    name="Execution Demo Agent",
    instructions="""
    You are a helpful assistant demonstrating different execution patterns.
    
    Provide clear, informative responses that help users understand:
    - Synchronous execution (blocking)
    - Asynchronous execution (non-blocking)
    - Streaming execution (real-time)
    
    Keep responses appropriate for the execution method being demonstrated.
    """
)

# Example 1: Synchronous execution
# 示例 1：同步执行，调用方会阻塞直到任务完成
def sync_execution_example():
    """Demonstrates Runner.run_sync() - blocking execution"""
    result = Runner.run_sync(root_agent, "Explain synchronous execution in simple terms")
    return result.final_output

# Example 2: Asynchronous execution
# 示例 2：异步执行，不阻塞当前事件循环
async def async_execution_example():
    """Demonstrates Runner.run() - non-blocking execution"""
    result = await Runner.run(root_agent, "Explain asynchronous execution benefits")
    return result.final_output

# Example 3: Streaming execution
# 示例 3：流式执行，逐块接收并实时输出响应
async def streaming_execution_example():
    """Demonstrates Runner.run_streamed() - real-time streaming"""
    full_response = ""
    
    result = Runner.run_streamed(root_agent, "Write a detailed explanation of streaming execution")
    async for event in result.stream_events():
        # Handle streaming events as they arrive
        # 处理实时到达的流式事件，只拼接文本增量事件
        if isinstance(event, RawResponsesStreamEvent) and isinstance(event.data, ResponseTextDeltaEvent):
            full_response += event.data.delta
            print(event.data.delta, end='', flush=True)  # Print in real-time
    
    print()  # New line after streaming
    return full_response
