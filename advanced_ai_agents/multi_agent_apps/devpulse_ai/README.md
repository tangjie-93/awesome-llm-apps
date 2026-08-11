# 🧠 DevPulseAI — Multi-Agent Signal Intelligence
# 🧠 `DevPulseAI` — 多智能体信号情报

A reference implementation demonstrating how to build a **multi-agent pipeline** that aggregates technical signals from multiple sources, scores them for relevance, assesses risks, and synthesizes an actionable intelligence digest.
这是一个参考实现，展示如何构建一个**多智能体流水线**，从多个来源聚合技术信号，对其相关性进行评分、评估风险，并综合生成可执行的情报摘要。

> **Design Philosophy:** Agents are used **only where reasoning is required.** Deterministic operations (collection, normalization, deduplication) are implemented as plain utilities — not agents.
> **设计理念：** 仅在**需要推理**的地方使用智能体。确定性操作（收集、规范化、去重）实现为普通工具，而不是智能体。

---

## Architecture
## 架构

```
┌─────────────────────────────────────────────────────────┐
│                    DATA SOURCES                         │
│  GitHub · ArXiv · HackerNews · Medium · HuggingFace     │
└──────────────────────┬──────────────────────────────────┘
                       │ raw signals
                       ▼
┌──────────────────────────────────────────────────────────┐
│  SignalCollector (UTILITY — no LLM)                      │
│  • Normalizes to unified schema                          │
│  • Deduplicates via source:id composite key              │
│  • Filters incomplete signals                            │
└──────────────────────┬───────────────────────────────────┘
                       │ normalized signals
                       ▼
┌──────────────────────────────────────────────────────────┐
│  RelevanceAgent (AGENT — gpt-4.1-mini)                   │
│  • Scores each signal 0–100 for developer relevance      │
│  • Considers: novelty, impact, actionability, timeliness  │
│  • Falls back to heuristics if no API key                 │
└──────────────────────┬───────────────────────────────────┘
                       │ scored signals
                       ▼
┌──────────────────────────────────────────────────────────┐
│  RiskAgent (AGENT — gpt-4.1-mini)                        │
│  • Assesses security vulnerabilities                      │
│  • Flags breaking changes and deprecations                │
│  • Rates risk: LOW / MEDIUM / HIGH / CRITICAL             │
└──────────────────────┬───────────────────────────────────┘
                       │ risk-assessed signals
                       ▼
┌──────────────────────────────────────────────────────────┐
│  SynthesisAgent (AGENT — gpt-4.1)                        │
│  • Cross-references relevance + risk data                 │
│  • Produces executive summary                             │
│  • Generates actionable recommendations                   │
└──────────────────────┬───────────────────────────────────┘
                       │
                       ▼
              📄 Intelligence Digest
```

---

## Why Signal Collection Is Not an Agent
## 为什么信号收集不是智能体

This is an **intentional, opinionated design choice** — not a shortcut.
这是一个**有意且明确立场的设计选择**，不是捷径。

Signal collection involves:
信号收集包括：

- Fetching data from HTTP APIs (deterministic)
- 从 `HTTP API` 获取数据（确定性）
- Normalizing fields to a unified schema (mechanical transformation)
- 将字段规范化为统一 `schema`（机械转换）
- Deduplicating by composite key (hash comparison)
- 通过复合键去重（哈希比较）

**None of these tasks require reasoning, judgment, or language understanding.**
**这些任务都不需要推理、判断或语言理解。**

Wrapping collection in an `Agent` class would be _decorative_ — it would have an LLM import that never gets called. This misleads readers into thinking an LLM is necessary, when the actual logic is a `for` loop with a `set()`.
将收集过程包装进 `Agent` 类只是_装饰性_做法，因为它会包含一个永远不会被调用的 `LLM` 导入。这会误导读者以为必须使用 `LLM`，而实际逻辑只是一个配合 `set()` 的 `for` 循环。

> **Rule of thumb:** If you can write the logic as a pure function with no ambiguity, it's a utility. If the output depends on understanding context, making judgment calls, or generating natural language, it's an agent.
> **经验法则：** 如果逻辑可以无歧义地写成纯函数，它就是工具。如果输出依赖理解上下文、做判断或生成自然语言，它就是智能体。

---

## Agent Roles & Model Selection
## 智能体角色与模型选择

| Component<br>组件 | Type<br>类型 | Model<br>模型 | Why This Model<br>为什么选择该模型 |
|---|---|---|---|
| `SignalCollector` | **Utility**<br>**工具** | _none_<br>_无_ | Deterministic — no reasoning required<br>确定性任务，不需要推理 |
| `RelevanceAgent` | **Agent**<br>**智能体** | `gpt-4.1-mini` | Classification task — fast, cheap, high-volume<br>分类任务，快速、低成本、适合高吞吐 |
| `RiskAgent` | **Agent**<br>**智能体** | `gpt-4.1-mini` | Structured analysis — careful but not expensive<br>结构化分析，足够审慎且成本不高 |
| `SynthesisAgent` | **Agent**<br>**智能体** | `gpt-4.1` | Cross-referencing & summarization — needs strongest reasoning<br>交叉引用和总结，需要最强推理能力 |

**Single provider by default (OpenAI)** to reduce onboarding friction. Override per-agent via environment variables:
默认使用**单一提供商（`OpenAI`）**以降低上手阻力。可通过环境变量按智能体覆盖：

```bash
export MODEL_RELEVANCE=gpt-4.1-nano    # cheaper, faster
export MODEL_RISK=o4-mini               # deeper reasoning for risk
export MODEL_SYNTHESIS=gpt-4.1          # default, strongest
```

---

## How to Run
## 如何运行

### Quick Verification (No API Key Required)
### 快速验证（无需 `API key`）

```bash
cd advanced_ai_agents/multi_agent_apps/devpulse_ai
python verify.py
```

This runs the full pipeline with mock data in **<1 second**. No network calls, no API keys.
这会使用模拟数据在 **`<1` 秒**内运行完整流水线。不会进行网络调用，也不需要 `API key`。

Expected output:
预期输出：

```
[OK] DevPulseAI reference pipeline executed successfully
```

### Full Pipeline (With API Key)
### 完整流水线（带 `API key`）

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
python main.py
```

Without an API key, agents automatically fall back to heuristic scoring.
如果没有 `API key`，智能体会自动回退到启发式评分。

### Streamlit Dashboard
### `Streamlit` 仪表板

```bash
streamlit run streamlit_app.py
```

---

## Project Structure
## 项目结构

```
devpulse_ai/
├── agents/
│   ├── __init__.py              # Package exports + design docs
│   ├── signal_collector.py      # UTILITY — normalize & dedup
│   ├── relevance_agent.py       # AGENT  — score relevance (gpt-4.1-mini)
│   ├── risk_agent.py            # AGENT  — assess risks (gpt-4.1-mini)
│   └── synthesis_agent.py       # AGENT  — produce digest (gpt-4.1)
├── adapters/
│   ├── github.py                # GitHub trending repos
│   ├── arxiv.py                 # ArXiv recent papers
│   ├── hackernews.py            # HackerNews top stories
│   ├── medium.py                # Medium AI/ML blogs
│   └── huggingface.py           # HuggingFace trending models
├── workflows/
│   └── signal-intelligence-pipeline.json
├── main.py                      # Full pipeline runner
├── verify.py                    # Mock-data verification (<1s)
├── streamlit_app.py             # Interactive dashboard
└── requirements.txt             # Minimal deps (single provider)
```

---

## Optional Extensions (Advanced Users)
## 可选扩展（高级用户）

These are **not required** for the reference implementation, but show how the architecture extends:
这些内容对参考实现**不是必需的**，但展示了架构如何扩展：

1. **Multi-provider models** — Swap `RelevanceAgent` to use Anthropic Claude or Google Gemini by updating the model config. The `agno` framework supports multiple providers.
1. **多提供商模型** — 通过更新模型配置，将 `RelevanceAgent` 替换为使用 `Anthropic Claude` 或 `Google Gemini`。`agno` 框架支持多个提供商。

2. **Vector search** — Add a Pinecone or Qdrant adapter to store and retrieve signals semantically for long-term pattern detection.
2. **向量搜索** — 添加 `Pinecone` 或 `Qdrant` 适配器，用于以语义方式存储和检索信号，支持长期模式检测。

3. **Streaming digests** — Use WebSocket streaming from `SynthesisAgent` for real-time intelligence feeds.
3. **流式摘要** — 使用来自 `SynthesisAgent` 的 `WebSocket` 流式传输，实现实时情报信息流。

4. **Custom adapters** — Add new signal sources by implementing a `fetch_*` function that returns `List[Dict]` with the standard schema (`id`, `source`, `title`, `description`, `url`, `metadata`).
4. **自定义适配器** — 通过实现返回标准 `schema`（`id`、`source`、`title`、`description`、`url`、`metadata`）的 `List[Dict]` 的 `fetch_*` 函数，添加新的信号来源。

5. **Feedback loop** — Store user feedback (👍/👎) in Supabase and use it to fine-tune relevance scoring over time.
5. **反馈循环** — 将用户反馈（👍/👎）存储在 `Supabase` 中，并用于随时间微调相关性评分。

---

## Dependencies
## 依赖

```
agno              # Agent framework
openai            # LLM provider (single default)
httpx             # HTTP client for adapters
feedparser        # RSS/Atom parsing for Medium
streamlit>=1.30   # Interactive dashboard
```

No `google-generativeai` required. Gemini is an optional extension if users want multi-provider support — install `google-genai` (not the deprecated `google-generativeai`) separately.
不需要 `google-generativeai`。如果用户想要多提供商支持，`Gemini` 是可选扩展，请单独安装 `google-genai`（而不是已弃用的 `google-generativeai`）。

---

## Design Tradeoffs
## 设计权衡

| Decision<br>决策 | Tradeoff<br>权衡 | Why<br>原因 |
|---|---|---|
| Single provider default<br>默认单一提供商 | Less flexibility<br>灵活性较低 | Reduces onboarding from 2+ keys to 1<br>将上手所需密钥从 `2+` 个减少到 `1` 个 |
| Signal collection as utility<br>将信号收集作为工具 | Less "agentic" demo<br>演示的“智能体感”较弱 | Honest architecture — agents where reasoning exists<br>架构诚实，只在存在推理的地方使用智能体 |
| Heuristic fallbacks<br>启发式回退 | Lower quality without API key<br>无 `API key` 时质量较低 | Pipeline always works, even for evaluation<br>流水线始终可运行，即使只是评估 |
| 5 signals per source default<br>默认每个来源 `5` 个信号 | Less data<br>数据较少 | Keeps demo fast (<10s with API, <1s mock)<br>保持演示快速（带 `API` 时 `<10s`，模拟数据 `<1s`） |
| No async in agents<br>智能体中不使用异步 | Less throughput<br>吞吐量较低 | Simpler code, clearer educational value<br>代码更简单，教学价值更清晰 |

---

_Built as a reference implementation for [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)._
_作为 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) 的参考实现构建。_
