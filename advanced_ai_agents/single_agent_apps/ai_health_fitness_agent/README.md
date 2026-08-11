# AI Health & Fitness Planner Agent 🏋️‍♂️
# `AI` 健康与健身规划智能体 🏋️‍♂️

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-a-personal-health-and-fitness-ai-agent-using-google-gemini) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整的分步教程](https://www.theunwindai.com/p/build-a-personal-health-and-fitness-ai-agent-using-google-gemini)，学习如何从零开始构建此项目，包括详细的代码讲解、说明和最佳实践。**

The **AI Health & Fitness Planner** is a personalized health and fitness Agent powered by Agno AI Agent framework. This app generates tailored dietary and fitness plans based on user inputs such as age, weight, height, activity level, dietary preferences, and fitness goals.
**`AI Health & Fitness Planner`** 是一个由 `Agno AI Agent` 框架提供支持的个性化健康与健身智能体。该应用会根据用户输入的年龄、体重、身高、活动水平、饮食偏好和健身目标，生成定制化饮食与健身计划。

## Features
## 功能

- **Health Agent and Fitness Agent**
  **`Health Agent` 和 `Fitness Agent`**
    - The app has two phidata agents that are specialists in giving Diet advice and Fitness/workout advice respectively.
      该应用包含两个 `phidata` 智能体，分别专注于提供饮食建议和健身/训练建议。

- **Personalized Dietary Plans**:
  **个性化饮食计划**：
  - Generates detailed meal plans (breakfast, lunch, dinner, and snacks).
    生成详细的餐食计划（早餐、午餐、晚餐和加餐）。
  - Includes important considerations like hydration, electrolytes, and fiber intake.
    包含补水、电解质和纤维摄入等重要注意事项。
  - Supports various dietary preferences like Keto, Vegetarian, Low Carb, etc.
    支持多种饮食偏好，例如 `Keto`、`Vegetarian`、`Low Carb` 等。

- **Personalized Fitness Plans**:
  **个性化健身计划**：
  - Provides customized exercise routines based on fitness goals.
    根据健身目标提供定制化训练安排。
  - Covers warm-ups, main workouts, and cool-downs.
    涵盖热身、主体训练和放松整理。
  - Includes actionable fitness tips and progress tracking advice.
    包含可执行的健身建议和进度跟踪建议。

- **Interactive Q&A**: Allows users to ask follow-up questions about their plans.
  **交互式问答**：允许用户围绕自己的计划提出后续问题。


## Requirements
## 要求

The application requires the following Python libraries:
该应用需要以下 `Python` 库：

- `agno`
- `agno` 库
- `google-generativeai`
- `google-generativeai` 库
- `streamlit`
- `streamlit` 库

Ensure these dependencies are installed via the `requirements.txt` file according to their mentioned versions
请确保通过 `requirements.txt` 文件按指定版本安装这些依赖。

## How to Run
## 如何运行

Follow the steps below to set up and run the application:
按照以下步骤设置并运行该应用：
Before anything else, Please get a free Gemini API Key provided by Google AI here: https://aistudio.google.com/apikey
在进行其他操作之前，请先在这里获取由 `Google AI` 提供的免费 `Gemini API Key`：https://aistudio.google.com/apikey

1. **Clone the Repository**:
   **克隆仓库**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/single_agent_apps/ai_health_fitness_agent
   ```

2. **Install the dependencies**
   **安装依赖**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the Streamlit app**
   **运行 `Streamlit` 应用**
    ```bash
    streamlit run health_agent.py
    ```
