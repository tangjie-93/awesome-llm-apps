# Agentic RAG with LangGraph: AI Blog Search
# 使用 `LangGraph` 的智能体式 `RAG`：`AI Blog Search`

## Overview
## 概览
AI Blog Search is an Agentic RAG application designed to enhance information retrieval from AI-related blog posts. This system leverages LangChain, LangGraph, and Google's Gemini model to fetch, process, and analyze blog content, providing users with accurate and contextually relevant answers.
`AI Blog Search` 是一个智能体式 `RAG` 应用，旨在增强从 `AI` 相关博客文章中检索信息的能力。该系统利用 `LangChain`、`LangGraph` 和 `Google` 的 `Gemini` 模型来获取、处理和分析博客内容，为用户提供准确且上下文相关的答案。

## LangGraph Workflow
## `LangGraph` 工作流
![LangGraph-Workflow](https://github.com/user-attachments/assets/07d8a6b5-f1ef-4b7e-b47a-4f14a192bd8a)

## Demo
## 演示
https://github.com/user-attachments/assets/cee07380-d3dc-45f4-ad26-7d944ba9c32b

## Features
## 功能
- **Document Retrieval:** Uses Qdrant as a vector database to store and retrieve blog content based on embeddings.
- **文档检索：** 使用 `Qdrant` 作为向量数据库，基于嵌入存储和检索博客内容。
- **Agentic Query Processing:** Uses an AI-powered agent to determine whether a query should be rewritten, answered, or require more retrieval.
- **智能体式查询处理：** 使用 `AI` 驱动的智能体判断查询应被重写、回答，还是需要更多检索。
- **Relevance Assessment:** Implements an automated relevance grading system using Google's Gemini model.
- **相关性评估：** 使用 `Google` 的 `Gemini` 模型实现自动相关性评分系统。
- **Query Refinement:** Enhances poorly structured queries for better retrieval results.
- **查询优化：** 优化结构较差的查询，以获得更好的检索结果。
- **Streamlit UI:** Provides a user-friendly interface for entering blog URLs, queries and retrieving insightful responses.
- **`Streamlit UI`：** 提供用户友好的界面，用于输入博客 `URL`、查询并检索有洞察力的响应。
- **Graph-Based Workflow:** Implements a structured state graph using LangGraph for efficient decision-making.
- **基于图的工作流：** 使用 `LangGraph` 实现结构化状态图，以进行高效决策。

## Technologies Used
## 使用的技术
- **Programming Language**: [Python 3.10+](https://www.python.org/downloads/release/python-31011/)
- **编程语言**：[Python 3.10+](https://www.python.org/downloads/release/python-31011/)
- **Framework**: [LangChain](https://www.langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- **框架**：[LangChain](https://www.langchain.com/) 和 [LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- **Database**: [Qdrant](https://qdrant.tech/)
- **数据库**：[Qdrant](https://qdrant.tech/)
- **Models**:
- **模型**：
  - Embeddings: [Google Gemini API (embedding-001)](https://ai.google.dev/gemini-api/docs/embeddings)
  - 嵌入：[Google Gemini API (`embedding-001`)](https://ai.google.dev/gemini-api/docs/embeddings)
  - Chat: [Google Gemini API (gemini-2.0-flash)](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-2.0-flash)
  - 聊天：[Google Gemini API (`gemini-2.0-flash`)](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-2.0-flash)
- **Blogs Loader**: [Langchain WebBaseLoader](https://python.langchain.com/docs/integrations/document_loaders/web_base/)
- **博客加载器**：[Langchain WebBaseLoader](https://python.langchain.com/docs/integrations/document_loaders/web_base/)
- **Document Splitter**: [RecursiveCharacterTextSplitter](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/)
- **文档切分器**：[RecursiveCharacterTextSplitter](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/)
- **User Interface (UI)**: [Streamlit](https://docs.streamlit.io/)
- **用户界面（`UI`）**：[Streamlit](https://docs.streamlit.io/)

## Requirements
## 要求
1. **Install Dependencies**:
1. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
2. **运行应用**：
   ```bash
   streamlit run app.py
   ```

3. **Use the Application**:
3. **使用应用**：
   - Paste your Google API Key in the sidebar.
   - 在侧边栏粘贴你的 `Google API Key`。
   - Paste the blog link.
   - 粘贴博客链接。
   - Enter your query about the blog post.
   - 输入你关于该博客文章的查询。

## :mailbox: Connect With Me
## :mailbox: 联系我
<img align="right" src="https://media.giphy.com/media/2HtWpp60NQ9CU/giphy.gif" alt="handshake gif" width="150">

<p align="left">
  <a href="https://linkedin.com/in/codewithcharan" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="codewithcharan" height="30" width="40" style="margin-right: 10px" /></a>
  <a href="https://instagram.com/joyboy._.ig" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="__mr.__.unique" height="30" width="40" /></a>
  <a href="https://twitter.com/Joyboy_x_" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="codewithcharan" height="30" width="40" style="margin-right: 10px" /></a>
</p>

<img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=500&height=70&duration=4000&lines=Thanks+for+visiting!+👋;+Message+me+on+Linkedin!;+I'm+always+down+to+collab+:)"/>
