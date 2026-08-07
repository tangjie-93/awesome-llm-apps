# 第 11 周：产品入口

**目标**：将已验证的 Agent 能力包装为可使用的产品入口，理解界面或语音入口的状态表达、失败反馈和人工接管边界。**本周输出**：一个可演示的最小入口及其关键状态说明。

## 本周指定目录与文件

- 主示例目录：[ai_travel_agent](../../../starter_ai_agents/ai_travel_agent/)
- Streamlit 入口：[travel_agent.py](../../../starter_ai_agents/ai_travel_agent/travel_agent.py)
- 研究产品入口：[openai_research_agent/research_agent.py](../../../starter_ai_agents/openai_research_agent/research_agent.py)
- 语音入口示例目录：[voice_ai_agents](../../../voice_ai_agents/)
- 生成式 UI 示例目录：[generative_ui_agents](../../../generative_ui_agents/)

| 学习日 | 学习任务 | 当日输出 |
| --- | --- | --- |
| D1 | 从 [travel_agent.py](../../../starter_ai_agents/ai_travel_agent/travel_agent.py) 或 [research_agent.py](../../../starter_ai_agents/openai_research_agent/research_agent.py) 选择一个已完成工作流作为入口能力 | 用户任务与成功标准 |
| D2 | 基于所选入口绘制输入、处理中、成功和失败状态 | 状态流转说明 |
| D3 | 参考 [voice_ai_agents](../../../voice_ai_agents/) 或 [generative_ui_agents](../../../generative_ui_agents/) 为关键输入和结果设计最小界面/语音交互 | 交互草图或提示词 |
| D4 | 定义错误反馈与人工接管条件 | 异常处理清单 |
| D5 | 完成端到端演示并收集一次反馈 | 演示记录与改进项 |

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

- 用户在每个状态下是否知道下一步该做什么：
- 失败信息是否足够明确且不泄露敏感数据：
- 哪些场景必须由人工确认或接管：
