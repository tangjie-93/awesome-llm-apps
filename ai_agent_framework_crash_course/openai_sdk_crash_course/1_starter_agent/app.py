"""
Tutorial 1 的 Streamlit Web 界面：你的第一个 Agent。

该页面提供一个交互式 Web 界面，用于测试个人助理 Agent 的
同步、异步和流式三种执行方式。
"""

import os
import asyncio
from pathlib import Path
import sys

import streamlit as st
from agents import Agent, Runner
from agents.stream_events import RawResponsesStreamEvent
from openai.types.responses.response_text_delta_event import ResponseTextDeltaEvent

_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client, get_openai_model

OPENAI_SETTINGS = configure_openai_client()

# 配置 Streamlit 页面标题、图标和布局。
st.set_page_config(
    page_title="Personal Assistant Agent",
    page_icon="🎯",
    layout="wide"
)

# 页面主标题和教程说明。
st.title("🎯 Personal Assistant Agent")
st.markdown("**Tutorial 1**: Your first OpenAI agent with different execution methods")

# 检查 OpenAI API Key 是否存在，缺失时直接停止页面运行。
if not os.getenv("OPENAI_API_KEY"):
    st.error("❌ OPENAI_API_KEY not found. Please create a .env file with your OpenAI API key.")
    st.stop()

MODEL_NAME = get_openai_model()

# 创建并缓存 Agent，避免 Streamlit 每次重跑脚本时重复初始化。
@st.cache_resource
def create_agent(model_name: str):
    """创建个人助理 Agent，并配置它的角色和回复要求。"""
    return Agent(
        name="Personal Assistant",
        model=model_name,
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

agent = create_agent(MODEL_NAME)

# 侧边栏：选择 Agent 的执行方式。
st.sidebar.title("Execution Methods")
execution_method = st.sidebar.selectbox(
    "Choose execution method:",
    ["Synchronous", "Asynchronous", "Streaming"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### About Execution Methods")
st.sidebar.caption(f"Model: `{MODEL_NAME}`")
st.sidebar.caption(f"API: `{OPENAI_SETTINGS.api_type}`")
if OPENAI_SETTINGS.base_url:
    st.sidebar.caption(f"Base URL: `{OPENAI_SETTINGS.base_url}`")

# 根据当前选择展示对应执行方式的说明。
if execution_method == "Synchronous":
    st.sidebar.info("**Synchronous**: Blocks until response is complete. Simple and straightforward.")
elif execution_method == "Asynchronous":
    st.sidebar.info("**Asynchronous**: Non-blocking execution. Good for concurrent operations.")
else:
    st.sidebar.info("**Streaming**: Real-time response streaming. Great for long responses.")

# 主区域：聊天界面。
st.markdown("### Chat Interface")

# 初始化聊天历史，首次打开页面时创建空消息列表。
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

# 渲染历史消息。
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 接收用户输入或侧边栏示例提示词，并触发 Agent 回复。
chat_prompt = st.chat_input("Ask your personal assistant anything...")
prompt = st.session_state.pending_prompt or chat_prompt
st.session_state.pending_prompt = None

if prompt:
    # 将用户消息加入会话状态，便于页面重跑后继续显示。
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 根据选择的执行方式生成助手回复。
    with st.chat_message("assistant"):
        try:
            if execution_method == "Synchronous":
                # 同步执行：等待完整响应返回后一次性展示。
                with st.spinner("Thinking..."):
                    result = Runner.run_sync(agent, prompt)
                    response = result.final_output
                    st.markdown(response)
            
            elif execution_method == "Asynchronous":
                # 异步执行：在事件循环中等待 Agent 结果。
                with st.spinner("Processing asynchronously..."):
                    async def get_async_response():
                        """异步调用 Agent，并返回最终文本。"""
                        result = await Runner.run(agent, prompt)
                        return result.final_output
                    
                    response = asyncio.run(get_async_response())
                    st.markdown(response)
            
            else:  # Streaming
                # 流式执行：边接收边刷新占位区域，模拟实时输出效果。
                response_placeholder = st.empty()
                
                async def stream_response():
                    """消费 Agent 的流式事件，并实时更新页面内容。"""
                    full_response = ""
                    result = Runner.run_streamed(agent, prompt)
                    async for event in result.stream_events():
                        if isinstance(event, RawResponsesStreamEvent) and isinstance(event.data, ResponseTextDeltaEvent):
                            full_response += event.data.delta
                            response_placeholder.markdown(full_response + "▌")
                    
                    if not full_response and result.final_output:
                        full_response = result.final_output
                    response_placeholder.markdown(full_response)
                    return full_response
                
                response = asyncio.run(stream_response())
            
            # 将助手回复加入聊天历史。
            st.session_state.messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            # 捕获运行异常并在聊天区显示错误信息。
            error_msg = f"❌ {type(e).__name__}: {str(e)}"
            st.error(error_msg)
            if type(e).__name__ == "APITimeoutError":
                st.warning("请求超时。请检查 OPENAI_BASE_URL 是否指向你的中转站地址，或适当调大 OPENAI_TIMEOUT。")
            with st.expander("Error details"):
                st.exception(e)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})

# 侧边栏：清空聊天历史。
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.session_state.pending_prompt = None
    st.rerun()

# 侧边栏：示例提示词，点击后写入聊天历史并刷新页面。
st.sidebar.markdown("---")
st.sidebar.markdown("### Example Prompts")

example_prompts = [
    "What are 3 productivity tips for remote work?",
    "Explain quantum computing in simple terms",
    "Write a short poem about technology",
    "How can I improve my focus and concentration?",
    "What's the difference between AI and machine learning?"
]

for prompt in example_prompts:
    if st.sidebar.button(prompt, key=f"example_{prompt[:20]}"):
        # 记录待处理提示词，下一次 rerun 时由统一聊天逻辑生成回复。
        st.session_state.pending_prompt = prompt
        st.rerun()

# 页面底部：展示本教程覆盖的核心知识点。
st.markdown("---")
st.markdown("""
### 📚 Tutorial Information

This is **Tutorial 1** of the OpenAI Agents SDK crash course. You're learning:
- ✅ Basic agent creation with the Agent class
- ✅ Different execution methods (sync, async, streaming)  
- ✅ Agent configuration with instructions
- ✅ Interactive web interfaces with Streamlit

**Next**: Try [Tutorial 2: Structured Output Agent](../2_structured_output_agent/) to learn about type-safe responses.
""")
