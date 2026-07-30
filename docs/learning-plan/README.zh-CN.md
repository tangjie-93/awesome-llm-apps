# AI Agent 学习计划

本计划与项目导航分离维护。项目路径、架构分类和阅读索引见 [Code Graph](../code-graph/PROJECT_CODE_GRAPH.zh-CN.md)；这里仅定义学习顺序、需要掌握的内容、每天的行动和可验收产出。

## 使用规则

- 每周学习 5 天，每天 60-90 分钟；第 6、7 天用于补课、复盘或休息。
- 每天开始前先阅读目标示例的 `README`、依赖文件和入口文件；不要把仓库根目录当成统一运行入口。
- 每天只验证一个假设。运行记录中不得写入 API Key、访问令牌或个人数据。
- 当天结束必须完成对应周目录中的学习笔记；运行输入、失败现象和改动依据必须在当天记录。
- 每日笔记使用统一模板：[每日学习笔记](daily-notes/README.zh-CN.md)。

## 阶段目标

| 阶段 | 周次 | 学习内容 | 阶段产出 |
| --- | --- | --- | --- |
| 基础闭环 | 0-2 | Agent 运行、提示词、结构化输出 | 可重复运行的单 Agent 与结构化任务样例 |
| 行动与状态 | 3-5 | 工具调用、会话、上下文、校验、追踪 | 含受控工具和失败定位记录的 Agent |
| 知识与连接 | 6-8 | RAG、检索评估、MCP 权限边界 | 带来源的知识库问答和 MCP 调用审计 |
| 编排与产品化 | 9-11 | 多 Agent、Skills、定时任务、UI/语音 | 个人技术情报 Agent 的最小可用版本 |

## 按周学习文档

| 周次 | 学习文档 | 主线 |
| --- | --- | --- |
| 0 | [环境与最小 Agent](./week-00-setup/README.zh-CN.md) | 环境变量、模型调用、运行入口 |
| 1 | [单 Agent](./week-01-single-agent/README.zh-CN.md) | 指令、输入样例、输出质量 |
| 2 | [结构化输出](./week-02-structured-output/README.zh-CN.md) | Schema、解析、校验失败 |
| 3 | [工具调用](./week-03-tools/README.zh-CN.md) | 工具定义、参数限制、失败回传 |
| 4 | [运行与会话](./week-04-runtime-sessions/README.zh-CN.md) | 同步、异步、流式、会话边界 |
| 5 | [可靠性](./week-05-reliability/README.zh-CN.md) | 上下文、Guardrail、Tracing |
| 6 | [基础 RAG](./week-06-rag-basics/README.zh-CN.md) | 切分、嵌入、召回、引用 |
| 7 | [RAG 诊断](./week-07-rag-diagnostics/README.zh-CN.md) | 混合检索、重排、失败归因 |
| 8 | [MCP](./week-08-mcp/README.zh-CN.md) | Server、Tool、权限、审计 |
| 9 | [多 Agent](./week-09-multi-agent/README.zh-CN.md) | 拆分、交接契约、聚合 |
| 10 | [Skills 与调度](./week-10-skills-automation/README.zh-CN.md) | 可复用工作流、幂等、重试 |
| 11 | [产品入口](./week-11-product-interface/README.zh-CN.md) | UI/语音、状态、人工接管 |

## 验收与毕业项目

毕业项目为“个人技术情报 Agent”：定时收集指定来源，以 RAG 检索和去重，通过 MCP 写入受控目标，并展示每日简报。

- 每条结论可追溯到来源。
- 失败任务可观察、可定位，且不会无限重试。
- 写入动作有权限边界和审计记录。
- 用户可看到任务的加载、失败、成功状态。

每周末在当周最后一篇笔记中回答：本周最重要的概念是什么？证据是什么？失败发生在哪一层？下周要验证的一个假设是什么？
