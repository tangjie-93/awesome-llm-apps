## 🗞️ AI Journalist Agent 
## 🗞️ `AI` 记者智能体

This Streamlit app is an AI-powered journalist agent that generates high-quality articles using OpenAI GPT-4o. It automates the process of researching, writing, and editing articles, allowing you to create compelling content on any topic with ease.
这个 `Streamlit` 应用是一个由 `AI` 驱动的记者智能体，使用 `OpenAI GPT-4o` 生成高质量文章。它自动化文章调研、写作和编辑流程，让你可以轻松围绕任何主题创建有吸引力的内容。

### Features
### 功能
- Searches the web for relevant information on a given topic
  针对给定主题在网络上搜索相关信息
- Writes well-structured, informative, and engaging articles
  撰写结构清晰、信息充分且有吸引力的文章
- Edits and refines the generated content to meet the high standards of the New York Times
  编辑并优化生成内容，使其达到 `New York Times` 的高标准

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
   克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/single_agent_apps/ai_journalist_agent
```
2. Install the required dependencies:
   安装所需依赖：

```bash
pip install -r requirements.txt
```
3. Get your OpenAI API Key
   获取你的 `OpenAI API Key`

- Sign up for an [OpenAI account](https://platform.openai.com/) (or the LLM provider of your choice) and obtain your API key.
  注册一个 [`OpenAI account`](https://platform.openai.com/)（或你选择的 `LLM` 提供商账号）并获取你的 `API key`。

4. Get your SerpAPI Key
   获取你的 `SerpAPI Key`

- Sign up for an [SerpAPI account](https://serpapi.com/) and obtain your API key.
  注册一个 [`SerpAPI account`](https://serpapi.com/) 并获取你的 `API key`。

5. Run the Streamlit App
   运行 `Streamlit` 应用
```bash
streamlit run journalist_agent.py
```

### How it Works?
### 工作原理

The AI Journalist Agent utilizes three main components:
`AI Journalist Agent` 使用三个主要组件：
- Searcher: Responsible for generating search terms based on the given topic and searching the web for relevant URLs using the SerpAPI.
  `Searcher`：负责根据给定主题生成搜索词，并使用 `SerpAPI` 在网络上搜索相关 `URL`。
- Writer: Retrieves the text from the provided URLs using the NewspaperToolkit and writes a high-quality article based on the extracted information.
  `Writer`：使用 `NewspaperToolkit` 从提供的 `URL` 中提取文本，并基于提取的信息撰写高质量文章。
- Editor: Coordinates the workflow between the Searcher and Writer, and performs final editing and refinement of the generated article.
  `Editor`：协调 `Searcher` 和 `Writer` 之间的工作流，并对生成的文章进行最终编辑和优化。
