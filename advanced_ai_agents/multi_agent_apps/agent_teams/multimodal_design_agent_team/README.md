# Multimodal AI Design Agent Team
# 多模态 `AI` 设计代理团队

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-multimodal-ai-agent-design-team) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-multimodal-ai-agent-design-team)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

A Streamlit application that provides comprehensive design analysis using a team of specialized AI agents powered by Google's Gemini model. 
一个 `Streamlit` 应用，使用由 `Google Gemini` 模型驱动的专业 `AI Agent` 团队提供全面的设计分析。

This application leverages multiple specialized AI agents to provide comprehensive analysis of UI/UX designs of your product and your competitors, combining visual understanding, user experience evaluation, and market research insights.
该应用利用多个专业 `AI Agent` 对你和竞争对手产品的 `UI/UX` 设计进行全面分析，结合视觉理解、用户体验评估和市场研究洞察。

## Features
## 功能

- **Specialized Design AI Agent Team**
- **专业设计 `AI Agent` 团队**

   - 🎨 **Visual Design Agent**: Evaluates design elements, patterns, color schemes, typography, and visual hierarchy
   - 🎨 **`Visual Design Agent`**：评估设计元素、模式、配色方案、字体排版和视觉层级
   - 🔄 **UX Analysis Agent**: Assesses user flows, interaction patterns, usability, and accessibility
   - 🔄 **`UX Analysis Agent`**：评估用户流程、交互模式、可用性和可访问性
   - 📊 **Market Analysis Agent**: Provides market insights, competitor analysis, and positioning recommendations
   - 📊 **`Market Analysis Agent`**：提供市场洞察、竞品分析和定位建议
   
- **Multiple Analysis Types**: Choose from Visual Design, UX, and Market Analysis
- **多种分析类型**：可选择 `Visual Design`、`UX` 和 `Market Analysis`
- **Comparative Analysis**: Upload competitor designs for comparative insights
- **对比分析**：上传竞品设计以获取对比洞察
- **Customizable Focus Areas**: Select specific aspects for detailed analysis
- **可自定义关注领域**：选择特定方面进行详细分析
- **Context-Aware**: Provide additional context for more relevant insights
- **上下文感知**：提供额外上下文以获得更相关的洞察
- **Real-time Processing**: Get instant analysis with progress indicators
- **实时处理**：通过进度指示器即时获取分析
- **Structured Output**: Receive well-organized, actionable insights
- **结构化输出**：获得组织清晰、可执行的洞察

## How to Run
## 运行方法

1. **Setup Environment**
1. **设置环境**
   ```bash
   # Clone the repository
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_design_agent_team

   # Create and activate virtual environment (optional)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Get API Key**
2. **获取 `API Key`**
   - Visit [Google AI Studio](https://aistudio.google.com/apikey)
   - 访问 [Google AI Studio](https://aistudio.google.com/apikey)
   - Generate an API key
   - 生成一个 `API key`

3. **Run the Application**
3. **运行应用**
   ```bash
   streamlit run design_agent_team.py
   ```

4. **Use the Application**
4. **使用应用**
   - Enter your Gemini API key in the sidebar
   - 在侧边栏输入你的 `Gemini API key`
   - Upload design files (supported formats: JPG, JPEG, PNG)
   - 上传设计文件（支持格式：`JPG`、`JPEG`、`PNG`）
   - Select analysis types and focus areas
   - 选择分析类型和关注领域
   - Add context if needed
   - 如有需要，添加上下文
   - Click "Run Analysis" to get insights
   - 点击 "Run Analysis" 获取洞察


## Technical Stack
## 技术栈

- **Frontend**: Streamlit
- **前端**：`Streamlit`
- **AI Model**: Google Gemini 2.0
- **`AI` 模型**：`Google Gemini 2.0`
- **Image Processing**: Pillow
- **图像处理**：`Pillow`
- **Market Research**: DuckDuckGo Search API
- **市场研究**：`DuckDuckGo Search API`
- **Framework**: Phidata for agent orchestration
- **框架**：用于代理编排的 `Phidata`

## Tips for Best Results
## 最佳效果提示

- Upload clear, high-resolution images
- 上传清晰的高分辨率图片
- Include multiple views/screens for better context
- 包含多个视图或屏幕，以提供更好的上下文
- Add competitor designs for comparative analysis
- 添加竞品设计用于对比分析
- Provide specific context about your target audience
- 提供关于目标受众的具体上下文
