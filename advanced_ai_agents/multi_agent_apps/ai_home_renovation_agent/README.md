# 🏚️ 🍌 AI Home Renovation Planner Agent 
# 🏚️ 🍌 `AI` 家装规划代理

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-home-renovation-planner-agent-using-nano-banana) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-home-renovation-planner-agent-using-nano-banana)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

A multi-agent system built with Google ADK that analyzes photos of your space, creates personalized renovation plans, and generates photorealistic renderings using Gemini 3 Flash and Gemini 3 Pro's multimodal capabilities.
一个基于 `Google ADK` 构建的多代理系统，可分析空间照片、创建个性化装修计划，并使用 `Gemini 3 Flash` 和 `Gemini 3 Pro` 的多模态能力生成照片级真实感效果图。

## Features
## 功能

- **🔍 Smart Image Analysis**: Upload room photos and inspiration images - agent automatically detects and analyzes them
- **🔍 智能图像分析**：上传房间照片和灵感图片，代理会自动检测并分析
- **🎨 Photorealistic Rendering**: Generates professional-quality images of your renovated space using Gemini 3 Pro
- **🎨 照片级真实感渲染**：使用 `Gemini 3 Pro` 生成专业质量的装修后空间图片
- **💰 Budget-Aware Planning**: Tailors recommendations to your budget constraints
- **💰 预算感知规划**：根据你的预算限制定制建议
- **📊 Complete Roadmap**: Provides timeline, budget breakdown, contractor list, and action checklist
- **📊 完整路线图**：提供时间线、预算拆分、承包商清单和行动检查清单
- **🤖 Multi-Agent Orchestration**: Demonstrates Coordinator/Dispatcher + Sequential Pipeline patterns
- **🤖 多代理编排**：演示 `Coordinator/Dispatcher` + `Sequential Pipeline` 模式
- **✏️ Iterative Refinement**: Edit generated renderings based on feedback
- **✏️ 迭代优化**：根据反馈编辑生成的效果图

## How It Works
## 工作原理

The system uses a **Coordinator/Dispatcher pattern** with three specialized agents:
系统使用 **`Coordinator/Dispatcher` 模式**，包含三个专业代理：

1. **Visual Assessor** 📸
1. **`Visual Assessor`** 📸
   - Analyzes uploaded room photos (layout, condition, dimensions)
   - 分析上传的房间照片（布局、状态、尺寸）
   - Extracts style from inspiration images
   - 从灵感图片中提取风格
   - Estimates costs and identifies improvement opportunities
   - 估算成本并识别改进机会

2. **Design Planner** 🎨
2. **`Design Planner`** 🎨
   - Creates budget-appropriate design plans
   - 创建符合预算的设计计划
   - Specifies exact materials, colors, and fixtures
   - 指定精确材料、颜色和固定装置
   - Prioritizes high-impact changes
   - 优先安排高影响力改动

3. **Project Coordinator** 🏗️
3. **`Project Coordinator`** 🏗️
   - Generates comprehensive renovation roadmap
   - 生成全面的装修路线图
   - Creates photorealistic rendering of renovated space
   - 创建装修后空间的照片级真实感效果图
   - Provides budget breakdown, timeline, and action steps
   - 提供预算拆分、时间线和行动步骤

## Quick Start
## 快速开始

1. **Clone the repository**
1. **克隆仓库**
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent
   ```

2. **Install dependencies**
2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
3. **设置你的 `API key`**
   ```bash
   export GOOGLE_API_KEY="your_gemini_api_key"
   ```
   Or create a `.env` file:
   或创建 `.env` 文件：
   ```
   GOOGLE_API_KEY=your_gemini_api_key
   ```

4. **Launch ADK Web** 
4. **启动 `ADK Web`**
   ```bash
   cd multi_agent_apps
   adk web
   ```

5. **Open browser** and select "ai_home_renovation_agent"
5. **打开浏览器** 并选择 "ai_home_renovation_agent"

## Usage Examples
## 使用示例

### Scenario 1: Current Room + Budget
### 场景 1：当前房间 + 预算
```
[Upload photo of your kitchen]
"What can I improve here with a $5k budget?"
```

→ Agent analyzes your space, suggests budget-friendly improvements, generates rendering
→ 代理会分析你的空间，建议预算友好的改进，并生成效果图

### Scenario 2: Room + Inspiration
### 场景 2：房间 + 灵感图
```
[Upload photo 1: your kitchen]
[Upload photo 2: Pinterest inspiration]
"Transform my kitchen to look like this. What's the cost?"
```

→ Agent extracts style from inspiration, applies to your room, provides budget + rendering
→ 代理会从灵感图中提取风格，将其应用到你的房间，并提供预算和效果图

### Scenario 3: Text Only
### 场景 3：仅文本
```
"Renovate my 10x12 kitchen with oak cabinets and laminate counters. 
Want modern farmhouse style with white shaker cabinets. Budget: $30k"
```

→ Agent creates design plan and generates rendering from description
→ 代理会根据描述创建设计计划并生成效果图

### Scenario 4: Iterative Refinement
### 场景 4：迭代优化
```
[After initial rendering]
"Make the cabinets cream instead of white"
"Add pendant lights over the island"
"Change flooring to lighter oak"
```

→ Agent refines the rendering with your feedback
→ 代理会根据你的反馈优化效果图

## Sample Prompts
## 示例提示词

- "I want to renovate my small galley kitchen. It's 8x12 feet, has oak cabinets from the 90s. I love modern farmhouse style. Budget: $25k"
- “我想翻新我的小型走廊式厨房。它是 `8x12` 英尺，有 `90` 年代的橡木橱柜。我喜欢现代农舍风格。预算：`$25k`”
- "My master bathroom is tiny (5x8) with a cramped tub. I want a spa-like retreat with walk-in shower. Budget: $15k"
- “我的主卫很小（`5x8`），浴缸很拥挤。我想要一个带步入式淋浴的水疗式休憩空间。预算：`$15k`”
- "Transform my boring bedroom into a cozy retreat. Thinking accent wall, new flooring. Budget: $12k"
- “把我乏味的卧室改造成舒适的休憩空间。考虑做重点墙和新地板。预算：`$12k`”

## Tools & Capabilities
## 工具和能力

- **google_search**: Finds renovation costs, materials, and trends
- **`google_search`**：查找装修成本、材料和趋势
- **estimate_renovation_cost**: Calculates costs by room type and scope
- **`estimate_renovation_cost`**：按房间类型和范围计算成本
- **calculate_timeline**: Estimates project duration
- **`calculate_timeline`**：估算项目周期
- **generate_renovation_rendering**: Creates photorealistic renderings
- **`generate_renovation_rendering`**：创建照片级真实感效果图
- **edit_renovation_rendering**: Refines renderings based on feedback
- **`edit_renovation_rendering`**：根据反馈优化效果图
- **Versioned artifacts**: Automatic version tracking for all renderings
- **版本化制品**：自动跟踪所有效果图版本

## Multi-Agent Pattern
## 多代理模式

Demonstrates **Coordinator/Dispatcher + Sequential Pipeline**:
演示 **`Coordinator/Dispatcher` + `Sequential Pipeline`**：

```
Coordinator (Root Agent)
    ├── Info Agent (quick Q&A)
    └── Planning Pipeline (Sequential)
          ├── Visual Assessor (image analysis)
          ├── Design Planner (specifications)
          └── Project Coordinator (rendering + roadmap)
```

**Why this pattern?**
**为什么使用这种模式？**

- Efficient: Only runs workflows that are needed
- 高效：只运行需要的工作流
- Modular: Each agent has clear responsibilities
- 模块化：每个代理都有清晰职责
- Scalable: Easy to add new features
- 可扩展：易于添加新功能
- Production-ready: Real-world agentic system pattern
- 生产就绪：真实世界的代理系统模式
