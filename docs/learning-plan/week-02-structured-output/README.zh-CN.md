# 第 2 周：结构化输出

**目标**：让 Agent 输出可解析且可校验的数据。需理解 Schema、解析和校验失败。**本周输出**：一份结构化结果定义、一条成功样例和一条失败处理用例。

## 本周指定目录与文件

- 主示例目录：[ai_data_analysis_agent](../../../starter_ai_agents/ai_data_analysis_agent/)
- 项目说明：[README.md](../../../starter_ai_agents/ai_data_analysis_agent/README.md)
- 依赖文件：[requirements.txt](../../../starter_ai_agents/ai_data_analysis_agent/requirements.txt)
- 入口文件：[ai_data_analyst.py](../../../starter_ai_agents/ai_data_analysis_agent/ai_data_analyst.py)
- 对照示例：[openai_research_agent/research_agent.py](../../../starter_ai_agents/openai_research_agent/research_agent.py)

| 学习日 | 学习任务 | 当日输出 |
| --- | --- | --- |
| D1 | 阅读 [ai_data_analyst.py](../../../starter_ai_agents/ai_data_analysis_agent/ai_data_analyst.py)，找出数据输入、查询结果和展示字段 | 字段说明 |
| D2 | 原样运行数据分析示例，记录一次可复现的结构化结果 | 基线 JSON/表格 |
| D3 | 参考 [research_agent.py](../../../starter_ai_agents/openai_research_agent/research_agent.py) 的报告结构，定义个人场景的结果字段 | Schema 草案 |
| D4 | 输入模糊请求，观察解析、SQL 或字段缺失失败 | 失败样例 |
| D5 | 补齐验收规则与错误提示 | 成功/失败对照 |

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

- 哪些字段必须校验：
- 错误是否能被下游程序识别：
- 下周准备验证的假设：
