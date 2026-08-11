# AI Financial Coach Agent with Google ADK 💰
# 使用 `Google ADK` 的 `AI` 财务教练代理 💰

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-multi-agent-personal-finance-coach) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-multi-agent-personal-finance-coach)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

The **AI Financial Coach** is a personalized financial advisor powered by Google's ADK (Agent Development Kit) framework. This app provides comprehensive financial analysis and recommendations based on user inputs including income, expenses, debts, and financial goals.
**`AI Financial Coach`** 是一个个性化财务顾问，由 `Google ADK`（`Agent Development Kit`）框架提供支持。该应用会基于用户输入的收入、支出、债务和财务目标，提供全面的财务分析和建议。

## Features
## 功能

- **Multi-Agent Financial Analysis System**
- **多代理财务分析系统**
    - Budget Analysis Agent: Analyzes spending patterns and recommends optimizations
    - `Budget Analysis Agent`：分析支出模式并推荐优化方案
    - Savings Strategy Agent: Creates personalized savings plans and emergency fund strategies
    - `Savings Strategy Agent`：创建个性化储蓄计划和应急基金策略
    - Debt Reduction Agent: Develops optimized debt payoff strategies using avalanche and snowball methods
    - `Debt Reduction Agent`：使用雪崩法和雪球法制定优化的债务偿还策略

- **Expense Analysis**:
- **支出分析**：
  - Supports both CSV upload and manual expense entry
  - 同时支持 `CSV` 上传和手动录入支出
  - CSV transaction analysis with date, category, and amount tracking
  - 对 `CSV` 交易进行分析，并跟踪日期、类别和金额
  - Visual breakdown of spending by category
  - 按类别可视化拆分支出
  - Automated expense categorization and pattern detection
  - 自动支出分类和模式检测

- **Savings Recommendations**:
- **储蓄建议**：
  - Emergency fund sizing and building strategies
  - 应急基金规模测算和建立策略
  - Custom savings allocations across different goals
  - 针对不同目标自定义储蓄分配
  - Practical automation techniques for consistent saving
  - 用于持续储蓄的实用自动化技巧
  - Progress tracking and milestone recommendations
  - 进度跟踪和里程碑建议

- **Debt Management**:
- **债务管理**：
  - Multiple debt handling with interest rate optimization
  - 处理多笔债务并优化利率策略
  - Comparison between avalanche and snowball methods
  - 对比雪崩法和雪球法
  - Visual debt payoff timeline and interest savings analysis
  - 可视化债务偿还时间线和利息节省分析
  - Actionable debt reduction recommendations
  - 可执行的债务减少建议

- **Interactive Visualizations**:
- **交互式可视化**：
  - Pie charts for expense breakdown
  - 用于支出拆分的饼图
  - Bar charts for income vs. expenses
  - 用于收入与支出对比的柱状图
  - Debt comparison graphs
  - 债务对比图
  - Progress tracking metrics
  - 进度跟踪指标


## How to Run
## 运行方法

Follow the steps below to set up and run the application:
按照以下步骤设置并运行应用：

1. **Get API Key**:
1. **获取 `API Key`**：
   - Get a free Gemini API Key from Google AI Studio: https://aistudio.google.com/apikey
   - 从 `Google AI Studio` 获取免费的 `Gemini API Key`：https://aistudio.google.com/apikey
   - Create a `.env` file in the project root and add your API key:
   - 在项目根目录创建 `.env` 文件并添加你的 `API key`：
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

2. **Clone the Repository**:
2. **克隆仓库**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent/
   ```

3. **Install Dependencies**:
3. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**:
4. **运行 `Streamlit` 应用**：
   ```bash
   streamlit run ai_financial_coach_agent.py
   ```

## CSV File Format
## `CSV` 文件格式

The application accepts CSV files with the following required columns:
该应用接受包含以下必需列的 `CSV` 文件：

- `Date`: Transaction date in YYYY-MM-DD format
- `Date`：交易日期，格式为 `YYYY-MM-DD`
- `Category`: Expense category
- `Category`：支出类别
- `Amount`: Transaction amount (supports currency symbols and comma formatting)
- `Amount`：交易金额（支持货币符号和逗号格式）

Example:
示例：

```csv
Date,Category,Amount
2024-01-01,Housing,1200.00
2024-01-02,Food,150.50
2024-01-03,Transportation,45.00
```

A template CSV file can be downloaded directly from the application's sidebar.
可直接从应用侧边栏下载模板 `CSV` 文件。
