# 🏠 AI Real Estate Agent Team
# 🏠 AI 房地产智能体团队

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-real-estate-agent-team) and learn how to build this AI SEO Audit Team from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-real-estate-agent-team)，通过详细代码讲解、说明和最佳实践，学习如何从零构建这个 `AI SEO Audit Team`。**

The **AI Real Estate Agent Team** is a sophisticated property search and analysis platform powered by specialized AI agents with Firecrawl's extract endpoint.
**`AI Real Estate Agent Team`** 是一个复杂的房产搜索与分析平台，由专业化 `AI Agent` 和 `Firecrawl` 的 `extract endpoint` 提供支持。

This application provides comprehensive real estate insights, market analysis, and property recommendations using advanced web scraping and AI-powered search capabilities.
该应用使用高级网页抓取和 `AI` 驱动的搜索能力，提供全面的房地产洞察、市场分析和房产推荐。

## Features
## 功能

- **Multi-Agent Analysis System**
- **多智能体分析系统**
    - **Property Search Agent**: Finds properties using direct Firecrawl integration
    - **房产搜索智能体**：通过直接集成 `Firecrawl` 查找房产
    - **Market Analysis Agent**: Provides concise market trends and neighborhood insights
    - **市场分析智能体**：提供简洁的市场趋势和社区洞察
    - **Property Valuation Agent**: Gives brief property valuations and investment analysis
    - **房产估值智能体**：提供简要房产估值和投资分析

- **Multi-Platform Property Search**:
- **多平台房产搜索**：
  - **Zillow**: Largest real estate marketplace with comprehensive listings
  - **Zillow**：拥有全面房源信息的最大房地产市场
  - **Realtor.com**: Official site of the National Association of Realtors
  - **Realtor.com**：`National Association of Realtors` 的官方网站
  - **Trulia**: Neighborhood-focused real estate search
  - **Trulia**：聚焦社区的房地产搜索平台
  - **Homes.com**: Comprehensive property search platform
  - **Homes.com**：综合房产搜索平台

- **Advanced Property Analysis**:
- **高级房产分析**：
  - Detailed property information extraction (address, price, bedrooms, bathrooms, sqft)
  - 详细提取房产信息（地址、价格、卧室数、浴室数、平方英尺）
  - Property features and amenities analysis
  - 房产特点和配套设施分析
  - Listing URLs and agent contact information
  - 房源 `URL` 和经纪人联系信息
  - Clickable property links for easy navigation
  - 可点击的房产链接，便于导航

- **Comprehensive Market Insights**:
- **全面市场洞察**：
  - Current market conditions (buyer's/seller's market)
  - 当前市场状况（买方市场/卖方市场）
  - Price trends and market direction
  - 价格趋势和市场方向
  - Neighborhood analysis with key insights
  - 包含关键洞察的社区分析
  - Investment potential assessment
  - 投资潜力评估
  - Strategic recommendations
  - 战略建议

- **Sequential Manual Execution**:
- **顺序手动执行**：
  - Optimized for speed and reliability
  - 针对速度和可靠性优化
  - Direct data flow between agents
  - 智能体之间直接传递数据
  - Manual coordination for better control
  - 通过手动协调获得更好的控制
  - Reduced overhead and improved performance
  - 降低开销并提升性能

- **Interactive UI Features**:
- **交互式 UI 功能**：
  - Real-time agent progression tracking
  - 实时跟踪智能体进度
  - Progress indicators for each search phase
  - 每个搜索阶段都有进度指示器
  - Downloadable analysis reports
  - 可下载的分析报告
  - Timing information for performance monitoring
  - 用于性能监控的耗时信息

## Requirements
## 要求

The application requires the following Python libraries:
该应用需要以下 `Python` 库：

- `agno`
- `agno` 库
- `streamlit`
- `streamlit` 库
- `firecrawl-py`
- `firecrawl-py` 库
- `python-dotenv`
- `python-dotenv` 库
- `pydantic`
- `pydantic` 库

You'll also need API keys for:
你还需要以下 `API` 密钥：

- **Cloud Version**: Google AI (Gemini) + Firecrawl
- **云端版本**：`Google AI`（`Gemini`）+ `Firecrawl`
- **Local Version**: Firecrawl only (uses Ollama locally)
- **本地版本**：仅需 `Firecrawl`（本地使用 `Ollama`）

## How to Run
## 如何运行

Follow these steps to set up and run the application:
按照以下步骤设置并运行应用：

### **API Version (Gemini 2.5 Flash)**
### **API 版本（Gemini 2.5 Flash）**

1. **Clone the Repository**:
1. **克隆仓库**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_real_estate_agent_team
   ```

2. **Install the dependencies**:
2. **安装依赖**：
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API keys**:
3. **设置你的 API 密钥**：
    - Get a Google AI API key from: https://aistudio.google.com/app/apikey
    - 从这里获取 `Google AI API` 密钥：https://aistudio.google.com/app/apikey
    - Get a Firecrawl API key from: [Firecrawl website](https://firecrawl.dev)
    - 从 [Firecrawl website](https://firecrawl.dev) 获取 `Firecrawl API` 密钥

4. **Run the Streamlit app**:
4. **运行 Streamlit 应用**：
    ```bash
    streamlit run real_estate_agent_team.py
    ```

### **Local Version (Ollama)**
### **本地版本（Ollama）**

1. **Install Ollama**:
1. **安装 Ollama**：
   ```bash
   #Pull the model: make sure to have a device that has more than 16GB RAM to run this model locally!
   ollama pull gpt-oss:20b  
   ```

2. **Install the dependencies**:
2. **安装依赖**：
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API key**:
3. **设置你的 API 密钥**：
    - Get a Firecrawl API key from: [Firecrawl website](https://firecrawl.dev)
    - 从 [Firecrawl website](https://firecrawl.dev) 获取 `Firecrawl API` 密钥

4. **Run the local Streamlit app**:
4. **运行本地 Streamlit 应用**：
    ```bash
    streamlit run local_ai_real_estate_agent_team.py
    ```

## Usage
## 使用方法

### **Cloud Version**
### **云端版本**

1. Enter your API keys in the sidebar:
1. 在侧边栏输入你的 `API` 密钥：
   - Google AI API Key
   - `Google AI API Key` 密钥
   - Firecrawl API Key
   - `Firecrawl API Key` 密钥

2. Select real estate websites to search from:
2. 选择要搜索的房地产网站：
   - Zillow
   - `Zillow` 网站
   - Realtor.com
   - `Realtor.com` 网站
   - Trulia
   - `Trulia` 网站
   - Homes.com
   - `Homes.com` 网站

3. Configure your property requirements:
3. 配置你的房产需求：
   - Location (city, state)
   - 位置（城市、州）
   - Budget range
   - 预算范围
   - Property details (type, bedrooms, bathrooms, sqft)
   - 房产详情（类型、卧室数、浴室数、平方英尺）
   - Special features and timeline
   - 特殊功能和时间线

4. Click "Start Property Analysis" to generate:
4. 点击“Start Property Analysis”生成：
   - Property listings with details
   - 带详情的房源列表
   - Market analysis and trends
   - 市场分析和趋势
   - Property valuations and recommendations
   - 房产估值和建议

### **Local Version**
### **本地版本**

1. Enter your Firecrawl API key in the sidebar
1. 在侧边栏输入你的 `Firecrawl API` 密钥
2. Ensure Ollama is running with `gpt-oss:20b` model
2. 确保 `Ollama` 正在运行 `gpt-oss:20b` 模型
3. Follow the same property configuration steps as cloud version
3. 按照与云端版本相同的房产配置步骤操作
4. Get the same comprehensive analysis with local AI processing
4. 通过本地 `AI` 处理获得同样全面的分析

## Agent Workflow
## 智能体工作流

### **Property Search Agent**
### **房产搜索智能体**

- Uses direct Firecrawl integration to search real estate websites
- 使用直接的 `Firecrawl` 集成搜索房地产网站
- Focuses on properties matching user criteria
- 聚焦符合用户条件的房产
- Extracts structured property data with all details
- 提取包含全部细节的结构化房产数据
- Organizes results with clickable listing URLs
- 使用可点击的房源 `URL` 组织结果

### **Market Analysis Agent**
### **市场分析智能体**

- **Market Condition**: Buyer's/seller's market, price trends
- **市场状况**：买方市场/卖方市场、价格趋势
- **Key Neighborhoods**: Brief overview of areas where properties are located
- **关键社区**：房产所在区域的简要概览
- **Investment Outlook**: 2-3 key points about investment potential
- **投资前景**：关于投资潜力的 `2-3` 个关键点
- **Format**: Concise bullet points under 100 words per section
- **格式**：每节使用不超过 `100` 个英文单词的简洁要点

### **Property Valuation Agent**
### **房产估值智能体**

- **Value Assessment**: Fair price, over/under priced analysis
- **价值评估**：公平价格、偏高/偏低定价分析
- **Investment Potential**: High/Medium/Low with brief reasoning
- **投资潜力**：高/中/低，并附简要理由
- **Key Recommendation**: One actionable insight per property
- **关键建议**：每套房产提供一条可执行洞察
- **Format**: Brief assessments under 50 words per property
- **格式**：每套房产的简要评估不超过 `50` 个英文单词

## Technical Architecture
## 技术架构

### **Data Sources**:
### **数据源**：

- **Firecrawl Extract API**: Structured property data extraction
- **Firecrawl Extract API**：结构化房产数据提取
- **Pydantic Schemas**: Structured data validation and formatting
- **Pydantic Schemas**：结构化数据校验和格式化

### **AI Framework**:
### **AI 框架**：

- **Cloud Version**: Agno Framework with Google Gemini 2.5 Flash
- **云端版本**：使用 `Google Gemini 2.5 Flash` 的 `Agno Framework`
- **Local Version**: Agno Framework with Ollama gpt-oss:20b
- **本地版本**：使用 `Ollama gpt-oss:20b` 的 `Agno Framework`
- **Streamlit**: Interactive web application interface
- **Streamlit**：交互式 Web 应用界面

### **Performance Features**:
### **性能特性**：

- **Sequential Execution**: Manual coordination for optimal performance
- **顺序执行**：通过手动协调获得最佳性能
- **Progress Tracking**: Real-time updates on analysis progress
- **进度跟踪**：实时更新分析进度
- **Error Recovery**: Graceful handling of extraction failures
- **错误恢复**：优雅处理提取失败
- **Direct Integration**: Bypasses tool wrappers for faster execution
- **直接集成**：绕过工具封装以加快执行

## File Structure
## 文件结构

```
ai_real_estate_agent_team/
├── real_estate_agent_team.py           # API version (Google Gemini)
├── local_ai_real_estate_agent_team.py  # Local version (Ollama)
├── requirements.txt                    # Python dependencies
├── README.md                          # This documentation
└── .env                               # Environment variables (create this)
```

## API Requirements
## API 要求

### **Cloud Version**
### **云端版本**

#### **`Google AI API`**
#### **`Google AI API` 服务**

- **Model**: Gemini 2.5 Flash
- **模型**：`Gemini 2.5 Flash`
- **Usage**: Multi-agent analysis and property insights
- **用途**：多智能体分析和房产洞察
- **Rate Limits**: Standard Google AI rate limits apply
- **速率限制**：适用标准 `Google AI` 速率限制

#### **`Firecrawl API`**
#### **`Firecrawl API` 服务**

- **Endpoint**: Extract API for structured data
- **端点**：用于结构化数据的 `Extract API`
- **Usage**: Property listing extraction from real estate websites
- **用途**：从房地产网站提取房源信息
- **Rate Limits**: Firecrawl standard rate limits
- **速率限制**：`Firecrawl` 标准速率限制

### **Local Version**
### **本地版本**

#### **Firecrawl API**
#### **`Firecrawl API` 服务**

- **Endpoint**: Extract API for structured data
- **端点**：用于结构化数据的 `Extract API`
- **Usage**: Property listing extraction from real estate websites
- **用途**：从房地产网站提取房源信息
- **Rate Limits**: Firecrawl standard rate limits
- **速率限制**：`Firecrawl` 标准速率限制

#### **Ollama (Local)**
#### **Ollama（本地）**

- **Model**: gpt-oss:20b
- **模型**：`gpt-oss:20b`
- **Usage**: All AI processing locally
- **用途**：所有 `AI` 处理均在本地完成
- **Requirements**: ~16GB RAM recommended
- **要求**：建议约 `16GB RAM`
- **No API costs**: Completely local processing
- **无 API 成本**：完全本地处理
