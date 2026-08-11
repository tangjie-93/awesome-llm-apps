## 🎙️ Voice RAG with OpenAI SDK

## 🎙️ 使用 OpenAI SDK 构建语音 RAG

### 🎓 FREE Step-by-Step Tutorial

### 🎓 免费分步教程

**👉** **[Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-voice-rag-agent)** **and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**

**👉** **[点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-voice-rag-agent)，学习如何从零开始构建该项目，并了解详细代码讲解、说明和最佳实践。**

This script demonstrates how to build a voice-enabled Retrieval-Augmented Generation (RAG) system using OpenAI's SDK and Streamlit. The application allows users to upload PDF documents, ask questions, and receive both text and voice responses using OpenAI's text-to-speech capabilities.

该脚本演示如何使用 OpenAI SDK 和 Streamlit 构建支持语音的检索增强生成（RAG）系统。应用允许用户上传 PDF 文档、提出问题，并通过 OpenAI 的文本转语音能力同时获得文本和语音回答。

### Features

### 功能特性

- Creates a voice-enabled RAG system using OpenAI's SDK
- 使用 OpenAI SDK 创建支持语音的 RAG 系统
- Supports PDF document processing and chunking
- 支持 PDF 文档处理和分块
- Uses Qdrant as the vector database for efficient similarity search
- 使用 Qdrant 作为向量数据库，实现高效相似度搜索
- Implements real-time text-to-speech with multiple voice options
- 实现实时文本转语音，并提供多种声音选项
- Provides a user-friendly Streamlit interface
- 提供用户友好的 Streamlit 界面
- Allows downloading of generated audio responses
- 支持下载生成的语音回答
- Supports multiple document uploads and tracking
- 支持多文档上传和处理状态跟踪

### How to get Started?

### 如何开始？

1. Clone the GitHub repository
2. 克隆 GitHub 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/rag_tutorials/voice_rag_openaisdk
```

1. Install the required dependencies:
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```

1. Set up your API keys:
2. 配置 API Key：

- Get your [OpenAI API key](https://platform.openai.com/)
- 获取你的 [OpenAI API Key](https://platform.openai.com/)
- Set up a [Qdrant Cloud](https://cloud.qdrant.io/) account and get your API key and URL
- 注册并配置 [Qdrant Cloud](https://cloud.qdrant.io/) 账号，获取 API Key 和 URL
- Create a `.env` file with your credentials:
- 创建 `.env` 文件并写入你的凭据：

```bash
OPENAI_API_KEY='your-openai-api-key'
QDRANT_URL='your-qdrant-url'
QDRANT_API_KEY='your-qdrant-api-key'
```

1. Run the Voice RAG application:
2. 运行 Voice RAG 应用：

```bash
streamlit run rag_voice.py
```

1. Open your web browser and navigate to the URL provided in the console output to interact with the Voice RAG system.
2. 打开浏览器，访问控制台输出的 URL，即可与 Voice RAG 系统交互。

### How it works?

### 工作原理

1. **Document Processing:**
2. **文档处理：**
   - Upload PDF documents through the Streamlit interface
   - 通过 Streamlit 界面上传 PDF 文档
   - Documents are split into chunks using LangChain's RecursiveCharacterTextSplitter
   - 使用 LangChain 的 RecursiveCharacterTextSplitter 将文档切分为文本块
   - Each chunk is embedded using FastEmbed and stored in Qdrant
   - 使用 FastEmbed 为每个文本块生成向量，并存储到 Qdrant 中
3. **Query Processing:**
4. **问题处理：**
   - User questions are converted to embeddings
   - 将用户问题转换为向量表示
   - Similar documents are retrieved from Qdrant
   - 从 Qdrant 中检索相似文档
   - A processing agent generates a clear, spoken-word friendly response
   - 处理 Agent 生成清晰且适合口语播报的回答
   - A TTS agent optimizes the response for speech synthesis
   - TTS Agent 对回答进行优化，使其更适合语音合成
5. **Voice Generation:**
6. **语音生成：**
   - Text responses are converted to speech using OpenAI's TTS
   - 使用 OpenAI 的 TTS 将文本回答转换为语音
   - Users can choose from multiple voice options
   - 用户可以从多种声音选项中选择
   - Audio can be played directly or downloaded as MP3
   - 语音可以直接播放，也可以下载为 MP3 文件
7. **Features:**
8. **能力总结：**
   - Real-time audio streaming
   - 实时音频流式播放
   - Multiple voice personality options
   - 多种语音人格选项
   - Document source tracking
   - 文档来源跟踪
   - Download capability for audio responses
   - 支持下载语音回答
   - Progress tracking for document processing
   - 支持跟踪文档处理进度

