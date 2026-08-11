# 🧐 Agentic RAG with Reasoning
# 🧐 带推理能力的智能体式 `RAG`

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-agentic-rag-app-with-reasoning) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里阅读完整的分步教程](https://www.theunwindai.com/p/build-an-agentic-rag-app-with-reasoning)，学习如何通过详细的代码讲解、说明和最佳实践从零开始构建它。**

A sophisticated RAG system that demonstrates an AI agent's step-by-step reasoning process using Agno, Gemini and OpenAI. This implementation allows users to add web sources, ask questions, and observe the agent's thought process in real-time with reasoning capabilities.
这是一个复杂的 `RAG` 系统，使用 `Agno`、`Gemini` 和 `OpenAI` 演示 `AI` 智能体的分步推理过程。该实现允许用户添加 Web 来源、提出问题，并实时观察智能体带有推理能力的思考过程。


## Features
## 功能

1. Interactive Knowledge Base Management
1. 交互式知识库管理
- Add URLs dynamically for web content
- 动态添加 Web 内容的 `URL`
- Default knowledge source: MCP vs A2A Protocol article
- 默认知识来源：`MCP vs A2A Protocol` 文章
- Persistent vector database storage using LanceDB
- 使用 `LanceDB` 进行持久化向量数据库存储
- Session state tracking prevents duplicate URL loading
- 会话状态跟踪可防止重复加载 `URL`


2. Transparent Reasoning Process
2. 透明的推理过程
- Real-time display of the agent's thinking steps
- 实时显示智能体的思考步骤
- Side-by-side view of reasoning and final answer
- 并排查看推理过程和最终答案
- Clear visibility into the RAG process
- 清晰查看 `RAG` 流程


3. Advanced RAG Capabilities
3. 高级 `RAG` 能力
- Vector search using OpenAI embeddings for semantic matching
- 使用 `OpenAI` 嵌入进行向量搜索，以实现语义匹配
- Source attribution with citations
- 通过引用进行来源归属


## Agent Configuration
## 智能体配置

- Gemini 2.5 Flash for language processing
- 使用 `Gemini 2.5 Flash` 进行语言处理
- OpenAI embedding model for vector search
- 使用 `OpenAI` 嵌入模型进行向量搜索
- ReasoningTools for step-by-step analysis
- 使用 `ReasoningTools` 进行分步分析
- Customizable agent instructions
- 可自定义的智能体指令
- Default knowledge source: MCP vs A2A Protocol article
- 默认知识来源：`MCP vs A2A Protocol` 文章

## Prerequisites
## 前置条件

You'll need the following API keys:
你需要以下 `API key`：

1. Google API Key
1. `Google API Key`

- Sign up at [aistudio.google.com](https://aistudio.google.com/apikey)
- 在 [aistudio.google.com](https://aistudio.google.com/apikey) 注册
- Navigate to API Keys section
- 前往 `API Keys` 部分
- Create a new API key
- 创建新的 `API key`

2. OpenAI API Key
2. `OpenAI API Key`

- Sign up at [platform.openai.com](https://platform.openai.com/)
- 在 [platform.openai.com](https://platform.openai.com/) 注册
- Navigate to API Keys section
- 前往 `API Keys` 部分
- Generate a new API key
- 生成新的 `API key`

## How to Run
## 如何运行

1. **Clone the Repository**:
1. **克隆仓库**：
    ```bash
    git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
    cd rag_tutorials/agentic_rag_with_reasoning
    ```

2. **Install the dependencies**:
2. **安装依赖**：
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**
3. **运行应用：**
    ```bash
    streamlit run rag_reasoning_agent.py
    ```

4. **Configure API Keys:**
4. **配置 `API Keys`：**

- Enter your Google API key in the first field
- 在第一个字段中输入你的 `Google API key`
- Enter your OpenAI API key in the second field
- 在第二个字段中输入你的 `OpenAI API key`
- Both keys are required for the app to function
- 应用运行需要这两个密钥


5. **Use the Application:**
5. **使用应用：**

- Default Knowledge Source: The app comes pre-loaded with the MCP vs A2A Protocol article
- 默认知识来源：应用预加载了 `MCP vs A2A Protocol` 文章
- Add Knowledge Sources: Use the sidebar to add URLs to your knowledge base
- 添加知识来源：使用侧边栏向知识库添加 `URL`
- Suggested Prompts: Click the prompt buttons (What is MCP?, MCP vs A2A, Agent Communication) for quick questions
- 建议提示：点击提示按钮（`What is MCP?`、`MCP vs A2A`、`Agent Communication`）快速提问
- Ask Questions: Enter queries in the main input field
- 提问：在主输入字段中输入查询
- View Reasoning: Watch the agent's thought process unfold in real-time in the left panel
- 查看推理：在左侧面板实时观看智能体的思考过程展开
- Get Answers: Receive comprehensive responses with source citations in the right panel
- 获取答案：在右侧面板接收带有来源引用的完整响应

## How It Works
## 工作原理

The application uses a sophisticated RAG pipeline with Agno v2.0:
该应用使用基于 `Agno v2.0` 的复杂 `RAG` 流水线：

### Knowledge Base Setup
### 知识库设置
- Documents are loaded from URLs using Agno's Knowledge class
- 使用 `Agno` 的 `Knowledge` 类从 `URL` 加载文档
- Text is automatically chunked and embedded using OpenAI's embedding model 
- 使用 `OpenAI` 的嵌入模型自动切分文本并生成嵌入
- Vectors are stored in LanceDB for efficient retrieval
- 向量存储在 `LanceDB` 中以便高效检索
- Vector search enables semantic matching for relevant information
- 向量搜索支持对相关信息进行语义匹配
- URLs are tracked in session state to prevent duplicate loading
- `URL` 会在会话状态中跟踪，以防重复加载

### Agent Processing
### 智能体处理
- User queries trigger the agent's reasoning process
- 用户查询会触发智能体的推理过程
- ReasoningTools help the agent think step-by-step
- `ReasoningTools` 帮助智能体分步思考
- The agent searches the knowledge base for relevant information
- 智能体在知识库中搜索相关信息
- Gemini 2.5 Flash generates comprehensive answers with citations
- `Gemini 2.5 Flash` 生成带引用的完整答案
- Streaming events provide real-time updates on reasoning and content
- 流式事件提供推理和内容的实时更新

### UI Flow
### `UI` 流程
- Enter API keys → Knowledge base loads with default MCP vs A2A article → Use suggested prompts or ask custom questions
- 输入 `API key` → 知识库加载默认的 `MCP vs A2A` 文章 → 使用建议提示或提出自定义问题
- Reasoning process displayed in left panel, answer generation in right panel
- 左侧面板显示推理过程，右侧面板生成答案
- Sources cited for transparency and verification
- 引用来源以提高透明度并便于验证
- All events streamed in real-time for better user experience
- 所有事件都会实时流式输出，以改善用户体验
