# 公司级 `RAG` 落地实施指南

本文档基于 `rag_tutorials` 目录下的 `23` 个 `README.md` 和主要代码实现整理，目标是帮助你从教程项目过渡到可在公司真实落地的 `RAG` 系统。

这里的重点不是再做一个 `Demo`，而是梳理公司级项目需要具备的能力：数据治理、权限、混合检索、重排序、引用、评估、监控、失败诊断、增量更新和可运维架构。

## 1. 总体结论

`rag_tutorials` 覆盖了公司级 `RAG` 的主要技术积木：

| 能力方向 | 对应项目 | 核心技术 |
| --- | --- | --- |
| 基础文档 `RAG` | `rag_chain`、`llama3.1_local_rag` | `LangChain`、`Chroma`、`Gemini`、`Ollama` |
| 智能体式 `RAG` | `agentic_rag_gpt5`、`agentic_rag_with_reasoning`、`agentic_rag_embedding_gemma` | `Agno`、`LanceDB`、`OpenAI`、`Gemini`、`Ollama` |
| 本地私有化 `RAG` | `local_rag_agent`、`qwen_local_rag`、`deepseek_local_rag_agent` | `Ollama`、`Qdrant`、`Qwen`、`DeepSeek`、`Llama` |
| 混合检索 `RAG` | `hybrid_search_rag`、`local_hybrid_search_rag` | `RAGLite`、`rerankers`、`PostgreSQL`、`SQLite` |
| 纠错式 `RAG` | `corrective_rag`、`ai_blog_search` | `LangGraph`、查询重写、相关性评分、`Web fallback` |
| 多数据库路由 | `rag_database_routing` | `Agno Router`、`Qdrant` 多库、`DuckDuckGo fallback` |
| 知识图谱 `RAG` | `knowledge_graph_rag_citations` | `Neo4j`、实体关系抽取、多跳推理、可验证引用 |
| 多模态 `RAG` | `vision_rag`、`multimodal_agentic_rag` | `Cohere Embed-4`、`Gemini Embedding 2`、`Google ADK` |
| 托管式 `RAG` | `contextualai_rag_agent`、`rag-as-a-service` | `Contextual AI`、`Ragie.ai`、`Claude` |
| 评估与诊断 | `agentic_rag_math_agent`、`rag_failure_diagnostics_clinic` | `DSPy`、`JEEBench`、失败模式分类、人工反馈 |

公司级落地建议：

1. 第一阶段不要直接做复杂 `Agent`，先把稳定的检索链路做好。
2. 基础架构优先选择 `hybrid search + rerank + citation + evaluation`。
3. 数据权限和引用可追溯比模型本身更重要。
4. 线上失败大多不是模型不够强，而是数据切块、索引过期、权限过滤、路由错误、重排序缺失、评估盲区导致。
5. 智能体能力适合第二阶段加入，用来做查询改写、多知识库路由、工具调用和失败自修复。

## 2. 公司级 `RAG` 推荐目标架构

推荐架构可以拆成 `8` 层：

| 层级 | 职责 | 推荐技术 |
| --- | --- | --- |
| 数据接入层 | 接入 `PDF`、网页、文档系统、知识库、工单、数据库、图片、音视频 | `PyPDFLoader`、`WebBaseLoader`、`PyMuPDF`、`BeautifulSoup`、自定义连接器 |
| 数据处理层 | 清洗、切块、摘要、元数据抽取、权限标记、版本管理 | `LangChain TextSplitter`、`LlamaIndex NodeParser`、自定义解析器 |
| 索引层 | 向量索引、关键词索引、图谱索引、元数据索引 | `Qdrant`、`pgvector`、`OpenSearch`、`Neo4j` |
| 检索层 | 查询改写、混合检索、过滤、重排序、上下文压缩 | `RAGLite`、`rerankers`、`Cohere Rerank`、`LangGraph` |
| 生成层 | 基于上下文生成回答、拒答、引用、结构化输出 | `OpenAI`、`Gemini`、`Claude`、本地 `Ollama` 模型 |
| 智能体层 | 多库路由、工具调用、检索策略选择、失败回退 | `Agno`、`LangGraph`、`Google ADK` |
| 评估层 | 离线评测、线上反馈、答案忠实度、引用准确率 | `DSPy`、自定义 `LLM-as-judge`、人工标注集 |
| 运维层 | 增量同步、索引重建、监控、审计、缓存、限流、租户隔离 | 队列、任务调度、日志平台、`PostgreSQL`、对象存储 |

一个可落地的主流程：

1. 用户提问。
2. 系统识别意图、业务域、权限范围。
3. 对查询做改写和扩展。
4. 根据业务域路由到一个或多个知识库。
5. 执行关键词检索和向量检索。
6. 合并候选片段并去重。
7. 使用 `reranker` 重新排序。
8. 做上下文压缩和引用组装。
9. 调用 `LLM` 生成带引用的回答。
10. 校验回答是否基于检索上下文。
11. 返回答案、引用、置信度和可追踪元数据。
12. 记录日志、反馈、耗时、成本和失败原因。

## 3. 关键知识点拆解

### 3.1 数据接入

教程项目中出现的数据源包括：

- `PDF` 文件上传。
- 网页 `URL`。
- 博客文章。
- 图片和 `PDF` 页面图。
- 音频、视频和多模态文件。
- 多个业务数据库。
- 托管式 `datastore`。

公司级项目需要比教程多做这些事情：

- 数据源连接器：对接 `Confluence`、`Notion`、`Google Drive`、`SharePoint`、内部文档库、客服系统、工单系统、`CRM`、代码仓库。
- 权限同步：文档级、段落级、部门级、租户级权限。
- 增量同步：新增、修改、删除都要反映到索引。
- 版本管理：同一文档多个版本，回答时需要知道命中哪个版本。
- 数据质量检查：空文档、扫描件、乱码、重复内容、过期内容、低质量 `OCR`。

建议设计的数据表：

| 表 | 作用 |
| --- | --- |
| `sources` | 原始数据源，例如文档、网页、工单、数据库记录 |
| `documents` | 解析后的文档对象 |
| `chunks` | 切分后的知识片段 |
| `embeddings` | 向量索引引用和 embedding 元信息 |
| `permissions` | 用户、部门、租户与文档权限 |
| `sync_jobs` | 同步任务状态 |
| `answer_logs` | 用户问题、检索结果、回答、引用、反馈 |

### 3.2 文档解析与切块

`rag_tutorials` 中主要用到：

- `RecursiveCharacterTextSplitter`
- `SentenceTransformersTokenTextSplitter`
- `LlamaIndex SimpleNodeParser`
- 自定义 word chunk
- `PyPDFLoader`
- `PyMuPDF`
- `WebBaseLoader`

切块是 `RAG` 质量的核心。公司级项目不要所有文档都用一个固定 `chunk_size`。

建议策略：

| 文档类型 | 切块策略 |
| --- | --- |
| `FAQ` | 一个问题和答案作为一个 chunk |
| 产品文档 | 按标题层级切块，保留章节路径 |
| 合同/制度 | 按条款切块，保留条款编号 |
| 财报/研报 | 按章节、表格、指标解释切块 |
| 客服工单 | 按问题、处理过程、最终结论切块 |
| 代码文档 | 按函数、类、模块切块 |
| 扫描件 `PDF` | 先做 `OCR`，再按版面结构切块 |

建议保留的元数据：

- `source_id`
- `document_id`
- `chunk_id`
- `title`
- `section_path`
- `page_number`
- `paragraph_index`
- `created_at`
- `updated_at`
- `version`
- `department`
- `tenant_id`
- `permission_tags`
- `source_url`
- `checksum`

### 3.3 `Embedding` 选型

项目里用到的 embedding 包括：

- `OpenAIEmbeddings`
- `text-embedding-3-small`
- `text-embedding-ada-002`
- `Gemini embedding-001`
- `text-embedding-004`
- `gemini-embedding-2`
- `Cohere embed-english-v3.0`
- `Cohere embed-v4.0`
- `EmbeddingGemma`
- `snowflake-arctic-embed`

公司选型考虑：

| 维度 | 说明 |
| --- | --- |
| 语言 | 是否支持中文、英文、混合语料 |
| 成本 | 批量入库成本和查询成本 |
| 维度 | 向量维度影响存储和检索性能 |
| 稳定性 | 模型是否长期可用，版本是否固定 |
| 部署 | 云端 `API` 还是本地私有化 |
| 多模态 | 是否支持图片、表格、`PDF` 页面、音频、视频 |
| 召回效果 | 对公司真实问题的 `Recall@K` |

建议：

- 普通企业中文知识库：优先选多语言强的 embedding。
- 成本敏感：用小模型 embedding + 强 `reranker`。
- 私有化部署：参考 `Ollama`、`EmbeddingGemma`、`snowflake-arctic-embed`。
- 多模态：参考 `Cohere Embed-4` 和 `Gemini Embedding 2`。
- 公司级必须固定 embedding 模型版本，否则索引重建和召回效果会漂移。

### 3.4 向量库和索引

项目中出现的存储：

| 存储 | 代表项目 | 适用场景 |
| --- | --- | --- |
| `Qdrant` | `qwen_local_rag`、`gemini_agentic_rag`、`rag_agent_cohere`、`corrective_rag` | 通用向量库，适合生产 |
| `LanceDB` | `agentic_rag_gpt5`、`agentic_rag_with_reasoning`、`agentic_rag_embedding_gemma` | 轻量、本地、开发快 |
| `Chroma` | `rag_chain`、`llama3.1_local_rag` | 教程、原型、本地实验 |
| `PgVector` | `autonomous_rag` | 已有 `PostgreSQL` 团队，运维简单 |
| `Neo4j` | `knowledge_graph_rag_citations` | 关系密集、多跳推理 |
| `RAGLite` 后端 | `hybrid_search_rag`、`local_hybrid_search_rag` | 混合检索和重排序实验 |
| 托管式平台 | `contextualai_rag_agent`、`rag-as-a-service` | 快速落地、少运维 |

公司级推荐：

- 如果团队没有强数据库偏好，优先 `Qdrant`。
- 如果公司已有成熟 `PostgreSQL` 运维，先用 `pgvector` 可以降低复杂度。
- 如果需要强关键词检索，搭配 `OpenSearch` 或 `Elasticsearch`。
- 如果业务依赖实体关系、供应链、组织结构、法规条款关联，补充 `Neo4j`。
- 如果只是原型，不建议一开始上太多组件。

### 3.5 检索策略

教程项目展示了多种检索方式：

- 普通向量相似度检索。
- 相似度阈值过滤。
- `Top-K` 检索。
- 多知识库检索。
- 查询重写。
- `Web fallback`。
- 混合检索。
- 重排序。
- 多跳图检索。
- 多模态 embedding 检索。

公司级推荐默认链路：

1. `Query normalization`：清洗问题，识别语言、时间、实体。
2. `Query rewrite`：补全缩写、业务术语、上下文。
3. `Query routing`：选择知识库、业务域、租户、权限范围。
4. `Metadata filter`：先按权限、部门、文档类型过滤。
5. `Hybrid search`：关键词检索 + 向量检索。
6. `Merge and dedupe`：合并候选并去重。
7. `Rerank`：使用跨编码器或 `LLM rerank`。
8. `Context compression`：压缩冗余内容。
9. `Citation assembly`：保留来源、页码、段落。
10. `Answer generation`：生成回答。
11. `Grounding check`：检查答案是否有依据。

### 3.6 混合检索

`hybrid_search_rag` 和 `local_hybrid_search_rag` 是公司级最值得参考的方向之一。

单纯向量检索的问题：

- 对编号、型号、精确术语不敏感。
- 对短查询不稳定。
- 对表格、代码、金额、日期召回差。
- 对领域专有名词可能误召回。

混合检索建议：

- 用关键词检索覆盖精确匹配。
- 用向量检索覆盖语义匹配。
- 用 `reranker` 做最终排序。
- 对用户问题中的实体、产品名、工单号、合同编号强制走关键词过滤。

推荐得分融合方式：

| 方法 | 说明 |
| --- | --- |
| 加权融合 | `score = alpha * vector_score + beta * keyword_score` |
| `RRF` | `Reciprocal Rank Fusion`，适合融合多个排序结果 |
| 分阶段召回 | 先大规模召回，再统一重排序 |
| 规则优先 | 命中编号、标题、强实体时优先 |

### 3.7 重排序

重排序是从 `Demo RAG` 到公司级 `RAG` 的关键一步。

建议：

- 初始召回 `Top 30` 到 `Top 100`。
- 用 `reranker` 选出 `Top 5` 到 `Top 12`。
- 回答时只使用重排序后的高质量上下文。

可选技术：

- `rerankers`
- `Cohere Rerank`
- `bge-reranker`
- `LLM-as-reranker`
- 业务规则重排，例如文档版本、发布时间、权威等级。

### 3.8 多知识库路由

`rag_database_routing` 展示了公司内部常见需求：不同知识应该进入不同数据库或 collection，例如：

- 产品文档。
- 客服 `FAQ`。
- 财务制度。
- 法务合同。
- 人力政策。
- 研发技术文档。
- 销售资料。

推荐路由策略：

1. 先用显式元数据判断，例如用户所在部门、页面入口、知识库标签。
2. 再用向量相似度跨库粗召回。
3. 对低置信问题使用 `LLM router`。
4. 如果内部知识库无法回答，再进入外部搜索或拒答。

不要只依赖 `LLM router`，因为它可能误判业务域。生产系统应结合规则、向量得分和模型判断。

### 3.9 纠错式 `RAG`

`corrective_rag` 和 `ai_blog_search` 展示了一个非常重要的模式：

- 检索结果是否相关，需要评分。
- 如果不相关，应该重写查询。
- 如果内部知识库不足，可以走外部搜索。
- 如果仍然没有依据，应该拒答。

公司级建议加入这些节点：

| 节点 | 作用 |
| --- | --- |
| `relevance_grader` | 判断检索片段是否相关 |
| `query_rewriter` | 改写低质量查询 |
| `fallback_search` | 内部知识不足时补充外部信息 |
| `answer_grounding_checker` | 检查答案是否被上下文支持 |
| `refusal_policy` | 没有依据时拒答 |

### 3.10 引用和可验证性

`knowledge_graph_rag_citations` 展示了公司级必须具备的能力：答案可追溯。

回答中至少应返回：

- 命中文档标题。
- 来源系统。
- 页码或段落位置。
- 原文片段。
- 文档版本。
- 更新时间。
- 权限范围。
- 相关性得分。

对于高风险业务，例如法务、财务、医疗、合规，建议每个关键结论都能追溯到引用，而不是只在末尾列几个来源。

### 3.11 知识图谱 `RAG`

知识图谱不是所有公司都必须一开始做，但在以下场景很有价值：

- 公司组织架构。
- 产品组件依赖。
- 客户、合同、订单、工单关系。
- 法规条款之间的引用关系。
- 供应链、资产、设备关系。
- 多跳问题，例如“这个客户受哪个合同条款影响，责任部门是谁”。

`knowledge_graph_rag_citations` 的核心模式：

1. 从文档中抽取实体。
2. 抽取实体关系。
3. 存入 `Neo4j`。
4. 查询时找到起点实体。
5. 沿关系多跳遍历。
6. 生成带来源引用的答案。

公司级建议先做“轻图谱”：

- 抽取实体和关系。
- 保留实体到原文 chunk 的引用。
- 查询时图谱检索和向量检索互补。

### 3.12 多模态 `RAG`

`vision_rag` 和 `multimodal_agentic_rag` 覆盖了图片、`PDF` 页面、音频、视频的检索。

适用场景：

- 财报图表问答。
- 产品设计图。
- 扫描件合同。
- 设备图片。
- 培训视频。
- 会议录音。
- 保险理赔图片。

技术路线：

- 图片或页面转 embedding。
- 文本问题转 embedding。
- 用余弦相似度找最相关图片或页面。
- 把图片和问题交给多模态模型回答。

注意：

- 多模态文件要放对象存储，不要直接塞数据库。
- 需要保存缩略图、原始文件、页面编号、时间戳。
- 对 `PDF` 页面图，最好同时保留 `OCR` 文本和视觉 embedding。

## 4. 推荐技术选型

### 4.1 快速上线版本

适合 `1` 到 `2` 个月内做公司内部知识助手。

| 模块 | 选择 |
| --- | --- |
| 后端 | `FastAPI` |
| 前端 | `React` 或公司内部平台 |
| 文档解析 | `PyPDFLoader`、`PyMuPDF`、自定义解析器 |
| 向量库 | `Qdrant` 或 `pgvector` |
| 关键词检索 | `PostgreSQL full-text` 或 `OpenSearch` |
| `Embedding` | 云端 embedding 或本地 embedding |
| 生成模型 | `OpenAI`、`Gemini`、`Claude` 或公司私有模型 |
| 编排 | 先用自定义服务流程，不急着上复杂 `Agent` |
| 评估 | 自定义评测集 + `LLM-as-judge` + 人工抽检 |
| 监控 | 日志、耗时、检索命中、用户反馈 |

### 4.2 私有化版本

适合强合规或数据不能出内网的公司。

| 模块 | 选择 |
| --- | --- |
| `LLM` | `Qwen`、`DeepSeek`、`Llama`、公司内模 |
| 模型服务 | `Ollama`、`vLLM`、`TGI` |
| `Embedding` | `EmbeddingGemma`、`bge`、`snowflake-arctic-embed` |
| 向量库 | `Qdrant`、`Milvus`、`pgvector` |
| 检索 | 混合检索 + 本地 `reranker` |
| 部署 | `Docker`、`Kubernetes` |
| 监控 | `Prometheus`、日志系统、链路追踪 |

### 4.3 高准确率版本

适合公司知识复杂、准确率要求高的场景。

| 能力 | 选择 |
| --- | --- |
| 多路召回 | 向量检索 + 关键词检索 + 图谱检索 |
| 重排序 | `reranker` 必选 |
| 查询改写 | `LLM` 改写 + 术语词典 |
| 权限过滤 | 检索前过滤和检索后校验双保险 |
| 引用 | 每个答案必须返回来源片段 |
| 评估 | 建立业务问题集和标准答案 |
| 诊断 | 失败分类、自动归因、回放能力 |

## 5. 公司级实施路线

### 阶段 0：需求和边界

先回答这些问题：

- 服务哪些部门？
- 数据源有哪些？
- 是否有敏感数据？
- 是否需要私有化？
- 是否允许外部模型 `API`？
- 用户最常问的 `50` 个问题是什么？
- 答案错误会造成什么风险？
- 是否必须给引用？
- 是否需要多轮对话？
- 是否需要操作业务系统，还是只做问答？

产出：

- 业务范围文档。
- 数据源清单。
- 权限模型。
- 风险分级。
- 首批 `golden questions`。

### 阶段 1：最小可用 `RAG`

目标：让内部用户能对一批文档提问，并返回带引用的答案。

必须实现：

- 文档上传或同步。
- 文档解析和切块。
- `Embedding` 入库。
- 向量检索。
- 元数据过滤。
- 回答生成。
- 引用返回。
- 基础日志。

暂时不要做：

- 复杂智能体。
- 多模态。
- 知识图谱。
- 自动执行业务操作。

### 阶段 2：准确率增强

加入：

- 关键词检索。
- 混合检索。
- 重排序。
- 查询改写。
- 相似度阈值。
- 上下文压缩。
- 答案依据校验。
- 拒答策略。

关键指标：

- `Recall@5`
- `Recall@10`
- `MRR`
- 答案忠实度。
- 引用准确率。
- 无依据回答率。

### 阶段 3：企业能力补齐

加入：

- 用户权限。
- 多租户隔离。
- 增量索引。
- 删除同步。
- 文档版本。
- 审计日志。
- 成本统计。
- 缓存。
- 失败回放。
- 管理后台。

### 阶段 4：高级能力

按业务需要加入：

- 多知识库路由。
- `Agentic RAG`。
- `Web fallback`。
- 知识图谱。
- 多模态检索。
- 自动诊断。
- 人工反馈闭环。

## 6. 推荐系统模块设计

### 6.1 后端服务

建议拆成这些服务或模块：

| 模块 | 职责 |
| --- | --- |
| `ingestion_service` | 数据接入、文件上传、同步任务 |
| `parser_service` | 文档解析、`OCR`、表格抽取 |
| `chunking_service` | 切块、摘要、元数据生成 |
| `index_service` | embedding、向量入库、关键词索引 |
| `retrieval_service` | 查询改写、检索、重排序 |
| `generation_service` | 组装 prompt、调用模型、生成答案 |
| `citation_service` | 来源引用、页码、片段定位 |
| `evaluation_service` | 离线评测、线上反馈、质量报表 |
| `admin_service` | 知识库管理、权限管理、索引重建 |

### 6.2 `API` 设计

建议至少提供：

| `API` | 用途 |
| --- | --- |
| `POST /documents/upload` | 上传文档 |
| `POST /sources/sync` | 同步数据源 |
| `POST /indexes/rebuild` | 重建索引 |
| `POST /chat` | 用户问答 |
| `POST /retrieve` | 只检索不生成，方便调试 |
| `GET /answers/{id}` | 查询历史回答 |
| `POST /feedback` | 用户反馈 |
| `GET /citations/{answer_id}` | 查看引用详情 |
| `GET /admin/metrics` | 查看质量和成本指标 |

### 6.3 Prompt 设计原则

公司级回答 prompt 必须明确：

- 只能基于检索上下文回答。
- 没有依据时必须拒答。
- 不能编造政策、金额、日期、流程。
- 必须保留引用。
- 对冲突信息要说明来源差异。
- 对过期信息要提示文档更新时间。
- 对高风险问题要建议咨询责任部门。

建议输出结构：

| 字段 | 说明 |
| --- | --- |
| `answer` | 直接回答 |
| `citations` | 引用列表 |
| `confidence` | 置信度 |
| `missing_info` | 缺失信息 |
| `follow_up_questions` | 推荐追问 |
| `debug` | 检索调试信息，仅内部可见 |

## 7. 评估体系

公司级 `RAG` 必须有评估，不然无法持续迭代。

### 7.1 离线评测集

至少准备：

- `100` 个真实用户问题。
- 每个问题的标准答案。
- 每个问题对应的正确来源文档。
- 难例：跨文档、多跳、旧版本、权限受限、答案不存在。

### 7.2 指标

| 指标 | 含义 |
| --- | --- |
| `Recall@K` | 正确文档是否出现在前 `K` 个检索结果中 |
| `MRR` | 正确文档排名是否靠前 |
| `Faithfulness` | 答案是否忠实于上下文 |
| `Citation Accuracy` | 引用是否真的支持答案 |
| `Answer Relevance` | 答案是否回答了问题 |
| `Refusal Accuracy` | 没有依据时是否正确拒答 |
| `Latency` | 端到端耗时 |
| `Cost per Query` | 单次问答成本 |
| `User Satisfaction` | 用户反馈满意度 |

### 7.3 线上反馈

需要记录：

- 用户问题。
- 改写后的问题。
- 命中的 chunk。
- 最终上下文。
- 模型回答。
- 引用。
- 用户点赞/点踩。
- 用户纠错文本。
- 耗时。
- 成本。
- 错误类型。

## 8. 常见失败模式和修复

参考 `rag_failure_diagnostics_clinic`，公司级常见问题包括：

| 失败模式 | 典型表现 | 修复方向 |
| --- | --- | --- |
| 检索幻觉 | 答案和检索文档矛盾 | 加 grounding check 和引用校验 |
| 切块错误 | 关键信息被切断 | 按结构切块，增加 overlap |
| `Embedding` 不匹配 | 语义相近但召回错误 | 换 embedding、加关键词检索、加 rerank |
| 索引过期 | 文档更新但答案仍旧 | 增量同步和版本校验 |
| 路由错误 | 问题进入错误知识库 | 规则 + 向量 + `LLM` 多级路由 |
| 长链推理漂移 | 多步问题逐渐偏离 | 分解问题，中间结果校验 |
| 工具误用 | `Agent` 调错工具 | 工具 schema、权限和调用前校验 |
| 会话记忆污染 | 用户之间或轮次间串数据 | 会话隔离和租户隔离 |
| 评估盲区 | 测试通过但线上失败 | 加真实问题集和失败回放 |
| 配置漂移 | 本地可用，生产失败 | 环境配置审计和启动检查 |
| 多租户干扰 | A 用户看到 B 用户数据 | 检索前权限过滤和审计 |

## 9. 权限和安全

公司级 `RAG` 必须默认不信任任何检索结果。

最低要求：

- 检索前做权限过滤。
- 检索后再次校验 chunk 权限。
- 引用只展示用户有权查看的来源。
- 不把敏感原文发送给无权限模型或外部服务。
- 记录谁问了什么、命中了什么、回答了什么。
- 支持数据删除和索引删除。
- 支持租户隔离。

高风险数据建议：

- 文档入库前做敏感信息分类。
- 对外部模型调用做脱敏。
- 对回答做敏感信息输出检查。
- 对管理员操作做审计。

## 10. 推荐你基于这些项目组合实现

如果你要真正实现一个公司级项目，建议这样组合：

### 第一版

参考：

- `hybrid_search_rag`
- `rag_chain`
- `rag_agent_cohere`

实现：

- `FastAPI` 后端。
- `Qdrant` 或 `pgvector` 向量库。
- 关键词检索。
- 混合检索。
- `reranker`。
- 引用返回。
- 简单管理后台。

### 第二版

参考：

- `corrective_rag`
- `ai_blog_search`
- `rag_database_routing`

加入：

- 查询重写。
- 相关性评分。
- 多知识库路由。
- `Web fallback`。
- 拒答策略。

### 第三版

参考：

- `knowledge_graph_rag_citations`
- `rag_failure_diagnostics_clinic`
- `agentic_rag_math_agent`

加入：

- 知识图谱。
- 失败诊断。
- 离线评估。
- 人工反馈闭环。

### 第四版

参考：

- `vision_rag`
- `multimodal_agentic_rag`

加入：

- 图片和 `PDF` 页面检索。
- 多模态问答。
- 音视频资料检索。

## 11. 一个推荐的公司级技术栈

如果没有强约束，建议：

| 模块 | 推荐 |
| --- | --- |
| 后端 | `Python` + `FastAPI` |
| 异步任务 | `Celery`、`RQ` 或公司已有队列 |
| 主数据库 | `PostgreSQL` |
| 向量库 | `Qdrant` |
| 关键词检索 | `OpenSearch` 或 `PostgreSQL full-text` |
| 对象存储 | `S3`、`MinIO` 或公司内部对象存储 |
| `Embedding` | 云端高质量 embedding 或本地 `bge/EmbeddingGemma` |
| `Rerank` | `Cohere Rerank`、`bge-reranker` 或 `rerankers` |
| `LLM` | `OpenAI`、`Gemini`、`Claude`、`Qwen`、`DeepSeek` |
| 编排 | 先自定义流程，后续加 `LangGraph` 或 `Agno` |
| 评估 | 自定义评测集 + `LLM-as-judge` + 人工抽检 |
| 可观测性 | 日志、指标、链路追踪、成本统计 |

## 12. 最小可落地里程碑

### 第 `1` 周：需求和数据准备

- 确定 `1` 个部门或 `1` 个业务场景。
- 收集 `50` 到 `100` 个真实问题。
- 整理首批文档。
- 明确权限边界。

### 第 `2` 到 `3` 周：基础 `RAG`

- 完成文档上传和解析。
- 完成切块和 embedding。
- 完成向量检索。
- 完成基础回答和引用。

### 第 `4` 到 `5` 周：准确率增强

- 加关键词检索。
- 加重排序。
- 加查询改写。
- 加拒答策略。
- 跑第一版评测。

### 第 `6` 到 `8` 周：生产化

- 加权限。
- 加增量同步。
- 加日志和监控。
- 加反馈。
- 加管理后台。
- 做灰度发布。

## 13. 上线前检查清单

上线前至少确认：

- 所有回答都有引用。
- 无依据问题能拒答。
- 用户只能检索自己有权限的文档。
- 删除文档后索引同步删除。
- 文档更新后索引能增量刷新。
- 能查看一次回答命中了哪些 chunk。
- 能复现一次错误回答的完整链路。
- 有离线评测集。
- 有线上反馈入口。
- 有成本和延迟监控。
- 有模型超时和降级策略。
- 有外部 `API` 失败 fallback。
- 有管理员审计日志。

## 14. 最终建议

如果你的目标是公司真实落地，不要从“做一个聊天框”开始，而要从“可信知识服务”开始。

优先级应该是：

1. 数据质量。
2. 权限安全。
3. 检索召回。
4. 重排序。
5. 引用可追溯。
6. 答案忠实度。
7. 评估闭环。
8. 监控和运维。
9. 智能体能力。
10. 多模态和知识图谱。

`RAG` 项目真正难的部分不是调用 `LLM API`，而是让公司知识能够被稳定、可控、可审计地检索和使用。
