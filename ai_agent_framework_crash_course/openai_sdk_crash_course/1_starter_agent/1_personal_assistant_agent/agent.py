import os
from pathlib import Path
import sys

from agents import Agent, Runner
from agents.stream_events import RawResponsesStreamEvent
from openai.types.responses.response_text_delta_event import ResponseTextDeltaEvent

_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client, get_openai_model

configure_openai_client()

# 创建一个个人助理 Agent，用于演示不同的运行方式。
root_agent = Agent(
    name="Personal Assistant Agent",
    model=get_openai_model(),
    instructions="""
    You are a helpful personal assistant.
    
    Your role is to:
    1. Answer questions clearly and concisely
    2. Provide helpful information and advice
    3. Be friendly and professional
    4. Offer practical solutions to problems
    
    When users ask questions:
    - Give accurate and helpful responses
    - Explain complex topics in simple terms
    - Offer follow-up suggestions when appropriate
    - Maintain a positive and supportive tone
    
    Keep responses concise but informative.
    """
)

# 以下函数分别展示同步、异步和流式三种调用模式。
def sync_example():
    """使用同步 Runner API 运行个人助理 Agent。

    该示例会阻塞当前线程，直到 Agent 完成提示词处理，
    然后返回最终的助手回复文本。

    返回:
        str: Agent 生成的最终输出内容。
    """
    result = Runner.run_sync(root_agent, "Hello, how does sync execution work?")
    return result.final_output


async def async_example():
    """使用异步 Runner API 运行个人助理 Agent。

    该示例需要在事件循环中调用，通过 await 等待 Agent 执行完成，
    不会阻塞其他异步任务。

    返回:
        str: Agent 生成的最终输出内容。
    """
    result = await Runner.run(root_agent, "Hello, how does async execution work?")
    return result.final_output


async def streaming_example():
    """以流式方式运行个人助理 Agent，并收集回复内容。

    该示例逐个消费 Agent 返回的流式事件，当事件中包含文本内容时，
    将其追加到完整回复中，最后返回拼接后的文本。

    返回:
        str: 从流式事件中拼接得到的完整回复文本。
    """
    response_text = ""
    result = Runner.run_streamed(root_agent, "Tell me about streaming execution")
    async for event in result.stream_events():
        if isinstance(event, RawResponsesStreamEvent) and isinstance(event.data, ResponseTextDeltaEvent):
            response_text += event.data.delta
    return response_text or result.final_output
