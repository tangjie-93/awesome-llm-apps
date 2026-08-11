<div align="center">

  <h1>🪟 Windows Use Autonomous Agent</h1>
  <h1>🪟 <code>Windows Use</code> 自主智能体</h1>

  <a href="https://github.com/CursorTouch/windows-use/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  </a>
  <img src="https://img.shields.io/badge/python-3.12%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-blue" alt="Platform">
  <br>

  <a href="https://x.com/CursorTouch">
    <img src="https://img.shields.io/badge/follow-%40CursorTouch-1DA1F2?logo=twitter&style=flat" alt="Follow on Twitter">
  </a>
  <a href="https://discord.com/invite/Aue9Yj2VzS">
    <img src="https://img.shields.io/badge/Join%20on-Discord-5865F2?logo=discord&logoColor=white&style=flat" alt="Join us on Discord">
  </a>

</div>

<br>

**Windows-Use** is a powerful automation agent that interact directly with the Windows at GUI layer. It bridges the gap between AI Agents and the Windows OS to perform tasks such as opening apps, clicking buttons, typing, executing shell commands, and capturing UI state all without relying on traditional computer vision models. Enabling any LLM to perform computer automation instead of relying on specific models for it.
**`Windows-Use`** 是一个强大的自动化智能体，可直接在 `Windows` 的 `GUI` 层进行交互。它弥合了 `AI Agents` 与 `Windows OS` 之间的差距，可执行打开应用、点击按钮、输入文本、执行 `shell` 命令和捕获 `UI` 状态等任务，全程无需依赖传统计算机视觉模型。这让任何 `LLM` 都能执行计算机自动化，而不必依赖专门模型。

## 🛠️Installation Guide
## 🛠️安装指南

### **Prerequisites**
### **前置条件**

- Python 3.12 or higher
- `Python 3.12` 或更高版本
- [UV](https://github.com/astral-sh/uv) (or `pip`)
- [UV](https://github.com/astral-sh/uv)（或 `pip`）
- Windows 10 or 11
- `Windows 10` 或 `11`

### **Installation Steps**
### **安装步骤**

**Install using `uv`:**
**使用 `uv` 安装：**

```bash
uv pip install windows-use
````

Or with pip:
或使用 `pip`：

```bash
pip install windows-use
```

## ⚙️Basic Usage
## ⚙️基本用法

```python
# main.py
from langchain_google_genai import ChatGoogleGenerativeAI
from windows_use.agent import Agent
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash')
agent = Agent(llm=llm,use_vision=True)
query=input("Enter your query: ")
agent_result=agent.invoke(query=query)
print(agent_result.content)
```

## 🤖 Run Agent
## 🤖 运行智能体

You can use the following to run from a script:
你可以使用以下方式从脚本运行：

```bash
python main.py
Enter your query: <YOUR TASK>
```

---

## 🎥 Demos
## 🎥 演示

**PROMPT:** Write a short note about LLMs and save to the desktop
**提示词：** 写一段关于 `LLMs` 的简短笔记并保存到桌面

<https://github.com/user-attachments/assets/0faa5179-73c1-4547-b9e6-2875496b12a0>

**PROMPT:** Change from Dark mode to Light mode
**提示词：** 从深色模式切换到浅色模式

<https://github.com/user-attachments/assets/47bdd166-1261-4155-8890-1b2189c0a3fd>

## Vision
## 愿景

Talk to your computer. Watch it get things done.
对你的电脑说话，看着它完成任务。

## Roadmap
## 路线图

### 🤖 Agent Intelligence
### 🤖 智能体智能

* [ ] **Integrate memory** : allow the agent to remember past interactions made by the user.
* [ ] **集成记忆**：允许智能体记住用户过去进行的交互。
* [ ] **Optimize token usage** : implement strategies like Ally Tree compression and prompt engineering to reduce overhead.
* [ ] **优化 `token` 使用**：实现 `Ally Tree` 压缩和提示工程等策略以减少开销。
* [ ] **Simulate advanced human-like input** : enable accurate and naturalistic mouse & keyboard interactions across apps.
* [ ] **模拟高级类人输入**：在多个应用中实现准确且自然的鼠标和键盘交互。
* [ ] **Support for local LLMs** : local models with near-parity performance to cloud-based APIs (e.g., Mistral, LLaMA, etc.).
* [ ] **支持本地 `LLMs`**：让本地模型具备接近云端 `APIs` 的性能（例如 `Mistral`、`LLaMA` 等）。
* [ ] **Improve reasoning and planning** : enhance the agent's ability to break down and sequence complex tasks.
* [ ] **改进推理和规划**：增强智能体拆解复杂任务并排序执行的能力。

### 🌳 Ally Tree Optimization
### 🌳 `Ally Tree` 优化

* [ ] **Improve UI element detection** : automatically identify and prioritize essential, interactive components on screen.
* [ ] **改进 `UI` 元素检测**：自动识别并优先处理屏幕上的关键交互组件。
* [ ] **Compress Ally Tree intelligently** : reduce complexity by pruning irrelevant branches.
* [ ] **智能压缩 `Ally Tree`**：通过剪除无关分支降低复杂度。
* [ ] **Context-aware prioritization** : rank UI elements based on relevance to the task at hand.
* [ ] **上下文感知优先级排序**：根据与当前任务的相关性对 `UI` 元素排序。

### 💡 User Experience
### 💡 用户体验

* [ ] **Reduce latency** : optimize to improve response time between GUI interaction.
* [ ] **降低延迟**：通过优化提升 `GUI` 交互之间的响应时间。
* [ ] **Polish command interface** : make it easier to write, speak, or type commands through a simplified UX layer.
* [ ] **打磨命令界面**：通过简化的 `UX` 层，让编写、说出或输入命令更容易。
* [ ] **Better error handling & recovery** : ensure graceful handling of edge cases and unclear instructions.
* [ ] **更好的错误处理和恢复**：确保优雅处理边缘情况和不清晰指令。

### 🧪 Evaluation
### 🧪 评估

* [ ] **LLM evaluation benchmarks** — track performance across different models and benchmarks.
* [ ] **`LLM` 评估基准** — 跟踪不同模型和基准上的性能。

## ⚠️ Caution
## ⚠️ 注意

Agent interacts directly with your Windows OS at GUI layer to perform actions. While the agent is designed to act intelligently and safely, it can make mistakes that might bring undesired system behaviour or cause unintended changes. Try to run the agent in a sandbox envirnoment.
智能体会直接在 `GUI` 层与你的 `Windows OS` 交互并执行操作。虽然该智能体被设计为智能且安全地行动，但它仍可能犯错，导致不期望的系统行为或意外更改。请尽量在沙盒环境中运行该智能体。

Made with ❤️ by [Jeomon George](https://github.com/Jeomon)
由 [Jeomon George](https://github.com/Jeomon) 用心制作

---

## Citation
## 引用

```bibtex
@software{
  author       = {George, Jeomon},
  title        = {Windows-Use: Enable AI to control Windows OS},
  year         = {2025},
  publisher    = {GitHub},
  url={https://github.com/CursorTouch/Windows-Use}
}
```
