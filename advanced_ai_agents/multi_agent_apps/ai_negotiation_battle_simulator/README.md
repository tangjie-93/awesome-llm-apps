# 🎮 AI Negotiation Battle Simulator
# 🎮 `AI` 谈判对战模拟器

### A Real-Time Agent vs Agent Showdown with AG-UI!
### 使用 `AG-UI` 的实时智能体对智能体对决！

Watch two AI agents battle it out in an epic used car negotiation! Built with **Google ADK** for the backend agents and **AG-UI + CopilotKit** for a jaw-dropping reactive frontend.
观看两个 `AI` 智能体在一场精彩的二手车谈判中对决！后端智能体使用 **`Google ADK`** 构建，令人惊艳的响应式前端使用 **`AG-UI` + `CopilotKit`** 构建。

## ✨ Features
## ✨ 功能

- **🤖 Dual AI Agents**: Buyer vs Seller with distinct personalities and negotiation strategies
- **🤖 双 `AI` 智能体**：买家对卖家，拥有不同个性和谈判策略
- **🔄 AG-UI Protocol**: Real-time streaming of agent actions, tool calls, and state changes
- **🔄 `AG-UI Protocol`**：实时流式传输智能体动作、工具调用和状态变化
- **💅 Jaw-Dropping UI**: Animated battle arena with live negotiation timeline
- **💅 惊艳 `UI`**：带实时谈判时间线的动画对战场景
- **🎭 8 Unique Personalities**: 4 buyers + 4 sellers with different negotiation styles
- **🎭 `8` 种独特个性**：`4` 个买家 + `4` 个卖家，拥有不同谈判风格
- **📊 Generative UI**: Custom React components render tool calls in real-time
- **📊 生成式 `UI`**：自定义 `React` 组件实时渲染工具调用
- **🔗 Shared State**: Agent state syncs bidirectionally with the frontend
- **🔗 共享状态**：智能体状态与前端双向同步

## 🏗️ Architecture
## 🏗️ 架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Next.js + CopilotKit Frontend                │
│   ┌─────────────┐    ┌──────────────┐    ┌─────────────┐        │
│   │ Battle Arena│    │  VS Display  │    │Chat Sidebar │        │
│   │   Timeline  │    │ Buyer/Seller │    │ (AG-UI)     │        │
│   └──────┬──────┘    └──────────────┘    └──────┬──────┘        │
└──────────┼────────────────────────────────────────┼─────────────┘
           │              AG-UI Events              │
           └────────────────────┬───────────────────┘
                                │
                    ┌───────────▼───────────┐
                    │   CopilotKit Runtime  │
                    │   (/api/copilotkit)   │
                    └───────────┬───────────┘
                                │ HTTP/SSE
                    ┌───────────▼───────────┐
                    │    FastAPI + AG-UI    │
                    │    ADK Middleware     │
                    └───────────┬───────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  ADK Negotiation Agent  │
                    │  (Battle Master)        │
                    │                         │
                    │  Tools:                 │
                    │  • configure_negotiation│
                    │  • start_negotiation    │
                    │  • buyer_make_offer     │
                    │  • seller_respond       │
                    └─────────────────────────┘
```

## 🚀 Quick Start
## 🚀 快速开始

### Prerequisites
### 前置条件

- Python 3.11+
- `Python 3.11+` 环境
- Node.js 18+
- `Node.js 18+` 环境
- Google AI API Key ([Get one here](https://aistudio.google.com/))
- `Google AI API Key` 密钥（[在这里获取](https://aistudio.google.com/)）

### 1. Clone and Navigate
### 1. 克隆并进入目录

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/multi_agent_apps/ai_negotiation_battle_simulator
```

### 2. Set Up Backend
### 2. 设置后端

```bash
cd backend
pip install -r requirements.txt

# Create .env file
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# Start the backend
python agent.py
```

The backend will start on `http://localhost:8000`
后端将在 `http://localhost:8000` 启动。

### 3. Set Up Frontend
### 3. 设置前端

```bash
cd frontend
npm install

# Start the frontend
npm run dev
```

The frontend will start on `http://localhost:3000`
前端将在 `http://localhost:3000` 启动。

### 4. Start Negotiating! 🎮
### 4. 开始谈判！🎮

Open `http://localhost:3000` and tell the Battle Master:
打开 `http://localhost:3000` 并告诉 `Battle Master`：
- "Start a negotiation for a used car"
- “为二手车开始一场谈判”
- "Show me available scenarios"
- “显示可用场景”
- "Use Desperate Dan as buyer and Shark Steve as seller"
- “使用 `Desperate Dan` 作为买家，使用 `Shark Steve` 作为卖家”

## 🎭 Personalities
## 🎭 个性

### Buyers
### 买家
| Personality<br>个性 | Emoji<br>表情 | Style<br>风格 |
|-------------|-------|-------|
| Desperate Dan<br>`Desperate Dan` | 😰 | Needs car TODAY, weak poker face<br>今天就需要车，不擅长掩饰情绪 |
| Analytical Alex<br>`Analytical Alex` | 🧮 | Cites every data point, very logical<br>引用每个数据点，非常理性 |
| Cool-Hand Casey<br>`Cool-Hand Casey` | 😎 | Master of the walkaway bluff<br>擅长假装随时离场的高手 |
| Fair-Deal Fran<br>`Fair-Deal Fran` | 🤝 | Just wants a win-win<br>只想达成双赢 |

### Sellers
### 卖家
| Personality<br>个性 | Emoji<br>表情 | Style<br>风格 |
|-------------|-------|-------|
| Shark Steve<br>`Shark Steve` | 🦈 | Never drops more than 5%<br>降价从不超过 `5%` |
| By-The-Book Beth<br>`By-The-Book Beth` | 📊 | Goes strictly by KBB<br>严格按 `KBB` 办事 |
| Motivated Mike<br>`Motivated Mike` | 😅 | Really needs to sell<br>真的急需卖出 |
| Drama Queen Diana<br>`Drama Queen Diana` | 🎭 | Everything is "final offer"<br>每句话都像是“最终报价” |

## 📁 Project Structure
## 📁 项目结构

```
ai_negotiation_battle_simulator/
├── README.md
├── .env.example
│
├── backend/                    # Python ADK + AG-UI
│   ├── agent.py               # Main agent with tools
│   ├── requirements.txt
│   ├── config/
│   │   ├── personalities.py   # 8 unique personalities
│   │   └── scenarios.py       # 3 negotiation scenarios
│   └── agents/
│       ├── buyer_agent.py
│       ├── seller_agent.py
│       └── orchestrator.py
│
└── frontend/                   # Next.js + CopilotKit
    ├── package.json
    ├── src/
    │   └── app/
    │       ├── layout.tsx     # CopilotKit provider
    │       ├── page.tsx       # Battle Arena UI
    │       ├── globals.css    # Battle animations
    │       └── api/
    │           └── copilotkit/
    │               └── route.ts  # CopilotKit runtime
    └── tailwind.config.js
```

## 🎬 Sample Battle
## 🎬 示例对战

```
🔔 NEGOTIATION BEGINS: 2019 Honda Civic EX

📋 ASKING PRICE: $15,500

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

😎 COOL-HAND CASEY (Round 1):
"I've seen similar Civics go for less. $11,500 seems fair 
given the market. Cash in hand today."

🦈 SHARK STEVE (Round 1):
"$15,000. This car is pristine. I've got two other 
interested buyers coming this weekend."

😎 COOL-HAND CASEY (Round 2):
"$12,500 is my limit. Take it or I walk."

🦈 SHARK STEVE (Round 2):
*considers* "$14,000. Final offer."

😎 COOL-HAND CASEY (Round 3):
"$13,000. Meet me in the middle."

🦈 SHARK STEVE (Round 3):
"...$13,500 and you've got a deal."

😎 COOL-HAND CASEY (Round 4):
"$13,250. Final answer."

🦈 SHARK STEVE (Round 4):
"Deal. 🤝"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ DEAL CLOSED AT $13,250 🎉
   Buyer saved: $2,250 (14.5% off asking)
```

## 🧠 How It Works
## 🧠 工作原理

1. **User Request**: You tell the Battle Master what kind of negotiation to run
1. **用户请求**：你告诉 `Battle Master` 要运行哪种谈判
2. **Configuration**: The agent sets up the scenario and personalities
2. **配置**：智能体设置场景和个性
3. **Tool Calls**: The agent alternates between `buyer_make_offer` and `seller_respond` tools
3. **工具调用**：智能体在 `buyer_make_offer` 和 `seller_respond` 工具之间交替调用
4. **AG-UI Streaming**: Each tool call streams to the frontend via AG-UI protocol
4. **`AG-UI` 流式传输**：每个工具调用都会通过 `AG-UI protocol` 流式传输到前端
5. **Generative UI**: Custom React components render each offer/response beautifully
5. **生成式 `UI`**：自定义 `React` 组件会美观地渲染每个报价/回应
6. **Shared State**: The negotiation timeline updates in real-time
6. **共享状态**：谈判时间线会实时更新
7. **Outcome**: Deal or no-deal is celebrated with animations!
7. **结果**：成交或未成交都会通过动画呈现！

## 📚 Learn More
## 📚 了解更多

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK 文档](https://google.github.io/adk-docs/)
- [AG-UI Protocol Docs](https://docs.ag-ui.com/)
- [AG-UI Protocol 文档](https://docs.ag-ui.com/)
- [CopilotKit Documentation](https://docs.copilotkit.ai/)
- [CopilotKit 文档](https://docs.copilotkit.ai/)

## 🤝 Contributing
## 🤝 贡献

Feel free to add:
欢迎添加：
- New negotiation scenarios (salary, apartment, contracts)
- 新谈判场景（薪资、公寓、合同）
- Additional personality types
- 更多个性类型
- More dramatic UI effects
- 更具戏剧性的 `UI` 效果
- Cross-framework agents (LangChain, CrewAI via A2A)
- 跨框架智能体（通过 `A2A` 使用 `LangChain`、`CrewAI`）

---

*May the best negotiator win!* 🏆
*愿最优秀的谈判者获胜！* 🏆
