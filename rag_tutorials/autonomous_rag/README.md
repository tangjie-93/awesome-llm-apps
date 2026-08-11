# 🤖 AutoRAG: Autonomous RAG with GPT-4o and Vector Database
# 🤖 `AutoRAG`：使用 `GPT-4o` 和向量数据库的自主式 `RAG`

**🎓 FREE Step-by-Step Tutorial**
**🎓 免费分步教程**

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-autonomous-rag-app-using-gpt-4o-and-vector-database) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里阅读完整的分步教程](https://www.theunwindai.com/p/build-autonomous-rag-app-using-gpt-4o-and-vector-database)，学习如何通过详细的代码讲解、说明和最佳实践从零开始构建它。**

This Streamlit application implements an Autonomous Retrieval-Augmented Generation (RAG) system using OpenAI's GPT-4o model and PgVector database. It allows users to upload PDF documents, add them to a knowledge base, and query the AI assistant with context from both the knowledge base and web searches.
这个 `Streamlit` 应用实现了一个自主式检索增强生成（`RAG`）系统，使用 `OpenAI` 的 `GPT-4o` 模型和 `PgVector` 数据库。它允许用户上传 `PDF` 文档，将其添加到知识库，并使用来自知识库和 Web 搜索的上下文查询 `AI` 助手。
Features
功能

### Freatures 
### 功能
- Chat interface for interacting with the AI assistant
- 用于与 `AI` 助手交互的聊天界面
- PDF document upload and processing
- `PDF` 文档上传和处理
- Knowledge base integration using PostgreSQL and Pgvector
- 使用 `PostgreSQL` 和 `Pgvector` 集成知识库
- Web search capability using DuckDuckGo
- 使用 `DuckDuckGo` 的 Web 搜索能力
- Persistent storage of assistant data and conversations
- 助手数据和对话的持久化存储

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
1. 克隆 `GitHub` 仓库
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/rag_tutorials/autonomous_rag
```

2. Install the required dependencies:
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```

3. Ensure PgVector Database is running:
3. 确保 `PgVector` 数据库正在运行：
The app expects PgVector to be running on [localhost:5532](http://localhost:5532/). Adjust the configuration in the code if your setup is different.
应用期望 `PgVector` 运行在 [localhost:5532](http://localhost:5532/)。如果你的设置不同，请在代码中调整配置。

```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16
```

4. Run the Streamlit App
4. 运行 `Streamlit` 应用
```bash
streamlit run autorag.py
```
