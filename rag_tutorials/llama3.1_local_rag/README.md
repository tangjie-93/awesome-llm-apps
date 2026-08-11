## 💻 Local Lllama-3.1 with RAG
## 💻 本地 `Lllama-3.1` 与 `RAG`
Streamlit app that allows you to chat with any webpage using local Llama-3.1 and Retrieval Augmented Generation (RAG). This app runs entirely on your computer, making it 100% free and without the need for an internet connection.
这个 `Streamlit` 应用允许你使用本地 `Llama-3.1` 和 `Retrieval Augmented Generation (RAG)` 与任意网页聊天。该应用完全在你的电脑上运行，因此 `100%` 免费且不需要互联网连接。


### Features
### 功能
- Input a webpage URL
- 输入网页 `URL`
- Ask questions about the content of the webpage
- 针对网页内容提问
- Get accurate answers using RAG and the Llama-3.1 model running locally on your computer
- 使用 `RAG` 和在你电脑本地运行的 `Llama-3.1` 模型获得准确答案

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
1. 克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/rag_tutorials/llama3.1_local_rag
```
2. Install the required dependencies:
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```
3. Run the Streamlit App
3. 运行 `Streamlit` 应用
```bash
streamlit run llama3.1_local_rag.py
```

### How it Works?
### 工作原理

- The app loads the webpage data using WebBaseLoader and splits it into chunks using RecursiveCharacterTextSplitter.
- 应用使用 `WebBaseLoader` 加载网页数据，并使用 `RecursiveCharacterTextSplitter` 将其拆分为块。
- It creates Ollama embeddings and a vector store using Chroma.
- 它会创建 `Ollama` 嵌入，并使用 `Chroma` 创建向量存储。
- The app sets up a RAG (Retrieval-Augmented Generation) chain, which retrieves relevant documents based on the user's question.
- 应用会设置一个 `RAG (Retrieval-Augmented Generation)` 链，根据用户的问题检索相关文档。
- The Llama-3.1 model is called to generate an answer using the retrieved context.
- 调用 `Llama-3.1` 模型，使用检索到的上下文生成答案。
- The app displays the answer to the user's question.
- 应用会显示对用户问题的答案。
