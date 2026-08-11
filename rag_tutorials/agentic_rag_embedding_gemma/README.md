## 🔥 Agentic RAG with EmbeddingGemma
## 🔥 使用 `EmbeddingGemma` 的智能体式 `RAG`

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-local-agentic-rag-app-with-google-embeddinggemma) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里阅读完整的分步教程](https://www.theunwindai.com/p/build-a-local-agentic-rag-app-with-google-embeddinggemma)，学习如何通过详细的代码讲解、说明和最佳实践从零开始构建它。**

This Streamlit app demonstrates an agentic Retrieval-Augmented Generation (RAG) Agent using Google's EmbeddingGemma for embeddings and Llama 3.2 as the language model, all running locally via Ollama.
这个 `Streamlit` 应用演示了一个智能体式检索增强生成（`RAG`）智能体，使用 `Google` 的 `EmbeddingGemma` 生成嵌入，并使用 `Llama 3.2` 作为语言模型，全部通过 `Ollama` 在本地运行。

### Features
### 功能

- **Local AI Models**: Uses EmbeddingGemma for vector embeddings and Llama 3.2 for text generation
- **本地 `AI` 模型**：使用 `EmbeddingGemma` 生成向量嵌入，并使用 `Llama 3.2` 生成文本
- **PDF Knowledge Base**: Dynamically add PDF URLs to build a knowledge base
- **`PDF` 知识库**：动态添加 `PDF URL` 来构建知识库
- **Vector Search**: Efficient similarity search using LanceDB
- **向量搜索**：使用 `LanceDB` 进行高效的相似度搜索
- **Interactive UI**: Beautiful Streamlit interface for adding sources and querying
- **交互式 `UI`**：美观的 `Streamlit` 界面，用于添加来源和查询
- **Streaming Responses**: Real-time response generation with tool call visibility
- **流式响应**：实时生成响应，并可查看工具调用

### How to Get Started?
### 如何开始？

1. Clone the GitHub repository
1. 克隆 `GitHub` 仓库
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/rag_tutorials/agentic_rag_embedding_gemma
```

2. Install the required dependencies:
2. 安装所需依赖：
```bash
pip install -r requirements.txt
```

3. Ensure Ollama is installed and running with the required models:
3. 确保已安装 `Ollama`，并且它正在运行所需模型：
   - Pull the models: `ollama pull embeddinggemma:latest` and `ollama pull llama3.2:latest`
   - 拉取模型：`ollama pull embeddinggemma:latest` 和 `ollama pull llama3.2:latest`
   - Start Ollama server if not running
   - 如果 `Ollama` 服务器尚未运行，请启动它

4. Run the Streamlit app:
4. 运行 `Streamlit` 应用：
```bash
streamlit run agentic_rag_embeddinggemma.py
```
   (Note: The app file is in the root directory)
   （注意：应用文件位于根目录中）

5. Open your web browser to the URL provided (usually http://localhost:8501) to interact with the RAG agent.
5. 在网页浏览器中打开提供的 `URL`（通常是 `http://localhost:8501`），与 `RAG` 智能体交互。

### How It Works?
### 工作原理

1. **Knowledge Base Setup**: Add PDF URLs in the sidebar to load and index documents.
1. **知识库设置**：在侧边栏添加 `PDF URL`，用于加载文档并建立索引。
2. **Embedding Generation**: EmbeddingGemma creates vector embeddings for semantic search.
2. **嵌入生成**：`EmbeddingGemma` 为语义搜索创建向量嵌入。
3. **Query Processing**: User queries are embedded and searched against the knowledge base.
3. **查询处理**：对用户查询生成嵌入，并在知识库中搜索。
4. **Response Generation**: Llama 3.2 generates answers based on retrieved context.
4. **响应生成**：`Llama 3.2` 基于检索到的上下文生成答案。
5. **Tool Integration**: The agent uses search tools to fetch relevant information.
5. **工具集成**：智能体使用搜索工具获取相关信息。

### Requirements
### 要求

- Python 3.8+
- `Python 3.8+`
- Ollama installed and running
- 已安装并运行 `Ollama`
- Required models: `embeddinggemma:latest`, `llama3.2:latest`
- 所需模型：`embeddinggemma:latest`、`llama3.2:latest`

### Technologies Used
### 使用的技术

- **Agno**: Framework for building AI agents
- **`Agno`**：用于构建 `AI` 智能体的框架
- **Streamlit**: Web app framework
- **`Streamlit`**：Web 应用框架
- **LanceDB**: Vector database
- **`LanceDB`**：向量数据库
- **Ollama**: Local LLM server
- **`Ollama`**：本地 `LLM` 服务器
- **EmbeddingGemma**: Google's embedding model
- **`EmbeddingGemma`**：`Google` 的嵌入模型
- **Llama 3.2**: Meta's language model
- **`Llama 3.2`**：`Meta` 的语言模型
