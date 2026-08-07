import streamlit as st
import asyncio
import os
from datetime import datetime
from agents import Agent, Runner, SQLiteSession
from dotenv import load_dotenv

# Load environment variables
# 加载环境变量

from pathlib import Path
import sys

# Locate the openai_sdk_crash_course root so shared config can be imported.
# 定位 openai_sdk_crash_course 根目录，方便导入共享配置。
_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

# Configure the OpenAI client before creating or running agents.
# 在创建或运行 Agent 前，先完成 OpenAI 客户端配置。
configure_openai_client()

load_dotenv()

# Page configuration
# Streamlit 页面配置
st.set_page_config(
    page_title="Session Management Demo",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize agents
# 初始化 Agent。cache_resource 会让 Agent 实例在 Streamlit 重跑时复用。
@st.cache_resource
def initialize_agents():
    """Initialize AI agents for different use cases.

    初始化不同使用场景下需要的 AI Agent。
    """
    
    # Main demo agent focuses on showing session memory behavior.
    # 主演示 Agent 用于展示 session 记忆能力。
    main_agent = Agent(
        name="Session Demo Assistant",
        instructions="""
        You are a helpful assistant demonstrating session memory capabilities.
        
        Remember previous conversation context and reference it when relevant.
        Reply concisely but show that you remember previous interactions.
        Be friendly and professional.
        """
    )
    
    # Support agent is used in multi-session and handoff scenarios.
    # Support Agent 用于多会话和交接场景中的客服上下文。
    support_agent = Agent(
        name="Support Agent",
        instructions="You are a customer support representative. Help with account and technical issues. Be helpful and solution-oriented."
    )
    
    # Sales agent uses a different instruction set to demonstrate context separation.
    # Sales Agent 使用不同指令，用于演示不同业务上下文的隔离。
    sales_agent = Agent(
        name="Sales Agent", 
        instructions="You are a sales representative. Help with product information and purchases. Be enthusiastic and informative."
    )
    
    return main_agent, support_agent, sales_agent

# Session management functions
# 会话管理工具类：封装 SQLiteSession 的创建、读取、清理和修改操作。
class SessionManager:
    def __init__(self):
        # Keep SQLiteSession objects in memory to reuse them during the app session.
        # 在内存中缓存 SQLiteSession 对象，方便 Streamlit 应用运行期间复用。
        self.sessions = {}
    
    def get_session(self, session_id: str, db_file: str = "demo_sessions.db"):
        """Get or create a session.

        获取已有 session；如果不存在，则创建新的 SQLiteSession。
        """
        if session_id not in self.sessions:
            # SQLiteSession persists history to db_file when a database path is provided.
            # 传入数据库文件后，SQLiteSession 会把对话历史持久化保存到该文件。
            self.sessions[session_id] = SQLiteSession(session_id, db_file)
        return self.sessions[session_id]
    
    async def clear_session(self, session_id: str):
        """Clear a specific session.

        清空指定 session 的历史，并从当前缓存中移除。
        """
        if session_id in self.sessions:
            await self.sessions[session_id].clear_session()
            del self.sessions[session_id]
    
    async def get_session_items(self, session_id: str, limit: int = None):
        """Get conversation items from a session.

        读取指定 session 中的对话条目，可通过 limit 限制数量。
        """
        if session_id in self.sessions:
            return await self.sessions[session_id].get_items(limit=limit)
        return []
    
    async def add_custom_items(self, session_id: str, items: list):
        """Add custom items to a session.

        向指定 session 手动追加自定义对话条目。
        """
        if session_id in self.sessions:
            await self.sessions[session_id].add_items(items)
    
    async def pop_last_item(self, session_id: str):
        """Remove the last item from a session.

        从指定 session 中移除最后一条对话条目。
        """
        if session_id in self.sessions:
            return await self.sessions[session_id].pop_item()
        return None

# Initialize session manager
# 初始化全局 SessionManager，并存入 Streamlit session_state。
if 'session_manager' not in st.session_state:
    st.session_state.session_manager = SessionManager()

# Main UI
# 主界面入口
def main():
    """Render the Streamlit app shell and dispatch to the selected demo.

    渲染 Streamlit 应用外壳，并根据用户选择切换到对应演示。
    """
    st.title("🔄 Session Management Demo")
    st.markdown("**Demonstrates OpenAI Agents SDK session capabilities**")
    
    # Initialize agents
    # 初始化三个 Agent，供不同演示页面使用。
    main_agent, support_agent, sales_agent = initialize_agents()
    
    # Sidebar for session configuration
    # 侧边栏用于选择演示类型和管理会话。
    with st.sidebar:
        st.header("⚙️ Session Configuration")
        
        demo_type = st.selectbox(
            "Select Demo Type",
            ["Basic Sessions", "Memory Operations", "Multi Sessions"]
        )
        
        if demo_type == "Basic Sessions":
            session_type = st.radio(
                "Session Type",
                ["In-Memory", "Persistent"]
            )
        
        st.divider()
        
        # Session controls
        # 会话控制：清空当前 SessionManager 缓存中的所有 session。
        st.subheader("Session Controls")
        
        if st.button("🗑️ Clear All Sessions"):
            with st.spinner("Clearing sessions..."):
                for session_id in list(st.session_state.session_manager.sessions.keys()):
                    asyncio.run(st.session_state.session_manager.clear_session(session_id))
                st.success("All sessions cleared!")
                st.rerun()
    
    # Main content area
    # 根据用户选择渲染不同演示区域。
    if demo_type == "Basic Sessions":
        render_basic_sessions(main_agent)
    elif demo_type == "Memory Operations":
        render_memory_operations(main_agent)
    elif demo_type == "Multi Sessions":
        render_multi_sessions(support_agent, sales_agent)

def render_basic_sessions(agent):
    """Render the basic sessions demo.

    渲染基础会话演示，用于对比内存会话和持久化会话。
    """
    st.header("📝 Basic Sessions Demo")
    st.markdown("Demonstrates fundamental session memory with automatic conversation history.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💾 In-Memory Session")
        st.caption("Temporary session storage (lost when app restarts)")
        
        # This demo reuses one in-memory style session ID during the app lifecycle.
        # 这个演示在应用生命周期内复用同一个内存会话 ID。
        session_id = "in_memory_demo"
        
        with st.form("in_memory_form"):
            user_input = st.text_input("Your message:", key="in_memory_input")
            submitted = st.form_submit_button("Send Message")
            
            if submitted and user_input:
                with st.spinner("Processing..."):
                    # Runner.run receives the session so conversation history is automatic.
                    # 把 session 传给 Runner.run 后，对话历史会自动接续。
                    session = st.session_state.session_manager.get_session(session_id)
                    result = asyncio.run(Runner.run(agent, user_input, session=session))
                    
                    st.success("Message sent!")
                    st.write(f"**Assistant:** {result.final_output}")
        
        # Show conversation history
        # 展示当前 session 中已保存的对话历史。
        if st.button("📋 Show Conversation", key="show_in_memory"):
            items = asyncio.run(st.session_state.session_manager.get_session_items(session_id))
            if items:
                st.write("**Conversation History:**")
                for i, item in enumerate(items, 1):
                    role_emoji = "👤" if item['role'] == 'user' else "🤖"
                    st.write(f"{i}. {role_emoji} **{item['role'].title()}:** {item['content']}")
            else:
                st.info("No conversation history yet.")
    
    with col2:
        st.subheader("💽 Persistent Session")
        st.caption("File-based storage (survives app restarts)")
        
        # This session uses a dedicated database file to demonstrate persistence.
        # 这个 session 使用独立数据库文件，演示持久化保存效果。
        session_id = "persistent_demo"
        
        with st.form("persistent_form"):
            user_input = st.text_input("Your message:", key="persistent_input")
            submitted = st.form_submit_button("Send Message")
            
            if submitted and user_input:
                with st.spinner("Processing..."):
                    # Use a file-backed SQLiteSession so history can survive app restarts.
                    # 使用文件型 SQLiteSession，让历史记录可以跨应用重启保留。
                    session = st.session_state.session_manager.get_session(session_id, "persistent_demo.db")
                    result = asyncio.run(Runner.run(agent, user_input, session=session))
                    
                    st.success("Message sent!")
                    st.write(f"**Assistant:** {result.final_output}")
        
        # Show conversation history
        # 展示持久化 session 中保存的对话历史。
        if st.button("📋 Show Conversation", key="show_persistent"):
            items = asyncio.run(st.session_state.session_manager.get_session_items(session_id))
            if items:
                st.write("**Conversation History:**")
                for i, item in enumerate(items, 1):
                    role_emoji = "👤" if item['role'] == 'user' else "🤖"
                    st.write(f"{i}. {role_emoji} **{item['role'].title()}:** {item['content']}")
            else:
                st.info("No conversation history yet.")

def render_memory_operations(agent):
    """Render the memory operations demo.

    渲染记忆操作演示，包括读取、追加、撤销和清空 session 条目。
    """
    st.header("🧠 Memory Operations Demo")
    st.markdown("Demonstrates advanced session memory operations including item manipulation and corrections.")
    
    # One session ID is used so each operation targets the same conversation history.
    # 使用固定 session ID，确保所有记忆操作都作用在同一段对话历史上。
    session_id = "memory_operations_demo"
    
    # Main conversation area
    # 主对话区：用于正常发送消息并写入 session。
    st.subheader("💬 Conversation")
    with st.form("memory_conversation"):
        user_input = st.text_input("Your message:")
        submitted = st.form_submit_button("Send Message")
        
        if submitted and user_input:
            with st.spinner("Processing..."):
                # Each run appends user and assistant items to the session.
                # 每次运行都会把用户消息和助手响应追加到 session。
                session = st.session_state.session_manager.get_session(session_id)
                result = asyncio.run(Runner.run(agent, user_input, session=session))
                
                st.success("Message sent!")
                st.write(f"**Assistant:** {result.final_output}")
    
    # Memory operations
    # 记忆操作区：左侧读取历史，右侧修改历史。
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Memory Inspection")
        
        # Read every item currently stored in the session.
        # 读取当前 session 中保存的所有条目。
        if st.button("🔍 Get All Items"):
            items = asyncio.run(st.session_state.session_manager.get_session_items(session_id))
            if items:
                st.write(f"**Total items:** {len(items)}")
                for i, item in enumerate(items, 1):
                    role_emoji = "👤" if item['role'] == 'user' else "🤖"
                    content_preview = item['content'][:100] + "..." if len(item['content']) > 100 else item['content']
                    st.write(f"{i}. {role_emoji} **{item['role'].title()}:** {content_preview}")
            else:
                st.info("No items in session yet.")
        
        # Get limited items
        # 只读取最近 N 条记录，便于查看较长会话的尾部内容。
        limit = st.number_input("Get last N items:", min_value=1, max_value=20, value=3)
        if st.button("📋 Get Recent Items"):
            items = asyncio.run(st.session_state.session_manager.get_session_items(session_id, limit=limit))
            if items:
                st.write(f"**Last {len(items)} items:**")
                for i, item in enumerate(items, 1):
                    role_emoji = "👤" if item['role'] == 'user' else "🤖"
                    st.write(f"{i}. {role_emoji} **{item['role'].title()}:** {item['content']}")
            else:
                st.info("No items to show.")
    
    with col2:
        st.subheader("✏️ Memory Manipulation")
        
        # Add custom items
        # 手动追加自定义 user/assistant 条目，用于模拟或修正历史。
        st.write("**Add Custom Items:**")
        with st.form("add_items_form"):
            user_content = st.text_area("User message to add:")
            assistant_content = st.text_area("Assistant response to add:")
            add_submitted = st.form_submit_button("➕ Add Items")
            
            if add_submitted and user_content and assistant_content:
                custom_items = [
                    {"role": "user", "content": user_content},
                    {"role": "assistant", "content": assistant_content}
                ]
                asyncio.run(st.session_state.session_manager.add_custom_items(session_id, custom_items))
                st.success("Custom items added!")
        
        # Pop last item (correction)
        # 弹出最后一条记录，常用于撤销最近一次响应或修正对话。
        if st.button("↶ Undo Last Response"):
            popped_item = asyncio.run(st.session_state.session_manager.pop_last_item(session_id))
            if popped_item:
                st.success(f"Removed: {popped_item['role']} - {popped_item['content'][:50]}...")
            else:
                st.warning("No items to remove.")
        
        # Clear session
        # 清空当前演示 session，重新开始记忆操作。
        if st.button("🗑️ Clear Session"):
            asyncio.run(st.session_state.session_manager.clear_session(session_id))
            st.success("Session cleared!")

def render_multi_sessions(support_agent, sales_agent):
    """Render the multi-sessions demo.

    渲染多会话演示，包括多用户、不同上下文和 Agent 交接场景。
    """
    st.header("👥 Multi Sessions Demo")
    st.markdown("Demonstrates managing multiple conversations and different agent contexts.")
    
    # Tabs separate the three common session organization patterns.
    # 使用 tabs 展示三种常见的 session 组织方式。
    tab1, tab2, tab3 = st.tabs(["👤 Multi-User", "🏢 Context-Based", "🔄 Agent Handoff"])
    
    with tab1:
        st.subheader("Different Users, Separate Sessions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**👩 Alice's Session**")
            # Alice and Bob use different session IDs so their histories stay isolated.
            # Alice 和 Bob 使用不同 session ID，因此对话历史互相隔离。
            alice_session_id = "user_alice"
            
            with st.form("alice_form"):
                alice_input = st.text_input("Alice's message:", key="alice_input")
                alice_submitted = st.form_submit_button("Send as Alice")
                
                if alice_submitted and alice_input:
                    with st.spinner("Processing Alice's message..."):
                        # Store multiple users in the same database file with separate session IDs.
                        # 多个用户可共用同一个数据库文件，但通过不同 session ID 隔离历史。
                        session = st.session_state.session_manager.get_session(alice_session_id, "multi_user.db")
                        result = asyncio.run(Runner.run(support_agent, alice_input, session=session))
                        st.write(f"**Support:** {result.final_output}")
            
            if st.button("📋 Alice's History", key="alice_history"):
                items = asyncio.run(st.session_state.session_manager.get_session_items(alice_session_id))
                for item in items:
                    role_emoji = "👩" if item['role'] == 'user' else "🛠️"
                    st.write(f"{role_emoji} **{item['role'].title()}:** {item['content']}")
        
        with col2:
            st.write("**👨 Bob's Session**")
            # Bob has an independent session even though the same support agent is used.
            # Bob 使用独立 session，即使背后调用的是同一个 Support Agent。
            bob_session_id = "user_bob"
            
            with st.form("bob_form"):
                bob_input = st.text_input("Bob's message:", key="bob_input")
                bob_submitted = st.form_submit_button("Send as Bob")
                
                if bob_submitted and bob_input:
                    with st.spinner("Processing Bob's message..."):
                        # Same database file, different session ID.
                        # 同一个数据库文件，不同 session ID。
                        session = st.session_state.session_manager.get_session(bob_session_id, "multi_user.db")
                        result = asyncio.run(Runner.run(support_agent, bob_input, session=session))
                        st.write(f"**Support:** {result.final_output}")
            
            if st.button("📋 Bob's History", key="bob_history"):
                items = asyncio.run(st.session_state.session_manager.get_session_items(bob_session_id))
                for item in items:
                    role_emoji = "👨" if item['role'] == 'user' else "🛠️"
                    st.write(f"{role_emoji} **{item['role'].title()}:** {item['content']}")
    
    with tab2:
        st.subheader("Different Contexts, Different Sessions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**🛠️ Support Context**")
            # A context-specific session keeps support history separate from sales history.
            # 使用上下文专属 session，让客服历史与销售历史分开。
            support_session_id = "support_context"
            
            with st.form("support_context_form"):
                support_input = st.text_input("Support question:", key="support_context_input")
                support_submitted = st.form_submit_button("Ask Support")
                
                if support_submitted and support_input:
                    with st.spinner("Processing support question..."):
                        session = st.session_state.session_manager.get_session(support_session_id, "contexts.db")
                        result = asyncio.run(Runner.run(support_agent, support_input, session=session))
                        st.write(f"**Support:** {result.final_output}")
        
        with col2:
            st.write("**💰 Sales Context**")
            # Sales conversations use a separate session and a separate agent prompt.
            # 销售对话使用独立 session 和独立 Agent 指令。
            sales_session_id = "sales_context"
            
            with st.form("sales_context_form"):
                sales_input = st.text_input("Sales inquiry:", key="sales_context_input")
                sales_submitted = st.form_submit_button("Ask Sales")
                
                if sales_submitted and sales_input:
                    with st.spinner("Processing sales inquiry..."):
                        session = st.session_state.session_manager.get_session(sales_session_id, "contexts.db")
                        result = asyncio.run(Runner.run(sales_agent, sales_input, session=session))
                        st.write(f"**Sales:** {result.final_output}")
    
    with tab3:
        st.subheader("Shared Session Across Different Agents")
        st.caption("Customer handoff scenario - same conversation, different agents")
        
        # Both agents use this one session to demonstrate handoff with shared history.
        # 两个 Agent 共用同一个 session，用于演示带共享历史的交接。
        shared_session_id = "customer_handoff"
        
        # Agent selector
        # 用户选择当前由哪个 Agent 处理同一段共享对话。
        selected_agent = st.radio(
            "Select Agent:",
            ["Sales Agent", "Support Agent"],
            horizontal=True
        )
        
        agent = sales_agent if selected_agent == "Sales Agent" else support_agent
        
        with st.form("handoff_form"):
            handoff_input = st.text_input("Customer message:")
            handoff_submitted = st.form_submit_button(f"Send to {selected_agent}")
            
            if handoff_submitted and handoff_input:
                with st.spinner(f"Processing with {selected_agent}..."):
                    # The selected agent changes, but the session stays the same.
                    # 当前 Agent 可以切换，但 session 保持不变。
                    session = st.session_state.session_manager.get_session(shared_session_id, "shared.db")
                    result = asyncio.run(Runner.run(agent, handoff_input, session=session))
                    st.write(f"**{selected_agent}:** {result.final_output}")
        
        # Show shared conversation history
        # 展示两个 Agent 共用的完整对话历史。
        if st.button("📋 Show Shared Conversation"):
            items = asyncio.run(st.session_state.session_manager.get_session_items(shared_session_id))
            if items:
                st.write("**Shared Conversation History:**")
                for i, item in enumerate(items, 1):
                    if item['role'] == 'user':
                        st.write(f"{i}. 👤 **Customer:** {item['content']}")
                    else:
                        # Try to determine which agent responded based on content
                        agent_emoji = "💰" if "sales" in item['content'].lower() or "price" in item['content'].lower() else "🛠️"
                        st.write(f"{i}. {agent_emoji} **Agent:** {item['content']}")
            else:
                st.info("No conversation history yet.")

# Footer
# 页脚说明
def render_footer():
    """Render a summary of demonstrated session capabilities.

    渲染本应用演示过的 session 能力总结。
    """
    st.divider()
    st.markdown("""
    ### 🎯 Session Capabilities Demonstrated
    
    1. **Basic Sessions**: In-memory vs persistent storage
    2. **Memory Operations**: get_items(), add_items(), pop_item(), clear_session()
    3. **Multi Sessions**: Multiple users, contexts, and agent handoffs
    
    **Key Benefits:**
    - Automatic conversation history management
    - Flexible session organization strategies
    - Memory manipulation for corrections and custom flows
    - Multi-agent conversation support
    """)

if __name__ == "__main__":
    main()
    render_footer()
