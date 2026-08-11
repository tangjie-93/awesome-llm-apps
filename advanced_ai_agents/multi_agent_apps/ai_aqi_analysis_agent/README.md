# 🌍 AQI Analysis Agent
# 🌍 `AQI` 分析代理

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-aqi-analysis-agent) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-aqi-analysis-agent)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**


The AQI Analysis Agent is a powerful air quality monitoring and health recommendation tool powered by Firecrawl and Agno's AI Agent framework. This app helps users make informed decisions about outdoor activities by analyzing real-time air quality data and providing personalized health recommendations.
`AQI Analysis Agent` 是一个强大的空气质量监测和健康建议工具，由 `Firecrawl` 和 `Agno` 的 `AI Agent` 框架提供支持。该应用通过分析实时空气质量数据并提供个性化健康建议，帮助用户对户外活动做出明智决策。

## Features
## 功能

- **Multi-Agent System**
- **多代理系统**
    - **AQI Analyzer**: Fetches and processes real-time air quality data
    - **`AQI Analyzer`**：获取并处理实时空气质量数据
    - **Health Recommendation Agent**: Generates personalized health advice
    - **`Health Recommendation Agent`**：生成个性化健康建议

- **Air Quality Metrics**:
- **空气质量指标**：
  - Overall Air Quality Index (AQI)
  - 整体空气质量指数（`AQI`）
  - Particulate Matter (PM2.5 and PM10)
  - 颗粒物（`PM2.5` 和 `PM10`）
  - Carbon Monoxide (CO) levels
  - 一氧化碳（`CO`）水平
  - Temperature
  - 温度
  - Humidity
  - 湿度
  - Wind Speed
  - 风速

- **Comprehensive Analysis**:
- **综合分析**：
  - Real-time data visualization
  - 实时数据可视化
  - Health impact assessment
  - 健康影响评估
  - Activity safety recommendations
  - 活动安全建议
  - Best time suggestions for outdoor activities
  - 户外活动最佳时间建议
  - Weather condition correlations
  - 天气条件相关性

- **Interactive Features**:
- **交互功能**：
  - Location-based analysis
  - 基于位置的分析
  - Medical condition considerations
  - 医疗状况考量
  - Activity-specific recommendations
  - 针对具体活动的建议
  - Downloadable reports
  - 可下载报告
  - Example queries for quick testing
  - 用于快速测试的示例查询

## How to Run
## 运行方法

Follow these steps to set up and run the application:
按照以下步骤设置并运行应用：

1. **Clone the Repository**:
1. **克隆仓库**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/ai_aqi_analysis_agent
   ```

2. **Install the dependencies**:
2. **安装依赖**：
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API keys**:
3. **设置你的 `API keys`**：
    - Get an OpenAI API key from: https://platform.openai.com/api-keys
    - 从以下地址获取 `OpenAI API key`：https://platform.openai.com/api-keys
    - Get a Firecrawl API key from: [Firecrawl website](https://www.firecrawl.dev/app/api-keys)
    - 从 [Firecrawl website](https://www.firecrawl.dev/app/api-keys) 获取 `Firecrawl API key`

4. **Run the Gradio app**:
4. **运行 `Gradio` 应用**：
    ```bash
    python ai_aqi_analysis_agent.py
    ```

5. **Access the Web Interface**:
5. **访问 `Web` 界面**：
    - The terminal will display two URLs:
    - 终端会显示两个 `URL`：
      - Local URL: `http://127.0.0.1:7860` (for local access)
      - 本地 `URL`：`http://127.0.0.1:7860`（用于本地访问）
      - Public URL: `https://xxx-xxx-xxx.gradio.live` (for temporary public access)
      - 公共 `URL`：`https://xxx-xxx-xxx.gradio.live`（用于临时公共访问）
    - Click on either URL to open the web interface in your browser
    - 点击任一 `URL` 即可在浏览器中打开 `Web` 界面

## Usage
## 使用方法

1. Enter your API keys in the API Configuration section
1. 在 `API Configuration` 区域输入你的 `API keys`
2. Input location details:
2. 输入位置详情：
   - City name
   - 城市名称
   - State (optional for Union Territories/US cities)
   - 州或省（对联邦属地/美国城市可选）
   - Country
   - 国家
3. Provide personal information:
3. 提供个人信息：
   - Medical conditions (optional)
   - 医疗状况（可选）
   - Planned outdoor activity
   - 计划的户外活动
4. Click "Analyze & Get Recommendations" to receive:
4. 点击 "Analyze & Get Recommendations" 获取：
   - Current air quality data
   - 当前空气质量数据
   - Health impact analysis
   - 健康影响分析
   - Activity safety recommendations
   - 活动安全建议
5. Try the example queries for quick testing
5. 尝试示例查询进行快速测试

## Note
## 注意

The air quality data is fetched using Firecrawl's web scraping capabilities. Due to caching and rate limiting, the data might not always match real-time values on the website. For the most accurate real-time data, consider checking the source website directly.
空气质量数据通过 `Firecrawl` 的网页抓取能力获取。由于缓存和速率限制，数据可能并不总是与网站上的实时值一致。若需要最准确的实时数据，建议直接查看源网站。
