# 🛡️ Trust-Gated Multi-Agent Research Team
# 🛡️ 信任门控多智能体研究团队

Build a multi-agent research pipeline where every AI agent must pass a **trust verification** before participating, and every action is recorded in a **hash-chained audit trail** that is independently verifiable.
构建一个多智能体研究流水线，其中每个 `AI` 智能体在参与前都必须通过**信任验证**，并且每个动作都会记录在可独立验证的**哈希链审计轨迹**中。

## Features
## 功能

- **Trust Gating** — Agents are scored (0-100) and tiered (gold/silver/bronze). Only agents meeting the threshold can participate
- **信任门控** — 智能体会被评分（`0-100`）并分层（`gold` / `silver` / `bronze`）。只有达到阈值的智能体才能参与
- **Cryptographic Audit Trail** — Every agent action is recorded with SHA-256 hashes chaining to the previous entry. If any record is tampered with, all subsequent hashes break
- **加密审计轨迹** — 每个智能体动作都会使用 `SHA-256` 哈希记录，并与上一条目链接。如果任何记录被篡改，所有后续哈希都会失效
- **Multi-Agent Pipeline** — Researcher → Analyst → Writer, each building on the previous output
- **多智能体流水线** — `Researcher` → `Analyst` → `Writer`，每一步都基于前一步输出继续构建
- **Visual Dashboard** — See which agents pass, which get blocked, and verify the entire audit chain
- **可视化仪表板** — 查看哪些智能体通过、哪些被阻止，并验证整条审计链
- **Zero External Dependencies** — Fully self-contained. Only requires `openai` and `streamlit`
- **零外部依赖** — 完全自包含，仅需要 `openai` 和 `streamlit`

## How It Works
## 工作原理

```
                ┌─────────────────────┐
                │   Trust Registry    │
                │  (verify agents)    │
                └──┬───────┬───────┬──┘
                   │       │       │
             ┌─────▼──┐ ┌──▼────┐ ┌▼────────┐
             │Research │ │Analyst│ │ Writer  │
             │ ✅ 75   │ │ ✅ 60 │ │ 🚫 5   │
             └────┬───┘ └──┬────┘ └─────────┘
                  │        │
                  ▼        ▼
          ┌──────────────────────┐
          │  Research Pipeline   │
          │  (trusted only)      │
          └──────────┬───────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │  Hash-Chained Audit  │
          │  (tamper-evident)    │
          └──────────────────────┘
```

1. **Trust Check** — Each agent's score is verified against the minimum threshold
1. **信任检查** — 每个智能体的分数都会与最低阈值进行验证
2. **Gate** — Agents below the threshold are blocked from the pipeline
2. **门控** — 低于阈值的智能体会被阻止进入流水线
3. **Execute** — Verified agents run in sequence, each building on the previous output
3. **执行** — 已验证的智能体按顺序运行，每个智能体都基于前一个输出继续构建
4. **Audit** — Every action (including trust checks) is recorded in a hash chain
4. **审计** — 每个动作（包括信任检查）都会记录在哈希链中

## Getting Started
## 入门

### Prerequisites
### 前置条件

- Python 3.9+
- `Python 3.9+` 环境
- OpenAI API key
- `OpenAI API key` 密钥

### Installation
### 安装

```bash
pip install -r requirements.txt
```

### Set your API key (optional — can also paste in the sidebar)
### 设置你的 `API key`（可选，也可以粘贴到侧边栏）

```bash
export OPENAI_API_KEY=your-api-key
```

### Run
### 运行

```bash
streamlit run trust_gated_agents.py
```

### Quick Start (3 steps)
### 快速开始（`3` 步）

1. Paste your OpenAI API key in the sidebar
1. 在侧边栏粘贴你的 `OpenAI API key`
2. Click **Run Trust-Gated Pipeline** — agents are pre-selected with an untrusted bot as Writer
2. 点击 **Run Trust-Gated Pipeline**，系统会预先选择一个不受信任的机器人作为 `Writer`
3. Watch: Researcher (75) and Analyst (60) pass, Untrusted Bot (5) gets blocked
3. 观察结果：`Researcher`（`75`）和 `Analyst`（`60`）通过，`Untrusted Bot`（`5`）被阻止

Swap the Writer dropdown to "Report Writer (score 45)" to see all 3 pass.
将 `Writer` 下拉框切换为 `"Report Writer (score 45)"`，即可看到全部 `3` 个智能体通过。

## Audit Trail
## 审计轨迹

The audit trail uses the same hash-chaining pattern as blockchain transaction logs:
审计轨迹使用与区块链交易日志相同的哈希链模式：

```json
[
  {
    "seq": 0,
    "agent": "researcher-001",
    "action": "trust_verification",
    "hash": "a1b2c3...",
    "prev_hash": "0000000000000000000000000000000000000000000000000000000000000000"
  },
  {
    "seq": 1,
    "agent": "researcher-001",
    "action": "pipeline_step_1",
    "hash": "d4e5f6...",
    "prev_hash": "a1b2c3..."
  }
]
```

Each entry's `hash` is computed from: `sequence + timestamp + agent + action + input_hash + output_hash + trust_score + prev_hash`. Changing any field in any entry invalidates every subsequent hash.
每个条目的 `hash` 都由 `sequence + timestamp + agent + action + input_hash + output_hash + trust_score + prev_hash` 计算得出。更改任何条目中的任何字段都会使后续每个哈希失效。

The exported JSON is independently verifiable — no special tools needed, just SHA-256.
导出的 `JSON` 可以独立验证，不需要特殊工具，只需要 `SHA-256`。

## Why This Matters
## 为什么这很重要

In multi-agent systems, two problems compound:
在多智能体系统中，两个问题会叠加：

1. **Trust** — How do you know which agents are reliable before giving them work?
1. **信任** — 在分配工作之前，你如何知道哪些智能体可靠？
2. **Accountability** — After something goes wrong, how do you reconstruct what happened?
2. **问责** — 出现问题后，你如何重建发生了什么？

Trust gating solves #1 by checking credentials before execution. The audit trail solves #2 by creating a tamper-evident record that survives the agents' own execution — stored externally, not in the agent's own memory.
信任门控通过在执行前检查凭据来解决第 `1` 个问题。审计轨迹通过创建可防篡改记录来解决第 `2` 个问题，该记录会独立于智能体自身执行而保存，存储在外部，而不是智能体自己的记忆中。

## Tech Stack
## 技术栈

- **Streamlit** — Interactive UI with visual trust dashboard
- **`Streamlit`** — 带可视化信任仪表板的交互式 `UI`
- **OpenAI** — GPT-4o-mini for agent reasoning
- **`OpenAI`** — 使用 `GPT-4o-mini` 进行智能体推理
- **SHA-256** — Hash-chained audit trail (no external crypto dependencies)
- **`SHA-256`** — 哈希链审计轨迹（无外部加密依赖）
