# 🐋 Qwen 3 Local RAG Reasoning Agent
# 🐋 `Qwen 3` 本地 `RAG` 推理 `Agent`

This RAG Application demonstrates how to build a powerful Retrieval-Augmented Generation (RAG) system using locally running Qwen 3 and Gemma 3 models via Ollama. It combines document processing, vector search, and web search capabilities to provide accurate, context-aware responses to user queries. Built with Agno v2.0.
这个 `RAG` 应用演示了如何通过 `Ollama` 使用本地运行的 `Qwen 3` 和 `Gemma 3` 模型，构建强大的 `Retrieval-Augmented Generation (RAG)` 系统。它结合文档处理、向量搜索和网页搜索能力，为用户查询提供准确且具备上下文的响应。基于 `Agno v2.0` 构建。

## Features
## 功能

- **🧠 Multiple Local LLM Options**:
- **🧠 多种本地 `LLM` 选项**：

  - Qwen3 (1.7b, 8b) - Alibaba's latest language models
  - `Qwen3`（`1.7b`、`8b`）- `Alibaba` 最新语言模型
  - Gemma3 (1b, 4b) - Google's efficient language models with multimodal capabilities
  - `Gemma3`（`1b`、`4b`）- `Google` 具备多模态能力的高效语言模型
  - DeepSeek (1.5b) - Alternative model option
  - `DeepSeek`（`1.5b`）- 备选模型选项
- **📚 Comprehensive RAG System**:
- **📚 全面的 `RAG` 系统**：

  - Upload and process PDF documents
  - 上传并处理 `PDF` 文档
  - Extract content from web URLs
  - 从网页 `URL` 提取内容
  - Intelligent chunking and embedding
  - 智能切块和嵌入
  - Similarity search with adjustable threshold
  - 带可调阈值的相似度搜索
- **🌐 Web Search Integration**:
- **🌐 网页搜索集成**：

  - Fallback to web search when document knowledge is insufficient
  - 当文档知识不足时回退到网页搜索
  - Configurable domain filtering
  - 可配置域名过滤
  - Source attribution in responses
  - 在响应中标注来源
- **🔄 Flexible Operation Modes**:
- **🔄 灵活的运行模式**：

  - Toggle between RAG and direct LLM interaction
  - 在 `RAG` 和直接 `LLM` 交互之间切换
  - Force web search when needed
  - 在需要时强制进行网页搜索
  - Adjust similarity thresholds for document retrieval
  - 调整文档检索的相似度阈值
- **💾 Vector Database Integration**:
- **💾 向量数据库集成**：

  - Qdrant vector database for efficient similarity search
  - 使用 `Qdrant` 向量数据库进行高效相似度搜索
  - Persistent storage of document embeddings
  - 持久化存储文档嵌入
- **🔧 Agno v2.0 Framework**:
- **🔧 `Agno v2.0` 框架**：

  - Uses Agno v2.0 Knowledge embedder system
  - 使用 `Agno v2.0 Knowledge` 嵌入器系统
  - Debug mode for enhanced development experience
  - 使用调试模式增强开发体验
  - Modern agent architecture with improved tool integration
  - 具备改进工具集成的现代 `agent` 架构

## How to Get Started
## 如何开始

### Prerequisites
### 前置条件

- [Ollama](https://ollama.ai/) installed locally
- 已在本地安装 [Ollama](https://ollama.ai/)
- Python 3.8+
- `Python 3.8+`
- Qdrant running locally (via Docker) for vector storage
- 本地运行用于向量存储的 `Qdrant`（通过 `Docker`）
- Exa API key (optional, for web search capability)
- `Exa API key`（可选，用于网页搜索能力）
- Agno v2.0 installed
- 已安装 `Agno v2.0`

### Installation
### 安装

1. Clone the GitHub repository
1. 克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd rag_tutorials/qwen_local_rag
```

2. Install the required dependencies:
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```

3. Pull the required models using Ollama:
3. 使用 `Ollama` 拉取所需模型：

```bash
ollama pull qwen3:1.7b # Or any other model you want to use
ollama pull snowflake-arctic-embed # For embeddings
```

4. Run Qdrant locally through Docker:
4. 通过 `Docker` 在本地运行 `Qdrant`：

```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant
```

5. Get your API keys (optional):
5. 获取你的 `API key`（可选）：

   - Exa API key (for web search fallback capability)
   - `Exa API key`（用于网页搜索回退能力）
   
6. Run the application:
6. 运行应用：

```bash
streamlit run qwen_local_rag_agent.py
```

## How It Works
## 工作原理

1. **Document Processing**:
1. **文档处理**：

   - PDF files are processed using PyPDFLoader
   - 使用 `PyPDFLoader` 处理 `PDF` 文件
   - Web content is extracted using WebBaseLoader
   - 使用 `WebBaseLoader` 提取网页内容
   - Documents are split into chunks with RecursiveCharacterTextSplitter
   - 使用 `RecursiveCharacterTextSplitter` 将文档拆分为块
   - Metadata is added to track source types and timestamps
   - 添加元数据以跟踪来源类型和时间戳

2. **Vector Database**:
2. **向量数据库**：

   - Document chunks are embedded using Ollama's embedding models via Agno's OllamaEmbedder
   - 通过 `Agno` 的 `OllamaEmbedder` 使用 `Ollama` 嵌入模型为文档块生成嵌入
   - Embeddings are stored in Qdrant vector database
   - 嵌入存储在 `Qdrant` 向量数据库中
   - Similarity search retrieves relevant documents based on query with configurable threshold
   - 相似度搜索会基于查询并使用可配置阈值检索相关文档

3. **Query Processing**:
3. **查询处理**：

   - User queries are analyzed to determine the best information source
   - 分析用户查询以确定最佳信息来源
   - System checks document relevance using similarity threshold
   - 系统使用相似度阈值检查文档相关性
   - Falls back to web search if no relevant documents are found (when enabled)
   - 如果未找到相关文档，则回退到网页搜索（启用时）
   - Supports forced web search mode via toggle
   - 支持通过切换开关强制进入网页搜索模式

4. **Response Generation**:
4. **响应生成**：

   - Local LLM (Qwen/Gemma/DeepSeek) generates responses based on retrieved context
   - 本地 `LLM`（`Qwen`/`Gemma`/`DeepSeek`）基于检索到的上下文生成响应
   - Agno agents use debug mode for enhanced visibility into tool calls
   - `Agno agents` 使用调试模式，以增强对工具调用的可见性
   - Sources are cited and displayed to the user
   - 引用来源并展示给用户
   - Web search results are clearly indicated when used
   - 使用网页搜索结果时会清楚标明
   - Reasoning process is displayed for reasoning models
   - 对推理模型显示推理过程

## Configuration Options
## 配置选项

- **Model Selection**: Choose between different Qwen, Gemma, and DeepSeek models
- **模型选择**：在不同的 `Qwen`、`Gemma` 和 `DeepSeek` 模型之间选择
- **RAG Mode**: Toggle between RAG-enabled and direct LLM interaction
- **`RAG` 模式**：在启用 `RAG` 和直接 `LLM` 交互之间切换
- **Search Tuning**: Adjust similarity threshold (0.0-1.0) for document retrieval
- **搜索调优**：调整用于文档检索的相似度阈值（`0.0-1.0`）
- **Web Search**: Enable/disable web search fallback and configure domain filtering
- **网页搜索**：启用/禁用网页搜索回退，并配置域名过滤
- **Debug Mode**: Agents use debug mode by default for better visibility into tool calls and execution flow
- **调试模式**：`Agents` 默认使用调试模式，以便更清楚地查看工具调用和执行流程

## Use Cases
## 使用场景

- **Document Q&A**: Ask questions about your uploaded documents
- **文档问答**：针对你上传的文档提问
- **Research Assistant**: Combine document knowledge with web search
- **研究助手**：结合文档知识和网页搜索
- **Local Privacy**: Process sensitive documents without sending data to external APIs
- **本地隐私**：处理敏感文档，无需将数据发送到外部 `API`
- **Offline Operation**: Run advanced AI capabilities with limited or no internet access
- **离线运行**：在互联网访问受限或无互联网访问的情况下运行高级 `AI` 能力

## Requirements
## 要求

See `requirements.txt` for the complete list of dependencies.
完整依赖列表请参见 `requirements.txt`。
