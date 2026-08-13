# Enterprise RAG 首批业务范围清单

> 版本：v0.1
> 日期：2026-08-13

## 目的

定义阶段 0 和阶段 1 的首批业务覆盖范围，避免知识库扩展失焦。

## 首批业务域

1. `security`
2. `hr`
3. `it`

## 首批问题类型

- 制度查询
- 流程查询
- 规范查询
- FAQ 查询
- 事件响应与操作说明

## 首批文档类型

- Markdown
- 纯文本
- FAQ

## 首批样例文档

- `security/access_policy.md`
- `security/incident_response.md`
- `hr/onboarding.md`
- `it/backup_policy.md`

## 不纳入范围

- 法务合同审查
- 财务报表推理
- 多媒体内容解析
- 外部网页自动抓取
- 自动执行业务动作

## 交付要求

- 每个业务域必须能单独定义知识库。
- 每个知识库必须能映射到文档组权限。
- 每个样例文档必须能被检索和引用。

