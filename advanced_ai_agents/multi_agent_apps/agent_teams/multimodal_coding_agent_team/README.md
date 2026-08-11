# 💻 Multimodal AI Coding Agent Team with o3-mini and Gemini
# 💻 使用 `o3-mini` 和 `Gemini` 的多模态 `AI` 编码代理团队

An AI Powered Streamlit application that serves as your personal coding assistant, powered by multiple Agents built on the new o3-mini model. You can also upload an image of a coding problem or describe it in text, and the AI agent will analyze, generate an optimal solution, and execute it in a sandbox environment.
一个由 `AI` 驱动的 `Streamlit` 应用，可作为你的个人编码助手；它由多个基于新 `o3-mini` 模型构建的 `Agent` 提供支持。你也可以上传编程题图片或用文字描述问题，`AI Agent` 会分析问题、生成最优解，并在沙盒环境中执行。

## Features
## 功能

#### Multi-Modal Problem Input
#### 多模态问题输入

- Upload images of coding problems (supports PNG, JPG, JPEG)
- 上传编程题图片（支持 `PNG`、`JPG`、`JPEG`）
- Type problems in natural language
- 用自然语言输入题目
- Automatic problem extraction from images
- 自动从图片中提取问题
- Interactive problem processing
- 交互式问题处理

#### Intelligent Code Generation
#### 智能代码生成

- Optimal solution generation with best time/space complexity
- 生成具有最佳时间和空间复杂度的最优解
- Clean, documented Python code output
- 输出整洁且带文档说明的 `Python` 代码
- Type hints and proper documentation
- 包含类型提示和适当文档
- Edge case handling
- 处理边界情况

#### Secure Code Execution
#### 安全代码执行

- Sandboxed code execution environment
- 沙盒化代码执行环境
- Real-time execution results
- 实时执行结果
- Error handling and explanations
- 错误处理与解释
- 30-second execution timeout protection
- `30` 秒执行超时保护

#### Multi-Agent Architecture
#### 多代理架构

- Vision Agent (Gemini-2.0-flash) for image processing
- 用于图像处理的 `Vision Agent`（`Gemini-2.0-flash`）
- Coding Agent (OpenAI- o3-mini) for solution generation
- 用于生成解法的 `Coding Agent`（`OpenAI` `o3-mini`）
- Execution Agent (OpenAI) for code running and result analysis
- 用于代码运行和结果分析的 `Execution Agent`（`OpenAI`）
- E2B Sandbox for secure code execution
- 用于安全代码执行的 `E2B Sandbox`

## How to Run
## 运行方法

Follow the steps below to set up and run the application:
按照以下步骤设置并运行应用：

- Get an OpenAI API key from: https://platform.openai.com/
- 从以下地址获取 `OpenAI API key`：https://platform.openai.com/
- Get a Google (Gemini) API key from: https://makersuite.google.com/app/apikey
- 从以下地址获取 `Google`（`Gemini`）`API key`：https://makersuite.google.com/app/apikey
- Get an E2B API key from: https://e2b.dev/docs/getting-started/api-key
- 从以下地址获取 `E2B API key`：https://e2b.dev/docs/getting-started/api-key

1. **Clone the Repository**
1. **克隆仓库**
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_coding_agent_team
   ```

2. **Install the dependencies**
2. **安装依赖**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**
3. **运行 `Streamlit` 应用**
    ```bash
    streamlit run ai_coding_agent_o3.py
    ```

4. **Configure API Keys**
4. **配置 `API Keys`**
   - Enter your API keys in the sidebar
   - 在侧边栏输入你的 `API keys`
   - All three keys (OpenAI, Gemini, E2B) are required for full functionality
   - 完整功能需要全部三个密钥（`OpenAI`、`Gemini`、`E2B`）

## Usage
## 使用方法

1. Upload an image of a coding problem OR type your problem description
1. 上传编程题图片，或输入你的问题描述
2. Click "Generate & Execute Solution"
2. 点击 "Generate & Execute Solution"
3. View the generated solution with full documentation
3. 查看带完整文档说明的生成解法
4. See execution results and any generated files
4. 查看执行结果和所有生成的文件
5. Review any error messages or execution timeouts
5. 查看所有错误消息或执行超时信息
