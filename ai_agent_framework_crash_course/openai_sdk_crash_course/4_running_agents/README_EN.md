# Tutorial 4: Running Agents

# 教程 4：运行 Agent

This chapter focuses on how to execute agents with Runner, async flows, run configuration, and streaming.

本章聚焦如何使用 Runner、异步流程、运行配置和流式输出来执行 Agent。

## What You'll Learn

## 你将学到什么

- Sync and async execution

  同步与异步执行

- Conversation management

  对话管理

- Run configuration

  运行配置

- Streaming events

  流式事件

## Quick Start

## 快速开始

1. Install dependencies

   安装依赖

```bash
pip install -r requirements.txt
```

2. Configure your API key

   配置 API Key

```bash
cp env.example .env
```

3. Run the examples

   运行示例

```bash
python agent_runner.py
python 4_1_execution_methods/agent.py
python 4_2_conversation_management/agent.py
python 4_3_run_configuration/agent.py
python 4_4_streaming_events/agent.py
```

## Files

## 文件

- `agent_runner.py`

  Runner 总入口

- `4_1_execution_methods/`

  执行方式示例

- `4_2_conversation_management/`

  会话管理示例

- `4_3_run_configuration/`

  运行配置示例

- `4_4_streaming_events/`

  流式事件示例

## Next Step

## 下一步

Continue to Tutorial 5 for context management.

继续学习教程 5：上下文管理。
