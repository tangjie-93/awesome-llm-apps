# `MCP AI Agents` 学习与实践指南

本文档基于 `mcp_ai_agents` 目录下的项目整理，面向正在学习 `AI Agent` 的开发者。重点回答三个问题：

1. 这个文件夹里有哪些内容？
2. 如果正在学习 `AI Agent`，哪些内容最值得学？
3. 学完后可以在哪些方向进行实践和落地？

## 1. 总体结论

`mcp_ai_agents` 是一组围绕 `MCP`（`Model Context Protocol`）构建的 `AI Agent` 示例。它们的共同目标是：让大模型不只会聊天，还能通过标准化协议连接外部工具和真实系统，例如 `GitHub`、`Notion`、浏览器、日历、邮件、旅行住宿、地图服务和多个专业工具服务器。

如果你正在学习 `AI Agent`，这个目录最有价值的地方在于它展示了：

- 如何把 `LLM` 和外部工具连接起来。
- 如何通过 `MCP server` 暴露工具能力。
- 如何让 `Agent` 根据自然语言选择工具、调用工具、组合结果。
- 如何把单工具 `Agent` 扩展成多工具、多服务、多专家 `Agent`。
- 如何设计权限、会话、记忆、路由、工具边界和失败回退。

一句话总结：这个目录适合学习“能操作真实软件和真实数据的 `AI Agent`”。

## 2. 目录项目地图

| 项目 | 类型 | 核心能力 | 主要技术 |
| --- | --- | --- | --- |
| `github_mcp_agent` | 单一服务 `MCP Agent` | 用自然语言分析 `GitHub` 仓库、`Issue`、`PR`、代码活动 | `Streamlit`、`Agno`、官方 `GitHub MCP Server`、`Docker`、`OpenAI` |
| `notion_mcp_agent` | 单一服务终端 `Agent` | 读取、修改、搜索 `Notion` 页面，支持会话记忆 | `Agno`、`MCPTools`、`Notion MCP Server`、`SQLite Memory`、`OpenAI` |
| `browser_mcp_agent` | 浏览器自动化 `Agent` | 用自然语言控制浏览器访问网页、点击、填表、截图、提取内容 | `mcp-agent`、`Playwright MCP`、`Streamlit`、`OpenAI-compatible API` |
| `multi_mcp_agent` | 多工具生产力助手 | 同时连接 `GitHub`、`Perplexity`、`Calendar`、`Gmail` 等服务 | `Agno`、`MultiMCPTools`、多个 `npx MCP server`、`OpenAI GPT-4o` |
| `multi_mcp_agent_router` | 多专家路由 `Agent` | 根据任务选择代码审查、安全审计、研究员、`BIM` 工程师等专家 | `Anthropic`、原生 `mcp ClientSession`、`stdio_client`、工具路由 |
| `ai_travel_planner_mcp_agent_team` | 业务型 `Agent Team` | 旅行规划，调用 `Airbnb MCP`、`Google Maps MCP`、`Google Search` 生成行程 | `Agno`、`MultiMCPTools`、`GoogleSearchTools`、`OpenAI`、`Streamlit` |

## 3. 你需要先理解的核心概念

### 3.1 什么是 `MCP`

`MCP` 可以理解为大模型和外部工具之间的标准协议。传统做法是每接一个工具就写一套自定义 `API adapter`，而 `MCP` 的价值是把工具暴露成统一协议，让 `Agent` 能通过标准方式发现工具、读取工具描述、调用工具并拿到结果。

在这些项目中，`MCP server` 通常通过以下方式启动：

- `npx` 启动，例如 `@modelcontextprotocol/server-github`、`@notionhq/notion-mcp-server`、`@playwright/mcp`。
- `Docker` 启动，例如官方 `GitHub MCP Server`。
- 自定义服务启动，例如旅行项目中的 `Google Maps MCP`。

### 3.2 `AI Agent` 和普通聊天机器人的区别

普通聊天机器人主要做文本生成。`AI Agent` 多了几个关键能力：

- 理解任务目标。
- 选择合适工具。
- 调用工具获取真实数据。
- 根据工具结果继续推理。
- 多轮执行直到完成任务。
- 维护会话状态和上下文。
- 对失败情况做重试、回退或解释。

这些项目里的 `Agent` 不是只回答问题，而是能真实访问 `GitHub`、操作 `Notion`、控制浏览器、规划日历、调用地图和住宿数据。

### 3.3 `MCP Agent` 的基本工作流

通用流程如下：

1. 用户输入自然语言任务。
2. `Agent` 读取系统提示词和可用工具列表。
3. `MCP client` 连接一个或多个 `MCP server`。
4. `Agent` 根据任务选择工具。
5. 工具通过 `MCP server` 调用真实服务。
6. `Agent` 接收工具结果。
7. 如果任务未完成，继续调用工具。
8. 最后汇总结果并返回用户。

### 3.4 学习重点

学习这个目录时，不要只看界面和效果，更要看这些工程问题：

- 工具是怎么注册给 `Agent` 的？
- `MCP server` 是怎么启动的？
- 凭据和密钥如何传入？
- 工具调用失败时怎么处理？
- 多个工具同时存在时如何选择？
- 如何避免一个 `Agent` 拥有过多工具？
- 如何维护用户会话和记忆？
- 如何限制工具权限？
- 如何让回答基于工具结果，而不是模型编造？

## 4. 项目逐个总结

### 4.1 `github_mcp_agent`

这是最适合入门的单服务 `MCP Agent`。

它做了什么：

- 使用官方 `GitHub MCP Server`。
- 通过自然语言查询仓库信息。
- 可以分析 `Issue`、`Pull Request`、仓库健康度、活动模式和代码趋势。
- 用 `Streamlit` 做界面。
- 用 `Agno Agent` 连接 `MCPTools`。
- 通过 `Docker` 运行官方 `GitHub MCP Server`。

你能学到：

- 如何把一个第三方服务通过 `MCP` 接给 `Agent`。
- 如何通过 `StdioServerParameters` 启动 `MCP server`。
- 如何给 `MCP server` 注入 `GitHub Token`。
- 如何设计面向代码仓库分析的系统提示词。
- 如何限制 `Agent` 基于 `GitHub API` 的事实回答。

适合实践：

- 公司内部仓库分析助手。
- `Issue` 分类和总结工具。
- `PR` 审查辅助工具。
- 开源项目健康度分析仪表盘。
- 自动生成周报：活跃 `Issue`、待审 `PR`、高风险改动。

### 4.2 `notion_mcp_agent`

这是一个终端式 `Notion Agent`，重点是“读写知识库”和“会话记忆”。

它做了什么：

- 连接 `Notion MCP Server`。
- 支持读取、更新、插入、搜索 `Notion` 页面。
- 可以创建段落、列表、表格、评论。
- 使用 `SQLite` 存储 `Agent` 记忆。
- 为每次会话生成 `user_id` 和 `session_id`。

你能学到：

- 如何接入企业知识工具。
- 如何让 `Agent` 不只读数据，还能写数据。
- 如何配置 `Notion Integration Token` 和页面权限。
- 如何做多轮对话记忆。
- 如何让 `Agent` 主动使用工具，而不是只靠模型回答。

适合实践：

- 会议纪要自动写入 `Notion`。
- 项目周报自动维护。
- 知识库问答和更新助手。
- 读文档后自动生成待办事项。
- 把聊天内容整理成 `Notion` 页面。

### 4.3 `browser_mcp_agent`

这是学习“浏览器自动化 `Agent`”的重点项目。

它做了什么：

- 使用 `mcp-agent` 框架。
- 连接 `Playwright MCP`。
- 用自然语言控制浏览器。
- 支持打开网页、点击按钮、滚动、填表、截图和内容提取。
- 支持 `OpenAI-compatible API`，可以配置为本地 `Ollama`。

你能学到：

- 如何把浏览器作为 `Agent` 的工具环境。
- 如何用 `MCP` 连接 `Playwright`。
- 如何处理异步 `Agent` 初始化和工具列表。
- 如何通过配置文件管理模型和密钥。
- 为什么浏览器自动化需要更强推理能力的模型。

适合实践：

- 自动化网页信息采集。
- 内部后台自动操作助手。
- 表单填写和流程测试。
- 网站内容总结。
- 竞品页面监控。
- `UI` 测试和验收辅助。

注意：

- 浏览器自动化有安全风险，不能随便给生产系统写权限。
- 需要限制访问域名、操作范围和敏感输入。
- 对支付、删除、发布等高风险操作要加人工确认。

### 4.4 `multi_mcp_agent`

这是一个多服务生产力助手，展示如何把多个 `MCP server` 合并给一个 `Agent`。

它做了什么：

- 同时连接多个 `MCP server`：
  - `GitHub`
  - `Perplexity`
  - `Calendar`
  - `Gmail`
- 使用 `Agno MultiMCPTools`。
- 通过 `OpenAI GPT-4o` 做核心模型。
- 使用 `SQLite` 保存会话记忆。
- 支持跨平台工作流，例如从研究结果到 `GitHub issue`，再到日历跟进。

你能学到：

- 如何管理多个 `MCP server`。
- 如何设计跨工具任务。
- 如何让一个 `Agent` 根据任务选择不同服务。
- 如何维护长期会话和上下文。
- 多工具 `Agent` 为什么需要清晰的工具使用规则。

适合实践：

- 个人研发助理。
- 项目管理助手。
- 研发工作流自动化。
- 邮件、日历、仓库联动。
- 信息检索后自动沉淀到任务系统。

风险点：

- 一个 `Agent` 拥有太多工具时，容易误调用。
- 不同服务权限混在一起，安全边界变复杂。
- 公司级场景建议加工具白名单、审批和审计日志。

### 4.5 `multi_mcp_agent_router`

这是这个目录里最值得深入学习的项目之一，因为它展示了“多专家 `Agent` + 工具隔离”的模式。

它做了什么：

- 定义多个专业 `Agent`：
  - 代码审查员。
  - 安全审计员。
  - 研究员。
  - `BIM/Revit` 工程师。
- 每个 `Agent` 有独立系统提示词。
- 每个 `Agent` 只连接自己需要的 `MCP server`。
- 用户请求可以自动路由，也可以手动选择专家。
- 使用 `Anthropic API` 调用 `Claude`。
- 使用原生 `mcp ClientSession` 和 `stdio_client` 管理工具连接。

你能学到：

- 为什么不要让一个 `Agent` 拥有所有工具。
- 如何按角色隔离工具权限。
- 如何把 `MCP tool schema` 转换成模型可用的工具格式。
- 如何实现工具调用循环。
- 如何把用户问题路由给合适的专家。
- 如何设计专业 `Agent` 的系统提示词。

适合实践：

- 公司内部多专家助手平台。
- 代码审查、安全审计、文档研究分工。
- 面向不同部门的专业 `Agent`。
- 工程设计、法务、财务、研发等角色型助手。
- 多工具权限隔离的 `Agent` 平台原型。

公司级价值：

这个项目体现了一个重要原则：工具越强，越需要隔离。生产环境里不要做“万能 `Agent`”，而应该做“路由器 + 专家 `Agent` + 最小工具权限”。

### 4.6 `ai_travel_planner_mcp_agent_team`

这是一个业务场景型 `Agent Team`，适合学习如何把多个实时数据源组织成完整业务流程。

它做了什么：

- 使用 `Airbnb MCP` 获取真实住宿数据。
- 使用 `Google Maps MCP` 做距离、路线和地点服务。
- 使用 `Google Search` 获取天气、餐厅、景点和本地信息。
- 使用 `OpenAI GPT-4o` 生成详细旅行计划。
- 用 `Streamlit` 提供交互界面。
- 支持导出 `.ics` 日历文件。

你能学到：

- 如何围绕一个业务目标设计 `Agent`。
- 如何组合多个实时工具。
- 如何写强约束任务提示词。
- 如何要求 `Agent` 主动使用所有工具。
- 如何把结果转成可下载的业务产物。

适合实践：

- 企业差旅规划助手。
- 销售拜访路线规划。
- 活动日程自动生成。
- 本地生活服务推荐。
- 任何需要“搜索 + 地图 + 业务约束 + 日程产物”的场景。

### 4.7 `browser_mcp_agent` 与 `multi_mcp_agent_router` 的组合价值

单独看 `browser_mcp_agent`，它是网页操作。单独看 `multi_mcp_agent_router`，它是专家路由。组合起来就能形成更强的实践方向：

- 一个研究员 `Agent` 使用浏览器抓取网页。
- 一个代码审查员 `Agent` 使用 `GitHub MCP` 分析仓库。
- 一个文档助手使用 `Notion MCP` 写入结论。
- 一个项目经理 `Agent` 使用日历和邮件安排后续动作。

这就是实际工作中 `Agentic Workflow` 的雏形。

## 5. 对学习 `AI Agent` 最有用的内容

如果你正在系统学习 `AI Agent`，建议重点学这些内容。

### 5.1 工具调用

核心问题：

- 模型如何知道有哪些工具？
- 工具参数如何定义？
- 工具结果如何返回给模型？
- 什么时候继续调用工具，什么时候停止？

对应项目：

- `github_mcp_agent`
- `browser_mcp_agent`
- `multi_mcp_agent_router`

### 5.2 外部系统连接

真实 `Agent` 必须连接业务系统，而不是只在文本里推理。

对应项目：

- `notion_mcp_agent`
- `github_mcp_agent`
- `multi_mcp_agent`
- `ai_travel_planner_mcp_agent_team`

### 5.3 多工具编排

一个复杂任务往往需要多个工具组合。

示例：

1. 用 `Perplexity` 查资料。
2. 用 `GitHub MCP` 建 `Issue`。
3. 用 `Calendar MCP` 安排会议。
4. 用 `Gmail MCP` 发总结邮件。

对应项目：

- `multi_mcp_agent`
- `ai_travel_planner_mcp_agent_team`

### 5.4 多专家路由

公司级 `Agent` 不应该是一个万能助手，而应该是多个专家协作。

对应项目：

- `multi_mcp_agent_router`

你需要学习：

- 用户意图分类。
- 专家 `Agent` 定义。
- 工具权限隔离。
- 每个专家独立记忆。
- 专家输出统一格式。

### 5.5 记忆和会话

`notion_mcp_agent` 和 `multi_mcp_agent` 都展示了会话 `ID` 和 `SQLite` 记忆。

你需要理解：

- 短期对话上下文。
- 长期用户偏好。
- 每个用户和会话如何隔离。
- 什么时候应该记，什么时候不应该记。
- 记忆是否需要用户授权。

### 5.6 权限和安全

`MCP Agent` 能操作真实系统，所以安全比普通聊天机器人更重要。

你需要关注：

- `API key` 和 `token` 管理。
- 最小权限原则。
- 工具白名单。
- 高风险操作确认。
- 审计日志。
- 用户隔离。
- 企业网络和防火墙限制。

## 6. 推荐学习顺序

### 阶段 1：理解单工具 `MCP Agent`

先学：

1. `github_mcp_agent`
2. `notion_mcp_agent`

目标：

- 理解 `MCP server` 怎么启动。
- 理解 `Agent` 怎么拿到工具。
- 理解自然语言如何转成工具调用。
- 理解凭据如何传给外部系统。

### 阶段 2：理解浏览器和真实交互

学习：

1. `browser_mcp_agent`

目标：

- 理解 `Playwright` 自动化。
- 理解浏览器作为 `Agent` 工具环境。
- 理解多步骤网页任务。

### 阶段 3：理解多工具助手

学习：

1. `multi_mcp_agent`
2. `ai_travel_planner_mcp_agent_team`

目标：

- 让一个 `Agent` 同时使用多个 `MCP server`。
- 学会跨平台工作流设计。
- 学会把工具结果合成业务产物。

### 阶段 4：理解多专家架构

学习：

1. `multi_mcp_agent_router`

目标：

- 学会按任务路由专家。
- 学会给不同专家分配不同工具。
- 学会实现工具隔离和专业化提示词。

## 7. 学完后可以做的实践方向

### 7.1 研发效率助手

可以做：

- 自动分析 `GitHub Issue`。
- 总结最近 `PR`。
- 识别长期未处理的 `bug`。
- 生成代码审查初稿。
- 把 `PR` 风险点写入 `Notion`。
- 自动创建后续任务。

适合参考：

- `github_mcp_agent`
- `multi_mcp_agent_router`
- `multi_mcp_agent`

### 7.2 个人或团队知识库助手

可以做：

- 查询 `Notion` 知识库。
- 自动整理会议纪要。
- 生成项目周报。
- 把对话总结写入文档。
- 搜索历史决策和任务。

适合参考：

- `notion_mcp_agent`
- `multi_mcp_agent`

### 7.3 浏览器自动化助手

可以做：

- 自动打开网页并提取信息。
- 自动填表。
- 自动下载页面数据。
- 自动做网站巡检。
- 自动测试内部后台流程。

适合参考：

- `browser_mcp_agent`

### 7.4 项目管理助手

可以做：

- 根据 `GitHub Issue` 安排会议。
- 把会议结论写入 `Notion`。
- 给相关人员发送邮件。
- 自动生成项目状态摘要。

适合参考：

- `multi_mcp_agent`

### 7.5 多专家企业助手平台

可以做：

- 代码审查专家。
- 安全审计专家。
- 文档研究专家。
- 产品需求分析专家。
- 运维排障专家。
- 财务制度问答专家。

适合参考：

- `multi_mcp_agent_router`

### 7.6 业务流程型 `Agent`

可以做：

- 差旅规划助手。
- 客户拜访路线规划。
- 活动日程生成。
- 销售线索研究。
- 招聘候选人信息整理。

适合参考：

- `ai_travel_planner_mcp_agent_team`

## 8. 如果要做公司级项目，应该怎么设计

### 8.1 推荐架构

公司级 `MCP Agent` 可以按以下架构设计：

| 模块 | 作用 |
| --- | --- |
| `User Interface` | `Web`、`CLI`、企业聊天工具入口 |
| `Router` | 判断用户意图，选择专家 `Agent` |
| `Specialist Agents` | 面向不同任务的专家 |
| `MCP Gateway` | 管理 `MCP server` 连接和工具权限 |
| `Tool Registry` | 记录工具 schema、权限、风险等级 |
| `Memory Store` | 用户记忆、会话历史、任务状态 |
| `Audit Log` | 记录工具调用、参数、结果、用户身份 |
| `Approval Layer` | 对高风险操作要求人工确认 |
| `Policy Engine` | 权限控制、数据脱敏、工具白名单 |

### 8.2 不建议一开始做万能 `Agent`

初学者很容易做一个“什么工具都有”的 `Agent`。这在演示中很酷，但在公司里风险很高。

更好的方式：

1. 一个路由器负责分类。
2. 每个专家只拿必要工具。
3. 高风险工具需要确认。
4. 所有工具调用写审计日志。
5. 用户权限影响工具可见性。

### 8.3 工具风险分级

建议把工具分成：

| 等级 | 类型 | 示例 | 策略 |
| --- | --- | --- | --- |
| `L1` | 只读工具 | 搜索、读取仓库、读取文档 | 可直接调用 |
| `L2` | 低风险写入 | 新建草稿、生成文档、创建本地文件 | 调用后提示用户确认 |
| `L3` | 业务写入 | 创建 `Issue`、写入 `Notion`、发邮件 | 调用前确认 |
| `L4` | 高风险操作 | 删除、支付、发布、改权限 | 默认禁止或强审批 |

### 8.4 公司级落地最低要求

上线前至少要有：

- 用户身份识别。
- 工具权限控制。
- `API key` 安全管理。
- 工具调用审计日志。
- 高风险操作确认。
- 超时和失败处理。
- 连接失败 fallback。
- 会话隔离。
- 敏感数据脱敏。
- 管理员可查看工具调用历史。

## 9. 建议你做的练手项目

### 9.1 第一个练手项目：`GitHub Repo Analyst`

目标：

- 输入仓库地址。
- 分析 `Issue`、`PR`、最近提交、活跃贡献者。
- 输出项目健康度报告。

参考：

- `github_mcp_agent`

你会练到：

- 单服务 `MCP` 接入。
- 工具调用。
- 事实型回答。
- `Streamlit` 界面。

### 9.2 第二个练手项目：`Notion Meeting Assistant`

目标：

- 用户输入会议内容。
- `Agent` 总结会议纪要。
- 写入指定 `Notion` 页面。
- 自动生成待办事项。

参考：

- `notion_mcp_agent`

你会练到：

- 写入型工具调用。
- 页面权限。
- 多轮对话。
- 记忆和会话。

### 9.3 第三个练手项目：`Browser Research Agent`

目标：

- 输入一个研究主题。
- 浏览器自动打开网页。
- 提取页面内容。
- 总结成报告。
- 保存到本地文件或 `Notion`。

参考：

- `browser_mcp_agent`
- `notion_mcp_agent`

你会练到：

- 浏览器自动化。
- 多步骤任务。
- 信息提取。
- 工具组合。

### 9.4 第四个练手项目：`Developer Productivity Agent`

目标：

- 查找最近高优先级 `Issue`。
- 总结相关背景。
- 搜索解决方案。
- 创建 `PR` 审查清单。
- 安排后续会议。

参考：

- `multi_mcp_agent`

你会练到：

- 多个 `MCP server`。
- 跨平台工作流。
- 任务链式执行。
- 会话记忆。

### 9.5 第五个练手项目：`Company Agent Router`

目标：

- 用户输入任意工作请求。
- 系统自动判断应该交给哪个专家。
- 专家只拥有必要工具。
- 输出标准化结果。

参考：

- `multi_mcp_agent_router`

你会练到：

- 多专家架构。
- 路由器设计。
- 工具权限隔离。
- 公司级 `Agent` 平台雏形。

## 10. 重点代码阅读路线

建议按这个顺序读代码：

1. `github_mcp_agent/github_agent.py`
   - 看 `StdioServerParameters`。
   - 看 `MCPTools`。
   - 看 `Agent` 如何调用 `MCP` 工具。

2. `notion_mcp_agent/notion_mcp_agent.py`
   - 看 `Notion MCP Server` 配置。
   - 看 `SQLite` 记忆。
   - 看 `session_id` 和 `user_id`。

3. `browser_mcp_agent/main.py`
   - 看 `MCPApp` 初始化。
   - 看 `Agent` 如何绑定 `Playwright` 工具。
   - 看异步 `Streamlit` 调用方式。

4. `multi_mcp_agent/multi_mcp_agent.py`
   - 看 `MultiMCPTools`。
   - 看多个 `npx MCP server` 如何组合。
   - 看多服务提示词设计。

5. `multi_mcp_agent_router/agent_forge.py`
   - 看 `Agent` 数据结构。
   - 看每个专家如何配置 `MCP server`。
   - 看 `mcp_tool_to_anthropic`。
   - 看工具调用循环。
   - 看自动路由和手动选择。

6. `ai_travel_planner_mcp_agent_team/app.py`
   - 看业务型 `Agent` 如何写详细指令。
   - 看 `Airbnb MCP`、`Google Maps MCP`、`Google Search` 如何组合。
   - 看如何把回答转成 `.ics` 日历文件。

## 11. 学习后的能力图谱

学完这个目录，你应该具备这些能力：

| 能力 | 说明 |
| --- | --- |
| 单工具 `Agent` | 能把一个外部系统接入 `Agent` |
| 多工具 `Agent` | 能让一个 `Agent` 调用多个服务 |
| 多专家 `Agent` | 能按任务路由到不同专家 |
| 工具权限设计 | 能按风险分配工具 |
| 会话记忆 | 能维护多轮上下文 |
| 浏览器自动化 | 能让 `Agent` 操作网页 |
| 业务流程编排 | 能把多个工具组合成完整工作流 |
| 安全意识 | 能识别写入、删除、发邮件等高风险操作 |

## 12. 最终建议

如果你正在学习 `AI Agent`，这个目录的学习价值很高，但不要只停留在“跑通示例”。

你应该重点练这三件事：

1. **工具化**：把真实系统封装成 `MCP server` 或接入现成 `MCP server`。
2. **流程化**：把多个工具组织成可靠工作流，而不是一次性聊天。
3. **安全化**：控制工具权限、记录审计日志、对高风险操作加确认。

最推荐的学习路径：

1. 先用 `github_mcp_agent` 理解单工具 `MCP Agent`。
2. 再用 `notion_mcp_agent` 学会写入型工具和记忆。
3. 接着用 `browser_mcp_agent` 学浏览器自动化。
4. 然后用 `multi_mcp_agent` 学多工具协作。
5. 最后用 `multi_mcp_agent_router` 学公司级多专家架构。

当你能自己实现一个“路由器 + 多专家 + 多 `MCP server` + 权限控制 + 审计日志”的系统时，你就已经从普通 `AI Agent Demo` 进入了公司级 `Agent` 平台实践。
