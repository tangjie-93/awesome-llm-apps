# 🧠 Math Tutor Agent – Agentic RAG with Feedback Loop
# 🧠 数学辅导智能体 - 带反馈循环的智能体式 `RAG`

This project implements an **Agentic-RAG architecture** to simulate a math professor that solves **JEE-level math questions** with step-by-step explanations. The system smartly routes queries between a vector database and web search, applies input/output guardrails, and incorporates human feedback for continuous learning.
本项目实现了一个 **智能体式 `RAG` 架构**，用于模拟一位数学教授，以分步讲解方式解答 **`JEE` 难度数学题**。系统会智能地在向量数据库和 Web 搜索之间路由查询，应用输入/输出护栏，并纳入人工反馈以实现持续学习。

## 📌 Features
## 📌 功能

- ✅ **Input Guardrails** (DSPy): Accepts only academic math questions.
- ✅ **输入护栏**（`DSPy`）：只接受学术数学问题。
- 📚 **Knowledge Base Search**: Uses **Qdrant Vector DB** with OpenAI Embeddings to match known questions.
- 📚 **知识库搜索**：使用带有 `OpenAI Embeddings` 的 **`Qdrant Vector DB`** 来匹配已知问题。
- 🌐 **Web Fallback**: Integrates **Tavily API** when no good match is found.
- 🌐 **Web 回退**：在找不到良好匹配时集成 **`Tavily API`**。
- ✍️ **GPT-4.1 Explanations**: Generates step-by-step math solutions.
- ✍️ **`GPT-4.1` 讲解**：生成分步数学解法。
- 🛡️ **Output Guardrails**: Filters for correctness and safety.
- 🛡️ **输出护栏**：按正确性和安全性进行过滤。
- 👍 **Human-in-the-Loop Feedback**: Users rate answers (Yes/No), logged for future learning.
- 👍 **人在回路反馈**：用户对答案进行评分（`Yes`/`No`），并记录下来用于未来学习。
- 📊 **Benchmarking**: Evaluated on **JEEBench** dataset with adjustable question limits.
- 📊 **基准测试**：在 **`JEEBench`** 数据集上评估，并支持可调整的问题数量限制。
- 💻 **Streamlit UI**: Interactive dashboard with multiple tabs.
- 💻 **`Streamlit UI`**：带有多个标签页的交互式仪表板。

## 🚀 Architecture Flow
## 🚀 架构流程
<img width="465" alt="Screenshot 2025-05-04 at 3 45 58 PM" src="https://github.com/user-attachments/assets/c0a9e612-2ef0-413c-b779-c99fe9f48619" />


## 📚 Knowledge Base
## 📚 知识库

- **Dataset:** [JEEBench (HuggingFace)](https://huggingface.co/datasets/daman1209arora/jeebench)
- **数据集：** [JEEBench (`HuggingFace`)](https://huggingface.co/datasets/daman1209arora/jeebench)
- **Vector DB:** Qdrant (with OpenAI Embeddings)
- **向量数据库：** `Qdrant`（使用 `OpenAI Embeddings`）
- **Storage:** Built with `llama-index` to persist embeddings and perform top-1 similarity search
- **存储：** 使用 `llama-index` 构建，用于持久化嵌入并执行 `top-1` 相似度搜索

## 🌐 Web Search
## 🌐 Web 搜索

- Uses **Tavily API** for fallback search when the KB doesn't contain a good match
- 当知识库没有良好匹配时，使用 **`Tavily API`** 进行回退搜索
- Fetched content is piped into **GPT-4o** for clean explanation
- 获取的内容会传入 **`GPT-4o`**，用于生成清晰讲解


## 🔐 Guardrails
## 🔐 护栏

- **Input Guardrail (DSPy):** Accepts only math-related academic questions
- **输入护栏（`DSPy`）：** 只接受与数学相关的学术问题
- **Output Guardrail (DSPy):** Blocks hallucinated or off-topic content
- **输出护栏（`DSPy`）：** 阻止幻觉内容或偏离主题的内容


## 👨‍🏫 Human-in-the-Loop Feedback
## 👨‍🏫 人在回路反馈

- Streamlit UI allows students to give 👍 / 👎 after seeing the answer
- `Streamlit UI` 允许学生在看到答案后给出 👍 / 👎
- Feedback is logged to a local JSON file for future improvement
- 反馈会记录到本地 `JSON` 文件中，用于未来改进

## 📊 Benchmarking
## 📊 基准测试

- Evaluated on **50 random JEEBench Math Questions**
- 在 **`50` 道随机 `JEEBench` 数学题** 上评估
- **Current Accuracy:** 66%
- **当前准确率：** `66%`
- Benchmark results saved to: `benchmark/results.csv`
- 基准测试结果保存到：`benchmark/results.csv`


## 🚀 Demo 
## 🚀 演示

To run the app with Streamlit:
使用 `Streamlit` 运行应用：

```bash
streamlit run app/streamlit.py
```


