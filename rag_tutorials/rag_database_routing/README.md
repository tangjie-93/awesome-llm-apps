# 📠 RAG Agent with Database Routing
# 📠 带数据库路由的 `RAG Agent`

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-rag-agent-with-database-routing) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-rag-agent-with-database-routing)，通过详细代码讲解、解释和最佳实践学习如何从零构建它。**

A Streamlit application that demonstrates an advanced implementation of RAG Agent with intelligent query routing. The system combines multiple specialized databases with smart fallback mechanisms to ensure reliable and accurate responses to user queries.
一个 `Streamlit` 应用，演示带智能查询路由的 `RAG Agent` 高级实现。该系统结合多个专用数据库和智能回退机制，确保可靠、准确地响应用户查询。

## Features
## 功能

- **Document Upload**: Users can upload multiple PDF documents related to a particular company. These documents are processed and stored in one of the three databases: Product Information, Customer Support & FAQ, or Financial Information.
  **文档上传**：用户可以上传与特定公司相关的多个 `PDF` 文档。这些文档会被处理并存储到三个数据库之一：`Product Information`、`Customer Support & FAQ` 或 `Financial Information`。

- **Natural Language Querying**: Users can ask questions in natural language. The system automatically routes the query to the most relevant database using a agno agent as the router.
  **自然语言查询**：用户可以用自然语言提问。系统会使用 `agno agent` 作为路由器，自动将查询路由到最相关的数据库。

- **RAG Orchestration**: Utilizes Langchain for orchestrating the retrieval augmented generation process, ensuring that the most relevant information is retrieved and presented to the user.
  **`RAG` 编排**：使用 `Langchain` 编排检索增强生成流程，确保检索到最相关的信息并呈现给用户。

- **Fallback Mechanism**: If no relevant documents are found in the databases, a LangGraph agent with a DuckDuckGo search tool is used to perform web research and provide an answer.
  **回退机制**：如果数据库中没有找到相关文档，会使用带有 `DuckDuckGo` 搜索工具的 `LangGraph agent` 执行网络研究并提供答案。

## How to Run?
## 如何运行？

1. **Clone the Repository**:
   **克隆仓库**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd rag_tutorials/rag_database_routing
   ```

2. **Install Dependencies**:
   **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   **运行应用**：
   ```bash
   streamlit run rag_database_routing.py
   ```

4. **Get OpenAI API Key**: Obtain an OpenAI API key and set it in the application. This is required for initializing the language models used in the application.
   **获取 `OpenAI API Key`**：获取一个 `OpenAI API key` 并在应用中设置它。这是初始化应用所用语言模型所必需的。

5. **Setup Qdrant Cloud**
   **设置 `Qdrant Cloud`**
- Visit [Qdrant Cloud](https://cloud.qdrant.io/)
  访问 [Qdrant Cloud](https://cloud.qdrant.io/)
- Create an account or sign in
  创建账户或登录
- Create a new cluster
  创建新集群
- Get your credentials:
  获取你的凭据：
   - Qdrant API Key: Found in API Keys section
     `Qdrant API Key`：可在 `API Keys` 部分找到
   - Qdrant URL: Your cluster URL (format: https://xxx-xxx.aws.cloud.qdrant.io)
     `Qdrant URL`：你的集群 `URL`（格式：`https://xxx-xxx.aws.cloud.qdrant.io`）

5. **Upload Documents**: Use the document upload section to add PDF documents to the desired database.
   **上传文档**：使用文档上传部分将 `PDF` 文档添加到所需数据库。

6. **Ask Questions**: Enter your questions in the query section. The application will route your question to the appropriate database and provide an answer.
   **提问**：在查询部分输入你的问题。应用会将你的问题路由到适当的数据库并提供答案。

## Technologies Used
## 使用的技术

- **Langchain**: For RAG orchestration, ensuring efficient retrieval and generation of information.
  **`Langchain`**：用于 `RAG` 编排，确保高效检索和生成信息。
- **Agno Agent**: Used as the router agent to determine the most relevant database for a given query.
  **`Agno Agent`**：作为路由代理，用于确定给定查询最相关的数据库。
- **LangGraph Agent**: Acts as a fallback mechanism, utilizing DuckDuckGo for web research when necessary.
  **`LangGraph Agent`**：作为回退机制，在必要时利用 `DuckDuckGo` 进行网络研究。
- **Streamlit**: Provides a user-friendly interface for document upload and querying.
  **`Streamlit`**：提供用于文档上传和查询的用户友好界面。
- **Qdrant**: Used for managing the databases, storing and retrieving document embeddings efficiently.
  **`Qdrant`**：用于管理数据库，高效存储和检索文档嵌入。

## How It Works?
## 工作原理？

**1. Query Routing**
**1. 查询路由**
The system uses a three-stage routing approach:
系统使用三阶段路由方法：
- Vector similarity search across all databases
  跨所有数据库执行向量相似度搜索
- LLM-based routing for ambiguous queries
  对模糊查询执行基于 `LLM` 的路由
- Web search fallback for unknown topics
  对未知主题回退到网络搜索

**2. Document Processing**
**2. 文档处理**
- Automatic text extraction from PDFs
  从 `PDF` 自动提取文本
- Smart text chunking with overlap
  带重叠的智能文本分块
- Vector embedding generation
  生成向量嵌入
- Efficient database storage
  高效数据库存储

**3. Answer Generation**
**3. 答案生成**
- Context-aware retrieval
  上下文感知检索
- Smart document combination
  智能文档组合
- Confidence-based responses
  基于置信度的响应
- Web research integration
  网络研究集成
