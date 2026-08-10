# Skill Evals / 技能评测

How this repo checks that its skills actually work — before they ship and on every change after.

这个目录用于检查本仓库里的技能是否真的可用：发布前检查，之后每次变更也检查。

Layout: one folder per skill, `evals/<skill-name>/`, mirroring the skill's name. These files never ship in an install; the skill folders contain only what runs at runtime.

目录结构是每个技能一个文件夹：`evals/<skill-name>/`，与技能名称保持一致。这些评测文件不会随安装发布；技能文件夹只包含运行时真正需要的内容。

The tier model follows [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/main/evals) — same names, same jobs — plus two tiers of our own, because skills here ship executable code and his don't.

分层模型沿用 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/main/evals)：名称相同，职责相同；另外新增两个本仓库自己的层级，因为这里的技能会发布可执行代码，而对方仓库不会。

| Tier | 层级 | What it checks | 检查内容 | Runs | 运行位置 | Cost | 成本 |
|---|---|---|---|---|---|---|---|
| `1. Structural` | `1. 结构` | Frontmatter, naming, `name==dir`, unfilled placeholders, text-only prompt dumps (`tools/skill_lint.py --strict`) | `frontmatter`、命名、`name==dir`、未填占位符、纯文本 prompt dump（`tools/skill_lint.py --strict`） | `CI` | `CI` | Free | 免费 |
| `1b. Security` *(ours)* | `1b. 安全`（本仓库） | Install lures, undeclared network calls, credential access, obfuscated payloads (`tools/skill_scanner.py`) | 安装诱导、未声明网络调用、凭据访问、混淆载荷（`tools/skill_scanner.py`） | `CI` | `CI` | Free | 免费 |
| `2. Trigger & routing` | `2. 触发与路由` | Positive prompts clear near-miss negatives on description vocabulary; with `2+` skills, positives rank their own skill first and no two descriptions near-collide (`tools/run_trigger_evals.py`) | 正向 prompt 能通过描述词汇避开近似负例；有 `2+` 个技能时，正例会把自身技能排在第一，且没有两个描述过度相撞（`tools/run_trigger_evals.py`） | `CI` | `CI` | Free | 免费 |
| `2b. Deterministic scripts` *(ours)* | `2b. 确定性脚本`（本仓库） | The skill's bundled scripts do what they claim — every classifier, edge case, and output shape against synthetic fixtures (`<skill>/test_*.py`) | 技能自带脚本确实做到声称的行为：用合成 fixtures 覆盖每个分类器、边界情况和输出形状（`<skill>/test_*.py`） | `CI` | `CI` | Free, ~10s | 免费，约 `10s` |
| `3. Behavioral` | `3. 行为` | An agent following the skill satisfies its `expectations[]` — `evals.json` uses [skill-creator's schema](https://github.com/anthropics/skills/tree/main/skills/skill-creator) verbatim, so its `run_eval.py`, benchmarking, and eval viewer work against our files unmodified | 跟随该技能的 agent 能满足 `expectations[]`；`evals.json` 原样使用 [skill-creator's schema](https://github.com/anthropics/skills/tree/main/skills/skill-creator)，因此它的 `run_eval.py`、benchmarking 和 eval viewer 可以不加修改地跑本仓库文件 | On demand | 按需运行 | Tokens | 消耗 token |

## Running / 运行

```bash
# Tiers 1-2b, exactly what CI runs - deterministic, git + Python only
# 第 1-2b 层，与 CI 完全一致 - 确定性检查，只需要 git + Python
python3 agent_skills/evals/tools/skill_lint.py agent_skills/project-graveyard --strict
python3 agent_skills/evals/tools/skill_scanner.py agent_skills
python3 agent_skills/evals/tools/run_trigger_evals.py
python3 agent_skills/evals/project-graveyard/test_graveyard.py
```

Tier `3` is on demand and spends tokens: each skill's `evals.json` is in skill-creator's schema, so run it with Anthropic's own tooling (install the skill-creator plugin and point `run_eval.py` at the file), or by hand — fresh agent session, paste each prompt, grade against `expectations[]`.

第 `3` 层按需运行，并且会消耗 `token`：每个技能的 `evals.json` 都使用 `skill-creator` 的 schema，因此可以用 Anthropic 自己的工具运行（安装 `skill-creator` 插件，并把 `run_eval.py` 指向该文件），也可以手动运行：开启新的 agent session，粘贴每条 prompt，再按 `expectations[]` 打分。

Cases marked `lexical: false` in `trigger-cases.json` (reasoning-triggered, e.g. necromancer mode) are only covered here.

`trigger-cases.json` 中标记为 `lexical: false` 的案例（需要推理触发，例如 `necromancer mode`）只在这一层覆盖。

Re-run tier `3` whenever `SKILL.md` behavior changes; re-run tier `2` whenever a `description` changes.

每当 `SKILL.md` 行为变化时，重新运行第 `3` 层；每当 `description` 变化时，重新运行第 `2` 层。

## Track Record / 历史记录

Not theater: tier `1` caught a symlink-path bug that silently disabled relapse detection on macOS, and an external reviewer running it in a clean Linux checkout caught a filesystem-ordering bug that mis-attributed the kill-chain. Both fixed before merge. That's the job.

这不是表演：第 `1` 层曾发现一个符号链接路径 bug，它会在 `macOS` 上静默禁用复发检测；一位外部 reviewer 在干净的 `Linux` checkout 中运行评测时，还发现了一个文件系统排序 bug，它会错误归因 kill-chain。两者都在合并前修复了。这就是评测该做的事。

## Adding a Skill / 添加技能

New skill -> new `evals/<skill-name>/` with at minimum a deterministic `test_<skill>.py` (self-contained, tempdir fixtures, exit `0/1`) and a `trigger-cases.json`. `CI` picks up `test_*.py` automatically.

新增技能时，新增对应的 `evals/<skill-name>/`。至少包含一个确定性的 `test_<skill>.py`（自包含、使用临时目录 fixtures、以 `0/1` 退出）和一个 `trigger-cases.json`。`CI` 会自动发现 `test_*.py`。
