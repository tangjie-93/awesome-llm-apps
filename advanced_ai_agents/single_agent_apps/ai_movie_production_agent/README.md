## 🎬 AI Movie Production Agent
## 🎬 `AI` 电影制作智能体

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-movie-production-agent-with-claude-3-5-sonnet) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整的分步教程](https://www.theunwindai.com/p/build-an-ai-movie-production-agent-with-claude-3-5-sonnet)，学习如何通过详细代码演练、解释和最佳实践从零构建这个项目。**

This Streamlit app is an AI-powered movie production assistant that helps bring your movie ideas to life using Claude 3.5 Sonnet model. It automates the process of script writing and casting, allowing you to create compelling movie concepts with ease.
这个 `Streamlit` 应用是一个由 `AI` 驱动的电影制作助手，使用 `Claude 3.5 Sonnet` 模型帮助你把电影创意变为现实。它自动化剧本写作和选角流程，让你轻松创建有吸引力的电影概念。

### Features
### 功能
- Generates script outlines based on your movie idea, genre, and target audience
- 根据你的电影创意、类型和目标观众生成剧本大纲
- Suggests suitable actors for main roles, considering their past performances and current availability
- 根据演员过往表现和当前档期，为主要角色推荐合适演员
- Provides a concise movie concept overview
- 提供简明的电影概念概览

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
   克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/single_agent_apps/ai_movie_production_agent
```
2. Install the required dependencies:
   安装所需依赖：

```bash
pip install -r requirements.txt
```
3. Get your Anthropic API Key
   获取你的 `Anthropic API Key`

- Sign up for an [Anthropic account](https://console.anthropic.com) (or the LLM provider of your choice) and obtain your API key.
- 注册一个 [Anthropic account](https://console.anthropic.com)（或你选择的 `LLM` 提供商账号），并获取你的 `API key`。

4. Get your SerpAPI Key
   获取你的 `SerpAPI Key`

- Sign up for an [SerpAPI account](https://serpapi.com/) and obtain your API key.
- 注册一个 [SerpAPI account](https://serpapi.com/)，并获取你的 `API key`。

5. Run the Streamlit App
   运行 `Streamlit App`
```bash
streamlit run movie_production_agent.py
```

### How it Works?
### 工作原理

The AI Movie Production Agent utilizes three main components:
`AI Movie Production Agent` 使用三个主要组件：
- **ScriptWriter**: Develops a compelling script outline with character descriptions and key plot points based on the given movie idea and genre.
- **ScriptWriter**：根据给定的电影创意和类型，开发包含角色描述和关键情节点的有吸引力剧本大纲。
- **CastingDirector**: Suggests suitable actors for the main roles, considering their past performances and current availability.
- **CastingDirector**：根据演员过往表现和当前档期，为主要角色推荐合适演员。
- **MovieProducer**: Oversees the entire process, coordinating between the ScriptWriter and CastingDirector, and providing a concise movie concept overview.
- **MovieProducer**：监督整个流程，协调 `ScriptWriter` 和 `CastingDirector`，并提供简明的电影概念概览。
