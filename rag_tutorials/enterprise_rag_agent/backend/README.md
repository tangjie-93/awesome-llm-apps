# Enterprise RAG Agent Backend

企业级 RAG 后端，目录按职责拆分：

- `app.py`：CLI 和 API 启动入口
- `core/`：配置和领域模型
- `ingestion/`：文档接入、解析、切块
- `storage/`：SQLite 存储
- `retrieval/`：检索与路由
- `security/`：权限控制
- `evaluation/`：答案评估
- `llm/`：大模型调用
- `application/`：服务编排与问答逻辑
- `api/`：FastAPI 路由
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
