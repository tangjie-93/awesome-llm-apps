import os
from dataclasses import dataclass
from agents import (
    Agent,
    Runner,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)
from agents.stream_events import RawResponsesStreamEvent
from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.types.responses.response_text_delta_event import ResponseTextDeltaEvent


@dataclass(frozen=True)
class OpenAIClientSettings:
    """OpenAI 兼容客户端的运行配置。"""

    api_key: str | None
    base_url: str | None
    timeout: float
    max_retries: int
    api_type: str


def load_openai_settings() -> OpenAIClientSettings:
    """从环境变量读取 OpenAI 客户端配置。"""
    return OpenAIClientSettings(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL") or None,
        timeout=float(os.getenv("OPENAI_TIMEOUT", "120")),
        max_retries=int(os.getenv("OPENAI_MAX_RETRIES", "2")),
        api_type=os.getenv("OPENAI_API_TYPE", "responses"),
    )


def configure_openai_client(settings: OpenAIClientSettings) -> None:
    """根据配置初始化 Agents SDK 使用的 OpenAI 客户端。"""
    if settings.api_type in {"responses", "chat_completions"}:
        set_default_openai_api(settings.api_type)

    set_default_openai_client(
        AsyncOpenAI(
            api_key=settings.api_key,
            base_url=settings.base_url,
            timeout=settings.timeout,
            max_retries=settings.max_retries,
        ),
        use_for_tracing=False,
    )


# 加载 .env 文件中的环境变量，例如 OPENAI_API_KEY 和 OPENAI_BASE_URL。
load_dotenv(override=True)

# 本地示例默认关闭 tracing，避免网络或权限问题导致非致命上报错误。
set_tracing_disabled(True)

configure_openai_client(load_openai_settings())

# 创建一个个人助理 Agent，用于演示不同的运行方式。
root_agent = Agent(
    name="Personal Assistant Agent",
    model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
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
