# Tutorial 6: Guardrails and Validation

# 教程 6：护栏与校验

This chapter adds validation and guardrails before the agent produces its final answer.

本章会在 Agent 输出最终答案之前加入校验和护栏。

## What You'll Learn

## 你将学到什么

- Input validation

  输入校验

- Safety checks

  安全检查

- Rejection and repair flows

  拒绝与修正流程

## Quick Start

## 快速开始

1. Install dependencies

   安装依赖

```bash
pip install openai-agents
```

2. Configure your API key

   配置 API Key

```bash
cp env.example .env
```

3. Run the example

   运行示例

```bash
python agent.py
```

## Files

## 文件

- `agent.py`

  护栏与校验示例

- `env.example`

  环境变量模板

## Next Step

## 下一步

Continue to Tutorial 7 for sessions.

继续学习教程 7：会话。

