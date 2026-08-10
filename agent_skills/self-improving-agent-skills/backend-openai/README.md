# OpenAI Backend
# OpenAI 后端

FastAPI backend that reimplements the self-improving skill loop with the OpenAI Responses API while preserving the existing frontend API contract.

这个 `FastAPI` 后端使用 `OpenAI Responses API` 重新实现自我改进 `skill` 循环，同时保留现有前端的 `API` 契约。

## Setup / 配置

```bash
cd backend-openai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the server:

运行服务：

```bash
OPENAI_API_KEY=sk-... python app.py
# http://localhost:8892
```

The UI can also send the API key with each request, so `OPENAI_API_KEY` is optional for local UI use.

前端界面也可以随每个请求发送 `API key`，因此本地通过界面使用时，`OPENAI_API_KEY` 是可选的。

## Defaults / 默认值

- Provider: `openai`
- Default model: `gpt-5-mini`
- Port: `8892`
- Upload limits: same as the Gemini backend (`10MB` total, `1MB` per file, `50` files)

## API Compatibility / API 兼容性

This backend supports the same endpoints as `backend/`, including:

该后端支持与 `backend/` 相同的端点，包括：

- `POST /api/upload`
- `POST /api/upload-files`
- `POST /api/analyze`
- `POST /api/regenerate`
- `POST /api/update-config`
- `POST /api/start/{session_id}`
- `POST /api/stop/{session_id}`
- `GET /api/status/{session_id}`
- `GET /api/download/{session_id}`
- `GET /api/examples`
- `POST /api/examples/{name}/load`
- `GET /health`

Request bodies accept `api_key`, `openai_api_key`, and legacy `gemini_api_key` for frontend compatibility.

请求体支持 `api_key`、`openai_api_key`，以及用于前端兼容的旧字段 `gemini_api_key`。

## Tests / 测试

```bash
python3 -m unittest discover tests -v
```
