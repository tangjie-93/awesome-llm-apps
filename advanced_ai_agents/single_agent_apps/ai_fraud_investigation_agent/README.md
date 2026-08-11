## 🔍 AI Fraud Investigation Agent
## 🔍 `AI` 欺诈调查智能体

An AI-powered autonomous fraud investigation agent that cross-references childcare provider licensing records against physical building data to detect anomalies. The agent uses public data — Cook County property records, Illinois DCFS licensing, Google Maps, and the Secretary of State — to find facilities where the physical evidence doesn't match the paperwork.
一个由 `AI` 驱动的自主欺诈调查智能体，会将托育服务提供商许可记录与实体建筑数据交叉比对，以发现异常。该智能体使用公共数据，包括 `Cook County` 房产记录、`Illinois DCFS` 许可、`Google Maps` 和州务卿数据，来查找实体证据与文件记录不一致的设施。

### Features
### 功能

- Searches Illinois DCFS licensing database for providers by ZIP code
  按邮编搜索 `Illinois DCFS` 许可数据库中的服务提供商
- Cross-references licensed capacity against actual building square footage from Cook County GIS records
  将许可容量与 `Cook County GIS` 记录中的实际建筑面积进行交叉比对
- Applies IL building code math to calculate maximum legal childcare occupancy
  应用 `IL` 建筑规范计算最大合法托育容量
- Analyzes Google Street View imagery to verify a facility looks like a real childcare center
  分析 `Google Street View` 图像，验证设施外观看起来是否像真实托育中心
- Checks Google Places for business status, rating, and whether the address shows a different business entirely
  检查 `Google Places` 中的营业状态、评分，以及该地址是否显示为完全不同的商家
- Verifies business entity registration with the Illinois Secretary of State
  通过 `Illinois Secretary of State` 验证商业实体注册信息
- Discovers cross-provider patterns: shared owners, address clusters, entities with no public footprint
  发现跨服务提供商模式：共享所有者、地址聚集、没有公共足迹的实体
- Narrates its full investigation in real time — reasoning is visible as the agent works
  实时叙述完整调查过程，智能体工作时推理过程可见

### How to get Started?
### 如何开始？

1. Clone the GitHub repository
   克隆 `GitHub` 仓库

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/single_agent_apps/ai_fraud_investigation_agent
```

2. Install the required dependencies
   安装所需依赖

```bash
pip install -r requirements.txt
```

3. Get your OpenRouter API Key
   获取你的 `OpenRouter API Key`

- Sign up at [openrouter.ai](https://openrouter.ai) and create an API key
  在 [`openrouter.ai`](https://openrouter.ai) 注册并创建一个 `API key`
- The free tier is sufficient for demo investigations
  免费层级足以用于演示调查
- Default model: `anthropic/claude-sonnet-4.6`
  默认模型：`anthropic/claude-sonnet-4.6`

4. Get your Google Maps API Key *(optional — skips visual analysis if omitted)*
   获取你的 `Google Maps API Key`（可选；如果省略则跳过视觉分析）

- Create a project at [console.cloud.google.com](https://console.cloud.google.com)
  在 [`console.cloud.google.com`](https://console.cloud.google.com) 创建一个项目
- Enable: **Geocoding API**, **Places API**, **Street View Static API**
  启用：**`Geocoding API`**、**`Places API`**、**`Street View Static API`**
- Create an API key and restrict it to these three APIs
  创建一个 `API key`，并将其限制为仅可访问这三个 `API`

5. Run the Streamlit App
   运行 `Streamlit` 应用

```bash
streamlit run fraud_investigation_agent.py
```

### How it Works?
### 工作原理

The AI Fraud Investigation Agent uses 7 specialized tools, all powered by public data sources:
`AI Fraud Investigation Agent` 使用 `7` 个专用工具，全部由公共数据源提供支持：

- **Provider Search** — Queries the Illinois DCFS licensing portal for all active providers in a ZIP code, returning capacity, license type, and license status
  **`Provider Search`**：查询 `Illinois DCFS` 许可门户中某个邮编下的所有活跃服务提供商，并返回容量、许可类型和许可状态

- **Property Analysis** — Pulls building square footage, lot size, property class, and year built from the Cook County Assessor's open data (Socrata API, no auth required)
  **`Property Analysis`**：从 `Cook County Assessor` 开放数据中拉取建筑面积、地块大小、房产类别和建造年份（`Socrata API`，无需认证）

- **Capacity Calculation** — Applies Illinois DCFS Part 407 building code math: `(building_sqft × 0.65) ÷ 35 = max legal children`. A 900 sq ft building cannot legally serve 50 children — this is a mathematical impossibility, not an opinion
  **`Capacity Calculation`**：应用 `Illinois DCFS Part 407` 建筑规范计算公式：`(building_sqft × 0.65) ÷ 35 = max legal children`。一栋 `900 sq ft` 的建筑不可能合法服务 `50` 名儿童，这是数学上的不可能，而不是观点

- **Street View** — Captures four-directional Google Street View images to check whether the address looks like a real childcare facility or something else entirely
  **`Street View`**：捕获四个方向的 `Google Street View` 图像，检查该地址看起来像真实托育设施，还是完全不同的场所

- **Places Info** — Queries Google Places for the current business listed at the address, its operating status, rating, and recent reviews
  **`Places Info`**：查询 `Google Places` 中该地址当前列出的商家、营业状态、评分和近期评论

- **Business Registration** — Probes the Illinois Secretary of State to verify the provider is a registered legal entity
  **`Business Registration`**：查询 `Illinois Secretary of State`，验证服务提供商是否为已注册的法律实体

- **Geocoding** — Converts addresses to coordinates for spatial analysis
  **`Geocoding`**：将地址转换为坐标，用于空间分析

The agent investigates each provider in the ZIP code, narrating its reasoning as it works. When it notices something suspicious — a building too small for its license, a closed storefront claiming to run childcare, a name appearing across multiple providers — it follows that thread and explains why it matters.
该智能体会调查邮编内的每个服务提供商，并在工作时叙述其推理过程。当它发现可疑情况，例如建筑面积相对许可容量过小、声称经营托育的店面已经关闭、同一个名称出现在多个服务提供商中，它会继续追踪该线索并解释其重要性。

### What the Agent Can (and Cannot) Detect
### 智能体可以（和不能）检测什么

**Can detect:**
**可以检测：**
- Licensed capacity physically impossible for the building size
  建筑面积在物理上无法支撑的许可容量
- Addresses where Google shows a different business or a closed/vacant building
  `Google` 显示为其他商家或已关闭/空置建筑的地址
- Providers with no Google listing, no reviews, no business registration
  没有 `Google` 列表、没有评论、没有商业注册的服务提供商
- Shared owner names or agents appearing across multiple providers
  出现在多个服务提供商中的共享所有者姓名或代理人

**Cannot detect:**
**不能检测：**
- Attendance fraud (billing for children who didn't show up) — requires non-public CCAP billing records
  出勤欺诈（为未到场儿童计费），这需要非公开的 `CCAP` 账单记录
- Any fraud requiring access to internal DHS or county billing data
  任何需要访问内部 `DHS` 或县级账单数据的欺诈

All findings are investigative leads, not legal conclusions. The agent uses language like "requires further investigation" and "exhibits anomalies" — never "fraud."
所有发现都是调查线索，而不是法律结论。该智能体会使用 “requires further investigation” 和 “exhibits anomalies” 这样的表述，而不会直接说 “fraud”。

### Geographic Scope
### 地理范围

This demo covers **Cook County, Illinois only**. Property data is sourced from the Cook County Assessor's open data, so the ZIP code selector is limited to 10 high-density Chicago neighborhoods known for concentrations of subsidized childcare providers:
此演示仅覆盖 **`Illinois` 州 `Cook County`**。房产数据来自 `Cook County Assessor` 开放数据，因此邮编选择器限制为 `10` 个高密度 `Chicago` 社区，这些社区以补贴托育服务提供商集中而闻名：

| ZIP<br>邮编 | Neighborhood<br>社区 |
|-----|-------------|
| 60623 | Little Village / North Lawndale<br>小村庄 / 北朗代尔 |
| 60629 | Chicago Lawn<br>芝加哥朗 |
| 60644 | Austin<br>奥斯汀 |
| 60621 | Englewood<br>恩格尔伍德 |
| 60628 | Roseland<br>罗斯兰 |
| 60619 | Chatham / Auburn Gresham<br>查塔姆 / 奥本格雷沙姆 |
| 60636 | West Englewood<br>西恩格尔伍德 |
| 60612 | Near West Side<br>近西区 |
| 60620 | Auburn Gresham<br>奥本格雷沙姆 |
| 60624 | Garfield Park<br>加菲尔德公园 |

The full [Surelock Homes](https://github.com/oso95/Surelock-Homes) system supports Minnesota and additional Illinois counties with a FastAPI backend, streaming dashboard, and offline mode.
完整的 [`Surelock Homes`](https://github.com/oso95/Surelock-Homes) 系统支持 `Minnesota` 和更多 `Illinois` 县，并提供 `FastAPI` 后端、流式仪表盘和离线模式。
