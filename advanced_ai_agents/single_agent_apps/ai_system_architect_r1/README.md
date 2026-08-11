# 🤖 AI System Architect Advisor with R1
# 🤖 使用 `R1` 的 `AI` 系统架构顾问

An Agno agentic system that provides expert software architecture analysis and recommendations using a dual-model approach combining DeepSeek R1's Reasoning and Claude. The system provides detailed technical analysis, implementation roadmaps, and architectural decisions for complex software systems.
一个 `Agno` 智能体系统，通过结合 `DeepSeek R1` 的推理能力和 `Claude` 的双模型方法，提供专家级软件架构分析和建议。该系统为复杂软件系统提供详细技术分析、实施路线图和架构决策。

## Features
## 功能

- **Dual AI Model Architecture**
- **双 `AI` 模型架构**
  - **DeepSeek Reasoner**: Provides initial technical analysis and structured reasoning about architecture patterns, tools, and implementation strategies
  - **DeepSeek Reasoner**：围绕架构模式、工具和实施策略提供初始技术分析和结构化推理
  - **Claude-3.5**: Generates detailed explanations, implementation roadmaps, and technical specifications based on DeepSeek's analysis
  - **Claude-3.5**：基于 `DeepSeek` 的分析生成详细解释、实施路线图和技术规格

- **Comprehensive Analysis Components**
- **全面的分析组件**
  - Architecture Pattern Selection
  - 架构模式选择
  - Infrastructure Resource Planning
  - 基础设施资源规划
  - Security Measures and Compliance
  - 安全措施和合规
  - Database Architecture
  - 数据库架构
  - Performance Requirements
  - 性能需求
  - Cost Estimation
  - 成本估算
  - Risk Assessment
  - 风险评估

- **Analysis Types**
- **分析类型**
  - Real-time Event Processing Systems
  - 实时事件处理系统
  - Healthcare Data Platforms
  - 医疗健康数据平台
  - Financial Trading Platforms
  - 金融交易平台
  - Multi-tenant SaaS Solutions
  - 多租户 `SaaS` 解决方案
  - Digital Content Delivery Networks
  - 数字内容分发网络
  - Supply Chain Management Systems
  - 供应链管理系统

## How to Run
## 如何运行

1. **Setup Environment**
   **设置环境**
   ```bash
   # Clone the repository
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/single_agent_apps/ai_system_architect_r1
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   **配置 `API Keys`**
   - Get DeepSeek API key from DeepSeek platform
   - 从 `DeepSeek` 平台获取 `DeepSeek API key`
   - Get Anthropic API key from [Anthropic Platform](https://www.anthropic.com)
   - 从 [Anthropic Platform](https://www.anthropic.com) 获取 `Anthropic API key`

3. **Run the Application**
   **运行应用**
   ```bash
   streamlit run ai_system_architect_r1.py
   ```

4. **Use the Interface**
   **使用界面**
   - Enter API credentials in sidebar
   - 在侧边栏输入 `API` 凭据
   - Structure your prompt with:
   - 使用以下内容组织你的提示词：
     - Project Context
     - 项目上下文
     - Requirements
     - 需求
     - Constraints
     - 约束
     - Scale
     - 规模
     - Security/Compliance needs
     - 安全/合规需求
   - View detailed analysis results
   - 查看详细分析结果

## Example Test Prompts:
## 示例测试提示词：

### 1. Financial Trading Platform
### 1. 金融交易平台
"We need to build a high-frequency trading platform that processes market data streams, executes trades with sub-millisecond latency, maintains audit trails, and handles complex risk calculations. The system needs to be globally distributed, handle 100,000 transactions per second, and have robust disaster recovery capabilities."
“我们需要构建一个高频交易平台，用于处理市场数据流、以亚毫秒延迟执行交易、维护审计跟踪，并处理复杂的风险计算。该系统需要全球分布式部署，处理每秒 `100,000` 笔交易，并具备强大的灾难恢复能力。”
### 2. Multi-tenant SaaS Platform
### 2. 多租户 `SaaS` 平台
"Design a multi-tenant SaaS platform for enterprise resource planning that needs to support customization per tenant, handle different data residency requirements, support offline capabilities, and maintain performance isolation between tenants. The system should scale to 10,000 concurrent users and support custom integrations."
“设计一个用于企业资源规划的多租户 `SaaS` 平台，需要支持按租户定制、处理不同的数据驻留要求、支持离线能力，并在租户之间保持性能隔离。该系统应扩展到 `10,000` 并发用户并支持自定义集成。”

## Notes
## 备注

- Requires both DeepSeek and Anthropic API keys
- 需要 `DeepSeek` 和 `Anthropic API keys`
- Provides real-time analysis with detailed explanations
- 提供带有详细解释的实时分析
- Supports chat-based interaction
- 支持基于聊天的交互
- Includes clear reasoning for all architectural decisions
- 为所有架构决策提供清晰推理
- API usage costs apply
- 会产生 `API` 使用费用

