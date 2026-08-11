# 🎨 🍌 Multimodal UI/UX Feedback Agent Team with Nano Banana
# 🎨 🍌 使用 `Nano Banana` 的多模态 `UI/UX` 反馈代理团队

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-ui-ux-feedback-agent-team-with-nano-banana) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-ui-ux-feedback-agent-team-with-nano-banana)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

A sophisticated multi-agent system built with Google ADK that analyzes landing page designs, provides expert UI/UX feedback, and automatically generates improved versions using Gemini 2.5 Flash's multimodal capabilities.
一个基于 `Google ADK` 构建的复杂多代理系统，可分析落地页设计、提供专家级 `UI/UX` 反馈，并使用 `Gemini 2.5 Flash` 的多模态能力自动生成改进版本。

## Features
## 功能

- **👁️ Visual AI Analysis**: Upload landing page screenshots - agents automatically analyze layout, typography, colors, and UX patterns
- **👁️ 视觉 `AI` 分析**：上传落地页截图，代理会自动分析布局、字体排版、颜色和 `UX` 模式
- **🎯 Expert Feedback**: Comprehensive critique covering visual hierarchy, accessibility, conversion optimization, and design best practices
- **🎯 专家反馈**：提供全面评审，覆盖视觉层级、可访问性、转化优化和设计最佳实践
- **✨ Automatic Improvements**: Generates improved landing page designs incorporating all recommendations
- **✨ 自动改进**：生成纳入全部建议的改进版落地页设计
- **📊 Detailed Reports**: Creates comprehensive reports summarizing issues and improvements made
- **📊 详细报告**：创建综合报告，总结发现的问题和已做的改进
- **🤖 Multi-Agent Orchestration**: Demonstrates Coordinator/Dispatcher + Sequential Pipeline patterns
- **🤖 多代理编排**：演示 `Coordinator/Dispatcher` + `Sequential Pipeline` 模式
- **♻️ Iterative Refinement**: Edit and refine generated designs based on additional feedback
- **♻️ 迭代优化**：根据额外反馈编辑并优化生成的设计
- **♿ Accessibility Focus**: WCAG compliance checks and recommendations
- **♿ 可访问性重点**：提供 `WCAG` 合规检查和建议

## How It Works
## 工作原理

The system uses a **Coordinator/Dispatcher pattern** with three specialized agents working in sequence:
系统使用 **`Coordinator/Dispatcher` 模式**，由三个专业代理按顺序协作：

### The Team
### 团队成员

1. **UI Critic Agent** 🎨
1. **`UI Critic Agent`** 🎨
   - Analyzes landing page design using Gemini 2.5 Flash's vision capabilities
   - 使用 `Gemini 2.5 Flash` 的视觉能力分析落地页设计
   - Can see and analyze uploaded images directly (no manual tool calls needed)
   - 可直接查看并分析上传图片（无需手动调用工具）
   - Evaluates layout, visual hierarchy, typography, color scheme, and CTA effectiveness
   - 评估布局、视觉层级、字体排版、配色方案和 `CTA` 有效性
   - Identifies critical issues and improvement opportunities
   - 识别关键问题和改进机会
   - Provides detailed scores across multiple dimensions
   - 从多个维度提供详细评分
   - References specific elements and provides actionable feedback
   - 引用具体元素并提供可执行反馈

2. **Design Strategist Agent** 📐
2. **`Design Strategist Agent`** 📐
   - Creates comprehensive improvement plan based on analysis
   - 基于分析创建全面的改进计划
   - Specifies exact colors (with hex codes), typography, and spacing
   - 指定精确颜色（含十六进制代码）、字体排版和间距
   - Prioritizes changes for maximum impact
   - 按最大影响力对改动排序
   - Ensures accessibility compliance (WCAG AA)
   - 确保符合可访问性标准（`WCAG AA`）
   - Considers mobile responsiveness
   - 考虑移动端响应式表现

3. **Visual Implementer Agent** 🚀
3. **`Visual Implementer Agent`** 🚀
   - Generates improved landing page design using Gemini 2.5 Flash
   - 使用 `Gemini 2.5 Flash` 生成改进版落地页设计
   - Implements all recommendations from the analysis
   - 落实分析中的全部建议
   - Creates high-quality, professional designs
   - 创建高质量、专业的设计
   - Generates comprehensive improvement report
   - 生成全面的改进报告
   - Maintains version history
   - 维护版本历史

## Quick Start
## 快速开始

### 1. Clone the repository
### 1. 克隆仓库
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_uiux_feedback_agent_team
```

### 2. Install dependencies
### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
### 3. 设置你的 `API key`
```bash
export GOOGLE_API_KEY="your_gemini_api_key"
```

Or create a `.env` file:
或创建 `.env` 文件：

```
GOOGLE_API_KEY=your_gemini_api_key
```

### 4. Launch ADK Web
### 4. 启动 `ADK Web`
```bash
cd advanced_ai_agents/multi_agent_apps/agent_teams
adk web
```

### 5. Open browser
### 5. 打开浏览器

Navigate to the ADK Web interface and select **multimodal_uiux_feedback_agent_team**
导航到 `ADK Web` 界面并选择 **`multimodal_uiux_feedback_agent_team`**

## Tools & Capabilities
## 工具和能力

### Core Tools
### 核心工具

- **Direct Vision Analysis**: Agents can see and analyze uploaded images automatically (no tool needed)
- **直接视觉分析**：代理可以自动查看并分析上传图片（无需工具）
- **edit_landing_page_image**: Refine existing designs based on feedback
- **`edit_landing_page_image`**：根据反馈优化现有设计
- **generate_improved_landing_page**: Create new improved designs from scratch
- **`generate_improved_landing_page`**：从零创建新的改进版设计
- **google_search**: Research UI/UX trends and best practices
- **`google_search`**：研究 `UI/UX` 趋势和最佳实践

### Features
### 特性

- **Native Vision Capabilities**: Agents automatically see uploaded images in conversations
- **原生视觉能力**：代理会在对话中自动查看上传图片
- **Versioned artifacts**: Automatic version tracking for all designs
- **版本化制品**：自动跟踪所有设计的版本
- **State management**: Maintains context across the conversation
- **状态管理**：在对话过程中保持上下文
- **Detailed prompts**: Generates ultra-specific prompts for high-quality results
- **详细提示词**：生成极其具体的提示词，以获得高质量结果
- **Sequential Processing**: Each agent builds on previous agent's analysis
- **顺序处理**：每个代理都基于前一个代理的分析继续工作

## Multi-Agent Architecture
## 多代理架构

```
Coordinator (Root Agent)
    ├── Info Agent (general Q&A)
    ├── Design Editor (iterative refinements)
    └── Analysis Pipeline (Sequential)
          ├── UI Critic (visual analysis & feedback)
          ├── Design Strategist (improvement planning)
          └── Visual Implementer (generate improved design + report)
```


## Best Practices for Users
## 用户最佳实践

### Getting Better Results
### 获取更好结果

1. **Use High-Quality Screenshots**
1. **使用高质量截图**
   - Full-page captures preferred
   - 优先使用整页截图
   - Minimum 1920x1080 resolution
   - 最低分辨率为 `1920x1080`
   - Clear, uncompressed images
   - 图片应清晰且未压缩

2. **Provide Context**
2. **提供上下文**
   - Mention target audience (B2B, B2C, enterprise, consumer)
   - 说明目标受众（`B2B`、`B2C`、企业、消费者）
   - Share goals (conversions, awareness, engagement)
   - 分享目标（转化、认知、互动）
   - Specify any constraints or requirements
   - 指明任何限制或要求

3. **Be Specific with Refinements**
3. **明确说明优化需求**
   - "Make the CTA button 20% larger with vibrant orange color"
   - “让 `CTA` 按钮放大 `20%`，并使用鲜亮的橙色”
   - vs "Make the button better"
   - 相比 "Make the button better"，上面的表达更具体

4. **Iterate Gradually**
4. **逐步迭代**
   - Make one category of changes at a time
   - 每次只修改一类问题
   - Review each version before requesting more changes
   - 在请求更多改动前先审查每个版本

### Common Use Cases
### 常见用例

- **Landing Page Audits**: Comprehensive analysis of existing pages
- **落地页审计**：对现有页面进行全面分析
- **Pre-Launch Review**: Get feedback before going live
- **上线前评审**：上线前获取反馈
- **A/B Testing Ideas**: Generate alternative designs to test
- **`A/B Testing` 思路**：生成可测试的替代设计
- **Competitive Analysis**: Compare your design to competitors
- **竞品分析**：将你的设计与竞争对手进行比较
- **Accessibility Audit**: Check WCAG compliance
- **可访问性审计**：检查 `WCAG` 合规性
- **Mobile Optimization**: Review mobile responsiveness
- **移动端优化**：评审移动端响应式表现
- **Conversion Optimization**: Improve CTA and user flow
- **转化优化**：改进 `CTA` 和用户流程

## Limitations
## 限制

- Image generation has inherent variability (run multiple times for options)
- 图像生成具有固有随机性（可多运行几次以获得不同选项）
- Complex interactions and animations cannot be fully captured
- 复杂交互和动画无法被完整捕捉
- Best suited for static landing page screenshots
- 最适合静态落地页截图
- Real code implementation requires manual development
- 真实代码实现需要手动开发
- Analysis focuses on visual design, not content quality or copy
- 分析重点是视觉设计，而不是内容质量或文案
