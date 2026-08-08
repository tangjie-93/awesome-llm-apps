from dataclasses import dataclass
from agents import Agent, RunContextWrapper, Runner, function_tool

from pathlib import Path
import sys

# 将课程根目录加入模块搜索路径，以便导入统一的客户端配置。
_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

# 配置本项目使用的 OpenAI 客户端和模型。
configure_openai_client()

@dataclass
class UserInfo:
    """保存用户信息和会话偏好的上下文对象。"""
    name: str
    uid: int
    preferences: dict = None
    
    def __post_init__(self):
        # 避免多个 UserInfo 实例意外共享同一个偏好字典。
        if self.preferences is None:
            self.preferences = {}

@function_tool
async def fetch_user_profile(wrapper: RunContextWrapper[UserInfo]) -> str:
    """从上下文中读取并返回用户详细资料。"""
    # Runner.run(..., context=user_context) 传入的对象可通过 wrapper.context 获取。
    user = wrapper.context
    return f"User Profile: {user.name} (ID: {user.uid}), Preferences: {user.preferences}"

@function_tool
async def update_user_preference(wrapper: RunContextWrapper[UserInfo], key: str, value: str) -> str:
    """更新上下文中的用户偏好设置。"""
    user = wrapper.context
    # 直接修改上下文对象，使同一次运行后的调用可以读取更新后的偏好。
    user.preferences[key] = value
    return f"Updated {user.name}'s preference: {key} = {value}"

@function_tool
async def get_personalized_greeting(wrapper: RunContextWrapper[UserInfo]) -> str:
    """根据用户上下文和问候偏好生成个性化问候语。"""
    user = wrapper.context
    preferred_style = user.preferences.get('greeting_style', 'formal')
    
    if preferred_style == 'casual':
        return f"Hey {user.name}! What's up?"
    elif preferred_style == 'friendly':
        return f"Hi there, {user.name}! How can I help you today?"
    else:
        return f"Good day, {user.name}. How may I assist you?"

# 创建带有上下文感知工具的 Agent，并用泛型声明其上下文类型为 UserInfo。
root_agent = Agent[UserInfo](
    name="Context-Aware Assistant",
    instructions="""
    You are a personalized assistant that uses user context to provide tailored responses.
    
    You have access to:
    - User profile information (name, ID, preferences)
    - Ability to update user preferences
    - Personalized greeting generation
    
    Use the context tools to:
    1. Fetch user information when needed
    2. Update preferences when users express them
    3. Provide personalized greetings and responses
    
    Always consider the user's context when responding.
    """,
    tools=[fetch_user_profile, update_user_preference, get_personalized_greeting]
)

# 上下文管理示例：创建用户状态、传给 Agent，并在运行后读取更新结果。
async def context_example():
    """演示如何使用用户信息作为 Agent 的运行上下文。"""
    
    # 创建本次 Agent 运行共享的用户上下文。
    user_context = UserInfo(
        name="Alice Johnson",
        uid=12345,
        preferences={"greeting_style": "friendly", "topic_interest": "technology"}
    )
    
    # 将上下文传入 Runner；工具可通过 RunContextWrapper 访问和更新该对象。
    result = await Runner.run(
        root_agent,
        "Hello! I'd like to know about my profile and prefer casual greetings.",
        context=user_context
    )
    
    print(f"Response: {result.final_output}")
    print(f"Updated context: {user_context}")
    
    return result
