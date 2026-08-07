# Tutorial 5: Context Management

# 教程 5：上下文管理

This chapter shows how to pass shared context into agent runs and keep state available across turns.

本章演示如何把共享上下文传入 Agent 运行过程，并在多轮对话中保留状态。

## What You'll Learn

## 你将学到什么

- Shared context objects

  共享上下文对象

- State passed into prompts

  传入提示词的状态

- Context-aware behavior

  感知上下文的行为

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

  上下文管理示例

- `env.example`

  环境变量模板

## Next Step

## 下一步

Continue to Tutorial 6 for guardrails and validation.

继续学习教程 6：护栏与校验。

