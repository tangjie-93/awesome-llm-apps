# RAG Failure Diagnostics Clinic
# `RAG` 失败诊断诊所

A small, framework-agnostic **RAG failure diagnostics clinic**.
一个小型、框架无关的 **`RAG` 失败诊断诊所**。

You paste a real bug description from your LLM + RAG pipeline.
你粘贴来自你的 `LLM + RAG` 流水线的真实 `bug` 描述。
The script asks an LLM to classify the failure into one of several **reusable patterns** and suggests a **minimal structural fix** (not just “add more context” or “try a better model”).
脚本会要求 `LLM` 将该失败归类为若干 **可复用模式** 之一，并建议一个 **最小结构性修复**（而不只是“添加更多上下文”或“尝试更好的模型”）。

The goal is to show a pattern-driven way to debug RAG incidents that can be adapted to any stack: LangChain, LlamaIndex, custom microservices, or in-house infra.
目标是展示一种由模式驱动的方式，用于调试可适配到任何技术栈的 `RAG` 事故：`LangChain`、`LlamaIndex`、自定义微服务或内部基础设施。

---

## What you will learn
## 你将学到什么

By running this example, you will learn how to:
通过运行这个示例，你将学习如何：

- Describe **real-world RAG bugs** in plain text so an LLM can reason about them.
  用纯文本描述 **真实世界的 `RAG bug`**，让 `LLM` 能够对其进行推理。
- Use a small library of **failure patterns** to triage incidents quickly.
  使用一个小型 **失败模式** 库快速分诊事故。
- Ask the model to propose **minimal structural changes** instead of pure prompt tweaks.
  要求模型提出 **最小结构性变更**，而不是纯粹的 `prompt` 微调。
- Call an **OpenAI-compatible API** from a small Python script.
  从一个小型 `Python` 脚本调用 **`OpenAI-compatible API`**。
- Save each diagnosis into a JSON report for later analysis or post-mortems.
  将每次诊断保存到 `JSON` 报告中，供后续分析或事后复盘使用。

This is not a full framework.
这不是一个完整框架。
It is a compact **clinic app** that demonstrates a pattern you can adapt in your own stacks.
它是一个紧凑的 **诊所应用**，用于演示一种你可以适配到自己技术栈中的模式。

---

## Folder structure
## 文件夹结构

This tutorial expects the following files in `rag_tutorials/rag_failure_diagnostics_clinic`:
本教程期望 `rag_tutorials/rag_failure_diagnostics_clinic` 中包含以下文件：

- `README.md` ← this file
  `README.md` ← 本文件
- `rag_failure_diagnostics_clinic.py` ← minimal interactive CLI script
  `rag_failure_diagnostics_clinic.py` ← 最小交互式 `CLI` 脚本
- `requirements.txt` ← Python dependencies
  `requirements.txt` ← `Python` 依赖

The script is completely self-contained.
该脚本完全自包含。
All pattern definitions and prompts live inside this folder.
所有模式定义和 `prompt` 都位于这个文件夹内。

---

## Failure patterns (P01–P12)
## 失败模式（`P01`-`P12`）

The clinic uses a small, opinionated set of **12 reusable failure patterns**.
该诊所使用一组小而有明确取舍的 **`12` 个可复用失败模式**。
Each bug is mapped to exactly one primary pattern, with optional secondary candidates.
每个 `bug` 都会被映射到且仅映射到一个主要模式，并可包含可选的次要候选模式。

You can modify or extend these patterns to match your own production incidents.
你可以修改或扩展这些模式，以匹配自己的生产事故。

| ID<br>编号 | Pattern name<br>模式名称 | Typical symptom<br>典型症状 |
| ---- | ----------------------------------------------------- | -------------------------------------------------------------- |
| P01<br>`P01` | Retrieval hallucination / grounding drift<br>检索幻觉 / 依据漂移 | Answer confidently contradicts retrieved documents.<br>答案自信地与检索到的文档相矛盾。 |
| P02<br>`P02` | Chunk boundary or segmentation bug<br>分块边界或切分 `bug` | Relevant facts are split or truncated across chunks.<br>相关事实在多个分块之间被拆散或截断。 |
| P03<br>`P03` | Embedding mismatch / semantic vs vector distance<br>嵌入不匹配 / 语义与向量距离不一致 | Cosine similarity does not match true relevance.<br>余弦相似度与真实相关性不匹配。 |
| P04<br>`P04` | Index skew or staleness<br>索引偏斜或过期 | Old or missing data even though source of truth is updated.<br>即使事实来源已更新，仍出现旧数据或缺失数据。 |
| P05<br>`P05` | Query rewriting or router misalignment<br>查询重写或路由器错位 | Router sends queries to the wrong tool or dataset.<br>路由器将查询发送到错误的工具或数据集。 |
| P06<br>`P06` | Long-chain reasoning drift<br>长链推理漂移 | Multi-step tasks gradually lose track of earlier constraints.<br>多步骤任务逐渐丢失对早期约束的跟踪。 |
| P07<br>`P07` | Tool-call misuse or ungrounded tools<br>工具调用误用或工具缺少依据 | Tools are called with wrong arguments or without grounding.<br>工具被用错误参数调用，或在缺少依据的情况下被调用。 |
| P08<br>`P08` | Session memory leak / missing context<br>会话记忆泄漏 / 上下文缺失 | Conversation loses important facts between turns or sessions.<br>对话在轮次或会话之间丢失重要事实。 |
| P09<br>`P09` | Evaluation blind spots<br>评估盲点 | System passes tests but fails on real incidents.<br>系统通过测试，但在真实事故中失败。 |
| P10<br>`P10` | Startup ordering / dependency not ready<br>启动顺序 / 依赖未就绪 | Services crash or 5xx during the first minutes after deploy.<br>服务在部署后的最初几分钟崩溃或返回 `5xx`。 |
| P11<br>`P11` | Config or secrets drift across environments<br>跨环境配置或密钥漂移 | Works locally, breaks only in staging / prod due to settings.<br>本地可用，但由于设置问题只在 `staging / prod` 中出错。 |
| P12<br>`P12` | Multi-tenant / multi-agent interference<br>多租户 / 多智能体干扰 | Requests or agents step on each other’s state or resources.<br>请求或智能体相互踩踏彼此的状态或资源。 |

The built-in examples roughly correspond to:
内置示例大致对应：

- Example 1 → retrieval hallucination / grounding drift (P01 style).
  示例 `1` → 检索幻觉 / 依据漂移（`P01` 风格）。
- Example 2 → startup ordering / dependency not ready (P10 style).
  示例 `2` → 启动顺序 / 依赖未就绪（`P10` 风格）。
- Example 3 → config or secrets drift across environments (P11 style).
  示例 `3` → 跨环境配置或密钥漂移（`P11` 风格）。

You are encouraged to replace these with your own incident snippets.
建议你将这些示例替换为自己的事故片段。

---

## How the clinic works
## 诊所如何工作

At a high level:
从高层来看：

1. The script builds a **system prompt** that explains the 12 patterns above.
   脚本会构建一个解释上述 `12` 个模式的 **`system prompt`**。
2. You pick one of three built-in examples or paste your own RAG / LLM bug description.
   你选择三个内置示例之一，或粘贴自己的 `RAG / LLM bug` 描述。
3. The model is asked to:
   模型会被要求：
   - Choose a **primary pattern ID** (P01–P12).
     选择一个 **主要模式 `ID`**（`P01`-`P12`）。
   - Optionally choose up to **two secondary candidates**.
     可选地选择最多 **两个次要候选模式**。
   - Explain the reasoning in short bullet points.
     用简短要点解释推理过程。
   - Propose a **minimal structural fix** (changes to retrieval, routing, eval, or infra).
     提出一个 **最小结构性修复**（对检索、路由、评估或基础设施的变更）。
4. The full answer is printed to the console and also saved into `rag_failure_report.json` together with the original bug text and model name.
   完整答案会打印到控制台，并同时保存到 `rag_failure_report.json`，其中包含原始 `bug` 文本和模型名称。

The intent is to show how a small **pattern vocabulary + prompt** can turn an LLM into a lightweight helper for incident triage.
其意图是展示一个小型 **模式词汇表 + `prompt`** 如何将 `LLM` 转化为事故分诊的轻量助手。

---

## Prerequisites
## 先决条件

- Python 3.9 or newer.
  `Python 3.9` 或更新版本。
- An API key for any **OpenAI-compatible** chat completion endpoint:
  任意 **`OpenAI-compatible`** 聊天补全端点的 `API key`：
  - For example, `OPENAI_API_KEY` for `https://api.openai.com/v1`.
    例如，用于 `https://api.openai.com/v1` 的 `OPENAI_API_KEY`。
  - Or your own proxy URL set via `OPENAI_BASE_URL`.
    或通过 `OPENAI_BASE_URL` 设置你自己的代理 `URL`。
- Basic familiarity with RAG pipelines, logs, and failure modes.
  对 `RAG` 流水线、日志和失败模式有基本了解。

---

## Setup
## 设置

From the root of the `awesome-llm-apps` repo:
从 `awesome-llm-apps` 仓库根目录开始：

```bash
cd rag_tutorials/rag_failure_diagnostics_clinic
pip install -r requirements.txt
````

Minimal `requirements.txt`:
最小 `requirements.txt`：

```text
openai>=1.6.0
```

Set your API key as an environment variable (recommended):
将你的 `API key` 设置为环境变量（推荐）：

```bash
export OPENAI_API_KEY="sk-..."
# optional, if you use a custom endpoint
# export OPENAI_BASE_URL="https://your-proxy.example.com/v1"
# export OPENAI_MODEL="gpt-4o-mini"
```

> Tip: If you prefer Colab, you can also copy the entire `rag_failure_diagnostics_clinic.py` file into a single Colab cell and run it there.
> 提示：如果你更喜欢 `Colab`，也可以复制整个 `rag_failure_diagnostics_clinic.py` 文件到单个 `Colab` 单元格中并在那里运行。

---

## Running the clinic
## 运行诊所

From inside `rag_tutorials/rag_failure_diagnostics_clinic`:
在 `rag_tutorials/rag_failure_diagnostics_clinic` 内：

```bash
python rag_failure_diagnostics_clinic.py
```

You will see a simple text UI:
你会看到一个简单的文本 `UI`：

* If `OPENAI_API_KEY` is not set, the script will ask for an API key.
  如果未设置 `OPENAI_API_KEY`，脚本会要求输入 `API key`。
* You can keep the default base URL (`https://api.openai.com/v1`) and model (`gpt-4o`) or override them.
  你可以保留默认基础 `URL`（`https://api.openai.com/v1`）和模型（`gpt-4o`），也可以覆盖它们。
* Then you choose:
  然后你选择：

  * `1` → built-in retrieval hallucination example (P01 style).
    `1` → 内置检索幻觉示例（`P01` 风格）。
  * `2` → startup ordering example (P10 style).
    `2` → 启动顺序示例（`P10` 风格）。
  * `3` → config / secrets drift example (P11 style).
    `3` → 配置 / 密钥漂移示例（`P11` 风格）。
  * `p` → paste your own bug description.
    `p` → 粘贴你自己的 `bug` 描述。

Each run prints a diagnosis and writes a `rag_failure_report.json` file containing the bug text, model settings, and assistant reply.
每次运行都会打印诊断结果，并写入一个 `rag_failure_report.json` 文件，其中包含 `bug` 文本、模型设置和助手回复。

You can commit several reports into your own repo as a lightweight **RAG incident library**.
你可以将多个报告提交到自己的仓库中，作为一个轻量级 **`RAG` 事故库**。

---

## Extending this tutorial
## 扩展本教程

Some ideas for extending this pattern:
以下是扩展此模式的一些想法：

* Replace the examples with anonymized incidents from your own logs.
  用来自你自己日志的匿名化事故替换这些示例。
* Add more patterns or split existing ones to match your stack.
  添加更多模式或拆分现有模式，以匹配你的技术栈。
* Emit a richer JSON schema (severity, owners, suspected components).
  输出更丰富的 `JSON schema`（严重性、负责人、疑似组件）。
* Plug the reports into an evaluation dashboard or incident tracker.
  将报告接入评估仪表板或事故跟踪器。
