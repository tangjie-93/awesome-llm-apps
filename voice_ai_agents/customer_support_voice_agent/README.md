# 🎙️ Customer Support Voice Agent
# 🎙️ 客户支持语音 Agent

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-customer-support-voice-agent) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**

**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-customer-support-voice-agent)，学习如何从零开始构建该项目，并了解详细代码讲解、说明和最佳实践。**

An OpenAI SDK powered customer support agent application that delivers voice-powered responses to questions about your knowledge base using OpenAI's GPT-4o and TTS capabilities. The system crawls through documentation websites with Firecrawl, processes the content into a searchable knowledge base with Qdrant, and provides both text and voice responses to user queries.

这是一个由 OpenAI SDK 驱动的客户支持 Agent 应用，可使用 OpenAI 的 GPT-4o 和 TTS 能力，对知识库相关问题生成语音回答。系统通过 Firecrawl 抓取文档网站，用 Qdrant 将内容处理成可搜索知识库，并同时向用户提供文本和语音回答。

## Features
## 功能特性

- Knowledge Base Creation
- 知识库创建

  - Crawls documentation websites using Firecrawl
  - 使用 Firecrawl 抓取文档网站
  - Stores and indexes content using Qdrant vector database
  - 使用 Qdrant 向量数据库存储和索引内容
  - Generates embeddings for semantic search capabilities using FastEmbed
  - 使用 FastEmbed 生成向量嵌入，支持语义搜索

- **AI Agent Team**
- **AI Agent 团队**

  - **Documentation Processor**: Analyzes documentation content and generates clear, concise responses to user queries
  - **文档处理 Agent**：分析文档内容，并针对用户问题生成清晰、简洁的回答
  - **TTS Agent**: Converts text responses into natural-sounding speech with appropriate pacing and emphasis
  - **TTS Agent**：将文本回答转换为自然语音，并控制合适的语速和重音
  - **Voice Customization**: Supports multiple OpenAI TTS voices:
  - **声音自定义**：支持多种 OpenAI TTS 声音：
    - alloy, ash, ballad, coral, echo, fable, onyx, nova, sage, shimmer, verse

- **Interactive Interface**
- **交互式界面**

  - Clean Streamlit UI with sidebar configuration
  - 简洁的 Streamlit 界面，包含侧边栏配置
  - Real-time documentation search and response generation
  - 实时文档搜索和回答生成
  - Built-in audio player with download capability
  - 内置音频播放器，并支持下载
  - Progress indicators for system initialization and query processing
  - 为系统初始化和查询处理提供进度提示

## How to Run
## 如何运行

1. **Setup Environment / 配置环境**

   ```bash
   # Clone the repository
   # 克隆仓库
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/voice_ai_agents/customer_support_voice_agent

   # Install dependencies
   # 安装依赖
   pip install -r requirements.txt
   ```

2. **Configure API Keys / 配置 API Key**

   - Get OpenAI API key from [OpenAI Platform](https://platform.openai.com)
   - 从 [OpenAI Platform](https://platform.openai.com) 获取 OpenAI API Key
   - Get Qdrant API key and URL from [Qdrant Cloud](https://cloud.qdrant.io)
   - 从 [Qdrant Cloud](https://cloud.qdrant.io) 获取 Qdrant API Key 和 URL
   - Get Firecrawl API key for documentation crawling
   - 获取 Firecrawl API Key，用于抓取文档

3. **Run the Application / 运行应用**

   ```bash
   streamlit run ai_voice_agent_docs.py
   ```

4. **Use the Interface / 使用界面**

   - Enter API credentials in the sidebar
   - 在侧边栏输入 API 凭据
   - Input the documentation URL you want to learn about
   - 输入你想查询的文档 URL
   - Select your preferred voice from the dropdown
   - 从下拉菜单选择偏好的声音
   - Click "Initialize System" to process the documentation
   - 点击 "Initialize System" 处理文档
   - Ask questions and receive both text and voice responses
   - 提出问题，并同时获得文本和语音回答

## Features in Detail
## 功能详解

- **Knowledge Base Creation**
- **知识库创建**

  - Builds a searchable knowledge base from your documentation
  - 根据你的文档构建可搜索知识库
  - Preserves document structure and metadata
  - 保留文档结构和元数据
  - Supports multiple page crawling (limited to 5 pages per default configuration)
  - 支持多页面抓取（默认配置限制为 5 个页面）

- **Vector Search**
- **向量搜索**

  - Uses FastEmbed for generating embeddings
  - 使用 FastEmbed 生成向量嵌入
  - Semantic search capabilities for finding relevant content
  - 通过语义搜索查找相关内容
  - Efficient document retrieval using Qdrant
  - 使用 Qdrant 实现高效文档检索

- **Voice Generation**
- **语音生成**

  - High-quality text-to-speech using OpenAI's TTS models
  - 使用 OpenAI TTS 模型生成高质量文本转语音
  - Multiple voice options for customization
  - 提供多种声音选项用于自定义
  - Natural speech patterns with proper pacing and emphasis
  - 支持自然语音节奏、合适语速和重音
