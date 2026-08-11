# TripCraft AI - Agent Architecture
# TripCraft AI - 智能体架构

TripCraft AI uses a sophisticated multi-agent system powered by Agno to create personalized travel experiences.
`TripCraft AI` 使用由 `Agno` 驱动的复杂多智能体系统来创建个性化旅行体验。

This document explains the different agents and their roles in the system.
本文档说明系统中的不同智能体及其角色。

## Team Structure
## 团队结构

The system is orchestrated by the "TripCraft AI Team", which coordinates multiple specialized agents to create comprehensive travel plans.
该系统由“TripCraft AI Team”编排，负责协调多个专业化智能体来创建完整旅行计划。

The team operates in a coordinated mode, ensuring all aspects of travel planning are handled efficiently.
团队以协调模式运行，确保旅行规划的各个方面都能被高效处理。

### Core Team Members
### 核心团队成员

1. **Destination Explorer**
1. **目的地探索智能体**
   - Primary role: Researches and recommends tourist attractions and experiences
   - 主要角色：研究并推荐旅游景点和体验
   - Tools: ExaTools for deep web research
   - 工具：使用 `ExaTools` 进行深度网页研究
   - Focus areas:
   - 关注领域：
     - Famous landmarks and monuments
     - 著名地标和纪念性建筑
     - Popular tourist spots
     - 热门旅游地点
     - Museums and cultural sites
     - 博物馆和文化场所
     - Shopping areas
     - 购物区域
     - Family-friendly activities
     - 适合家庭的活动
   - Provides structured information about attractions including opening hours, fees, and visit duration
   - 提供关于景点的结构化信息，包括开放时间、费用和游览时长

2. **Hotel Search Agent**
2. **酒店搜索智能体**
   - Primary role: Accommodation research and recommendations
   - 主要角色：住宿研究和推荐
   - Focuses on finding the perfect stay based on:
   - 聚焦根据以下条件找到合适住宿：
     - Location preferences
     - 位置偏好
     - Budget constraints
     - 预算限制
     - Required amenities
     - 所需设施
     - Room types
     - 房型
     - Property features
     - 住宿属性特征

3. **Dining Agent**
3. **餐饮智能体**
   - Primary role: Restaurant and culinary experience recommendations
   - 主要角色：餐厅和美食体验推荐
   - Considers:
   - 考虑：
     - Cuisine types
     - 菜系类型
     - Price ranges
     - 价格区间
     - Dietary restrictions
     - 饮食限制
     - Ambiance and atmosphere
     - 环境和氛围
     - Location and accessibility
     - 位置和可达性
     - Special dining experiences
     - 特色餐饮体验

4. **Budget Agent**
4. **预算智能体**
   - Primary role: Financial planning and cost optimization
   - 主要角色：财务规划和成本优化
   - Responsibilities:
   - 职责：
     - Trip cost breakdown
     - 旅行成本拆分
     - Budget allocation
     - 预算分配
     - Cost-saving recommendations
     - 节省成本建议
     - Currency considerations
     - 货币因素
     - Emergency fund planning
     - 应急资金规划

5. **Flight Search Agent**
5. **航班搜索智能体**
   - Primary role: Air travel planning and optimization
   - 主要角色：航空旅行规划和优化
   - Handles:
   - 处理：
     - Flight route research
     - 航线研究
     - Airline comparisons
     - 航空公司比较
     - Schedule optimization
     - 航班时刻优化
     - Connection planning
     - 中转规划
     - Airport transfer coordination
     - 机场接驳协调

6. **Itinerary Specialist**
6. **行程专家**
   - Primary role: Creates detailed day-by-day travel schedules
   - 主要角色：创建详细的逐日旅行日程
   - Expertise:
   - 专长：
     - Hour-by-hour activity planning
     - 按小时规划活动
     - Optimized timing for attractions
     - 优化景点游览时间
     - Transportation scheduling
     - 交通安排
     - Realistic travel times
     - 现实可行的交通时间
     - Buffer time management
     - 缓冲时间管理
     - Weather-adaptive scheduling
     - 适应天气的日程安排
     - Traveler-specific pacing
     - 针对旅行者的节奏安排

## Team Coordination
## 团队协调

The team works together through a sophisticated coordination system that:
团队通过复杂的协调系统协同工作，该系统会：

1. Analyzes user preferences and requirements
1. 分析用户偏好和需求
2. Delegates tasks to specialized agents
2. 将任务委派给专业化智能体
3. Combines individual agent outputs into a cohesive travel plan
3. 将各个智能体的输出合并为连贯的旅行计划
4. Ensures all aspects of the trip are properly synchronized
4. 确保旅程的各个方面得到妥善同步
5. Maintains budget alignment across all decisions
5. 在所有决策中保持预算一致

## Tools and Technologies
## 工具和技术

The agents utilize various tools including:
智能体使用多种工具，包括：

- **ReasoningTools**: For logical decision-making and plan optimization
- **ReasoningTools**：用于逻辑决策和计划优化
- **ExaTools**: For deep web research and information gathering
- **ExaTools**：用于深度网页研究和信息收集
- **FirecrawlTools**: For real-time data and current information
- **FirecrawlTools**：用于实时数据和最新信息

## Output Format
## 输出格式

The team produces detailed travel itineraries that include:
团队会生成详细旅行行程，其中包括：

- Executive summary of the trip
- 旅程执行摘要
- Comprehensive travel logistics
- 完整旅行后勤信息
- Day-by-day itineraries
- 逐日行程
- Detailed accommodation information
- 详细住宿信息
- Curated experiences and activities
- 精选体验和活动
- Complete budget breakdown
- 完整预算拆分

## Best Practices
## 最佳实践

The agent system follows these key principles:
该智能体系统遵循以下关键原则：

1. Thorough analysis of user preferences
1. 全面分析用户偏好
2. Detailed research using multiple data sources
2. 使用多个数据源进行详细研究
3. Practical and implementable recommendations
3. 提供实际且可实施的建议
4. Backup options and contingency plans
4. 提供备选方案和应急计划
5. Clear communication and structured output
5. 清晰沟通和结构化输出
6. Budget consciousness across all decisions
6. 在所有决策中保持预算意识

## Integration
## 集成

This agent architecture is designed to work seamlessly with the TripCraft AI backend, providing a robust foundation for creating personalized travel experiences that feel both magical and practical.
该智能体架构旨在与 `TripCraft AI` 后端无缝协作，为创建既有惊喜感又实用的个性化旅行体验提供稳固基础。
