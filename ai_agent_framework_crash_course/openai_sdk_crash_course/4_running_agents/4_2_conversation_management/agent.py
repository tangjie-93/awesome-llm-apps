from agents import Agent, Runner, SQLiteSession

# Create an agent for demonstrating conversation management
# 创建用于演示对话上下文管理的 Agent

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
    name="Conversation Agent",
    instructions="You are a helpful assistant that remembers conversation context. Reply concisely but reference previous context when relevant."
)

# Example 1: Manual conversation management
# 示例 1：手动维护对话历史
async def manual_conversation_example():
    """Demonstrates manual conversation management using result.to_input_list()"""
    
    # First turn
    # 第一轮：建立初始对话
    result = await Runner.run(root_agent, "My name is Alice and I live in San Francisco.")
    print(f"Turn 1: {result.final_output}")
    
    # Second turn - manually pass conversation history
    # 第二轮：将上一轮结果转换为输入列表并手动传入
    new_input = result.to_input_list() + [{"role": "user", "content": "What city do I live in?"}]
    result = await Runner.run(root_agent, new_input)
    print(f"Turn 2: {result.final_output}")
    
    return result

# Example 2: Automatic conversation management with Sessions
# 示例 2：使用 Session 自动维护对话历史
async def session_conversation_example():
    """Demonstrates automatic conversation management using SQLiteSession"""
    
    # Create session instance
    # 创建会话实例，后续请求通过同一实例共享上下文
    session = SQLiteSession("conversation_123")
    
    # First turn
    # 第一轮：写入会话上下文
    result = await Runner.run(root_agent, "I'm a software developer working on AI projects.", session=session)
    print(f"Session Turn 1: {result.final_output}")
    
    # Second turn - session automatically remembers context
    # 第二轮：Session 自动带上之前保存的上下文
    result = await Runner.run(root_agent, "What kind of work do I do?", session=session)
    print(f"Session Turn 2: {result.final_output}")
    
    return result
