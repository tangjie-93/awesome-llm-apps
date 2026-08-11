# PharmaQuery
# `PharmaQuery`（药物查询）

## Overview
## 概述
PharmaQuery is an advanced Pharmaceutical Insight Retrieval System designed to help users gain meaningful insights from research papers and documents in the pharmaceutical domain.
`PharmaQuery` 是一个高级药物洞察检索系统，旨在帮助用户从制药领域的研究论文和文档中获得有意义的洞察。

## Demo
## 演示
https://github.com/user-attachments/assets/c12ee305-86fe-4f71-9219-57c7f438f291

## Features
## 功能
- **Natural Language Querying**: Ask complex questions about the pharmaceutical industry and get concise, accurate answers.
  **自然语言查询**：询问有关制药行业的复杂问题，并获得简洁、准确的答案。
- **Custom Database**: Upload your own research documents to enhance the retrieval system's knowledge base.
  **自定义数据库**：上传你自己的研究文档，以增强检索系统的知识库。
- **Similarity Search**: Retrieves the most relevant documents for your query using AI embeddings.
  **相似度搜索**：使用 `AI embeddings` 为你的查询检索最相关的文档。
- **Streamlit Interface**: User-friendly interface for queries and document uploads.
  **`Streamlit` 界面**：用于查询和文档上传的用户友好界面。

## Technologies Used
## 使用的技术
- **Programming Language**: [Python 3.10+](https://www.python.org/downloads/release/python-31011/)
  **编程语言**：[Python 3.10+](https://www.python.org/downloads/release/python-31011/)
- **Framework**: [LangChain](https://www.langchain.com/)
  **框架**：[LangChain](https://www.langchain.com/)
- **Database**: [ChromaDB](https://www.trychroma.com/)
  **数据库**：[ChromaDB](https://www.trychroma.com/)
- **Models**:
  **模型**：
  - Embeddings: [Google Gemini API (embedding-001)](https://ai.google.dev/gemini-api/docs/embeddings)
    嵌入：[Google Gemini API (embedding-001)](https://ai.google.dev/gemini-api/docs/embeddings)
  - Chat: [Google Gemini API (gemini-1.5-pro)](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-pro)
    聊天：[Google Gemini API (gemini-1.5-pro)](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-pro)
- **PDF Processing**: [PyPDFLoader](https://python.langchain.com/docs/integrations/document_loaders/pypdfloader/)
  **`PDF` 处理**：[PyPDFLoader](https://python.langchain.com/docs/integrations/document_loaders/pypdfloader/)
- **Document Splitter**: [SentenceTransformersTokenTextSplitter](https://python.langchain.com/api_reference/text_splitters/sentence_transformers/langchain_text_splitters.sentence_transformers.SentenceTransformersTokenTextSplitter.html)
  **文档分割器**：[SentenceTransformersTokenTextSplitter](https://python.langchain.com/api_reference/text_splitters/sentence_transformers/langchain_text_splitters.sentence_transformers.SentenceTransformersTokenTextSplitter.html)

## Requirements
## 要求
1. **Install Dependencies**:
   **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   **运行应用**：
   ```bash
   streamlit run app.py
   ```

3. **Use the Application**:
   **使用应用**：
   - Paste your Google API Key in the sidebar.
     在侧边栏粘贴你的 `Google API Key`。
   - Enter your query in the main interface.
     在主界面输入你的查询。
   - Optionally, upload research papers in the sidebar to enhance the database.
     可选择在侧边栏上传研究论文，以增强数据库。

## :mailbox: Connect With Me
## :mailbox: 联系我
<img align="right" src="https://media.giphy.com/media/2HtWpp60NQ9CU/giphy.gif" alt="handshake gif" width="150">

<p align="left">
  <a href="https://linkedin.com/in/codewithcharan" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="codewithcharan" height="30" width="40" style="margin-right: 10px" /></a>
  <a href="https://instagram.com/joyboy._.ig" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="__mr.__.unique" height="30" width="40" /></a>
  <a href="https://twitter.com/Joyboy_x_" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="codewithcharan" height="30" width="40" style="margin-right: 10px" /></a>
</p>
