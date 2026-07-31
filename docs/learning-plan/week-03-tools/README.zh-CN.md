# 第 3 周：工具调用

**目标**：让 Agent 在受控边界内使用工具。需理解工具定义、参数限制和失败回传。**本周输出**：一个只读工具、调用日志与失败提示。

## 本周指定目录与文件

- 主示例目录：[web_scraping_ai_agent](../../../starter_ai_agents/web_scraping_ai_agent/)
- 项目说明：[README.md](../../../starter_ai_agents/web_scraping_ai_agent/README.md)
- 依赖文件：[requirements.txt](../../../starter_ai_agents/web_scraping_ai_agent/requirements.txt)
- 云端入口：[ai_scrapper.py](../../../starter_ai_agents/web_scraping_ai_agent/ai_scrapper.py)
- 本地入口：[local_ai_scrapper.py](../../../starter_ai_agents/web_scraping_ai_agent/local_ai_scrapper.py)
- 对照示例：[ai_travel_agent/travel_agent.py](../../../starter_ai_agents/ai_travel_agent/travel_agent.py)

| 学习日 | 学习任务 | 当日输出 |
| --- | --- | --- |
| D1 | 阅读 [ai_scrapper.py](../../../starter_ai_agents/web_scraping_ai_agent/ai_scrapper.py) 的网页抓取调用链和输入参数 | 工具输入输出说明 |
| D2 | 原样运行网页抓取示例，记录什么时候调用抓取工具 | 调用日志 |
| D3 | 参考 [travel_agent.py](../../../starter_ai_agents/ai_travel_agent/travel_agent.py) 的搜索用法，增加一个只读查询工具 | 工具实现 |
| D4 | 为 URL、搜索词或数量参数加入范围/枚举限制 | 参数边界表 |
| D5 | 模拟网页不可访问或工具失败，检查用户提示 | 失败用例 |

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

- 工具何时不应被调用：
- 参数限制是否可验证：
- 下周准备验证的假设：
