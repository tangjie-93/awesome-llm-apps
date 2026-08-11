## 🖇️ RAG-as-a-Service with Claude 3.5 Sonnet
## 🖇️ 使用 `Claude 3.5 Sonnet` 的 `RAG-as-a-Service`

Build and deploy a production-ready Retrieval-Augmented Generation (RAG) service using Claude 3.5 Sonnet and Ragie.ai. This implementation allows you to create a document querying system with a user-friendly Streamlit interface in less than 50 lines of Python code.
使用 `Claude 3.5 Sonnet` 和 `Ragie.ai` 构建并部署可用于生产的 `Retrieval-Augmented Generation (RAG)` 服务。该实现让你可以用少于 `50` 行 `Python` 代码创建一个带有友好 `Streamlit` 界面的文档查询系统。

### Features
### 功能
- Production-ready RAG pipeline
- 可用于生产的 `RAG` 流水线
- Integration with Claude 3.5 Sonnet for response generation
- 集成 `Claude 3.5 Sonnet` 用于生成响应
- Document upload from URLs
- 从 `URL` 上传文档
- Real-time document querying
- 实时文档查询
- Support for both fast and accurate document processing modes
- 支持快速和精确两种文档处理模式

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
1. 克隆 `GitHub` 仓库
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/rag_tutorials/rag-as-a-service
```

2. Install the required dependencies:
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```

3. Get your Anthropic API and Ragie API Key
3. 获取你的 `Anthropic API` 和 `Ragie API Key`

- Sign up for an [Anthropic account](https://console.anthropic.com/) and get your API key
- 注册 [Anthropic account](https://console.anthropic.com/) 并获取你的 `API key`
- Sign up for an [Ragie account](https://www.ragie.ai/) and get your API key
- 注册 [Ragie account](https://www.ragie.ai/) 并获取你的 `API key`

4. Run the Streamlit app
4. 运行 `Streamlit` 应用
```bash
streamlit run rag_app.py
```
