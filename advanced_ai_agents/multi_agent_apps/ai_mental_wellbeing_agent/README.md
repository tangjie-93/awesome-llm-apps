# AI Mental Wellbeing Agent Team 🧠
# `AI` 心理健康智能体团队 🧠

The AI Mental Wellbeing Agent Team is a supportive mental health assessment and guidance system powered by [AG2](https://github.com/ag2ai/ag2?tab=readme-ov-file)(formerly AutoGen)'s AI Agent framework. This app provides personalized mental health support through the coordination of specialized AI agents, each focusing on different aspects of mental health care based on user inputs such as emotional state, stress levels, sleep patterns, and current symptoms. This is built on AG2's new swarm feature run through initiate_swarm_chat() method.
`AI` 心理健康智能体团队是一个由 [AG2](https://github.com/ag2ai/ag2?tab=readme-ov-file)（原 `AutoGen`）的 `AI Agent` 框架驱动的支持型心理健康评估和指导系统。该应用通过协调专门的 `AI` 智能体来提供个性化心理健康支持，每个智能体都会根据用户输入的情绪状态、压力水平、睡眠模式和当前症状等信息，关注心理健康护理的不同方面。它基于 `AG2` 新的 `swarm` 功能构建，并通过 `initiate_swarm_chat()` 方法运行。

## Features
## 功能

- **Specialized Mental Wellbeing Support Team**
- **专业心理健康支持团队**
    - 🧠 **Assessment Agent**: Analyzes emotional state and psychological needs with clinical precision and empathy
    - 🧠 **评估智能体**：以临床级精确度和同理心分析情绪状态与心理需求
    - 🎯 **Action Agent**: Creates immediate action plans and connects users with appropriate resources
    - 🎯 **行动智能体**：创建即时行动计划，并将用户连接到合适资源
    - 🔄 **Follow-up Agent**: Designs long-term support strategies and prevention plans
    - 🔄 **跟进智能体**：设计长期支持策略和预防计划

- **Comprehensive Mental Wellbeing Support**:
- **全面心理健康支持**：
  - Detailed psychological assessment
  - 详细心理评估
  - Immediate coping strategies
  - 即时应对策略
  - Resource recommendations
  - 资源推荐
  - Long-term support planning
  - 长期支持规划
  - Crisis prevention strategies
  - 危机预防策略
  - Progress monitoring systems
  - 进展监测系统

- **Customizable Input Parameters**:
- **可自定义输入参数**：
  - Current emotional state
  - 当前情绪状态
  - Sleep patterns
  - 睡眠模式
  - Stress levels
  - 压力水平
  - Support system information
  - 支持系统信息
  - Recent life changes
  - 近期生活变化
  - Current symptoms
  - 当前症状

- **Interactive Results**: 
- **交互式结果**：
   - Real-time assessment summaries
   - 实时评估摘要
   - Detailed recommendations in expandable sections
   - 可展开区域中的详细建议
   - Clear action steps and resources
   - 清晰的行动步骤和资源
   - Long-term support strategies
   - 长期支持策略

## How to Run
## 如何运行

Follow these steps to set up and run the application:
按照以下步骤设置并运行该应用：

1. **Clone the Repository**:
1. **克隆仓库**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/ai_mental_wellbeing_agent
   ```

2. **Install Dependencies**:
2. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

3. **Create Environment File**:
3. **创建环境文件**：
   Create a `.env` file in the project directory:
   在项目目录中创建 `.env` 文件：
   ```bash
   echo "AUTOGEN_USE_DOCKER=0" > .env
   ```
   This disables Docker requirement for code execution in AutoGen.
   这会关闭 `AutoGen` 中代码执行对 `Docker` 的要求。

4. **Set Up OpenAI API Key**:
4. **设置 `OpenAI API Key`**：
   - Obtain an OpenAI API key from [OpenAI's platform](https://platform.openai.com)
   - 从 [OpenAI 平台](https://platform.openai.com)获取 `OpenAI API key`
   - You'll input this key in the app's sidebar when running
   - 运行时，你会在应用侧边栏中输入此密钥

5. **Run the Streamlit App**:
5. **运行 `Streamlit` 应用**：
   ```bash
   streamlit run ai_mental_wellbeing_agent.py
   ```


## ⚠️ Important Notice
## ⚠️ 重要提示

This application is a supportive tool and does not replace professional mental health care. If you're experiencing thoughts of self-harm or severe crisis:
该应用是支持型工具，不能替代专业心理健康护理。如果你正在经历自伤想法或严重危机：

- Call National Crisis Hotline: 988
- 拨打全国危机热线：988
- Call Emergency Services: 911
- 拨打紧急服务电话：911
- Seek immediate professional help
- 立即寻求专业帮助
