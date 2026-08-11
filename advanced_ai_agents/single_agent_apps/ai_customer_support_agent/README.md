## 🛒 AI Customer Support Agent with Memory
## 🛒 带记忆的 `AI Customer Support Agent`

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-customer-support-agent-with-memory) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整的分步教程](https://www.theunwindai.com/p/build-an-ai-customer-support-agent-with-memory)，学习如何从零开始构建此项目，包括详细的代码讲解、说明和最佳实践。**

This Streamlit app implements an AI-powered customer support agent for synthetic data generated using GPT-4o. The agent uses OpenAI's GPT-4o model and maintains a memory of past interactions using the Mem0 library with Qdrant as the vector store.
这个 `Streamlit` 应用实现了一个面向由 `GPT-4o` 生成的合成数据的 `AI` 客户支持智能体。该智能体使用 `OpenAI` 的 `GPT-4o` 模型，并通过 `Mem0` 库维护历史交互记忆，以 `Qdrant` 作为向量存储。

### Features
### 功能

- Chat interface for interacting with the AI customer support agent
  用于与 `AI` 客户支持智能体交互的聊天界面
- Persistent memory of customer interactions and profiles
  对客户交互和资料的持久化记忆
- Synthetic data generation for testing and demonstration
  用于测试和演示的合成数据生成
- Utilizes OpenAI's GPT-4o model for intelligent responses
  使用 `OpenAI` 的 `GPT-4o` 模型生成智能回复

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
   克隆 `GitHub` 仓库
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/single_agent_apps/ai_customer_support_agent
```

2. Install the required dependencies:
   安装所需依赖：

```bash
pip install -r requirements.txt
```

3. Ensure Qdrant is running:
   确保 `Qdrant` 正在运行：
The app expects Qdrant to be running on localhost:6333. Adjust the configuration in the code if your setup is different.
该应用期望 `Qdrant` 运行在 `localhost:6333`。如果你的设置不同，请在代码中调整配置。

```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant
```

4. Run the Streamlit App
   运行 `Streamlit` 应用
```bash
streamlit run customer_support_agent.py
```
