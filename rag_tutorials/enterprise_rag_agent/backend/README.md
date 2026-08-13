# Enterprise RAG Agent Backend

企业级 RAG 后端，目录按职责拆分：

- `app.py`：CLI 和 API 启动入口
- `enterprise_rag_agent/core/`：配置和领域模型
- `enterprise_rag_agent/ingestion/`：文档接入、解析、切块
- `enterprise_rag_agent/storage/`：SQLite 存储
- `enterprise_rag_agent/retrieval/`：检索与路由
- `enterprise_rag_agent/security/`：权限控制
- `enterprise_rag_agent/evaluation/`：答案评估
- `enterprise_rag_agent/llm/`：大模型调用
- `enterprise_rag_agent/application/`：服务编排与问答逻辑
- `enterprise_rag_agent/api/`：FastAPI 路由
- `sample_docs/`：示例知识库文档
- `tests/`：单元测试

## 启动

```bash
pip install -r requirements.txt
python app.py
```

默认会启动 API 服务；首次使用时可以再执行：

```bash
python app.py ingest sample_docs
python app.py ask "安全事件怎么升级？"
```

## 模型配置

通过 OpenAI 兼容接口支持 ChatGPT 和 DeepSeek。

ChatGPT：

```env
ENTERPRISE_RAG_LLM_PROVIDER=chatgpt
ENTERPRISE_RAG_MODEL=gpt-4o-mini
OPENAI_API_KEY=...
ENTERPRISE_RAG_LLM_BASE_URL=https://api.openai.com/v1
```

DeepSeek：

```env
ENTERPRISE_RAG_LLM_PROVIDER=deepseek
ENTERPRISE_RAG_MODEL=deepseek-chat
ENTERPRISE_RAG_LLM_API_KEY=...
ENTERPRISE_RAG_LLM_BASE_URL=https://api.deepseek.com
```
