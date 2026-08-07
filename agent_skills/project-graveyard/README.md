# 🪦 Project Graveyard Agent Skill
# 🪦 项目墓园 Agent Skill

**Every developer has the folder. Twenty-something dead projects, each abandoned for reasons nobody wrote down.**

**每个开发者都有这样一个文件夹。二十来个死掉的项目，每一个都因为某些没人写下来的原因被遗弃。**

This skill reads the git history of every abandoned project on your machine and answers three questions:

这个 skill 会读取你机器上每个废弃项目的 git 历史，并回答三个问题：

**Why did each one die?** Evidence, not vibes. The last commits touch Stripe files: it died at the payments wall. Another repo's first commit lands three days after this one's last: the killer gets named.

**它们为什么死掉？** 看证据，不凭感觉。最后几次提交改到了 Stripe 文件：它死在支付墙前。另一个仓库的第一次提交出现在这个项目最后一次提交的三天后：凶手会被点名。

**What's your pattern?** Your projects die at day 19. Four of six were abandoned within 48 hours of starting something new.

**你的模式是什么？** 你的项目通常死在第 19 天。6 个项目里有 4 个，是在你开始新项目后的 48 小时内被放弃的。

**Which one still has a pulse?** Somewhere in that folder is a project that's 90% done: built, documented, never shipped. This finds it, checks what got easier since it died, and writes the short list of steps between it and a URL.

**哪一个还活着？** 那个文件夹里可能有一个已经完成 90% 的项目：功能做了、文档写了，但从未发布。这个 skill 会找出它，检查它死后哪些事情变简单了，并写出从现在到上线 URL 之间的简短步骤清单。

A representative scan (invented projects, real classifier verdicts). Your agent turns it into the funeral: an epitaph per corpse, your patterns named, and an offer to start resurrecting the strongest pulse right now. Yours will hurt more.

下面是一次代表性扫描（项目是虚构的，分类器判断是真实的）。你的 Agent 会把它变成一场葬礼：每具尸体一段墓志铭，指出你的行为模式，并提出现在就复活最有生命迹象项目的建议。你自己的报告会更扎心。

<img width="1672" height="941" alt="ChatGPT Image Jul 9, 2026, 06_46_05 PM" src="https://github.com/user-attachments/assets/b80456c7-cd6f-49d8-adcf-641230d4c601" />

## What it detects
## 它能检测什么

Cause of death, read from git history:

从 git 历史中读出的死亡原因：

| Cause | How it knows |
|---|---|
| **shiny object** | Another repo you own had its first commit within days of this one's last. The killer is named. |
| **闪亮新玩具** | 你另一个仓库的第一次提交，出现在这个项目最后一次提交后的几天内。凶手会被点名。 |
| **deploy fear** | README done, 20+ commits, real code, zero deploy config. It worked. It never shipped. |
| **部署恐惧** | README 写好了，20+ 次提交，有真实代码，但没有任何部署配置。它能跑，只是从没上线。 |
| **payments / auth wall** | The final commits touch stripe/billing or oauth/login code. |
| **支付 / 鉴权墙** | 最后的提交碰到了 stripe/billing 或 oauth/login 代码。 |
| **boilerplate wall** | 60%+ of all file changes were config files. It died configuring. |
| **样板配置墙** | 超过 60% 的文件改动都是配置文件。它死在配置里。 |
| **rewrite spiral** | Multiple rewrite/migrate commits; rebuilt instead of finished. |
| **重写螺旋** | 多次 rewrite/migrate 提交；一直重建，而不是完成。 |
| **scope explosion** | 100+ files, no deploy config. It grew instead of shipping. |
| **范围爆炸** | 100+ 个文件，却没有部署配置。它一直膨胀，而不是发布。 |
| **slow fade** | Commit gaps stretched until they stopped. No wall, no killer; it drifted. |
| **缓慢消失** | 提交间隔越来越长，直到停止。没有墙，也没有凶手；它只是漂走了。 |

It also separates the **finished** (deployed, pushed, documented; done, not abandoned) from the **unversioned** (no git, so no autopsy). Then it ranks the dead by **pulse**, how close each is to shipping, and the agent takes over:

它还会区分**已完成项目**（已部署、已推送、已写文档；完成了，不是废弃）和**未版本化项目**（没有 git，所以无法验尸）。然后它会按**脉搏**给死项目排序，也就是每个项目距离上线有多近，接着由 Agent 接手：

- **Autopsy interview**: ambiguous deaths get a question; git evidence is marked *(forensic)*, your answers *(confirmed)*.
- **验尸访谈**：模糊死因会触发追问；git 证据标记为 *(forensic)*，你的回答标记为 *(confirmed)*。
- **World-check**: before prescribing a dig, it checks what changed since the death: the API that now has an SDK, the model that's 20x cheaper.
- **世界状态检查**：在建议复活前，它会检查项目死后世界发生了什么变化：现在有 SDK 的 API、便宜 20 倍的模型等。
- **Resurrection**: a ≤7-step plan ending at *shipped*, and an offer to start on step 1 right now.
- **复活计划**：一份不超过 7 步、以 *shipped* 结束的计划，并提出现在就开始第 1 步。
- **Relapse watch**: resurrections are recorded (`--state` + `--mark-resurrected`); every later scan reports whether the patient is holding.
- **复发观察**：复活记录会被保存（`--state` + `--mark-resurrected`）；之后每次扫描都会报告这个病人是否还撑得住。
- **Necromancer mode**: ask your agent to build something new and it checks the graveyard first; you may have built 60% of it in 2024.
- **亡灵法师模式**：当你让 Agent 构建新东西时，它会先检查墓园；你可能在 2024 年已经做完了其中 60%。

## Install (10 seconds)
## 安装（10 秒）

```bash
npx skills add https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/project-graveyard
```

The [skills CLI](https://skills.sh) installs it into whatever agents you have (Claude Code, Codex, Cursor, Copilot, Antigravity, and others); or copy this folder into your agent's skills dir. Then: *"run the graveyard on ~/dev and ~/projects"*.

[skills CLI](https://skills.sh) 会把它安装到你已有的 Agent 中（Claude Code、Codex、Cursor、Copilot、Antigravity 等）；你也可以直接把这个文件夹复制到 Agent 的 skills 目录里。然后说：*"run the graveyard on ~/dev and ~/projects"*。

Standalone, no agent required:

也可以独立运行，不需要 Agent：

```bash
python3 project-graveyard/scripts/graveyard.py ~/dev ~/projects
```

## Scope and privacy
## 范围和隐私

Everything runs locally: one plain-Python file, stdlib only, zero network calls, read-only. It reads git metadata (commit dates, messages, filenames), never your code's contents. Name folders and it scans only those; given none, it checks a fixed list of usual project spots (`DEFAULT_ROOTS`, line 30 of the script), never "everything on your machine." Want to post your report? `--redact` swaps project names for `project-1..n`.

所有内容都在本地运行：一个纯 Python 文件，只使用标准库，没有网络请求，只读操作。它读取 git 元数据（提交日期、提交信息、文件名），不会读取你的代码内容。指定文件夹后，它只扫描这些文件夹；如果不指定，它只检查一组固定的常见项目位置（脚本第 30 行的 `DEFAULT_ROOTS`），不会扫描“你机器上的一切”。想发布报告？`--redact` 会把项目名替换成 `project-1..n`。

Prove it works before installing, from a clone of this repo:

安装前可以先在本仓库克隆中验证它能运行：

```bash
python3 agent_skills/evals/project-graveyard/test_graveyard.py   # 16 checks, ~10 seconds
```

Limits: no git means no autopsy (counted, not diagnosed). "Dead" is 45+ days silent, tunable with `--days`. Tested on macOS and Linux.

限制：没有 git 就无法验尸（会计数，但不诊断）。默认 45+ 天无提交视为“死亡”，可通过 `--days` 调整。已在 macOS 和 Linux 上测试。

## Files
## 文件

```text
project-graveyard/                  # ← this is all that gets copied
├── SKILL.md                        # agent instructions: report format, epitaph rules, resurrection protocol
├── README.md                       # this file
├── scripts/graveyard.py            # scanner + autopsy + pulse ranking (Python 3.8+, stdlib, offline)
└── references/causes-of-death.md   # the taxonomy: signals, confidence, resurrection strategy per cause
```

Part of [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) · Apache-2.0 · Last verified: July 2026

[awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) 的一部分 · Apache-2.0 · 最后验证时间：2026 年 7 月
