# AI Game Design Agent Team 🎮
# `AI` 游戏设计智能体团队 🎮

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-game-design-agent-team) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-game-design-agent-team)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

The AI Game Design Agent Team is a collaborative game design system powered by [AG2](https://github.com/ag2ai/ag2?tab=readme-ov-file)(formerly AutoGen)'s AI Agent framework. This app generates comprehensive game concepts through the coordination of multiple specialized AI agents, each focusing on different aspects of game design based on user inputs such as game type, target audience, art style, and technical requirements. This is built on AG2's new swarm feature run through initiate_chat() method.
`AI` 游戏设计智能体团队是一个协作式游戏设计系统，由 [AG2](https://github.com/ag2ai/ag2?tab=readme-ov-file)（前身为 `AutoGen`）的 `AI Agent` 框架驱动。该应用会协调多个专门的 `AI` 智能体，根据用户输入的游戏类型、目标受众、美术风格和技术需求等信息，生成全面的游戏概念。它基于 `AG2` 新的 `swarm` 功能构建，并通过 `initiate_chat()` 方法运行。

## Features
## 功能

- **Specialized Game Design Agent Team**
- **专门的游戏设计智能体团队**

  - 🎭 **Story Agent**: Specializes in narrative design and world-building, including character development, plot arcs, dialogue writing, and lore creation
  - 🎭 **`Story Agent`**：专注于叙事设计和世界构建，包括角色塑造、剧情弧线、对白写作和背景设定创作
  - 🎮 **Gameplay Agent**: Focuses on game mechanics and systems design, including player progression, combat systems, resource management, and balancing
  - 🎮 **`Gameplay Agent`**：专注于游戏机制和系统设计，包括玩家成长、战斗系统、资源管理和平衡性
  - 🎨 **Visuals Agent**: Handles art direction and audio design, covering UI/UX, character/environment art style, sound effects, and music composition
  - 🎨 **`Visuals Agent`**：处理美术指导和音频设计，涵盖 `UI/UX`、角色/环境美术风格、音效和音乐创作
  - ⚙️ **Tech Agent**: Provides technical architecture and implementation guidance, including engine selection, optimization strategies, networking requirements, and development roadmap
  - ⚙️ **`Tech Agent`**：提供技术架构和实现指导，包括引擎选择、优化策略、联网需求和开发路线图
  - 🎯 **Task Agent**: Coordinates between all specialized agents and ensures cohesive integration of different game aspects
  - 🎯 **`Task Agent`**：协调所有专门智能体，确保不同游戏方面能够一致整合

- **Comprehensive Game Design Outputs**:
- **全面的游戏设计输出**：

  - Detailed narrative and world-building elements
  - 详细的叙事和世界构建元素
  - Core gameplay mechanics and systems
  - 核心玩法机制和系统
  - Visual and audio direction
  - 视觉和音频方向
  - Technical specifications and requirements
  - 技术规格和需求
  - Development timeline and budget considerations
  - 开发时间线和预算考量
  - Coherent game design from the team.
  - 团队产出的连贯游戏设计。

- **Customizable Input Parameters**:
- **可自定义输入参数**：

  - Game type and target audience
  - 游戏类型和目标受众
  - Art style and visual preferences
  - 美术风格和视觉偏好
  - Platform requirements
  - 平台需求
  - Development constraints (time, budget)
  - 开发约束（时间、预算）
  - Core mechanics and gameplay features
  - 核心机制和玩法功能

- **Interactive Results**:
- **交互式结果**：
  - Quick show of game design ideas from each agent
  - 快速展示每个智能体的游戏设计想法
  - Detailed results are presented in expandable sections for easy navigation and reference
  - 详细结果会在可展开区域中展示，便于导航和参考

## How to Run
## 如何运行

Follow these steps to set up and run the application:
按照以下步骤设置并运行该应用：

1. **Clone the Repository**:
1. **克隆仓库**：

   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_game_design_agent_team
   ```

2. **Install Dependencies**:
2. **安装依赖**：

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**:
3. **设置 `OpenAI API Key`**：

   - Obtain an OpenAI API key from [OpenAI's platform](https://platform.openai.com)
   - 从 [OpenAI's platform](https://platform.openai.com) 获取 `OpenAI API key`
   - You'll input this key in the app's sidebar when running
   - 运行时你将在应用侧边栏输入该密钥

4. **Run the Streamlit App**:
4. **运行 `Streamlit` 应用**：

   ```bash
   streamlit run game_design_agent_team.py
   ```

## Usage
## 使用方式

1. Enter your OpenAI API key in the sidebar
1. 在侧边栏输入你的 `OpenAI API key`
2. Fill in the game details:
2. 填写游戏详情：
   - Background vibe and setting
   - 背景氛围和设定
   - Game type and target audience
   - 游戏类型和目标受众
   - Visual style preferences
   - 视觉风格偏好
   - Technical requirements
   - 技术需求
   - Development constraints
   - 开发约束
3. Click "Generate Game Concept" to receive comprehensive design documentation from all agents
3. 点击 `Generate Game Concept`，接收所有智能体生成的综合设计文档
4. Review the outputs in the expandable sections for each aspect of game design
4. 在每个游戏设计方面的可展开区域中查看输出
