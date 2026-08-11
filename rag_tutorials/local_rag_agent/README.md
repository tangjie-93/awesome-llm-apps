## 🦙 Local RAG Agent with Llama 3.2
## 🦙 使用 `Llama 3.2` 的本地 `RAG Agent`

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-local-rag-agent) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-local-rag-agent)，通过详细的代码讲解、说明和最佳实践学习如何从零构建它。**

This application implements a Retrieval-Augmented Generation (RAG) system using Llama 3.2 via Ollama, with Qdrant as the vector database. Built with Agno v2.0.
此应用通过 `Ollama` 使用 `Llama 3.2` 实现 `Retrieval-Augmented Generation (RAG)` 系统，并使用 `Qdrant` 作为向量数据库。基于 `Agno v2.0` 构建。


### Features
### 功能
- Fully local RAG implementation
- 完全本地化的 `RAG` 实现
- Powered by Llama 3.2 through Ollama
- 通过 `Ollama` 使用 `Llama 3.2` 驱动
- Vector search using Qdrant
- 使用 `Qdrant` 进行向量搜索
- Interactive AgentOS interface
- 交互式 `AgentOS` 界面
- No external API dependencies
- 无外部 `API` 依赖
- Uses Agno v2.0 Knowledge class for document management
- 使用 `Agno v2.0 Knowledge` 类进行文档管理

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
1. 克隆 `GitHub` 仓库
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
```

2. Install the required dependencies:
2. 安装所需依赖：

```bash
cd awesome-llm-apps/rag_tutorials/local_rag_agent
pip install -r requirements.txt
```

3. Install and start [Qdrant](https://qdrant.tech/) vector database locally
3. 在本地安装并启动 [Qdrant](https://qdrant.tech/) 向量数据库

```bash
docker pull qdrant/qdrant
docker run -p 6333:6333 qdrant/qdrant
```

4. Install [Ollama](https://ollama.com/download) and pull Llama 3.2 for LLM and OpenHermes as the embedder for OllamaEmbedder
4. 安装 [Ollama](https://ollama.com/download)，拉取用于 `LLM` 的 `Llama 3.2`，并拉取作为 `OllamaEmbedder` 嵌入器的 `OpenHermes`
```bash
ollama pull llama3.2
ollama pull openhermes
```

5. Run the AI RAG Agent 
5. 运行 `AI RAG Agent`
```bash
python local_rag_agent.py
```

6. Open your web browser and navigate to the URL provided in the console output (typically `http://localhost:7777`) to interact with the RAG agent through the AgentOS interface.
6. 打开浏览器并访问控制台输出中提供的 `URL`（通常是 `http://localhost:7777`），通过 `AgentOS` 界面与 `RAG agent` 交互。

### Note
### 注意
- The knowledge base loads a Thai Recipes PDF on the first run. You can comment out the `knowledge_base.add_content()` line after the first run to avoid reloading.
- 知识库会在首次运行时加载一个泰国食谱 `PDF`。首次运行后，你可以注释掉 `knowledge_base.add_content()` 这一行以避免重复加载。
- The AgentOS interface provides a web-based UI for interacting with your agent.
- `AgentOS` 界面提供了一个基于网页的 `UI`，用于与你的 `agent` 交互。

