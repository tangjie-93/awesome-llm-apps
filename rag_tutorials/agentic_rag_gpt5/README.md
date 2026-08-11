# 🧠 Agentic RAG with GPT-5
# 🧠 使用 `GPT-5` 的智能体式 `RAG`

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-agentic-rag-with-openai-gpt-5) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里阅读完整的分步教程](https://www.theunwindai.com/p/build-agentic-rag-with-openai-gpt-5)，学习如何通过详细的代码讲解、说明和最佳实践从零开始构建它。**

An agentic RAG application built with the Agno framework, featuring GPT-5 and LanceDB for efficient knowledge retrieval and question answering.
这是一个使用 `Agno` 框架构建的智能体式 `RAG` 应用，集成 `GPT-5` 和 `LanceDB`，用于高效的知识检索和问答。

## ✨ Features
## ✨ 功能

- **🤖 GPT-5**: Latest OpenAI model for intelligent responses
- **🤖 `GPT-5`**：用于智能响应的最新 `OpenAI` 模型
- **🗄️ LanceDB**: Lightweight vector database for fast similarity search
- **🗄️ `LanceDB`**：用于快速相似度搜索的轻量级向量数据库
- **🔍 Agentic RAG**: Intelligent retrieval augmented generation
- **🔍 智能体式 `RAG`**：智能检索增强生成
- **📝 Markdown Formatting**: Beautiful, structured responses
- **📝 `Markdown` 格式化**：美观且结构化的响应
- **🌐 Dynamic Knowledge**: Add URLs to expand knowledge base
- **🌐 动态知识**：添加 `URL` 来扩展知识库
- **⚡ Real-time Streaming**: Watch answers generate live
- **⚡ 实时流式输出**：实时查看答案生成过程
- **🎯 Clean Interface**: Simplified UI without configuration complexity
- **🎯 简洁界面**：简化的 `UI`，无需复杂配置

## 🚀 Quick Start
## 🚀 快速开始

### Prerequisites
### 前置条件

- Python 3.11+
- `Python 3.11+`
- OpenAI API key with GPT-5 access
- 拥有 `GPT-5` 访问权限的 `OpenAI API key`

### Installation
### 安装

1. **Clone and navigate to the project**
1. **克隆并进入项目目录**
   ```bash
   cd rag_tutorials/agentic_rag_gpt5
   ```

2. **Install dependencies**
2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
3. **设置你的 `OpenAI API key`**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
   Or create a `.env` file:
   或创建一个 `.env` 文件：
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

4. **Run the application**
4. **运行应用**
   ```bash
   streamlit run agentic_rag_gpt5.py
   ```

## 🎯 How to Use
## 🎯 如何使用

1. **Enter your OpenAI API key** in the sidebar
1. 在侧边栏中**输入你的 `OpenAI API key`**
2. **Add knowledge sources** by entering URLs in the sidebar
2. 在侧边栏输入 `URL` 来**添加知识来源**
3. **Ask questions** using the text area or suggested prompts
3. 使用文本区域或建议提示来**提问**
4. **Watch answers stream** in real-time with markdown formatting
4. 以 `Markdown` 格式实时**观看答案流式生成**

### Suggested Questions
### 建议问题

- **"What is Agno?"** - Learn about the Agno framework and agents
- **“什么是 `Agno`？”** - 了解 `Agno` 框架和智能体
- **"Teams in Agno"** - Understand how teams work in Agno
- **“`Agno` 中的团队”** - 理解团队在 `Agno` 中如何工作
- **"Build RAG system"** - Get a step-by-step guide to building RAG systems
- **“构建 `RAG` 系统”** - 获取构建 `RAG` 系统的分步指南

## 🏗️ Architecture
## 🏗️ 架构

### Core Components
### 核心组件

- **`Agent`**: Orchestrates the entire Q&A process
- **`Agent`**：编排整个问答流程
- **`UrlKnowledge`**: Manages document loading from URLs
- **`UrlKnowledge`**：管理从 `URL` 加载文档
- **`LanceDb`**: Vector database for efficient similarity search
- **`LanceDb`**：用于高效相似度搜索的向量数据库
- **`OpenAIEmbedder`**: Converts text to embeddings
- **`OpenAIEmbedder`**：将文本转换为嵌入
- **`OpenAIChat`**: GPT-5-nano model for generating responses
- **`OpenAIChat`**：用于生成响应的 `GPT-5-nano` 模型

### Data Flow
### 数据流

1. **Knowledge Loading**: URLs are processed and stored in LanceDB
1. **知识加载**：处理 `URL` 并将其存储到 `LanceDB`
2. **Vector Search**: OpenAI embeddings enable semantic search
2. **向量搜索**：`OpenAI` 嵌入支持语义搜索
3. **Response Generation**: GPT-5-nano processes information and generates answers
3. **响应生成**：`GPT-5-nano` 处理信息并生成答案
4. **Streaming Output**: Real-time display of formatted responses
4. **流式输出**：实时显示格式化响应

## 🔧 Configuration
## 🔧 配置

### Database Settings
### 数据库设置
- **Vector DB**: LanceDB with local storage
- **向量数据库**：使用本地存储的 `LanceDB`
- **Table Name**: `agentic_rag_docs`
- **表名**：`agentic_rag_docs`
- **Search Type**: Vector similarity search
- **搜索类型**：向量相似度搜索

## 📚 Knowledge Management
## 📚 知识管理

### Adding Sources
### 添加来源
- Use the sidebar to add new URLs
- 使用侧边栏添加新的 `URL`
- Sources are automatically processed and indexed
- 来源会被自动处理并建立索引
- Current sources are displayed as numbered list
- 当前来源会以编号列表显示

### Default Knowledge
### 默认知识
- Starts with Agno documentation: `https://docs.agno.com/introduction/agents.md`
- 默认从 `Agno` 文档开始：`https://docs.agno.com/introduction/agents.md`
- Expandable with any web-based documentation
- 可使用任何基于 Web 的文档进行扩展

## 🎨 UI Features
## 🎨 `UI` 功能

### Sidebar
### 侧边栏
- **API Key Management**: Secure input for OpenAI credentials
- **`API Key` 管理**：安全输入 `OpenAI` 凭据
- **URL Addition**: Dynamic knowledge base expansion
- **`URL` 添加**：动态扩展知识库
- **Current Sources**: Numbered list of loaded URLs
- **当前来源**：已加载 `URL` 的编号列表

### Main Interface
### 主界面
- **Suggested Prompts**: Quick access to common questions
- **建议提示**：快速访问常见问题
- **Query Input**: Large text area for custom questions
- **查询输入**：用于自定义问题的大型文本区域
- **Real-time Streaming**: Live answer generation
- **实时流式输出**：实时生成答案
- **Markdown Rendering**: Beautiful formatted responses
- **`Markdown` 渲染**：美观的格式化响应
