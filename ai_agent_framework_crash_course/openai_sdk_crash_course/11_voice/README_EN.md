# Tutorial 11: Voice

# 教程 11：语音

This chapter shows how to build voice experiences in static, streamed, and realtime modes.

本章演示如何以静态、流式和实时三种模式构建语音体验。

## What You'll Learn

## 你将学到什么

- Audio input and output

  音频输入与输出

- Streamed voice pipelines

  流式语音管线

- Realtime conversations

  实时对话

## Quick Start

## 快速开始

1. Install dependencies for the mode you want

   安装对应模式所需依赖

```bash
cd static
pip install -r requirements.txt
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

## Modes

## 模式

- `static/`

  静态语音示例

- `streamed/`

  流式语音示例

- `realtime/`

  实时语音示例

## Files

## 文件

- `static/agent.py`

  静态模式入口

- `streamed/agent.py`

  流式模式入口

- `realtime/agent.py`

  实时模式入口

## End

## 结束

This is the final chapter in the crash course.

这是本 crash course 的最后一章。
