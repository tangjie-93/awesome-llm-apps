# AI Services Agency 👨‍💼
# AI 服务机构 👨‍💼

An AI application that simulates a full-service digital agency using multiple AI agents to analyze and plan software projects.
一个 `AI` 应用，使用多个 `AI Agent` 模拟全服务数字机构，用于分析和规划软件项目。

Each agent represents a different role in the project lifecycle, from strategic planning to technical implementation.
每个智能体代表项目生命周期中的不同角色，从战略规划到技术实施。

## Demo:
## 演示：

https://github.com/user-attachments/assets/a0befa3a-f4c3-400d-9790-4b9e37254405

## Features
## 功能

### Five specialized AI agents
### 五个专业化 AI 智能体

- **CEO Agent**: Strategic leader and final decision maker
- **CEO 智能体**：战略领导者和最终决策者
  - Analyzes startup ideas using structured evaluation
  - 使用结构化评估分析创业想法
  - Makes strategic decisions across product, technical, marketing, and financial domains
  - 在产品、技术、市场和财务领域做出战略决策
  - Uses AnalyzeProjectRequirements tool
  - 使用 `AnalyzeProjectRequirements` 工具

- **CTO Agent**: Technical architecture and feasibility expert
- **CTO 智能体**：技术架构和可行性专家
  - Evaluates technical requirements and feasibility
  - 评估技术需求和可行性
  - Provides architecture decisions
  - 提供架构决策
  - Uses CreateTechnicalSpecification tool
  - 使用 `CreateTechnicalSpecification` 工具

- **Product Manager Agent**: Product strategy specialist
- **产品经理智能体**：产品战略专家
  - Defines product strategy and roadmap
  - 定义产品战略和路线图
  - Coordinates between technical and marketing teams
  - 协调技术团队和市场团队
  - Focuses on product-market fit
  - 聚焦产品市场匹配

- **Developer Agent**: Technical implementation expert
- **开发者智能体**：技术实施专家
  - Provides detailed technical implementation guidance
  - 提供详细的技术实施指导
  - Suggests optimal tech stack and cloud solutions
  - 建议最优技术栈和云解决方案
  - Estimates development costs and timelines
  - 估算开发成本和时间线

- **Client Success Agent**: Marketing strategy leader
- **客户成功智能体**：市场战略负责人
  - Develops go-to-market strategies
  - 制定进入市场策略
  - Plans customer acquisition approaches
  - 规划客户获取方法
  - Coordinates with product team
  - 与产品团队协调

### Custom Tools
### 自定义工具

The agency uses specialized tools built with OpenAI Schema for structured analysis:
该机构使用基于 `OpenAI Schema` 构建的专业工具进行结构化分析：

- **Analysis Tools**: AnalyzeProjectRequirements for market evaluation and analysis of startup idea
- **分析工具**：`AnalyzeProjectRequirements` 用于创业想法的市场评估和分析
- **Technical Tools**: CreateTechnicalSpecification for technical assessment
- **技术工具**：`CreateTechnicalSpecification` 用于技术评估

### 🤝 Multi-Agent Collaboration
### 🤝 多智能体协作

The agency coordinates five specialists through explicit communication flows:
该机构通过明确的沟通流协调五位专家：

- CEO drives strategic oversight across the team
- `CEO` 负责推动整个团队的战略监督
- CTO and Developer collaborate on implementation feasibility
- `CTO` 和开发者协作评估实施可行性
- Product and Client Success coordinate roadmap and go-to-market planning
- 产品与客户成功团队协调路线图和进入市场规划
- Each analysis is returned in a dedicated section in the Streamlit UI
- 每项分析都会在 `Streamlit UI` 的专用区域中返回

### 🔗 Agent Communication Flows
### 🔗 智能体沟通流

- CEO ↔️ All Agents (Strategic Oversight)
- `CEO` ↔️ 所有智能体（战略监督）
- CTO ↔️ Developer (Technical Implementation)
- `CTO` ↔️ 开发者（技术实施）
- Product Manager ↔️ Client Success Manager (Go-to-Market Strategy)
- 产品经理 ↔️ 客户成功经理（进入市场策略）
- Product Manager ↔️ Developer (Feature Implementation)
- 产品经理 ↔️ 开发者（功能实施）
- (and more!)
- （以及更多！）

## How to Run
## 如何运行

Follow the steps below to set up and run the application:
按照以下步骤设置并运行应用：

Before anything else, Please get your OpenAI API Key here: https://platform.openai.com/api-keys
在开始之前，请先在这里获取你的 `OpenAI API Key`：https://platform.openai.com/api-keys

1. **Clone the Repository**:
1. **克隆仓库**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_services_agency
   ```

2. **Install the dependencies**:
2. **安装依赖**：
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
3. **运行 Streamlit 应用**：
    ```bash
    streamlit run agency.py
    ```

4. **Enter your OpenAI API Key** in the sidebar when prompted and start analyzing your startup idea!
4. 出现提示时，在侧边栏输入你的 **`OpenAI API Key`**，然后开始分析你的创业想法！
