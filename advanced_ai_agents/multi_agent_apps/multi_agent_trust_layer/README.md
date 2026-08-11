# 🤝 Multi-Agent Trust Layer - Secure Agent-to-Agent Communication
# 🤝 多智能体信任层 - 安全的智能体到智能体通信

Learn how to build a trust layer for multi-agent systems that enables secure delegation, trust scoring, and policy enforcement between AI agents.
学习如何为多智能体系统构建信任层，在 `AI` 智能体之间实现安全委托、信任评分和策略执行。

## Features
## 功能

- **Agent Identity**: Each agent has a verifiable identity with a human sponsor
- **智能体身份**：每个智能体都有可验证身份，并关联一位人类担保人
- **Trust Scoring**: Behavioral monitoring with a 0-1000 trust score
- **信任评分**：通过行为监控生成 `0-1000` 的信任分数
- **Delegation Chains**: Cryptographically narrow scope when delegating tasks
- **委托链**：在委托任务时通过加密方式收窄权限范围
- **Policy Enforcement**: Enforce compliance rules across agent interactions
- **策略执行**：在智能体交互中执行合规规则
- **Audit Trail**: Full observability of agent-to-agent communications
- **审计轨迹**：对智能体到智能体通信提供完整可观测性

## How It Works
## 工作原理

```
┌─────────────────┐         ┌─────────────────┐
│   Agent A       │◀───────▶│   Trust Layer   │
│  (Orchestrator) │   TLS   │                 │
└─────────────────┘         │  • Identity     │
                            │  • Trust Score  │
┌─────────────────┐         │  • Delegation   │
│   Agent B       │◀───────▶│  • Policy       │
│  (Specialist)   │   TLS   │  • Audit        │
└─────────────────┘         └─────────────────┘
```

1. **Registration**: Agents register with verified identity and human sponsor
1. **注册**：智能体使用已验证身份和人类担保人进行注册
2. **Trust Establishment**: Initial trust score based on sponsor reputation
2. **信任建立**：基于担保人声誉生成初始信任分数
3. **Delegation**: Parent agents can delegate tasks with narrowed permissions
3. **委托**：父级智能体可以在权限收窄后委托任务
4. **Monitoring**: All actions are tracked and trust scores updated
4. **监控**：跟踪所有动作并更新信任分数
5. **Enforcement**: Policies determine what each agent can do
5. **执行**：策略决定每个智能体可以执行的操作

## Requirements
## 要求

- Python 3.8+
- `Python 3.8+`
- OpenAI API key (or any LLM provider)
- `OpenAI API key`（或任意 `LLM` 提供商）
- Required Python packages (see `requirements.txt`)
- 所需 `Python` 包（见 `requirements.txt`）

## Installation
## 安装

1. Clone this repository:
1. 克隆此仓库：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/multi_agent_trust_layer
   ```

2. Install the required packages:
2. 安装所需包：
   ```bash
   pip install -r requirements.txt
   ```

## Usage
## 使用

1. Set your API key:
1. 设置你的 `API key`：
   ```bash
   export OPENAI_API_KEY=your-openai-api-key
   ```

2. Run the trust layer demo:
2. 运行信任层演示：
   ```bash
   python multi_agent_trust_layer.py
   ```

3. Watch agents interact through the trust layer with full observability.
3. 观察智能体通过信任层交互，并获得完整可观测性。

## Example: Agent Delegation Chain
## 示例：智能体委托链

```python
# Orchestrator agent creates a delegation for a specialist
delegation = trust_layer.create_delegation(
    from_agent="orchestrator-001",
    to_agent="researcher-002",
    scope={
        "allowed_actions": ["web_search", "summarize"],
        "max_tokens": 10000,
        "time_limit_minutes": 30,
        "allowed_domains": ["arxiv.org", "github.com"]
    },
    task_description="Research recent papers on AI safety"
)

# Researcher can only perform actions within the delegated scope
result = researcher.execute_with_delegation(
    delegation=delegation,
    action="web_search",
    params={"query": "AI safety papers 2024"}
)
```

## Trust Score System
## 信任评分系统

Trust scores range from 0-1000:
信任分数范围为 `0-1000`：

| Score Range<br>分数范围 | Level<br>级别 | Permissions<br>权限 |
|-------------|-------|-------------|
| 900-1000 | Trusted<br>受信任 | Full access within role<br>角色内完全访问 |
| 700-899 | Standard<br>标准 | Normal operations<br>正常操作 |
| 500-699 | Probation<br>观察期 | Limited actions, extra logging<br>受限操作，额外日志记录 |
| 300-499 | Restricted<br>受限 | Human approval required<br>需要人类批准 |
| 0-299 | Suspended<br>暂停 | No autonomous actions<br>不允许自主操作 |

### Score Updates
### 分数更新

```python
# Positive behaviors increase trust
+10: Successfully completed delegated task
+5:  Stayed within scope boundaries
+2:  Provided accurate information

# Negative behaviors decrease trust
-50: Attempted action outside scope
-30: Provided inaccurate information
-20: Exceeded resource limits
-100: Security violation
```

## Example Output
## 示例输出

```
🤝 Multi-Agent Trust Layer Demo
================================

📋 Registering agents...
✅ Registered: orchestrator-001 (Human Sponsor: alice@company.com)
✅ Registered: researcher-002 (Human Sponsor: bob@company.com)
✅ Registered: writer-003 (Human Sponsor: carol@company.com)

🔐 Creating delegation chain...
✅ Delegation: orchestrator-001 → researcher-002
   Scope: web_search, summarize
   Time Limit: 30 minutes

🤖 Agent researcher-002 executing: web_search
   Query: "AI safety papers 2024"
✅ Action ALLOWED (within delegated scope)
   Trust Score: 850 → 860 (+10)

🤖 Agent researcher-002 executing: send_email
❌ Action DENIED (not in delegated scope)
   Trust Score: 860 → 810 (-50)

📊 Trust Scores:
   orchestrator-001: 900 (Trusted)
   researcher-002: 810 (Standard)
   writer-003: 850 (Standard)
```

## Key Concepts
## 核心概念

### 1. Agent Identity
### 1. 智能体身份

Every agent has a cryptographic identity tied to a human sponsor:
每个智能体都有一个与人类担保人绑定的加密身份：

```python
@dataclass
class AgentIdentity:
    agent_id: str
    public_key: str
    human_sponsor: str  # Accountable human
    organization: str
    roles: List[str]
    created_at: datetime
```

### 2. Delegation Chains
### 2. 委托链

Delegations form a chain where each link can only narrow scope:
委托会形成一条链，其中每个链接只能收窄范围：

```python
@dataclass  
class Delegation:
    delegation_id: str
    parent_agent: str
    child_agent: str
    scope: DelegationScope
    signature: str  # Signed by parent
    parent_delegation: Optional[str]  # Links to parent's delegation
```

### 3. Policy Enforcement
### 3. 策略执行

Policies define what agents can do based on trust and role:
策略会根据信任和角色定义智能体可以做什么：

```python
policies:
  researcher:
    base_trust_required: 500
    allowed_actions:
      - web_search
      - read_document
      - summarize
    denied_actions:
      - execute_code
      - send_email
    resource_limits:
      max_tokens_per_hour: 100000
      max_api_calls_per_minute: 60
```

## Architecture
## 架构

```
┌────────────────────────────────────────────────────┐
│                   Trust Layer                       │
├─────────────┬─────────────┬─────────────┬──────────┤
│  Identity   │  Trust      │  Delegation │  Policy  │
│  Registry   │  Scoring    │  Manager    │  Engine  │
├─────────────┴─────────────┴─────────────┴──────────┤
│                   Audit Logger                      │
└────────────────────────────────────────────────────┘
         ▲              ▲              ▲
         │              │              │
    ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
    │ Agent A │    │ Agent B │    │ Agent C │
    └─────────┘    └─────────┘    └─────────┘
```

## Extending the Tutorial
## 扩展教程

- Add cryptographic signatures for delegation verification
- 添加用于委托验证的加密签名
- Implement reputation systems across organizations
- 实现跨组织声誉系统
- Add real-time trust score visualization
- 添加实时信任分数可视化
- Connect to external identity providers (OAuth, SAML)
- 连接外部身份提供商（`OAuth`、`SAML`）
- Implement secure communication channels (mTLS)
- 实现安全通信通道（`mTLS`）

## Related Projects
## 相关项目

- [LangGraph](https://github.com/langchain-ai/langgraph) - Multi-agent orchestration
- [LangGraph](https://github.com/langchain-ai/langgraph) - 多智能体编排
- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent framework
- [CrewAI](https://github.com/joaomdmoura/crewAI) - 多智能体框架
- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent conversations
- [AutoGen](https://github.com/microsoft/autogen) - 多智能体对话
