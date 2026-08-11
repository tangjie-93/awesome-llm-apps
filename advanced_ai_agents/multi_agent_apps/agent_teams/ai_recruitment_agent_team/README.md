# 💼 AI Recruitment Agent Team
# 💼 AI 招聘智能体团队

A Streamlit application that simulates a full-service recruitment team using multiple AI agents to automate and streamline the hiring process.
一个 `Streamlit` 应用，使用多个 `AI Agent` 模拟全流程招聘团队，以自动化并简化招聘流程。

Each agent represents a different recruitment specialist role - from resume analysis and candidate evaluation to interview scheduling and communication - working together to provide comprehensive hiring solutions.
每个智能体代表不同的招聘专家角色，从简历分析、候选人评估到面试安排和沟通协作，共同提供完整的招聘解决方案。

The system combines the expertise of technical recruiters, HR coordinators, and scheduling specialists into a cohesive automated workflow.
该系统将技术招聘人员、`HR` 协调员和日程安排专家的能力整合为一个连贯的自动化工作流。

## Features
## 功能

#### Specialized AI Agents
#### 专业化 AI 智能体

- Technical Recruiter Agent: Analyzes resumes and evaluates technical skills
- 技术招聘智能体：分析简历并评估技术技能
- Communication Agent: Handles professional email correspondence
- 沟通智能体：处理专业电子邮件往来
- Scheduling Coordinator Agent: Manages interview scheduling and coordination
- 日程协调智能体：管理面试日程安排与协调
- Each agent has specific expertise and collaborates for comprehensive recruitment
- 每个智能体都有特定专业能力，并通过协作完成完整招聘流程

#### End-to-End Recruitment Process
#### 端到端招聘流程

- Automated resume screening and analysis
- 自动化简历筛选与分析
- Role-specific technical evaluation
- 面向岗位的技术评估
- Professional candidate communication
- 专业的候选人沟通
- Automated interview scheduling
- 自动化面试安排
- Integrated feedback system
- 集成反馈系统

## Important Things to do before running the application
## 运行应用前的重要准备事项

- Create/Use a new Gmail account for the recruiter
- 为招聘人员创建或使用一个新的 `Gmail` 账号
- Enable 2-Step Verification and generate an App Password for the Gmail account
- 为该 `Gmail` 账号启用两步验证，并生成一个应用专用密码
- The App Password is a 16 digit code (use without spaces) that should be generated here - [Google App Password](https://support.google.com/accounts/answer/185833?hl=en) Please go through the steps to generate the password - it will of the format - 'afec wejf awoj fwrv' (remove the spaces and enter it in the streamlit app)
- 应用专用密码是一个 `16` 位代码（使用时不要包含空格），应在这里生成：[Google App Password](https://support.google.com/accounts/answer/185833?hl=en)。请按照步骤生成密码，其格式类似于 `'afec wejf awoj fwrv'`（删除空格后输入到 `Streamlit` 应用中）。
- Create/ Use a Zoom account and go to the Zoom App Marketplace to get the API credentials :
- 创建或使用一个 `Zoom` 账号，并前往 `Zoom App Marketplace` 获取 `API` 凭据：
[Zoom Marketplace](https://marketplace.zoom.us)
- Go to Developer Dashboard and create a new app - Select Server to Server OAuth and get the credentials, You see 3 credentials - Client ID, Client Secret and Account ID
- 前往 `Developer Dashboard` 创建新应用，选择 `Server to Server OAuth` 并获取凭据；你会看到 `3` 个凭据：`Client ID`、`Client Secret` 和 `Account ID`。
- After that, you need to add a few scopes to the app - so that the zoom link of the candidate is sent and created through the mail.
- 之后需要为应用添加若干 `scope`，以便通过邮件创建并发送候选人的 `Zoom` 链接。
- The Scopes are meeting:write:invite_links:admin, meeting:write:meeting:admin, meeting:write:meeting:master, meeting:write:invite_links:master, meeting:write:open_app:admin, user:read:email:admin, user:read:list_users:admin, billing:read:user_entitlement:admin, dashboard:read:list_meeting_participants:admin [last 3 are optional]
- 需要的 `Scope` 包括 `meeting:write:invite_links:admin`、`meeting:write:meeting:admin`、`meeting:write:meeting:master`、`meeting:write:invite_links:master`、`meeting:write:open_app:admin`、`user:read:email:admin`、`user:read:list_users:admin`、`billing:read:user_entitlement:admin`、`dashboard:read:list_meeting_participants:admin`（最后 `3` 个为可选）。

## How to Run
## 如何运行

1. **Setup Environment**
1. **设置环境**
   ```bash
   # Clone the repository
    git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
    cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_recruitment_agent_team
    
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
2. **配置 API 密钥**
   - OpenAI API key for GPT-4o access
   - 用于访问 `GPT-4o` 的 `OpenAI API` 密钥
   - Zoom API credentials (Account ID, Client ID, Client Secret)
   - `Zoom API` 凭据（`Account ID`、`Client ID`、`Client Secret`）
   - Email App Password of Recruiter's Email
   - 招聘人员邮箱的应用专用密码

3. **Run the Application**
3. **运行应用**
   ```bash
   streamlit run ai_recruitment_agent_team.py
   ```

## System Components
## 系统组件

- **Resume Analyzer Agent**
- **简历分析智能体**
  - Skills matching algorithm
  - 技能匹配算法
  - Experience verification
  - 经验核验
  - Technical assessment
  - 技术评估
  - Selection decision making
  - 筛选决策

- **Email Communication Agent**
- **邮件沟通智能体**
  - Professional email drafting
  - 专业邮件起草
  - Automated notifications
  - 自动化通知
  - Feedback communication
  - 反馈沟通
  - Follow-up management
  - 跟进管理

- **Interview Scheduler Agent**
- **面试日程智能体**
  - Zoom meeting coordination
  - `Zoom` 会议协调
  - Calendar management
  - 日历管理
  - Timezone handling
  - 时区处理
  - Reminder system
  - 提醒系统

- **Candidate Experience**
- **候选人体验**
  - Simple upload interface
  - 简单的上传界面
  - Real-time feedback
  - 实时反馈
  - Clear communication
  - 清晰沟通
  - Streamlined process
  - 简化流程

## Technical Stack
## 技术栈

- **Framework**: Phidata
- **框架**：`Phidata`
- **Model**: OpenAI GPT-4o
- **模型**：`OpenAI GPT-4o`
- **Integration**: Zoom API, EmailTools Tool from Phidata
- **集成**：`Zoom API`、`Phidata` 的 `EmailTools Tool`
- **PDF Processing**: PyPDF2
- **PDF 处理**：`PyPDF2`
- **Time Management**: pytz
- **时间管理**：`pytz`
- **State Management**: Streamlit Session State
- **状态管理**：`Streamlit Session State`

## Disclaimer
## 免责声明

This tool is designed to assist in the recruitment process but should not completely replace human judgment in hiring decisions.
此工具旨在辅助招聘流程，但不应在招聘决策中完全取代人工判断。

All automated decisions should be reviewed by human recruiters for final approval.
所有自动化决策都应由人工招聘人员复核并最终批准。

## Future Enhancements
## 未来增强

- Integration with ATS systems
- 与 `ATS` 系统集成
- Advanced candidate scoring
- 高级候选人评分
- Video interview capabilities
- 视频面试能力
- Skills assessment integration
- 技能评估集成
- Multi-language support
- 多语言支持
