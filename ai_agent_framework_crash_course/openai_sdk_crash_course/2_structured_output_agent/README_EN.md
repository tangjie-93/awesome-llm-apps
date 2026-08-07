# Tutorial 2: Structured Output

# 教程 2：结构化输出

This chapter shows how to make an agent return typed, structured data instead of plain text.

本章演示如何让 Agent 返回带类型的结构化数据，而不是只输出普通文本。

## What You'll Learn

## 你将学到什么

- Schema-driven outputs

  基于 schema 的输出

- Pydantic models for validation

  用 Pydantic 模型做校验

- Ticket classification and extraction

  工单分类与信息抽取

- Review parsing and normalization

  评价解析与标准化

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
python support_ticket_agent.py
python product_review_agent.py
```

## Files

## 文件

- `support_ticket_agent.py`

  支持工单结构化输出示例

- `product_review_agent.py`

  产品评价结构化输出示例

- `2_1_support_ticket_agent/`

  支持工单子示例

- `2_2_product_review_agent/`

  产品评价子示例

## Next Step

## 下一步

Continue to Tutorial 3 for tool use.

继续学习教程 3：工具调用。
