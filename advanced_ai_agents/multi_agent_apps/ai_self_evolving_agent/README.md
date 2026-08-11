# 🧬 Self-Evolving AI Agent
# 🧬 自进化 `AI Agent`

A multi-agent app built on [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) that turns a
single natural-language goal into a working program. It **automatically generates a
multi-agent workflow**, executes it to produce code, then **verifies and repairs** that code
with a second model — no manual agent wiring required.
这是一个基于 [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) 构建的多智能体应用，可将单个自然语言目标转化为可运行程序。它会**自动生成多智能体工作流**，执行该工作流来产出代码，然后使用第二个模型**验证并修复**代码，无需手动连接智能体。

The included example takes the goal *"Generate HTML code for a Tetris game that can be played
in the browser"* and writes a ready-to-play `index.html`.
内置示例使用目标 *"Generate HTML code for a Tetris game that can be played in the browser"*，并生成一个可直接游玩的 `index.html`。

## ✨ What It Demonstrates
## ✨ 它展示了什么

- **Automatic workflow generation** — `WorkFlowGenerator` designs the agents and steps from a plain-English goal.
- **自动工作流生成** — `WorkFlowGenerator` 会根据普通英文目标设计智能体和步骤。
- **Multi-agent execution** — `AgentManager` + `WorkFlow` instantiate and run the generated agents.
- **多智能体执行** — `AgentManager` + `WorkFlow` 会实例化并运行生成的智能体。
- **Cross-model code verification** — generation runs on OpenAI `gpt-4o-mini`; a separate Anthropic Claude pass verifies and fixes the output.
- **跨模型代码验证** — 生成过程运行在 `OpenAI` 的 `gpt-4o-mini` 上；单独的 `Anthropic Claude` 流程会验证并修复输出。
- **Self-evolving by design** — the workflow is built and refined by the system itself rather than hand-coded.
- **按设计自进化** — 工作流由系统自行构建和优化，而不是手写编码。

## 🛠️ How to Get Started
## 🛠️ 如何开始

1. **Clone the repository**
1. **克隆仓库**
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/advanced_ai_agents/multi_agent_apps/ai_self_evolving_agent
   ```

2. **Install dependencies**
2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   pip install git+https://github.com/EvoAgentX/EvoAgentX.git
   ```

3. **Set your API keys**
3. **设置你的 `API key`**
   ```bash
   export OPENAI_API_KEY=<your-openai-api-key>
   export ANTHROPIC_API_KEY=<your-anthropic-api-key>
   ```
   (Or place them in a `.env` file in this folder.)
   （也可以将它们放入此文件夹中的 `.env` 文件。）

4. **Run the agent**
4. **运行智能体**
   ```bash
   python ai_Self-Evolving_agent.py
   ```
   The generated game is written to `examples/output/tetris_game/index.html` — open it in a browser to play.
   生成的游戏会写入 `examples/output/tetris_game/index.html`，在浏览器中打开即可游玩。

## 🔧 How It Works
## 🔧 工作原理

1. **Define a goal** in natural language (e.g. build a Tetris game).
1. 用自然语言**定义目标**（例如构建一个 `Tetris` 游戏）。
2. **Generate a workflow** — `WorkFlowGenerator` produces a multi-agent graph for the goal.
2. **生成工作流** — `WorkFlowGenerator` 会为目标生成一个多智能体图。
3. **Run the workflow** — `AgentManager` builds the agents and `WorkFlow` executes them with `gpt-4o-mini`.
3. **运行工作流** — `AgentManager` 构建智能体，`WorkFlow` 使用 `gpt-4o-mini` 执行它们。
4. **Verify the output** — a Claude model (via LiteLLM) reviews and repairs the generated code through `CodeVerification`.
4. **验证输出** — `Claude` 模型（通过 `LiteLLM`）会使用 `CodeVerification` 审查并修复生成的代码。
5. **Save the result** — the final code is extracted and written to the output directory.
5. **保存结果** — 最终代码会被提取并写入输出目录。

## 📚 Learn More
## 📚 了解更多

This example is powered by the open-source **EvoAgentX** framework. For docs, tutorials, and
additional optimizers (TextGrad, AFlow, MIPRO), see the
[EvoAgentX repository](https://github.com/EvoAgentX/EvoAgentX).
此示例由开源 **`EvoAgentX`** 框架驱动。如需文档、教程和其他优化器（`TextGrad`、`AFlow`、`MIPRO`），请参阅 [EvoAgentX 仓库](https://github.com/EvoAgentX/EvoAgentX)。
