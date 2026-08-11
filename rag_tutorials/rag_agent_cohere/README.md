# RAG Agent with Cohere ⌘R
# 基于 `Cohere` 的 `RAG Agent` ⌘R

A RAG Agentic system built with Cohere's new model Command-r7b-12-2024, Qdrant for vector storage, Langchain for RAG and LangGraph for orchestration. This application allows users to upload documents, ask questions about them, and get AI-powered responses with fallback to web search when needed.
一个使用 `Cohere` 新模型 `Command-r7b-12-2024` 构建的 `RAG Agentic` 系统，使用 `Qdrant` 进行向量存储，使用 `Langchain` 实现 `RAG`，并使用 `LangGraph` 进行编排。该应用允许用户上传文档、围绕文档提问，并在需要时回退到网络搜索来获得 `AI` 驱动的回答。

## Features
## 功能

- **Document Processing**
  **文档处理**
  - PDF document upload and processing
    `PDF` 文档上传和处理
  - Automatic text chunking and embedding
    自动文本分块和嵌入
  - Vector storage in Qdrant cloud
    在 `Qdrant Cloud` 中进行向量存储

- **Intelligent Querying**
  **智能查询**
  - RAG-based document retrieval
    基于 `RAG` 的文档检索
  - Similarity search with threshold filtering
    带阈值过滤的相似度搜索
  - Automatic fallback to web search when no relevant documents found
    未找到相关文档时自动回退到网络搜索
  - Source attribution for answers
    为答案提供来源归因

- **Advanced Capabilities**
  **高级能力**
  - DuckDuckGo web search integration
    `DuckDuckGo` 网络搜索集成
  - LangGraph agent for web research
    用于网络研究的 `LangGraph agent`
  - Context-aware response generation
    上下文感知的响应生成
  - Long answer summarization
    长答案总结

- **Model Specific Features**
  **模型特定功能**
  - Command-r7b-12-2024 model for Chat and RAG
    用于 `Chat` 和 `RAG` 的 `Command-r7b-12-2024` 模型
  - cohere embed-english-v3.0 model for embeddings
    用于嵌入的 `cohere embed-english-v3.0` 模型
  - create_react_agent function from langgraph
    来自 `langgraph` 的 `create_react_agent` 函数
  - DuckDuckGoSearchRun tool for web search
    用于网络搜索的 `DuckDuckGoSearchRun` 工具

## Prerequisites
## 先决条件

### 1. Cohere API Key
### 1. `Cohere API Key`
1. Go to [Cohere Platform](https://dashboard.cohere.ai/api-keys)
   前往 [Cohere Platform](https://dashboard.cohere.ai/api-keys)
2. Sign up or log in to your account
   注册或登录你的账户
3. Navigate to API Keys section
   转到 `API Keys` 部分
4. Create a new API key
   创建新的 `API key`

### 2. Qdrant Cloud Setup
### 2. `Qdrant Cloud` 设置
1. Visit [Qdrant Cloud](https://cloud.qdrant.io/)
   访问 [Qdrant Cloud](https://cloud.qdrant.io/)
2. Create an account or sign in
   创建账户或登录
3. Create a new cluster
   创建新集群
4. Get your credentials:
   获取你的凭据：
   - Qdrant API Key: Found in API Keys section
     `Qdrant API Key`：可在 `API Keys` 部分找到
   - Qdrant URL: Your cluster URL (format: `https://xxx-xxx.aws.cloud.qdrant.io`)
     `Qdrant URL`：你的集群 `URL`（格式：`https://xxx-xxx.aws.cloud.qdrant.io`）


## How to Run
## 如何运行

1. Clone the repository:
   克隆仓库：
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd rag_tutorials/rag_agent_cohere
```

2. Install dependencies:
   安装依赖：
```bash
pip install -r requirements.txt
```

```bash
streamlit run rag_agent_cohere.py
```
