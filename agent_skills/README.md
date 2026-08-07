# 🧩 Agent Skills
# 🧩 Agent 技能

**Drop-in skills for Claude Code, Codex, Cursor, OpenClaw, Hermes, Antigravity, and any [SKILL.md](https://agentskills.io)-compatible agent.**

**适用于 Claude Code、Codex、Cursor、OpenClaw、Hermes、Antigravity，以及任何兼容 [SKILL.md](https://agentskills.io) 的 Agent，可直接接入使用。**

A skill is a folder with a `SKILL.md` file — plus scripts and references — that your agent discovers and loads on demand. One skill works across Claude Code, Codex, Cursor, and other coding agents.

一个技能是包含 `SKILL.md` 文件的文件夹，通常还会包含脚本和参考资料；Agent 会按需发现并加载它。同一个技能可以在 Claude Code、Codex、Cursor 和其他编码 Agent 中复用。

## The bar
## 标准

Most "skills" on registries are text-only prompt dumps — advice the model already knows, wrapped in frontmatter. Skills here have to earn their place:

很多注册表里的“技能”只是纯文本提示词堆叠，也就是把模型本来就知道的建议包装在 frontmatter 里。这里的技能必须真正有价值：

- **Real scripts** — deterministic work runs as code, not as token generation
- **真实脚本** —— 确定性的工作通过代码运行，而不是依赖模型生成 token

- **Researched references** — deep content loads on demand, with sources
- **经过研究的参考资料** —— 深度内容按需加载，并附带来源

- **Evidence over vibes** — every claim a skill makes must be checkable
- **证据优先** —— 技能中的每个主张都必须可以验证

- **Local and private by default** — no network calls unless declared, nothing leaves your machine
- **默认本地且私密** —— 除非明确声明，否则不会发起网络请求，也不会把任何内容发出你的机器

- **Tested before shipped** — on real inputs, not just happy-path fixtures
- **发布前经过测试** —— 使用真实输入测试，而不只是测试理想路径样例

## Skills
## 技能列表

| Skill | What it does |
|---|---|
| 技能 | 作用 |
| [🧠 advisor-orchestrator-worker](advisor-orchestrator-worker/) | Turns your agent into the orchestrator of a three-tier model team: cheap stateless workers in parallel, expensive advisor consulted only at commitment boundaries, verification gates between every step — budgeted so a run can't burn a hole in your API bill |
| [🧠 advisor-orchestrator-worker](advisor-orchestrator-worker/) | 将你的 Agent 变成三层模型团队的调度器：并行调用低成本无状态 worker，只在关键决策边界咨询高成本 advisor，每一步之间设置验证关卡，并通过预算控制避免 API 费用失控 |
| [⚰️ project-graveyard](project-graveyard/) | Scans your machine for dead side projects, autopsies why each one died from its git history (deploy fear, payments wall, killed by a newer project), shows your personal death patterns, and resurrects the one with a pulse — with relapse tracking on every resurrection it prescribes |
| [⚰️ project-graveyard](project-graveyard/) | 扫描你机器上停滞的副项目，通过 git 历史分析每个项目停滞的原因（害怕部署、支付链路受阻、被新项目替代等），展示你的项目停滞模式，并挑出仍有生命力的项目进行恢复，同时跟踪每次恢复后的复发情况 |
| [♾️ self-improving-agent-skills](self-improving-agent-skills/) | Automatically optimizes agent skills using Gemini and ADK |
| [♾️ self-improving-agent-skills](self-improving-agent-skills/) | 使用 Gemini 和 ADK 自动优化 Agent 技能 |

More coming, released one at a time.

更多技能会陆续发布，每次发布一个。

## ⚡ Install
## ⚡ 安装

One command, any agent — the [skills CLI](https://skills.sh) detects what you have installed (Claude Code, Codex, Cursor, Copilot, Antigravity, OpenClaw, Hermes, and other coding agents) and puts the skill in the right place:

一个命令即可适配任意 Agent：[skills CLI](https://skills.sh) 会检测你安装了哪些工具（Claude Code、Codex、Cursor、Copilot、Antigravity、OpenClaw、Hermes 和其他编码 Agent），并把技能放到正确位置：

```bash
npx skills add https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/<skill>
```

Prefer manual? Clone the repo and copy the skill folder into your agent's skills dir:

想手动安装？克隆仓库后，把技能文件夹复制到你的 Agent 技能目录中：

| Agent | Skills dir |
|---|---|
| Agent | 技能目录 |
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Cursor | `~/.cursor/skills/` |
| GitHub Copilot / VS Code | `~/.copilot/skills/` |
| Antigravity CLI | `.agents/skills/` in your project |
| Antigravity CLI | 项目中的 `.agents/skills/` |
| OpenClaw | `~/.openclaw/skills/` |
| Hermes | `~/.hermes/skills/` (also reads `~/.agents/skills/`) |
| Hermes | `~/.hermes/skills/`，同时也会读取 `~/.agents/skills/` |

Team install: put the skill in `.agents/skills/` inside your repo — it's the shared project-level dir most 2026 agents read (Codex, Cursor, Copilot, Antigravity; Claude Code uses `.claude/skills/`).

团队安装：把技能放到仓库内的 `.agents/skills/` 目录中。这是大多数 2026 年 Agent 会读取的项目级共享目录（Codex、Cursor、Copilot、Antigravity 都支持；Claude Code 使用 `.claude/skills/`）。

## Before you install any skill — including ours
## 安装任何技能前请先确认，包括我们的技能

Skills run with your agent's permissions: your shell, your files, your credentials. Treat them like software, not documents. Read the `SKILL.md` and every script before installing, from us or anyone. Skills here declare any network use up front and ship no install-time execution — nothing asks your agent to `curl | bash` anything, ever.

技能会以你的 Agent 权限运行：包括你的 shell、文件和凭据。请把它们当作软件，而不是普通文档。无论技能来自我们还是其他人，安装前都应该阅读 `SKILL.md` 和每个脚本。这里的技能会提前声明任何网络使用，并且不会在安装阶段执行代码，也绝不会要求你的 Agent 执行 `curl | bash` 之类的命令。

Every skill also has an executable eval in [`evals/`](evals/) — run it from the clone before installing, and note what you *don't* copy: the skill folder contains only what runs at runtime.

每个技能在 [`evals/`](evals/) 中也有可执行的评测脚本。安装前请先在克隆仓库中运行它，并注意哪些内容不需要复制：技能文件夹只包含运行时真正需要的内容。
