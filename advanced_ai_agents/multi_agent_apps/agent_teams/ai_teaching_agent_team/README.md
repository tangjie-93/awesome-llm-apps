# 👨‍🏫 AI Teaching Agent Team
# 👨‍🏫 AI 教学智能体团队

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-teaching-agent-team) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-teaching-agent-team)，通过详细代码讲解、说明和最佳实践，学习如何从零构建这个应用。**

A Streamlit application that brings together a team of specialized AI teaching agents who collaborate like a professional teaching faculty.
一个 `Streamlit` 应用，汇集一组专业化 `AI` 教学智能体，让它们像专业教师团队一样协作。

Each agent acts as a specialized educator: a curriculum designer, learning path expert, resource librarian, and practice instructor - working together to create a complete educational experience through Google Docs.
每个智能体都扮演专业教育者角色：课程设计师、学习路径专家、资源馆员和练习指导老师，并通过 `Google Docs` 协作创建完整的学习体验。

## 🪄 Meet your AI Teaching Agent Team
## 🪄 认识你的 AI 教学智能体团队

#### 🧠 Professor Agent
#### 🧠 教授智能体

- Creates fundamental knowledge base in Google Docs
- 在 `Google Docs` 中创建基础知识库
- Organizes content with proper headings and sections
- 使用合适的标题和章节组织内容
- Includes detailed explanations and examples
- 包含详细解释和示例
- Output: Comprehensive knowledge base document with table of contents
- 输出：带目录的综合知识库文档

#### 🗺️ Academic Advisor Agent
#### 🗺️ 学术顾问智能体

- Designs learning path in a structured Google Doc
- 在结构化的 `Google Doc` 中设计学习路径
- Creates progressive milestone markers
- 创建渐进式里程碑标记
- Includes time estimates and prerequisites
- 包含时间估算和先修要求
- Output: Visual roadmap document with clear progression paths
- 输出：带清晰进阶路径的可视化路线图文档

#### 📚 Research Librarian Agent
#### 📚 研究馆员智能体

- Compiles resources in an organized Google Doc
- 在有序的 `Google Doc` 中汇编资源
- Includes links to academic papers and tutorials
- 包含学术论文和教程链接
- Adds descriptions and difficulty levels
- 添加描述和难度等级
- Output: Categorized resource list with quality ratings
- 输出：带质量评级的分类资源列表

#### ✍️ Teaching Assistant Agent
#### ✍️ 助教智能体

- Develops exercises in an interactive Google Doc
- 在交互式 `Google Doc` 中开发练习
- Creates structured practice sections
- 创建结构化练习章节
- Includes solution guides
- 包含解答指南
- Output: Complete practice workbook with answers
- 输出：带答案的完整练习册

## How to Run
## 如何运行

1. Clone the repository
1. 克隆仓库
  ```bash
   # Clone the repository
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_teaching_agent_team

   # Install dependencies
   pip install -r requirements.txt
   ```

## Configuration - IMPORTANT STEP
## 配置 - 重要步骤

1. Get your OpenAI API Key
1. 获取你的 `OpenAI API Key`

- Create an account on [OpenAI Platform](https://platform.openai.com/)
- 在 [OpenAI Platform](https://platform.openai.com/) 创建账号
- Navigate to API Keys section
- 前往 `API Keys` 区域
- Create a new API key
- 创建新的 `API key`

2. Get your Composio API Key
2. 获取你的 `Composio API Key`

- Create an account on [Composio Platform](https://composio.ai/)
- 在 [Composio Platform](https://composio.ai/) 创建账号
- **IMPORTANT** - For you to use the app, you need to make new connection ID with google docs and composio.Follow the below two steps to do so:
- **重要**：要使用该应用，你需要为 `Google Docs` 和 `Composio` 创建新的连接 `ID`。请按下面两步操作：
  - composio add googledocs (IN THE TERMINAL)
  - `composio add googledocs`（在终端中执行）
  - Create a new connection
  - 创建一个新连接
  - Select OAUTH2
  - 选择 `OAUTH2`
  - Select Google Account and Done.
  - 选择 `Google Account` 并完成。
  - On the composio account website, go to apps, select google docs tool, and [click create integration](https://app.composio.dev/app/googledocs) (violet button) and click Try connecting default’s googldocs button and we are done.
  - 在 `Composio` 账号网站中，进入 `apps`，选择 `google docs` 工具，然后[点击 create integration](https://app.composio.dev/app/googledocs)（紫色按钮），再点击 `Try connecting default’s googldocs` 按钮，即可完成。

3. Sign up and get the [SerpAPI Key](https://serpapi.com/)
3. 注册并获取 [SerpAPI Key](https://serpapi.com/)

## How to Use?
## 如何使用？

1. Start the Streamlit app
1. 启动 `Streamlit` 应用

```bash
streamlit run teaching_agent_team.py
```

2. Use the application
2. 使用应用

- Enter your OpenAI API key in the sidebar (if not set in environment)
- 在侧边栏输入你的 `OpenAI API key`（如果未在环境中设置）
- Enter your Composio API key in the sidebar
- 在侧边栏输入你的 `Composio API key`
- Type a topic you want to learn about (e.g., "Python Programming", "Machine Learning")
- 输入你想学习的主题（例如“Python Programming”、“Machine Learning”）
- Click "Generate Learning Plan"
- 点击“Generate Learning Plan”
- Wait for the agents to generate your personalized learning plan
- 等待智能体生成你的个性化学习计划
- View the results and terminal output in the interface
- 在界面中查看结果和终端输出
