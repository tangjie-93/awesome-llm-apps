## 📰 Multi-Agent AI Researcher
## 📰 多智能体 `AI` 研究员

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-multi-agent-llm-app-with-gpt-4o) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-multi-agent-llm-app-with-gpt-4o)，通过详细代码讲解、说明和最佳实践学习如何从零构建该应用。**

This Streamlit app empowers you to research top stories and users on HackerNews using a team of AI assistants with GPT-4o. 
这个 `Streamlit` 应用让你可以使用由 `GPT-4o` 驱动的 `AI` 助手团队，研究 `HackerNews` 上的热门故事和用户。

### Features
### 功能
- Research top stories and users on HackerNews
- 研究 `HackerNews` 上的热门故事和用户
- Utilize a team of AI assistants specialized in story and user research
- 使用专门从事故事和用户研究的 `AI` 助手团队
- Generate blog posts, reports, and social media content based on your research queries
- 根据你的研究查询生成博客文章、报告和社交媒体内容

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
1. 克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/multi_agent_apps/multi_agent_researcher
```
2. Install the required dependencies:
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```
3. Get your OpenAI API Key
3. 获取你的 `OpenAI API Key`

- Sign up for an [OpenAI account](https://platform.openai.com/) (or the LLM provider of your choice) and obtain your API key.
- 注册 [OpenAI 账号](https://platform.openai.com/)（或你选择的 `LLM` 提供商账号），并获取你的 `API key`。

4. Run the Streamlit App
4. 运行 `Streamlit` 应用
```bash
streamlit run research_agent.py
```

### How it works?
### 工作原理

- Upon running the app, you will be prompted to enter your OpenAI API key. This key is used to authenticate and access the OpenAI language models.
- 运行应用后，系统会提示你输入 `OpenAI API key`。该密钥用于身份验证并访问 `OpenAI` 语言模型。
- Once you provide a valid API key, three specialized AI agents are created:
- 提供有效 `API key` 后，将创建三个专门的 `AI` 智能体：
    - **HackerNews Researcher**: Specializes in getting top stories from HackerNews using the HackerNews API.
    - **`HackerNews` 研究员**：专门使用 `HackerNews API` 获取 `HackerNews` 热门故事。
    - **Web Searcher**: Searches the web for additional information on topics using DuckDuckGo search.
    - **网页搜索器**：使用 `DuckDuckGo` 搜索来查找主题的更多网络信息。
    - **Article Reader**: Reads and extracts content from article URLs using newspaper4k tools.
    - **文章阅读器**：使用 `newspaper4k` 工具从文章 `URL` 中读取并提取内容。

- These agents work together as a coordinated team under the **HackerNews Team** which orchestrates the research process.
- 这些智能体在 **`HackerNews Team`** 下作为协调团队协同工作，由该团队编排研究流程。
- Enter your research query in the provided text input field. This could be a topic, keyword, or specific question related to HackerNews stories or users.
- 在提供的文本输入框中输入你的研究查询。它可以是与 `HackerNews` 故事或用户相关的主题、关键词或具体问题。
- The HackerNews Team follows a structured workflow:
- `HackerNews Team` 遵循结构化工作流：
    1. First searches HackerNews for relevant stories based on your query
    1. 首先根据你的查询在 `HackerNews` 中搜索相关故事
    2. Uses the Article Reader to extract detailed content from the story URLs
    2. 使用 `Article Reader` 从故事 `URL` 中提取详细内容
    3. Leverages the Web Searcher to gather additional context and information
    3. 利用 `Web Searcher` 收集更多上下文和信息
    4. Finally provides a thoughtful and engaging summary with title, summary, and reference links
    4. 最后提供包含标题、摘要和参考链接的周到且有吸引力的总结
- The generated content is structured as an Article with a title, summary, and reference links for easy review and use.
- 生成的内容会以文章形式组织，包含标题、摘要和参考链接，便于审阅和使用。
