# 🛡️ AI Agent Governance - Policy-Based Sandboxing
# 🛡️ `AI Agent Governance` - 基于策略的沙箱

Learn how to build a governance layer that enforces deterministic policies on AI agents, preventing dangerous actions before they execute.
学习如何构建一个治理层，对 `AI` 智能体执行确定性策略，在危险操作执行前将其阻止。

## Features
## 功能

- **Policy-Based Sandboxing**: Define what your AI agent can and cannot do using declarative policies
  **基于策略的沙箱**：使用声明式策略定义你的 `AI` 智能体可以做什么、不能做什么
- **Action Interception**: Catch and validate agent actions before execution
  **动作拦截**：在执行前捕获并验证智能体动作
- **Audit Logging**: Full trail of agent actions for compliance and debugging
  **审计日志**：为合规和调试保留完整的智能体动作轨迹
- **File System Guards**: Restrict read/write to specific directories
  **文件系统防护**：将读写限制在指定目录内
- **Network Guards**: Allowlist-only external API access
  **网络防护**：仅允许访问白名单中的外部 `API`
- **Rate Limiting**: Prevent runaway agents with configurable limits
  **速率限制**：通过可配置限制防止智能体失控运行

## How It Works
## 工作原理

1. **Policy Definition**: Define your security policies in YAML format
   **策略定义**：以 `YAML` 格式定义你的安全策略
2. **Action Wrapping**: Wrap your agent's tools with the governance layer
   **动作包装**：用治理层包装智能体的工具
3. **Interception**: Before any tool executes, the policy engine validates the action
   **拦截**：在任何工具执行前，策略引擎会验证该动作
4. **Decision**: Actions are allowed, denied, or require human approval
   **决策**：动作会被允许、拒绝，或要求人工审批
5. **Audit**: All decisions are logged for compliance and debugging
   **审计**：所有决策都会被记录，用于合规和调试

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Agent     │────▶│  Governance  │────▶│    Tool     │
│  (LLM)      │     │    Layer     │     │  Execution  │
└─────────────┘     └──────────────┘     └─────────────┘
                           │
                    ┌──────▼──────┐
                    │   Policy    │
                    │   Engine    │
                    └─────────────┘
```

## Requirements
## 要求

- Python 3.8+
  `Python 3.8+`
- OpenAI API key (or any LLM provider)
  `OpenAI API key`（或任意 `LLM` 提供商）
- Required Python packages (see `requirements.txt`)
  所需 `Python` 包（见 `requirements.txt`）

## Installation
## 安装

1. Clone this repository:
   克隆此仓库：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/single_agent_apps/ai_agent_governance
   ```

2. Install the required packages:
   安装所需包：
   ```bash
   pip install -r requirements.txt
   ```

## Usage
## 使用方法

1. Set your API key:
   设置你的 `API key`：
   ```bash
   export OPENAI_API_KEY=your-openai-api-key
   ```

2. Run the governance demo:
   运行治理演示：
   ```bash
   python ai_agent_governance.py
   ```

3. Try different actions and see how the policy engine handles them.
   尝试不同动作，观察策略引擎如何处理它们。

## Example Policy Configuration
## 示例策略配置

```yaml
policies:
  filesystem:
    allowed_paths: ["/workspace", "/tmp"]
    denied_paths: ["/etc", "/home", "~/.ssh"]
    
  network:
    allowed_domains: ["api.openai.com", "api.github.com"]
    block_all_others: true
    
  execution:
    max_actions_per_minute: 60
    require_approval_for: ["delete_file", "execute_shell"]
    
  tools:
    allowed: ["read_file", "write_file", "web_search"]
    denied: ["execute_code", "send_email"]
```

## Example Output
## 示例输出

```
🛡️ AI Agent Governance Demo
============================

📋 Loading policy: workspace_sandbox.yaml

🤖 Agent request: "Read the contents of /etc/passwd"
❌ DENIED: Path '/etc/passwd' is outside allowed directories

🤖 Agent request: "Write analysis to /workspace/report.md"  
✅ ALLOWED: Action permitted by policy

🤖 Agent request: "Make HTTP request to unknown-api.com"
❌ DENIED: Domain 'unknown-api.com' not in allowlist

🤖 Agent request: "Delete /workspace/temp.txt"
⏸️ PENDING: Action requires human approval
   [Y/n]: 
```

## Technical Details
## 技术细节

### Policy Engine
### 策略引擎

The policy engine evaluates actions against a set of rules:
策略引擎会根据一组规则评估动作：

```python
class PolicyEngine:
    def evaluate(self, action: Action) -> Decision:
        # Check each policy rule
        for rule in self.rules:
            result = rule.evaluate(action)
            if result.is_terminal:
                return result
        return Decision.ALLOW
```

### Action Interception
### 动作拦截

Tools are wrapped with governance checks:
工具会被治理检查包装：

```python
def governed_tool(func):
    def wrapper(*args, **kwargs):
        action = Action(name=func.__name__, args=args, kwargs=kwargs)
        decision = policy_engine.evaluate(action)
        
        if decision == Decision.DENY:
            raise PolicyViolation(decision.reason)
        elif decision == Decision.REQUIRE_APPROVAL:
            if not get_human_approval(action):
                raise PolicyViolation("Human denied the action")
        
        # Log the action
        audit_log.record(action, decision)
        
        return func(*args, **kwargs)
    return wrapper
```

### Audit Logging
### 审计日志

All actions are logged with full context:
所有动作都会连同完整上下文一起记录：

```python
{
    "timestamp": "2024-01-15T10:30:00Z",
    "action": "write_file",
    "args": {"path": "/workspace/report.md"},
    "decision": "ALLOW",
    "policy_matched": "filesystem.allowed_paths",
    "agent_id": "research-agent-001"
}
```

## Key Concepts Learned
## 学到的关键概念

1. **Deterministic vs Probabilistic Safety**: Why policy enforcement is more reliable than prompt engineering
   **确定性安全与概率性安全**：为什么策略执行比提示词工程更可靠
2. **Defense in Depth**: Multiple layers of validation for robust security
   **纵深防御**：通过多层验证实现稳健安全
3. **Audit Trails**: Importance of logging for compliance and debugging
   **审计轨迹**：日志记录对合规和调试的重要性
4. **Principle of Least Privilege**: Only grant the permissions agents actually need
   **最小权限原则**：只授予智能体实际需要的权限

## Extending the Tutorial
## 扩展本教程

- Add custom policy rules for your use case
  为你的使用场景添加自定义策略规则
- Implement human-in-the-loop approval workflows
  实现 `human-in-the-loop` 审批工作流
- Connect to external policy management systems
  连接到外部策略管理系统
- Add real-time monitoring and alerting
  添加实时监控和告警

## Related Projects
## 相关项目

- [LangChain](https://github.com/langchain-ai/langchain) - LLM application framework
  [`LangChain`](https://github.com/langchain-ai/langchain) - `LLM` 应用框架
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Input/output validation for LLMs
  [`Guardrails AI`](https://github.com/guardrails-ai/guardrails) - 面向 `LLM` 的输入/输出验证
