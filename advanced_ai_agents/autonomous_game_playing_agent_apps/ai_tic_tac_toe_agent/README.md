# 🎮 Agent X vs Agent O: Tic-Tac-Toe Game
# 🎮 `Agent X` 对战 `Agent O`：井字棋游戏

An interactive Tic-Tac-Toe game where two AI agents powered by different language models compete against each other built on Agno Agent Framework and Streamlit as UI.
这是一个交互式井字棋游戏，两个由不同语言模型驱动的 `AI` 智能体相互竞争，基于 `Agno Agent Framework` 构建，并使用 `Streamlit` 作为界面。

This example shows how to build an interactive Tic Tac Toe game where AI agents compete against each other. The application showcases how to:
该示例展示如何构建一个由 `AI` 智能体相互竞争的交互式井字棋游戏。该应用展示了如何：

- Coordinate multiple AI agents in a turn-based game
- 在回合制游戏中协调多个 `AI` 智能体
- Use different language models for different players
- 为不同玩家使用不同语言模型
- Create an interactive web interface with Streamlit
- 使用 `Streamlit` 创建交互式网页界面
- Handle game state and move validation
- 处理游戏状态和走法验证
- Display real-time game progress and move history
- 显示实时游戏进度和走法历史

## Features
## 功能

- Multiple AI models support (GPT-4, Claude, Gemini, etc.)
- 支持多个 `AI` 模型（`GPT-4`、`Claude`、`Gemini` 等）
- Real-time game visualization
- 实时游戏可视化
- Move history tracking with board states
- 跟踪包含棋盘状态的走法历史
- Interactive player selection
- 交互式玩家选择
- Game state management
- 游戏状态管理
- Move validation and coordination
- 走法验证与协调

## How to Run?
## 如何运行？

1. **Setup Environment**
1. **设置环境**

   ```bash
   # Clone the repository
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/autonomous_game_playing_agent_apps/ai_tic_tac_toe_agent

   # Install dependencies
   pip install -r requirements.txt
   ```

### 2. Install dependencies
### 2. 安装依赖

```shell
pip install -r requirements.txt
```

### 3. Setup API Keys
### 3. 设置 `API Keys`

The game supports multiple AI models. Create a `.env` file in this directory and add your API keys:
该游戏支持多个 `AI` 模型。在此目录中创建 `.env` 文件，并添加你的 `API keys`：

1. **Create a `.env` file:**
1. **创建 `.env` 文件：**

   ```bash
   # In the ai_tic_tac_toe_agent directory
   touch .env
   ```

2. **Add your API keys to the `.env` file:**
2. **将你的 `API keys` 添加到 `.env` 文件：**

   ```env
   # Required for OpenAI models (gpt-4o, o3-mini)
   OPENAI_API_KEY=your_actual_openai_api_key_here

   # Optional - for additional models
   ANTHROPIC_API_KEY=your_actual_anthropic_api_key_here  # For Claude models
   GOOGLE_API_KEY=your_actual_google_api_key_here        # For Gemini models
   GROQ_API_KEY=your_actual_groq_api_key_here           # For Groq models
   ```

   > **Note:** Replace the placeholder values with your actual API keys. The app will show helpful error messages if required keys are missing.
   > **说明：** 请将占位值替换为你实际的 `API keys`。如果缺少必需的密钥，应用会显示有用的错误信息。

### 4. Run the Game
### 4. 运行游戏

```shell
streamlit run app.py
```

- Open [localhost:8501](http://localhost:8501) to view the game interface
- 打开 [localhost:8501](http://localhost:8501) 查看游戏界面

## How It Works
## 工作原理

The game consists of three agents:
该游戏由三个智能体组成：

1. **Master Agent (Referee)**
1. **主控智能体（裁判）**
   - Coordinates the game
   - 协调游戏
   - Validates moves
   - 验证走法
   - Maintains game state
   - 维护游戏状态
   - Determines game outcome
   - 判断游戏结果

2. **Two Player Agents**
2. **两个玩家智能体**
   - Make strategic moves
   - 做出策略性走法
   - Analyze board state
   - 分析棋盘状态
   - Follow game rules
   - 遵循游戏规则
   - Respond to opponent moves
   - 响应对手走法

## Available Models
## 可用模型

The game supports various AI models:
该游戏支持多种 `AI` 模型：

- GPT-4o (OpenAI)
- `GPT-4o`（`OpenAI`）模型
- GPT-o3-mini (OpenAI)
- `GPT-o3-mini`（`OpenAI`）模型
- Gemini (Google)
- `Gemini`（`Google`）模型
- Llama 3 (Groq)
- `Llama 3`（`Groq`）模型
- Claude (Anthropic)
- `Claude`（`Anthropic`）模型

## Game Features
## 游戏功能

1. **Interactive Board**
1. **交互式棋盘**
   - Real-time updates
   - 实时更新
   - Visual move tracking
   - 可视化走法跟踪
   - Clear game status display
   - 清晰的游戏状态显示

2. **Move History**
2. **走法历史**
   - Detailed move tracking
   - 详细走法跟踪
   - Board state visualization
   - 棋盘状态可视化
   - Player action timeline
   - 玩家操作时间线

3. **Game Controls**
3. **游戏控制**
   - Start/Pause game
   - 开始/暂停游戏
   - Reset board
   - 重置棋盘
   - Select AI models
   - 选择 `AI` 模型
   - View game history
   - 查看游戏历史

4. **Performance Analysis**
4. **性能分析**
   - Move timing
   - 走法耗时
   - Strategy tracking
   - 策略跟踪
   - Game statistics
   - 游戏统计
