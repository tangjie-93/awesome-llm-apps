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

快速跳转：

- [第 0 周：环境与最小 Agent](week-00-setup/README.zh-CN.md)
- [第 1 周：单 Agent](week-01-single-agent/README.zh-CN.md)
- [第 2 周：结构化输出](week-02-structured-output/README.zh-CN.md)
- [第 3 周：工具调用](week-03-tools/README.zh-CN.md)
- [第 4 周：运行与会话](week-04-runtime-sessions/README.zh-CN.md)
- [第 5 周：可靠性](week-05-reliability/README.zh-CN.md)
- [第 6 周：基础 RAG](week-06-rag-basics/README.zh-CN.md)
- [第 7 周：RAG 诊断](week-07-rag-diagnostics/README.zh-CN.md)
- [第 8 周：MCP](week-08-mcp/README.zh-CN.md)
- [第 9 周：多 Agent](week-09-multi-agent/README.zh-CN.md)
- [第 10 周：Skills 与调度](week-10-skills-automation/README.zh-CN.md)
- [第 11 周：产品入口](week-11-product-interface/README.zh-CN.md)

| 周次 | 学习文档 | 主线 |
| --- | --- | --- |
| 0 | [环境与最小 Agent](week-00-setup/README.zh-CN.md) | 环境变量、模型调用、运行入口 |
| 1 | [单 Agent](week-01-single-agent/README.zh-CN.md) | 指令、输入样例、输出质量 |
| 2 | [结构化输出](week-02-structured-output/README.zh-CN.md) | Schema、解析、校验失败 |
| 3 | [工具调用](week-03-tools/README.zh-CN.md) | 工具定义、参数限制、失败回传 |
| 4 | [运行与会话](week-04-runtime-sessions/README.zh-CN.md) | 同步、异步、流式、会话边界 |
| 5 | [可靠性](week-05-reliability/README.zh-CN.md) | 上下文、Guardrail、Tracing |
| 6 | [基础 RAG](week-06-rag-basics/README.zh-CN.md) | 切分、嵌入、召回、引用 |
| 7 | [RAG 诊断](week-07-rag-diagnostics/README.zh-CN.md) | 混合检索、重排、失败归因 |
| 8 | [MCP](week-08-mcp/README.zh-CN.md) | Server、Tool、权限、审计 |
| 9 | [多 Agent](week-09-multi-agent/README.zh-CN.md) | 拆分、交接契约、聚合 |
| 10 | [Skills 与调度](week-10-skills-automation/README.zh-CN.md) | 可复用工作流、幂等、重试 |
| 11 | [产品入口](week-11-product-interface/README.zh-CN.md) | UI/语音、状态、人工接管 |

## 具体项目与入口文件

下面这些链接直接指向仓库里的可运行示例。学习每一周时，优先打开对应项目的 README、依赖文件和入口脚本。

| 学习主题 | 示例目录 | 入口文件 |
| --- | --- | --- |
| 最小 Streamlit + LLM 应用 | [ai_reasoning_agent](../../starter_ai_agents/ai_reasoning_agent/README.md) | [reasoning_agent.py](../../starter_ai_agents/ai_reasoning_agent/reasoning_agent.py)、[local_ai_reasoning_agent.py](../../starter_ai_agents/ai_reasoning_agent/local_ai_reasoning_agent.py) |
| 博客转播客 | [ai_blog_to_podcast_agent](../../starter_ai_agents/ai_blog_to_podcast_agent/README.md) | [blog_to_podcast_agent.py](../../starter_ai_agents/ai_blog_to_podcast_agent/blog_to_podcast_agent.py) |
| 数据分析 | [ai_data_analysis_agent](../../starter_ai_agents/ai_data_analysis_agent/README.md) | [ai_data_analyst.py](../../starter_ai_agents/ai_data_analysis_agent/ai_data_analyst.py) |
| 数据可视化 | [ai_data_visualisation_agent](../../starter_ai_agents/ai_data_visualisation_agent/README.md) | [ai_data_visualisation_agent.py](../../starter_ai_agents/ai_data_visualisation_agent/ai_data_visualisation_agent.py) |
| 工具调用与网页抓取 | [web_scraping_ai_agent](../../starter_ai_agents/web_scraping_ai_agent/README.md) | [ai_scrapper.py](../../starter_ai_agents/web_scraping_ai_agent/ai_scrapper.py)、[local_ai_scrapper.py](../../starter_ai_agents/web_scraping_ai_agent/local_ai_scrapper.py) |
| 旅行规划 Agent | [ai_travel_agent](../../starter_ai_agents/ai_travel_agent/README.MD) | [travel_agent.py](../../starter_ai_agents/ai_travel_agent/travel_agent.py)、[local_travel_agent.py](../../starter_ai_agents/ai_travel_agent/local_travel_agent.py) |
| 多模态 Agent | [multimodal_ai_agent](../../starter_ai_agents/multimodal_ai_agent/README.md) | [mutimodal_agent.py](../../starter_ai_agents/multimodal_ai_agent/mutimodal_agent.py)、[multimodal_reasoning_agent.py](../../starter_ai_agents/multimodal_ai_agent/multimodal_reasoning_agent.py) |
| 医学影像多模态演示 | [ai_medical_imaging_agent](../../starter_ai_agents/ai_medical_imaging_agent/README.md) | [ai_medical_imaging.py](../../starter_ai_agents/ai_medical_imaging_agent/ai_medical_imaging.py) |
| 多智能体研究报告 | [openai_research_agent](../../starter_ai_agents/openai_research_agent/README.md) | [research_agent.py](../../starter_ai_agents/openai_research_agent/research_agent.py) |
| 创业趋势多 Agent 分析 | [ai_startup_trend_analysis_agent](../../starter_ai_agents/ai_startup_trend_analysis_agent/README.md) | [startup_trends_agent.py](../../starter_ai_agents/ai_startup_trend_analysis_agent/startup_trends_agent.py) |
| Mixture-of-Agents 聚合 | [mixture_of_agents](../../starter_ai_agents/mixture_of_agents/) | [mixture-of-agents.py](../../starter_ai_agents/mixture_of_agents/mixture-of-agents.py) |
| 保险顾问 Agent | [ai_life_insurance_advisor_agent](../../starter_ai_agents/ai_life_insurance_advisor_agent/README.md) | [life_insurance_advisor_agent.py](../../starter_ai_agents/ai_life_insurance_advisor_agent/life_insurance_advisor_agent.py) |
| 音乐生成 Agent | [ai_music_generator_agent](../../starter_ai_agents/ai_music_generator_agent/README.md) | [music_generator_agent.py](../../starter_ai_agents/ai_music_generator_agent/music_generator_agent.py) |
| 梗图生成与浏览器自动化 | [ai_meme_generator_agent_browseruse](../../starter_ai_agents/ai_meme_generator_agent_browseruse/README.md) | [ai_meme_generator_agent.py](../../starter_ai_agents/ai_meme_generator_agent_browseruse/ai_meme_generator_agent.py) |
| 金融分析 Agent | [xai_finance_agent](../../starter_ai_agents/xai_finance_agent/README.md) | [xai_finance_agent.py](../../starter_ai_agents/xai_finance_agent/xai_finance_agent.py) |

## 验收与毕业项目

毕业项目为“个人技术情报 Agent”：定时收集指定来源，以 RAG 检索和去重，通过 MCP 写入受控目标，并展示每日简报。

- 每条结论可追溯到来源。
- 失败任务可观察、可定位，且不会无限重试。
- 写入动作有权限边界和审计记录。
- 用户可看到任务的加载、失败、成功状态。

每周末在当周最后一篇笔记中回答：本周最重要的概念是什么？证据是什么？失败发生在哪一层？下周要验证的一个假设是什么？
