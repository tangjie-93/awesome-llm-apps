# AG2 Adaptive Research Team
# AG2 自适应研究团队

A Streamlit app that blends agent teamwork with agent-enabled routing and fallback, built entirely on AG2.
一个 Streamlit 应用，将智能体团队协作与智能体驱动的路由和回退机制结合起来，完全基于 AG2 构建。

## What This Shows
## 展示内容

- **Agent teamwork**: explicit roles and sequential handoffs
- **智能体团队协作**：明确的角色划分和顺序交接
- **Agent-enabled routing**: a clear decision step with local-doc vs web fallback
- **智能体驱动路由**：清晰的决策步骤，可在本地文档和网络回退之间选择
- **AG2-first implementation**: no Microsoft AutoGen dependency; installs via `ag2[openai]`
- **AG2 优先实现**：不依赖 Microsoft AutoGen；通过 `ag2[openai]` 安装

## Features
## 功能

- Local document upload (PDF, TXT, MD)
- 上传本地文档（PDF、TXT、MD）
- Routing decision based on document coverage
- 根据文档覆盖范围做出路由决策
- Optional web fallback via SearxNG
- 通过 SearxNG 提供可选的网络回退
- Verifier step to check evidence sufficiency
- 使用验证器步骤检查证据是否充分
- Final synthesis with citations
- 生成带引用的最终综合答案

## How To Run
## 运行方式

1. Install dependencies:
1. 安装依赖：

```bash
pip install -r requirements.txt
```

2. Run the app:
2. 运行应用：

```bash
streamlit run app.py
```

3. Provide your OpenAI API key in the sidebar and ask a question.
3. 在侧边栏提供你的 OpenAI API 密钥，然后提出问题。

## How It Works
## 工作原理

1. **Triage Agent** decides whether the question should be answered from local docs or the web.
1. **分诊智能体** 判断问题应由本地文档回答，还是转向网络检索。
2. **Local/Web Research Agent** collects evidence.
2. **本地/网络研究智能体** 收集证据。
3. **Verifier Agent** checks evidence strength.
3. **验证器智能体** 检查证据强度。
4. **Synthesizer Agent** produces the final answer with citations.
4. **综合智能体** 生成带引用的最终答案。

## Optional Add-ons (AG2 0.11)
## 可选扩展（AG2 0.11）

- **AG-UI protocol integration** for richer UI rendering
- **AG-UI 协议集成**，用于更丰富的 UI 渲染
- **OpenTelemetry tracing** for debugging multi-agent workflows
- **OpenTelemetry 链路追踪**，用于调试多智能体工作流

These are optional and not required to run this example.
这些扩展是可选项，运行此示例并不需要它们。

## Notes
## 说明

- Default model used is `gpt-5-nano`. You can change it in the sidebar before running a query.
- 默认使用的模型是 `gpt-5-nano`。你可以在运行查询前，在侧边栏中更改模型。
- Web fallback uses the SearxNG public instance at `https://searxng.site/search`. This instance may be rate-limited.
- 网络回退使用 SearxNG 公共实例 `https://searxng.site/search`。该实例可能受到速率限制。
