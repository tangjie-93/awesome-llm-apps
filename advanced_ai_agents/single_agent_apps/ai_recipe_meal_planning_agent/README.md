# 🍽️ AI Recipe & Meal Planning Agent
# 🍽️ `AI` 食谱与膳食规划智能体

An intelligent meal planning agent built with Agno that helps you discover recipes, analyze nutrition, estimate costs, and create weekly meal plans based on your ingredients and dietary preferences.
一个使用 `Agno` 构建的智能膳食规划智能体，可根据你的食材和饮食偏好帮助你发现食谱、分析营养、估算成本并创建每周膳食计划。

## Features
## 功能

🔍 **Recipe Discovery**
🔍 **食谱发现**
- Find recipes based on available ingredients
- 根据可用食材查找食谱
- Support for dietary restrictions (vegetarian, vegan, keto, paleo, etc.)
- 支持饮食限制（素食、纯素、`keto`、`paleo` 等）
- Ingredient substitution suggestions
- 提供食材替代建议
- Detailed cooking instructions and timing
- 提供详细烹饪说明和时间安排

📊 **Nutrition Analysis**
📊 **营养分析**
- Comprehensive nutritional breakdown per serving
- 按每份提供全面营养拆解
- User-friendly health assessments
- 提供易懂的健康评估
- Calorie, protein, carb, and fat tracking
- 跟踪热量、蛋白质、碳水和脂肪
- Sodium and fiber content analysis
- 分析钠和纤维含量

💰 **Cost Estimation**
💰 **成本估算**
- Grocery cost estimation for ingredients
- 估算食材的杂货采购成本
- Budget-friendly meal suggestions
- 提供预算友好的餐食建议
- Cost per serving calculations
- 计算每份成本

📅 **Weekly Meal Planning**
📅 **每周膳食规划**
- Balanced meal plans for any household size
- 为任意家庭规模生成均衡膳食计划
- Dietary preference accommodation
- 适配饮食偏好
- Shopping list optimization
- 优化购物清单
- Budget-conscious planning
- 面向预算进行规划

🧠 **Session-Based Conversations**
🧠 **基于会话的对话**
- Remembers context during your current browser session
- 在当前浏览器会话中记住上下文
- Preferences are not persisted after restart (no long-term storage)
- 重启后不会持久化偏好（无长期存储）

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
   克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/single_agent_apps/ai_recipe_meal_planning_agent
```

2. Install the required dependencies:
   安装所需依赖：

```bash
pip install -r requirements.txt
```

3. Get your OpenAI API Key
   获取你的 `OpenAI API Key`

- Sign up for an [OpenAI account](https://platform.openai.com/) and obtain your API key.
- 注册一个 [OpenAI account](https://platform.openai.com/)，并获取你的 `API key`。

4. Get your Spoonacular API Key
   获取你的 `Spoonacular API Key`

- Sign up for a [Spoonacular account](https://spoonacular.com/food-api) and obtain your API key (free tier ~50 requests/day).
- 注册一个 [Spoonacular account](https://spoonacular.com/food-api)，并获取你的 `API key`（免费层约 `50` 次请求/天）。

5. Create a `.env` file in this folder
   在此文件夹中创建 `.env` 文件

```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional but recommended for full recipe & nutrition functionality
SPOONACULAR_API_KEY=your_spoonacular_api_key_here
```

6. Run the Streamlit App
   运行 `Streamlit App`

```bash
streamlit run ai_recipe_meal_planning_agent.py
```

7. Open your browser at `http://localhost:8501`
   在浏览器中打开 `http://localhost:8501`

## Example Interactions
## 示例交互

**Recipe Discovery:**
**食谱发现：**
- "I have chicken, broccoli, and rice. What can I make?"
- “我有鸡肉、西兰花和米饭。我能做什么？”
- "Find me vegan recipes using lentils"
- “帮我查找使用扁豆的纯素食谱”
- "Show me quick 30-minute dinner ideas"
- “给我展示 `30` 分钟快手晚餐创意”

**Nutrition Analysis:**
**营养分析：**
- "What's the nutritional content of this recipe?"
- “这个食谱的营养成分是什么？”
- "Is this meal high in protein?"
- “这顿餐食蛋白质含量高吗？”
- "How many calories per serving?"
- “每份有多少卡路里？”

**Meal Planning:**
**膳食规划：**
- "Create a week's worth of vegetarian meals for 2 people"
- “为 `2` 个人创建一周的素食餐食”
- "I need a low-sodium meal plan"
- “我需要一个低钠膳食计划”
- "Plan budget-friendly meals for a family of 4"
- “为 `4` 口之家规划预算友好的餐食”

**Cost Estimation:**
**成本估算：**
- "How much will these ingredients cost?"
- “这些食材要花多少钱？”
- "What's the most budget-friendly option?"
- “最预算友好的选项是什么？”
- "Estimate weekly grocery costs for this meal plan"
- “估算这个膳食计划的每周杂货采购成本”

## Application Architecture
## 应用架构

### Built with Agno Framework
### 使用 `Agno Framework` 构建
- **Agent**: OpenAI GPT-5 mini powered meal planning agent
- **Agent**：由 `OpenAI GPT-5 mini` 驱动的膳食规划智能体
- **Memory**: Conversation memory for personalized recommendations
- **Memory**：用于个性化推荐的对话记忆
- **Tools**: Custom tools for recipe search and analysis + DuckDuckGo web search
- **Tools**：用于食谱搜索和分析的自定义工具 + `DuckDuckGo` 网页搜索
- **Interface**: Streamlit web application
- **Interface**：`Streamlit` 网页应用

### Custom Tools
### 自定义工具
1. `search_recipes(ingredients, diet_type=None)` - Recipe discovery via Spoonacular API with detailed instructions
   `search_recipes(ingredients, diet_type=None)` - 通过 `Spoonacular API` 发现食谱并提供详细说明
2. `analyze_nutrition(recipe_name)` - Detailed nutritional analysis via Spoonacular
   `analyze_nutrition(recipe_name)` - 通过 `Spoonacular` 进行详细营养分析
3. `estimate_costs(ingredients, servings=4)` - Budget planning and cost estimation
   `estimate_costs(ingredients, servings=4)` - 预算规划和成本估算
4. `create_meal_plan(dietary_preference="balanced", people=2, days=7, budget="moderate")` - Comprehensive weekly meal planning with shopping list
   `create_meal_plan(dietary_preference="balanced", people=2, days=7, budget="moderate")` - 包含购物清单的综合每周膳食规划
5. `DuckDuckGoTools` - Web search for additional context
   `DuckDuckGoTools` - 用于补充上下文的网页搜索

### Key Technologies
### 关键技术
- **Agno**: AI agent framework
- **Agno**：`AI Agent` 框架
- **Streamlit**: Web interface and user interaction
- **Streamlit**：网页界面和用户交互
- **Spoonacular API**: Recipe and nutrition data
- **Spoonacular API**：食谱和营养数据
- **OpenAI GPT-5 mini**: Natural language understanding and generation
- **OpenAI GPT-5 mini**：自然语言理解和生成

## Customization
## 自定义

### Adding New Dietary Preferences
### 添加新的饮食偏好
Modify the `search_recipes` tool to include additional diet types supported by Spoonacular API.
修改 `search_recipes` 工具，以包含 `Spoonacular API` 支持的其他饮食类型。

### Extending Cost Database
### 扩展成本数据库
Update the `ingredient_costs` dictionary in `estimate_grocery_costs()` with local pricing.
使用本地价格更新 `estimate_grocery_costs()` 中的 `ingredient_costs` 字典。

### Custom Meal Categories
### 自定义餐食类别
Edit the `meal_categories` in `create_weekly_meal_plan()` to match your preferences.
编辑 `create_weekly_meal_plan()` 中的 `meal_categories` 以匹配你的偏好。

## Troubleshooting
## 故障排查

**API Key Issues:**
**`API Key` 问题：**
- Ensure your `.env` file is in the correct directory
- 确保你的 `.env` 文件位于正确目录
- Verify API keys are valid and have sufficient credits
- 验证 `API key` 有效且额度充足
- Check API key format (no extra spaces or quotes)
- 检查 `API key` 格式（不要有多余空格或引号）
 - Note: Without `SPOONACULAR_API_KEY`, recipe search and nutrition tools will return an error; other features will still load.
 - 注意：如果没有 `SPOONACULAR_API_KEY`，食谱搜索和营养工具会返回错误；其他功能仍会加载。

**Recipe Search Not Working:**
**食谱搜索无法工作：**
- Verify Spoonacular API key is set correctly
- 验证 `Spoonacular API key` 是否设置正确
- Check your API usage limits (150 requests/day for free tier)
- 检查你的 `API` 使用限制（免费层为 `150` 次请求/天）
- Try simpler ingredient searches
- 尝试更简单的食材搜索

**Memory Issues:**
**记忆问题：**
- The agent uses conversation memory to remember preferences
- 该智能体使用对话记忆来记住偏好
- Clear browser cache if experiencing persistent issues
- 如果持续遇到问题，请清除浏览器缓存
- Restart the application to reset conversation history
- 重启应用以重置对话历史

## Contributing
## 贡献

Feel free to contribute by:
欢迎通过以下方式贡献：
- Adding new recipe sources or APIs
- 添加新的食谱来源或 `API`
- Improving nutrition analysis algorithms
- 改进营养分析算法
- Enhancing cost estimation accuracy
- 提高成本估算准确性
- Adding new meal planning features
- 添加新的膳食规划功能

## License
## 许可证

This project is open source. Please check the main repository for license details.
本项目是开源项目。请查看主仓库了解许可证详情。

## Support
## 支持

For issues and questions:
如有问题和疑问：
- Check the troubleshooting section above
- 查看上方故障排查部分
- Review the Agno documentation
- 查看 `Agno` 文档
- Open an issue in the main repository
- 在主仓库中提交 `issue`
