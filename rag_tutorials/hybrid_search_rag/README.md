# 👀 RAG App with Hybrid Search 
# 👀 带有 `Hybrid Search` 的 `RAG` 应用

A powerful document Q&A application that leverages Hybrid Search (RAG) and Claude's advanced language capabilities to provide comprehensive answers. Built with RAGLite for robust document processing and retrieval, and Streamlit for an intuitive chat interface, this system seamlessly combines document-specific knowledge with Claude's general intelligence to deliver accurate and contextual responses.
一个强大的文档问答应用，利用 `Hybrid Search (RAG)` 和 `Claude` 的高级语言能力提供全面回答。该系统使用 `RAGLite` 实现稳健的文档处理和检索，并使用 `Streamlit` 提供直观的聊天界面，可将文档特定知识与 `Claude` 的通用智能无缝结合，交付准确且有上下文的回答。

## Features
## 功能

- **Hybrid Search Question Answering**
  **混合搜索问答**
    - RAG-based answers for document-specific queries
      针对文档特定查询的基于 `RAG` 的回答
    - Fallback to Claude for general knowledge questions
      对一般知识问题回退到 `Claude`

- **Document Processing**:
  **文档处理**：
  - PDF document upload and processing
    `PDF` 文档上传和处理
  - Automatic text chunking and embedding
    自动文本分块和嵌入
  - Hybrid search combining semantic and keyword matching
    结合语义匹配和关键词匹配的混合搜索
  - Reranking for better context selection
    通过重新排序选择更好的上下文

- **Multi-Model Integration**:
  **多模型集成**：
  - Claude for text generation - tested with Claude 3 Opus 
    使用 `Claude` 进行文本生成 - 已使用 `Claude 3 Opus` 测试
  - OpenAI for embeddings - tested with text-embedding-3-large
    使用 `OpenAI` 进行嵌入 - 已使用 `text-embedding-3-large` 测试
  - Cohere for reranking - tested with Cohere 3.5 reranker
    使用 `Cohere` 进行重新排序 - 已使用 `Cohere 3.5 reranker` 测试

## Prerequisites
## 前置条件

You'll need the following API keys and database setup:
你需要以下 `API keys` 和数据库设置：

1. **Database**: Create a free PostgreSQL database at [Neon](https://neon.tech):
   **数据库**：在 [Neon](https://neon.tech) 创建免费的 `PostgreSQL` 数据库：
   - Sign up/Login at Neon
     在 `Neon` 注册或登录
   - Create a new project
     创建新项目
   - Copy the connection string (looks like: `postgresql://user:pass@ep-xyz.region.aws.neon.tech/dbname`)
     复制连接字符串（类似于：`postgresql://user:pass@ep-xyz.region.aws.neon.tech/dbname`）

2. **API Keys**:
   **`API Keys`**：
   - [OpenAI API key](https://platform.openai.com/api-keys) for embeddings
     用于嵌入的 [OpenAI API key](https://platform.openai.com/api-keys)
   - [Anthropic API key](https://console.anthropic.com/settings/keys) for Claude
     用于 `Claude` 的 [Anthropic API key](https://console.anthropic.com/settings/keys)
   - [Cohere API key](https://dashboard.cohere.com/api-keys) for reranking
     用于重新排序的 [Cohere API key](https://dashboard.cohere.com/api-keys)

## How to get Started?
## 如何开始？

1. **Clone the Repository**:
   **克隆仓库**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/rag_tutorials/hybrid_search_rag
   ```

2. **Install Dependencies**:
   **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

3. **Install spaCy Model**:
   **安装 `spaCy` 模型**：
   ```bash
   pip install https://github.com/explosion/spacy-models/releases/download/xx_sent_ud_sm-3.7.0/xx_sent_ud_sm-3.7.0-py3-none-any.whl
   ```

4. **Run the Application**:
   **运行应用**：
   ```bash
   streamlit run main.py
   ```

## Usage
## 使用方法

1. Start the application
   启动应用
2. Enter your API keys in the sidebar:
   在侧边栏中输入你的 `API keys`：
   - OpenAI API key
     `OpenAI API key` 密钥
   - Anthropic API key
     `Anthropic API key` 密钥
   - Cohere API key
     `Cohere API key` 密钥
   - Database URL (optional, defaults to SQLite)
     `Database URL`（可选，默认使用 `SQLite`）
3. Click "Save Configuration"
   点击 `Save Configuration`
4. Upload PDF documents
   上传 `PDF` 文档
5. Start asking questions!
   开始提问！
   - Document-specific questions will use RAG
     文档特定问题会使用 `RAG`
   - General questions will use Claude directly
     一般问题会直接使用 `Claude`

## Database Options
## 数据库选项

The application supports multiple database backends:
该应用支持多种数据库后端：

- **PostgreSQL** (Recommended):
  **`PostgreSQL`**（推荐）：
  - Create a free serverless PostgreSQL database at [Neon](https://neon.tech)
    在 [Neon](https://neon.tech) 创建免费的无服务器 `PostgreSQL` 数据库
  - Get instant provisioning and scale-to-zero capability
    获得即时配置和缩容到零能力
  - Connection string format: `postgresql://user:pass@ep-xyz.region.aws.neon.tech/dbname`
    连接字符串格式：`postgresql://user:pass@ep-xyz.region.aws.neon.tech/dbname`

- **MySQL**:
  **`MySQL` 数据库**：
  ```
  mysql://user:pass@host:port/db
  ```
- **SQLite** (Local development):
  **`SQLite`**（本地开发）：
  ```
  sqlite:///path/to/db.sqlite
  ```

## Contributing
## 贡献

Contributions are welcome! Please feel free to submit a Pull Request.
欢迎贡献！请随时提交 `Pull Request`。
