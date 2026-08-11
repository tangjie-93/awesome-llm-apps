# 🔍 Knowledge Graph RAG with Verifiable Citations
# 🔍 带可验证引用的 `Knowledge Graph RAG`

A Streamlit application demonstrating how **Knowledge Graph-based Retrieval-Augmented Generation (RAG)** provides multi-hop reasoning with fully verifiable source attribution.
一个 `Streamlit` 应用，用于演示基于 **`Knowledge Graph` 的 `Retrieval-Augmented Generation (RAG)`** 如何提供多跳推理和完全可验证的来源归因。

## 🎯 What Makes This Different?
## 🎯 它有何不同？

Traditional vector-based RAG finds similar text chunks, but struggles with:
传统基于向量的 `RAG` 可以找到相似文本块，但难以处理：
- Questions requiring information from multiple documents
  需要来自多个文档信息的问题
- Complex reasoning chains
  复杂推理链
- Providing verifiable sources for each claim
  为每个主张提供可验证来源

**Knowledge Graph RAG** solves these by:
**`Knowledge Graph RAG`** 通过以下方式解决这些问题：
1. **Building a structured graph** of entities and relationships from documents
   从文档中**构建实体和关系的结构化图**
2. **Traversing connections** to find related information (multi-hop reasoning)
   **遍历连接**以查找相关信息（多跳推理）
3. **Tracking provenance** so every claim links back to its source
   **跟踪来源**，使每个主张都能链接回其来源

## ✨ Features
## ✨ 功能

| Feature<br>功能 | Description<br>描述 |
|---------|-------------|
| 🔗 **Multi-hop Reasoning**<br>🔗 **多跳推理** | Traverse entity relationships to answer complex questions<br>遍历实体关系以回答复杂问题 |
| 📚 **Verifiable Citations**<br>📚 **可验证引用** | Every claim includes source document and text<br>每个主张都包含来源文档和文本 |
| 🧠 **Reasoning Trace**<br>🧠 **推理轨迹** | See exactly how the answer was derived<br>准确查看回答是如何推导出来的 |
| 🏠 **Fully Local**<br>🏠 **完全本地** | Uses Ollama for LLM, Neo4j for graph storage<br>使用 `Ollama` 运行 `LLM`，使用 `Neo4j` 进行图存储 |

## 🚀 Quick Start
## 🚀 快速开始

### Prerequisites
### 前置条件

1. **Ollama** - Local LLM inference
   **`Ollama`** - 本地 `LLM` 推理
   ```bash
   # Install from https://ollama.ai
   ollama pull llama3.2
   ```

2. **Neo4j** - Knowledge graph database
   **`Neo4j`** - 知识图谱数据库
   ```bash
   # Using Docker
   docker run -d \
     --name neo4j \
     -p 7474:7474 -p 7687:7687 \
     -e NEO4J_AUTH=neo4j/password \
     neo4j:latest
   ```

### Installation
### 安装

```bash
# Clone and navigate
cd knowledge_graph_rag_citations

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run knowledge_graph_rag.py
```

## 📖 How It Works
## 📖 工作原理

### Step 1: Document → Knowledge Graph
### 步骤 1：文档 → 知识图谱

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Document      │ ──► │  LLM Extraction  │ ──► │ Knowledge Graph │
│   (Text/PDF)    │     │  (Entities+Rels) │     │    (Neo4j)      │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

The LLM extracts:
`LLM` 会提取：
- **Entities**: People, organizations, concepts, technologies
  **实体**：人物、组织、概念、技术
- **Relationships**: How entities connect (e.g., "works_for", "created", "uses")
  **关系**：实体如何连接（例如 `works_for`、`created`、`uses`）
- **Provenance**: Source document and chunk for each extraction
  **来源**：每次提取对应的来源文档和文本块

### Step 2: Query → Multi-hop Traversal
### 步骤 2：查询 → 多跳遍历

```
┌─────────┐     ┌─────────────┐     ┌─────────────┐     ┌───────────┐
│  Query  │ ──► │  Find Start │ ──► │  Traverse   │ ──► │  Context  │
│         │     │   Entities  │     │  Relations  │     │  + Sources│
└─────────┘     └─────────────┘     └─────────────┘     └───────────┘
```

### Step 3: Answer → Verified Citations
### 步骤 3：回答 → 已验证引用

```
┌─────────────┐     ┌─────────────┐     ┌──────────────────┐
│   Context   │ ──► │  Generate   │ ──► │  Answer with     │
│ + Sources   │     │   Answer    │     │  [1][2] Citations│
└─────────────┘     └─────────────┘     └──────────────────┘
                                                │
                                                ▼
                                        ┌──────────────────┐
                                        │ Citation Details │
                                        │ • Source Doc     │
                                        │ • Source Text    │
                                        │ • Reasoning Path │
                                        └──────────────────┘
```

## 🖥️ Usage Example
## 🖥️ 使用示例

### 1. Add a Document
### 1. 添加文档

Paste or select a sample document. The system extracts entities and relationships:
粘贴或选择一个示例文档。系统会提取实体和关系：

```
Document: "GraphRAG was developed by Microsoft Research. 
           Darren Edge led the project..."

Extracted:
  ├── Entity: GraphRAG (TECHNOLOGY)
  ├── Entity: Microsoft Research (ORGANIZATION)  
  ├── Entity: Darren Edge (PERSON)
  └── Relationship: Darren Edge --[WORKS_FOR]--> Microsoft Research
```

### 2. Ask a Question
### 2. 提问

```
Question: "Who developed GraphRAG and what organization are they from?"
```

### 3. Get Verified Answer
### 3. 获取已验证回答

```
Answer: GraphRAG was developed by researchers at Microsoft Research [1], 
        with Darren Edge leading the project [2].

Citations:
  [1] Source: AI Research Paper
      Text: "GraphRAG is a technique developed by Microsoft Research..."
      
  [2] Source: AI Research Paper  
      Text: "...introduced by researchers including Darren Edge..."
```

## 🔧 Configuration
## 🔧 配置

| Setting<br>设置 | Default<br>默认值 | Description<br>描述 |
|---------|---------|-------------|
| Neo4j URI<br>`Neo4j URI` 设置 | `bolt://localhost:7687` | Neo4j connection string<br>`Neo4j` 连接字符串 |
| Neo4j User<br>`Neo4j` 用户 | `neo4j` | Database username<br>数据库用户名 |
| Neo4j Password<br>`Neo4j` 密码 | - | Database password<br>数据库密码 |
| LLM Model<br>`LLM` 模型 | `llama3.2` | Ollama model for extraction/generation<br>用于提取和生成的 `Ollama` 模型 |

## 🏗️ Architecture
## 🏗️ 架构

```
knowledge_graph_rag_citations/
├── knowledge_graph_rag.py   # Main Streamlit application
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

### Key Components
### 核心组件

- **`KnowledgeGraphManager`**: Neo4j interface for graph operations
  **`KnowledgeGraphManager`**：用于图操作的 `Neo4j` 接口
- **`extract_entities_with_llm()`**: LLM-based entity/relationship extraction
  **`extract_entities_with_llm()`**：基于 `LLM` 的实体/关系提取
- **`generate_answer_with_citations()`**: Multi-hop RAG with provenance tracking
  **`generate_answer_with_citations()`**：带来源跟踪的多跳 `RAG`

## 🎓 Learn More
## 🎓 了解更多

This example is inspired by [VeritasGraph](https://github.com/bibinprathap/VeritasGraph), an enterprise-grade framework for:
此示例受 [VeritasGraph](https://github.com/bibinprathap/VeritasGraph) 启发，后者是一个企业级框架，用于：
- On-premise knowledge graph RAG
  本地部署的知识图谱 `RAG`
- Visual reasoning traces (Veritas-Scope)
  可视化推理轨迹（`Veritas-Scope`）
- LoRA-tuned LLM integration
  `LoRA` 微调的 `LLM` 集成

## 📝 License
## 📝 许可证

MIT License
`MIT License` 许可证
