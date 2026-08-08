# Evals

Manual evaluations for the chatgpt-app-builder skill.

## Format

Each eval file is a JSON array:

```json
[
  {
    "query": "User input to test",
    "expected_behavior": "OUTCOME. What the response should do."
  }
]
```

## Running Evals

In Claude Code:

```
Run the evals in evals/<reference>.json. For each query, spawn a Sonnet agent with the chatgpt-app-builder skill context and compare the response against expected_behavior. Report pass/fail for each.
```

## 中文对照

### 评测

本文档说明如何对 chatgpt-app-builder 技能进行手动评测。每个评测文件是 JSON 数组，包含测试输入和预期行为；在 Claude Code 中运行后，需要逐项报告通过或失败。
