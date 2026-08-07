# 第 5 周：可靠性

**目标**：定位并约束 Agent 的失败。需理解上下文管理、Guardrail 和 Tracing。**本周输出**：三类故障记录和定位报告。

## 本周指定目录与文件

- 主示例目录：[openai_research_agent](../../../starter_ai_agents/openai_research_agent/)
- 项目说明：[README.md](../../../starter_ai_agents/openai_research_agent/README.md)
- 入口文件：[research_agent.py](../../../starter_ai_agents/openai_research_agent/research_agent.py)
- 可靠性对照：[ai_medical_imaging.py](../../../starter_ai_agents/ai_medical_imaging_agent/ai_medical_imaging.py)
- 工具失败对照：[web_scraping_ai_agent/ai_scrapper.py](../../../starter_ai_agents/web_scraping_ai_agent/ai_scrapper.py)

| 学习日 | 学习任务 | 当日输出 |
| --- | --- | --- |
| D1 | 在 [research_agent.py](../../../starter_ai_agents/openai_research_agent/research_agent.py) 中构造超长研究主题并记录现象 | 上下文故障样例 |
| D2 | 参考 [ai_medical_imaging.py](../../../starter_ai_agents/ai_medical_imaging_agent/ai_medical_imaging.py)，构造越权/高风险请求并验证拒绝边界 | 拒绝记录 |
| D3 | 在 [ai_scrapper.py](../../../starter_ai_agents/web_scraping_ai_agent/ai_scrapper.py) 中构造无效 URL，观察错误链路 | 工具故障记录 |
| D4 | 使用 [research_agent.py](../../../starter_ai_agents/openai_research_agent/research_agent.py) 的 tracing/过程展示定位一次失败 | 追踪证据 |
| D5 | 整理模型、工具、校验、上下文故障判别表 | 判别表 |

## 每日笔记

### D1-D5

日期：  
关联示例：  
今天学习什么：  
需要弄清的问题：  
实践记录（输入、命令、输出或错误）：  
今日输出与验收证据：  
今天确认的结论：  
明天只验证的一个问题：

## 周末复盘

- 最难定位的失败层：
- 哪条规则真正阻止了风险：
- 下周准备验证的假设：
