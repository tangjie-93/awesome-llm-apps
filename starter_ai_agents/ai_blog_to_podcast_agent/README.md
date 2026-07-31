# Blog to Podcast Agent
# 博客转播客代理

This Streamlit app converts blog posts into podcast audio.
这个 Streamlit 应用可以把博客文章转换成播客音频。

It uses OpenAI for summarization, Firecrawl for scraping, and ElevenLabs for speech generation.
它使用 OpenAI 做摘要，Firecrawl 抓取内容，ElevenLabs 生成语音。

## Features
## 功能特性

- Scrape public blog posts from a URL.
- 从 URL 抓取公开博客内容。
- Generate a concise summary for the episode.
- 为播客内容生成简洁摘要。
- Turn the summary into MP3 audio.
- 将摘要转换为 MP3 音频。
- Keep API keys in the Streamlit sidebar.
- 在 Streamlit 侧边栏中管理 API Key。

## Setup
## 安装

1. Clone the repository.
1. 克隆仓库。
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps
   cd starter_ai_agents/ai_blog_to_podcast_agent
   ```
2. Install dependencies.
2. 安装依赖。
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app.
3. 运行应用。
   ```bash
   streamlit run blog_to_podcast_agent.py
   ```

## Usage
## 使用方式

1. Enter your OpenAI, Firecrawl, and ElevenLabs API keys.
1. 输入 OpenAI、Firecrawl 和 ElevenLabs 的 API Key。
2. Paste a blog URL.
2. 粘贴博客链接。
3. Click Generate Podcast.
3. 点击生成播客。
4. Listen to or download the result.
4. 收听或下载生成结果。
