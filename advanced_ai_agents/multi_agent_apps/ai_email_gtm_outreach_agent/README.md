### AI Email GTM Outreach Agent
### `AI Email GTM` 外联代理

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-email-gtm-outreach-agent-team) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-email-gtm-outreach-agent-team)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

An end-to-end, multi-agent Streamlit app that automates B2B outreach using GPT-5 and Exa. It discovers relevant companies, finds the right contacts (Founder's Office, GTM/Sales leadership, Partnerships/BD, Product Marketing), researches website + Reddit insights, and drafts tailored emails in your selected style.
一个端到端的多代理 `Streamlit` 应用，使用 `GPT-5` 和 `Exa` 自动化 `B2B` 外联。它会发现相关公司，查找合适联系人（创始人办公室、`GTM/Sales` 负责人、合作伙伴/`BD`、产品营销），研究网站和 `Reddit` 洞察，并按你选择的风格起草定制邮件。

## Features
## 功能

- **Multi-agent workflow**:
- **多代理工作流**：
  - **Company Finder**: Uses Exa to discover companies matching your targeting and offering.
  - **`Company Finder`**：使用 `Exa` 发现与你的目标定位和产品服务匹配的公司。
  - **Contact Finder**: Finds 2–3 relevant decision makers per company and emails (marks inferred emails clearly if needed).
  - **`Contact Finder`**：为每家公司查找 `2–3` 位相关决策者及其邮箱（如需推断邮箱，会明确标注）。
  - **Researcher**: Pulls 2–4 interesting insights per company from their website and Reddit to enable genuine personalization.
  - **`Researcher`**：从每家公司的网站和 `Reddit` 提取 `2–4` 条有价值洞察，以实现真实个性化。
  - **Email Writer**: Uses GPT-5 to produce concise, structured outreach emails.
  - **`Email Writer`**：使用 `GPT-5` 生成简洁、结构化的外联邮件。

- **Operator controls**:
- **操作者控制项**：
  - **Number of companies** to target (1–10)
  - 目标 **公司数量**（`1–10`）
  - **Email style**: Professional, Casual, Cold, or Consultative
  - **邮件风格**：`Professional`、`Casual`、`Cold` 或 `Consultative`
  - Live stage-by-stage progress UI and results with clean section dividers
  - 实时分阶段进度 `UI`，并用清晰分隔区展示结果

- **Security-first**:
- **安全优先**：
  - API keys entered in the Streamlit sidebar; not hardcoded or committed
  - `API keys` 在 `Streamlit` 侧边栏输入；不会硬编码或提交到仓库

## Requirements
## 要求

Install dependencies from `requirements.txt`:
从 `requirements.txt` 安装依赖：

```bash
pip install -r advanced_ai_agents/multi_agent_apps/ai_email_gtm_outreach_agent/requirements.txt
```

Required environment variables (set via sidebar or your shell):
必需环境变量（通过侧边栏或你的 `shell` 设置）：

- `OPENAI_API_KEY`
- `OPENAI_API_KEY`（`OpenAI API key` 环境变量）
- `EXA_API_KEY`
- `EXA_API_KEY`（`Exa API key` 环境变量）

## How to Run
## 运行方法

```bash
streamlit run advanced_ai_agents/multi_agent_apps/ai_email_gtm_outreach_agent/ai_email_gtm_outreach_agent.py
```

## Usage
## 使用方法

1. Enter your `OPENAI_API_KEY` and `EXA_API_KEY` in the left sidebar.
1. 在左侧边栏输入你的 `OPENAI_API_KEY` 和 `EXA_API_KEY`。
2. Provide targeting description and offering.
2. 提供目标定位描述和产品服务。
3. Choose number of companies and an email style.
3. 选择公司数量和邮件风格。
4. Click “Start Outreach”. Watch the stages: Companies → Contacts → Research → Emails.
4. 点击 “Start Outreach”。查看各阶段：Companies → Contacts → Research → Emails。
5. Review companies, contacts, research insights, and download or copy suggested emails.
5. 查看公司、联系人、研究洞察，并下载或复制建议邮件。

## Notes
## 说明

- The app uses the `gpt-5` model via OpenAI. If unavailable in your account, switch the model in `ai_email_gtm_outreach_agent.py` to one you have access to.
- 该应用通过 `OpenAI` 使用 `gpt-5` 模型。如果你的账户不可用，请在 `ai_email_gtm_outreach_agent.py` 中切换为你有权限访问的模型。
- Exa is used for web discovery; ensure your `EXA_API_KEY` is valid.
- `Exa` 用于网页发现；请确保你的 `EXA_API_KEY` 有效。

## Troubleshooting
## 故障排查

- If the app stalls on a stage, verify your API keys and network connectivity.
- 如果应用卡在某个阶段，请检查你的 `API keys` 和网络连接。
- If JSON parsing errors occur, rerun the stage; models occasionally add extra text around JSON.
- 如果出现 `JSON` 解析错误，请重新运行该阶段；模型偶尔会在 `JSON` 周围添加额外文本。
- For rate limits, reduce number of companies.
- 如遇速率限制，请减少公司数量。
