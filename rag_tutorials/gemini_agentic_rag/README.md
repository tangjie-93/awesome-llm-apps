# 🤔 Agentic RAG with Gemini Flash Thinking
# 🤔 使用 `Gemini Flash Thinking` 的智能体式 `RAG`

A RAG Agentic system built with the new Gemini 2.0 Flash Thinking model and gemini-exp-1206, Qdrant for vector storage, and Agno (phidata prev) for agent orchestration. This application features intelligent query rewriting, document processing, and web search fallback capabilities to provide comprehensive AI-powered responses.
一个智能体式 `RAG` 系统，基于新的 `Gemini 2.0 Flash Thinking` 模型和 `gemini-exp-1206` 构建，使用 `Qdrant` 进行向量存储，并使用 `Agno`（以前为 `phidata`）进行智能体编排。该应用具备智能查询重写、文档处理和网页搜索回退能力，可提供全面的 `AI` 驱动回答。

## Features
## 功能

- **Document Processing**
  **文档处理**
  - PDF document upload and processing
    `PDF` 文档上传和处理
  - Web page content extraction
    网页内容提取
  - Automatic text chunking and embedding
    自动文本分块和嵌入
  - Vector storage in Qdrant cloud
    在 `Qdrant cloud` 中进行向量存储

- **Intelligent Querying**
  **智能查询**
  - Query rewriting for better retrieval
    为获得更好检索效果而进行查询重写
  - RAG-based document retrieval
    基于 `RAG` 的文档检索
  - Similarity search with threshold filtering
    带阈值过滤的相似度搜索
  - Automatic fallback to web search
    自动回退到网页搜索
  - Source attribution for answers
    为回答提供来源归因

- **Advanced Capabilities**
  **高级能力**
  - Exa AI web search integration
    `Exa AI` 网页搜索集成
  - Custom domain filtering for web search
    面向网页搜索的自定义域名过滤
  - Context-aware response generation
    上下文感知的回答生成
  - Chat history management
    聊天历史管理
  - Query reformulation agent
    查询改写智能体

- **Model Specific Features**
  **模型特定功能**
  - Gemini Thinking 2.0 Flash for chat and reasoning
    使用 `Gemini Thinking 2.0 Flash` 进行聊天和推理
  - Gemini Embedding model for vector embeddings
    使用 `Gemini Embedding` 模型进行向量嵌入
  - Agno Agent framework for orchestration
    使用 `Agno Agent` 框架进行编排
  - Streamlit-based interactive interface
    基于 `Streamlit` 的交互式界面

## Prerequisites
## 前置条件

### 1. Google API Key
### 1. `Google API` 密钥
1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
   前往 [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign up or log in to your account
   注册或登录你的账号
3. Create a new API key
   创建新的 `API key`

### 2. Qdrant Cloud Setup
### 2. `Qdrant Cloud` 设置
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
   - Qdrant URL: Your cluster URL (format: `https://xxx-xxx.cloud.qdrant.io`)
     `Qdrant URL`：你的集群 URL（格式：`https://xxx-xxx.cloud.qdrant.io`）

### 3. Exa AI API Key (Optional)
### 3. `Exa AI API` 密钥（可选）
1. Visit [Exa AI](https://exa.ai)
   访问 [Exa AI](https://exa.ai)
2. Sign up for an account
   注册账号
3. Generate an API key for web search capabilities
   生成用于网页搜索能力的 `API key`

## How to Run
## 如何运行

1. Clone the repository:
   克隆仓库：
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd rag_tutorials/gemini_agentic_rag
```

2. Install dependencies:
   安装依赖：
```bash
pip install -r requirements.txt
```

3. Run the application:
   运行应用：
```bash
streamlit run agentic_rag_gemini.py
```

## Usage
## 使用方法

1. Configure API keys in the sidebar:
   在侧边栏中配置 `API keys`：
   - Enter your Google API key
     输入你的 `Google API key`
   - Add Qdrant credentials
     添加 `Qdrant` 凭据
   - (Optional) Add Exa AI key for web search
     （可选）添加用于网页搜索的 `Exa AI key`

2. Upload documents:
   上传文档：
   - Use the file uploader for PDFs
     使用文件上传器上传 `PDF`
   - Enter URLs for web content
     输入网页内容的 `URLs`

3. Ask questions:
   提问：
   - Type your query in the chat interface
     在聊天界面中输入你的查询
   - View rewritten queries and sources
     查看重写后的查询和来源
   - See web search results when relevant
     在相关时查看网页搜索结果

4. Manage your session:
   管理你的会话：
   - Clear chat history as needed
     按需清除聊天历史
   - Configure web search domains
     配置网页搜索域名
   - Monitor processed documents
     监控已处理的文档
