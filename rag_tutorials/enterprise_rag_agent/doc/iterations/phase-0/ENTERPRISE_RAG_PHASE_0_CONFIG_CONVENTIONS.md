# Enterprise RAG 阶段 0 配置约定

> 版本：v0.1
> 日期：2026-08-13

## 目的

统一阶段 0 的配置来源，避免业务边界散落在代码、前端和文档里。

## 必须存在的默认配置

- `ENTERPRISE_RAG_COMPANY`
- `ENTERPRISE_RAG_DB_PATH`
- `ENTERPRISE_RAG_DEFAULT_KB`
- `ENTERPRISE_RAG_CHUNK_SIZE`
- `ENTERPRISE_RAG_CHUNK_OVERLAP`
- `ENTERPRISE_RAG_TOP_K`
- `ENTERPRISE_RAG_RERANK_TOP_K`
- `ENTERPRISE_RAG_ENABLE_LLM`
- `ENTERPRISE_RAG_LLM_PROVIDER`
- `ENTERPRISE_RAG_MODEL`
- `ENTERPRISE_RAG_LLM_BASE_URL`
- `ENTERPRISE_RAG_DEFAULT_GROUPS`
- `ENTERPRISE_RAG_RISK_LEVELS`
- `ENTERPRISE_RAG_RISK_BY_GROUP`
- `ENTERPRISE_RAG_BUSINESS_DOMAINS`
- `ENTERPRISE_RAG_DOCUMENT_TYPES`
- `ENTERPRISE_RAG_EXCLUDED_SCOPES`

## 阶段 0 推荐值

- 默认知识库：`general`
- 默认文档权限组：`public`
- 默认业务组：`security`、`hr`、`it`、`ops`
- 默认风险映射：`low`、`medium`、`high`
- 默认组风险映射：`public:low`、`security:high`、`hr:medium`、`it:medium`、`ops:high`

## 阶段 0 可覆盖配置格式

- `ENTERPRISE_RAG_DEFAULT_GROUPS`：逗号分隔，例如 `public,security,hr,it,ops`
- `ENTERPRISE_RAG_RISK_LEVELS`：逗号分隔，例如 `low,medium,high`
- `ENTERPRISE_RAG_RISK_BY_GROUP`：逗号分隔的 `group:risk`，例如 `public:low,security:high,hr:medium`
- `ENTERPRISE_RAG_BUSINESS_DOMAINS`：逗号分隔的 `code:description`，例如 `security:安全制度,hr:入职培训`
- `ENTERPRISE_RAG_DOCUMENT_TYPES`：逗号分隔，例如 `Markdown,Text,FAQ`
- `ENTERPRISE_RAG_EXCLUDED_SCOPES`：逗号分隔，例如 `多租户隔离,自动执行动作`

## 约束规则

1. 业务边界相关信息不写死在前端页面。
2. 文档默认值可以来自 `.env.example`，但必须有文档说明。
3. 权限组和知识库列表应可被配置或初始化数据覆盖。
4. `high` 风险内容的处理方式必须在配置文档中明确。
5. 不同环境的数据库路径必须可配置。

## 配置分层

- 环境配置：公司名、数据库路径、模型开关、模型提供方
- 业务配置：知识库列表、权限组、风险等级、默认处理策略
- 运行配置：chunk 参数、top_k、rerank_top_k

## 不做

- 复杂配置中心接入
- 动态租户配置下发
- 在线灰度配置管理
