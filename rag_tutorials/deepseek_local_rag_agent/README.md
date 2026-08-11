# 🐋 Deepseek Local RAG Reasoning Agent 
# 🐋 `Deepseek` 本地 `RAG` 推理智能体

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-local-rag-reasoning-agent-with-deepseek-r1) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-local-rag-reasoning-agent-with-deepseek-r1)，学习如何通过详细代码讲解、说明和最佳实践从零构建此项目。**

A powerful reasoning agent that combines local Deepseek models with RAG capabilities. Built using Deepseek (via Ollama), Snowflake for embeddings, Qdrant for vector storage, and Agno for agent orchestration, this application offers both simple local chat and advanced RAG-enhanced interactions with comprehensive document processing and web search capabilities.
一个强大的推理智能体，将本地 `Deepseek` 模型与 `RAG` 能力结合。该应用使用 `Deepseek`（通过 `Ollama`）、`Snowflake` 做嵌入、`Qdrant` 做向量存储、`Agno` 做智能体编排，同时提供简单本地聊天和高级 `RAG` 增强交互，并具备全面的文档处理和网页搜索能力。

## Features
## 功能

- **Dual Operation Modes**
  **双操作模式**
  - Local Chat Mode: Direct interaction with Deepseek locally
    `Local Chat Mode`：直接在本地与 `Deepseek` 交互
  - RAG Mode: Enhanced reasoning with document context and web search integration - llama3.2
    `RAG Mode`：结合文档上下文和网页搜索集成的增强推理 - `llama3.2`

- **Document Processing** (RAG Mode)
  **文档处理**（`RAG Mode`）
  - PDF document upload and processing
    `PDF` 文档上传和处理
  - Web page content extraction
    网页内容提取
  - Automatic text chunking and embedding
    自动文本分块和嵌入
  - Vector storage in Qdrant cloud
    在 `Qdrant cloud` 中进行向量存储

- **Intelligent Querying** (RAG Mode)
  **智能查询**（`RAG Mode`）
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
  - Thinking process visualization
    思考过程可视化

- **Model Specific Features**
  **模型特定功能**
  - Flexible model selection:
    灵活的模型选择：
    - Deepseek r1 1.5b (lighter, suitable for most laptops)
      `Deepseek r1 1.5b`（更轻量，适合大多数笔记本电脑）
    - Deepseek r1 7b (more capable, requires better hardware)
      `Deepseek r1 7b`（能力更强，需要更好的硬件）
  - Snowflake Arctic Embedding model (SOTA) for vector embeddings
    使用 `Snowflake Arctic Embedding` 模型（`SOTA`）进行向量嵌入
  - Agno Agent framework for orchestration
    使用 `Agno Agent` 框架进行编排
  - Streamlit-based interactive interface
    基于 `Streamlit` 的交互式界面

## Prerequisites
## 前置条件

### 1. Ollama Setup
### 1. `Ollama` 设置
1. Install [Ollama](https://ollama.ai)
   安装 [Ollama](https://ollama.ai)
2. Pull the Deepseek r1 model(s):
   拉取 `Deepseek r1` 模型：
```bash
# For the lighter model
ollama pull deepseek-r1:1.5b

# For the more capable model (if your hardware supports it)
ollama pull deepseek-r1:7b

ollama pull snowflake-arctic-embed
ollama pull llama3.2
```

### 2. Qdrant Cloud Setup (for RAG Mode)
### 2. `Qdrant Cloud` 设置（用于 `RAG Mode`）
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
cd rag_tutorials/deepseek_local_rag_agent
```

2. Install dependencies:
   安装依赖：
```bash
pip install -r requirements.txt
```

3. Run the application:
   运行应用：
```bash
streamlit run deepseek_rag_agent.py
```
