# 🎮 AI 3D PyGame Visualizer with DeepSeek R1
# 🎮 使用 `DeepSeek R1` 的 `AI 3D PyGame` 可视化器

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-3d-pygame-visualizer-with-deepseek-r1) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-3d-pygame-visualizer-with-deepseek-r1)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

This Project demonstrates R1's code capabilities with a PyGame code generator and visualizer with browser use. The system uses DeepSeek for reasoning, OpenAI for code extraction, and browser automation agents to visualize the code on Trinket.io.
该项目通过带浏览器使用能力的 `PyGame` 代码生成器和可视化器，展示 `R1` 的代码能力。系统使用 `DeepSeek` 进行推理，使用 `OpenAI` 提取代码，并通过浏览器自动化智能体在 `Trinket.io` 上可视化代码。

### Features
### 功能

- Generates PyGame code from natural language descriptions
- 根据自然语言描述生成 `PyGame` 代码
- Uses DeepSeek Reasoner for code logic and explanation
- 使用 `DeepSeek Reasoner` 处理代码逻辑和解释
- Extracts clean code using OpenAI GPT-4o
- 使用 `OpenAI GPT-4o` 提取干净的代码
- Automates code visualization on Trinket.io using browser agents
- 使用浏览器智能体在 `Trinket.io` 上自动完成代码可视化
- Provides a streamlined Streamlit interface
- 提供简洁的 `Streamlit` 界面
- Multi-agent system for handling different tasks (navigation, coding, execution, viewing)
- 使用多智能体系统处理不同任务（导航、编码、执行、查看）

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
1. 克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/advanced_ai_agents/autonomous_game_playing_agent_apps/ai_3dpygame_r1
```

2. Install the required dependencies:
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```

3. Create a `.env` file
3. 创建 `.env` 文件

```env
DEEPSEEK_API_KEY=your_deepseek_api_key
OPENAI_API_KEY=your_openai_api_key
OPENAI_BASE_URL=https://your-proxy-domain/v1
```

4. Get your API Keys
4. 获取你的 `API Keys`

- Sign up for [DeepSeek](https://platform.deepseek.com/) and obtain your API key
- 注册 [DeepSeek](https://platform.deepseek.com/) 并获取你的 `API key`
- Sign up for [OpenAI](https://platform.openai.com/) and obtain your API key
- 注册 [OpenAI](https://platform.openai.com/) 并获取你的 `API key`
- If your `OpenAI` access uses a proxy or gateway, put its `base URL` in `OPENAI_BASE_URL`
- 如果你的 `OpenAI` 访问走中转站或网关，把它的 `base URL` 填到 `OPENAI_BASE_URL`

5. Run the AI PyGame Visualizer
5. 运行 `AI PyGame` 可视化器

```bash
streamlit run ai_3dpygame_r1.py
```

6. Browser use automatically opens your web browser and navigate to the URL provided in the console output to interact with the PyGame generator.
6. 浏览器使用功能会自动打开你的网页浏览器，并导航到控制台输出中提供的 `URL`，以便与 `PyGame` 生成器交互。

### How it works?
### 工作原理

1. **Query Processing:** User enters a natural language description of the desired PyGame visualization.
1. **查询处理：** 用户输入所需 `PyGame` 可视化的自然语言描述。
2. **Code Generation:**
2. **代码生成：**
   - DeepSeek Reasoner analyzes the query and provides detailed reasoning with code
   - `DeepSeek Reasoner` 分析查询，并提供包含代码的详细推理
   - OpenAI agent extracts clean, executable code from the reasoning
   - `OpenAI` 智能体从推理内容中提取干净、可执行的代码
3. **Visualization:**
3. **可视化：**
   - Browser agents automate the process of running code on Trinket.io
   - 浏览器智能体自动执行在 `Trinket.io` 上运行代码的流程
   - Multiple specialized agents handle different tasks:
   - 多个专门智能体处理不同任务：
     - Navigation to Trinket.io
     - 导航到 `Trinket.io`
     - Code input
     - 代码输入
     - Execution
     - 执行
     - Visualization viewing
     - 可视化查看
4. **User Interface:** Streamlit provides an intuitive interface for entering queries, viewing code, and managing the visualization process.
4. **用户界面：** `Streamlit` 提供直观界面，用于输入查询、查看代码并管理可视化流程。
