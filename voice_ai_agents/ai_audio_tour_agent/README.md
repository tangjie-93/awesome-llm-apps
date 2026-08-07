# 🎧 Self-Guided AI Audio Tour Agent
# 🎧 自助式 AI 语音导览 Agent

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-self-guided-ai-audio-tour-agent) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**

**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-a-self-guided-ai-audio-tour-agent)，学习如何从零开始构建该项目，并了解详细代码讲解、说明和最佳实践。**

A conversational voice agent system that generates immersive, self-guided audio tours based on the user's **location**, **areas of interest**, and **tour duration**. Built on a multi-agent architecture using OpenAI Agents SDK, real-time information retrieval, and expressive TTS for natural speech output.

这是一个对话式语音 Agent 系统，可根据用户的**位置**、**兴趣领域**和**导览时长**生成沉浸式自助语音导览。项目基于多 Agent 架构构建，使用 OpenAI Agents SDK、实时信息检索和富有表现力的 TTS 输出自然语音。

---

## 🚀 Features
## 🚀 功能特性

### 🎙️ Multi-Agent Architecture
### 🎙️ 多 Agent 架构

- **Orchestrator Agent**  
  Coordinates the overall tour flow, manages transitions, and assembles content from all expert agents.
- **编排 Agent**  
  协调整体导览流程，管理段落切换，并整合所有专家 Agent 生成的内容。

- **History Agent**  
  Delivers insightful historical narratives with an authoritative voice.
- **历史 Agent**  
  以权威语气讲述有洞察力的历史故事。

- **Architecture Agent**  
  Highlights architectural details, styles, and design elements using a descriptive and technical tone.
- **建筑 Agent**  
  用描述性和技术性的语气突出建筑细节、风格和设计元素。

- **Culture Agent**  
  Explores local customs, traditions, and artistic heritage with an enthusiastic voice.
- **文化 Agent**  
  以热情的语气介绍当地习俗、传统和艺术遗产。

- **Culinary Agent**  
  Describes iconic dishes and food culture in a passionate and engaging tone.
- **美食 Agent**  
  以生动且有感染力的语气介绍代表性菜品和饮食文化。

---

### 📍 Location-Aware Content Generation
### 📍 感知位置的内容生成

- Dynamic content generation based on user-input **location**
- 根据用户输入的**位置**动态生成内容
- Real-time **web search integration** to fetch relevant, up-to-date details
- 集成实时**网页搜索**，获取相关且最新的细节
- Personalized content delivery filtered by user **interest categories**
- 根据用户的**兴趣类别**筛选并生成个性化内容

---

### ⏱️ Customizable Tour Duration
### ⏱️ 可自定义导览时长

- Selectable tour length: **15, 30, or 60 minutes**
- 可选择导览时长：**15、30 或 60 分钟**
- Time allocations adapt to user interest weights and location relevance
- 时间分配会根据用户兴趣权重和地点相关性动态调整
- Ensures well-paced and proportioned narratives across sections
- 确保各个导览段落节奏合理、比例均衡

---

### 🔊 Expressive Speech Output
### 🔊 富有表现力的语音输出

- High-quality audio generated using **Gpt-4o Mini Audio**
- 使用 **Gpt-4o Mini Audio** 生成高质量音频

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
1. 克隆 GitHub 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd voice_ai_agents/ai_audio_tour_agent
```

2. Install the required dependencies:
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```

3. Get your OpenAI API Key
3. 获取你的 OpenAI API Key

- Sign up for an [OpenAI account](https://platform.openai.com/) (or the LLM provider of your choice) and obtain your API key.
- 注册 [OpenAI 账号](https://platform.openai.com/)（或你选择的 LLM 提供商账号），并获取 API Key。

4. Run the Streamlit App
4. 运行 Streamlit 应用

```bash
streamlit run ai_audio_tour_agent.py
```
