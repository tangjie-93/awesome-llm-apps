# 🔄 Corrective RAG Agent
# 🔄 校正式 `RAG` 智能体
A sophisticated Retrieval-Augmented Generation (RAG) system that implements a corrective multi-stage workflow using LangGraph. This system combines document retrieval, relevance grading, query transformation, and web search to provide comprehensive and accurate responses.
一个复杂的 `Retrieval-Augmented Generation (RAG)` 系统，使用 `LangGraph` 实现校正式多阶段工作流。该系统结合文档检索、相关性评分、查询转换和网页搜索，提供全面且准确的回答。

## Features
## 功能

- **Smart Document Retrieval**: Uses Qdrant vector store for efficient document retrieval
  **智能文档检索**：使用 `Qdrant` 向量存储进行高效文档检索
- **Document Relevance Grading**: Employs Claude 4.5 sonnet to assess document relevance
  **文档相关性评分**：使用 `Claude 4.5 sonnet` 评估文档相关性
- **Query Transformation**: Improves search results by optimizing queries when needed
  **查询转换**：在需要时通过优化查询提升搜索结果
- **Web Search Fallback**: Uses Tavily API for web search when local documents aren't sufficient
  **网页搜索回退**：当本地文档不足时，使用 `Tavily API` 进行网页搜索
- **Multi-Model Approach**: Combines OpenAI embeddings and Claude 4.5 sonnet for different tasks
  **多模型方法**：结合 `OpenAI embeddings` 和 `Claude 4.5 sonnet` 处理不同任务
- **Interactive UI**: Built with Streamlit for easy document upload and querying
  **交互式 UI**：使用 `Streamlit` 构建，便于文档上传和查询

## How to Run?
## 如何运行？

1. **Clone the Repository**:
   **克隆仓库**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd rag_tutorials/corrective_rag
   ```

2. **Install Dependencies**:
   **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**:
   **设置 `API Keys`**：
   You'll need to obtain the following API keys:
   你需要获取以下 `API keys`：
   - [OpenAI API key](https://platform.openai.com/api-keys) (for embeddings)
     [OpenAI API key](https://platform.openai.com/api-keys)（用于 `embeddings`）
   - [Anthropic API key](https://console.anthropic.com/settings/keys) (for Claude 4.5 sonnet as LLM)
     [Anthropic API key](https://console.anthropic.com/settings/keys)（用于作为 `LLM` 的 `Claude 4.5 sonnet`）
   - [Tavily API key](https://app.tavily.com/home) (for web search)
     [Tavily API key](https://app.tavily.com/home)（用于网页搜索）
   - Qdrant Cloud Setup
     `Qdrant Cloud` 设置
      1. Visit [Qdrant Cloud](https://cloud.qdrant.io/)
         访问 [Qdrant Cloud](https://cloud.qdrant.io/)
      2. Create an account or sign in
         创建账号或登录
      3. Create a new cluster
         创建新集群
      4. Get your credentials:
         获取你的凭据：
         - Qdrant API Key: Found in API Keys section
           `Qdrant API Key`：可在 `API Keys` 部分找到
         - Qdrant URL: Your cluster URL (format: `https://xxx-xxx.aws.cloud.qdrant.io`)
           `Qdrant URL`：你的集群 URL（格式：`https://xxx-xxx.aws.cloud.qdrant.io`）

4. **Run the Application**:
   **运行应用**：
   ```bash
   streamlit run corrective_rag.py
   ```

5. **Use the Application**:
   **使用应用**：
   - Upload documents or provide URLs
     上传文档或提供 `URLs`
   - Enter your questions in the query box
     在查询框中输入你的问题
   - View the step-by-step Corrective RAG process
     查看逐步执行的 `Corrective RAG` 流程
   - Get comprehensive answers
     获得全面的回答

## Tech Stack
## 技术栈

- **LangChain**: For RAG orchestration and chains
  **`LangChain`**：用于 `RAG` 编排和链
- **LangGraph**: For workflow management
  **`LangGraph`**：用于工作流管理
- **Qdrant**: Vector database for document storage
  **`Qdrant`**：用于文档存储的向量数据库
- **Claude 4.5 sonnet**: Main language model for analysis and generation
  **`Claude 4.5 sonnet`**：用于分析和生成的主要语言模型
- **OpenAI**: For document embeddings
  **`OpenAI`**：用于文档嵌入
- **Tavily**: For web search capabilities
  **`Tavily`**：用于网页搜索能力
- **Streamlit**: For the user interface
  **`Streamlit`**：用于用户界面
