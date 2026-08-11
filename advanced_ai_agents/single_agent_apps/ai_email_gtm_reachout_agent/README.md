# 🚀 AI Email GTM Reachout Agent
# 🚀 `AI` 邮件 `GTM` 外联智能体

### 🎓 FREE Step-by-Step Tutorial 
### 🎓 免费分步教程
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-email-gtm-outreach-agent-team) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整的分步教程](https://www.theunwindai.com/p/build-an-ai-email-gtm-outreach-agent-team)，学习如何从零开始构建此项目，包括详细的代码讲解、说明和最佳实践。**

An intelligent, fully automated B2B outreach system that discovers companies, finds decision makers, researches company intelligence, and generates personalized cold emails using AI agents.
一个智能、全自动的 `B2B` 外联系统，使用 `AI` 智能体发现公司、寻找决策者、研究公司情报，并生成个性化冷邮件。

## ✨ Features
## ✨ 功能

### 🔍 **Automated Company Discovery**
### 🔍 **自动化公司发现**
- Uses Exa search to find target companies based on industry, size, and business criteria
  使用 `Exa` 搜索，根据行业、规模和业务条件查找目标公司
- Identifies companies showing growth, recent funding, or expansion
  识别表现出增长、近期融资或扩张迹象的公司
- Supports multiple company categories: SaaS/Technology, E-commerce/Retail, Financial Services, Healthcare/Biotech, Manufacturing/Industrial
  支持多种公司类别：`SaaS/Technology`、`E-commerce/Retail`、`Financial Services`、`Healthcare/Biotech`、`Manufacturing/Industrial`

### 👥 **Intelligent Contact Finding**
### 👥 **智能联系人查找**
- Automatically discovers decision makers in target departments
  自动发现目标部门中的决策者
- Finds email addresses and LinkedIn profiles
  查找电子邮件地址和 `LinkedIn` 资料
- Targets roles like CEO, CTO, VP of Engineering, CMO, VP Marketing, Sales Directors, HR Directors
  定位 `CEO`、`CTO`、`VP of Engineering`、`CMO`、`VP Marketing`、`Sales Directors`、`HR Directors` 等角色

### 🔬 **Deep Company Research**
### 🔬 **深度公司研究**
- Comprehensive company intelligence gathering
  全面收集公司情报
- Analyzes website, recent news, product offerings, technology stack
  分析网站、近期新闻、产品服务和技术栈
- Identifies pain points, growth opportunities, and market positioning
  识别痛点、增长机会和市场定位
- Extracts insights relevant for personalized outreach
  提取与个性化外联相关的洞察

### ✉️ **Personalized Email Generation**
### ✉️ **个性化邮件生成**
- Creates highly personalized cold emails based on research
  基于研究创建高度个性化的冷邮件
- Uses department-specific templates for different professional types
  针对不同专业类型使用按部门定制的模板
- Maintains friendly, conversational tone (20-year-old sales rep style)
  保持友好、对话式语气（`20` 岁销售代表风格）
- Avoids corporate jargon and clichés
  避免企业套话和陈词滥调
- References specific company challenges and achievements
  引用具体的公司挑战和成就

### 🎯 **Smart Targeting**
### 🎯 **智能定位**
- **Company Categories**: SaaS/Technology, E-commerce, Financial Services, Healthcare, Manufacturing
  **公司类别**：`SaaS/Technology`、`E-commerce`、`Financial Services`、`Healthcare`、`Manufacturing`
- **Company Sizes**: Startup (1-50), SMB (51-500), Enterprise (500+), All Sizes
  **公司规模**：`Startup`（`1-50`）、`SMB`（`51-500`）、`Enterprise`（`500+`）、`All Sizes`
- **Target Departments**: GTM (Sales & Marketing), HR, Engineering/Tech, Operations, Finance, Product, Executive Leadership
  **目标部门**：`GTM`（`Sales & Marketing`）、`HR`、`Engineering/Tech`、`Operations`、`Finance`、`Product`、`Executive Leadership`
- **Service Types**: Software Solution, Consulting Services, Professional Services, Technology Platform, Custom Development
  **服务类型**：`Software Solution`、`Consulting Services`、`Professional Services`、`Technology Platform`、`Custom Development`

## 🛠️ Installation
## 🛠️ 安装

1. **Clone the repository**
   **克隆仓库**
```bash
git clone <repository-url>
cd ai_email_gtm_reachout_agent
```

2. **Install dependencies**
   **安装依赖**
```bash
pip install -r requirements.txt
```

**Note**: Make sure you have Agno version 2.0.4 or higher installed.
**注意**：请确保已安装 `Agno` `2.0.4` 或更高版本。

3. **Set up API keys**
   **设置 `API key`**
```bash
# Required API keys
export EXA_API_KEY="your_exa_api_key"
export OPENAI_API_KEY="your_openai_api_key"
```

## 🚀 Quick Start
## 🚀 快速开始

1. **Run the application**
   **运行应用**
```bash
streamlit run ai_email_gtm_reachout.py
```

2. **Configure your outreach campaign**:
   **配置你的外联活动**：
   - Select target company category and size
     选择目标公司类别和规模
   - Choose departments to target
     选择要定位的部门
   - Enter your contact information
     输入你的联系信息
   - Describe your service offering
     描述你的服务方案
   - Select personalization level
     选择个性化级别

3. **Launch automated campaign**:
   **启动自动化活动**：
   - Click "Start Automated Campaign"
     点击 “Start Automated Campaign”
   - Watch as AI discovers companies, finds contacts, researches details, and generates personalized emails
     观察 `AI` 如何发现公司、查找联系人、研究详情并生成个性化邮件

## 📋 Usage Guide
## 📋 使用指南

### Step 1: Target Company Discovery
### 步骤 1：目标公司发现
- Choose from predefined company categories
  从预定义公司类别中选择
- Select preferred company size
  选择偏好的公司规模
- Specify number of companies to find (1-20)
  指定要查找的公司数量（`1-20`）

### Step 2: Your Information
### 步骤 2：你的信息
- **Required**: Name, Email, Organization, Service Description
  **必填**：姓名、电子邮件、组织、服务描述
- **Optional**: LinkedIn, Phone, Website, Calendar Link
  **可选**：`LinkedIn`、电话、网站、日历链接

### Step 3: Outreach Configuration
### 步骤 3：外联配置
- Select service/product category
  选择服务/产品类别
- Choose personalization level (Basic/Medium/Deep)
  选择个性化级别（`Basic`/`Medium`/`Deep`）
- Pick target departments
  选择目标部门

### Step 4: Generate Campaign
### 步骤 4：生成活动
- Review your configuration
  检查你的配置
- Click "Start Automated Campaign"
  点击 “Start Automated Campaign”
- Monitor progress and view generated emails
  监控进度并查看生成的邮件

## 🎨 Email Templates
## 🎨 邮件模板

The system includes department-specific templates:
该系统包含按部门定制的模板：

### GTM (Sales & Marketing)
### `GTM`（`Sales & Marketing`）
- Software Solution templates
  `Software Solution` 模板
- Consulting Services templates
  `Consulting Services` 模板

### Human Resources
### 人力资源
- Software Solution templates
  `Software Solution` 模板
- Consulting Services templates
  `Consulting Services` 模板
- Investment Opportunity templates
  `Investment Opportunity` 模板

### Marketing Professional
### 营销专业人员
- Product Demo templates
  `Product Demo` 模板
- Service Offering templates
  `Service Offering` 模板

### B2B Sales Representative
### `B2B` 销售代表
- Product Demo templates
  `Product Demo` 模板
- Service Offering templates
  `Service Offering` 模板

## 🔧 Configuration Options
## 🔧 配置选项

### Company Categories
### 公司类别
- **SaaS/Technology Companies**: Software, cloud services, tech platforms
  **`SaaS/Technology Companies`**：软件、云服务、技术平台
- **E-commerce/Retail**: Online retail, marketplaces, D2C brands
  **`E-commerce/Retail`**：在线零售、市场平台、`D2C` 品牌
- **Financial Services**: Banks, fintech, insurance, investment firms
  **`Financial Services`**：银行、金融科技、保险、投资公司
- **Healthcare/Biotech**: Healthcare providers, biotech, health tech
  **`Healthcare/Biotech`**：医疗服务提供商、生物技术、健康科技
- **Manufacturing/Industrial**: Manufacturing, industrial automation, supply chain
  **`Manufacturing/Industrial`**：制造业、工业自动化、供应链

### Personalization Levels
### 个性化级别
- **Basic**: Standard personalization with company name and basic details
  **`Basic`**：包含公司名称和基本详情的标准个性化
- **Medium**: Includes recent company news and achievements
  **`Medium`**：包含近期公司新闻和成就
- **Deep**: Comprehensive personalization with specific pain points and opportunities
  **`Deep`**：包含具体痛点和机会的全面个性化

## 📊 Output Format
## 📊 输出格式

Each generated email includes:
每封生成的邮件包含：
- **Personalized Email**: Ready-to-send cold email
  **个性化邮件**：可直接发送的冷邮件
- **Company Research**: Detailed company intelligence
  **公司研究**：详细的公司情报
- **Contacts Found**: Decision maker information
  **找到的联系人**：决策者信息

## 🔑 API Requirements
## 🔑 `API` 要求

### Exa API
### `Exa API`
- Used for company discovery and research
  用于公司发现和研究
- Get your API key from [exa.ai](https://exa.ai)
  从 [`exa.ai`](https://exa.ai) 获取你的 `API key`
- Required for finding companies and gathering intelligence
  查找公司和收集情报时必需

### OpenAI API
### `OpenAI API`
- Used for email generation and content creation
  用于邮件生成和内容创建
- Get your API key from [platform.openai.com](https://platform.openai.com)
  从 [`platform.openai.com`](https://platform.openai.com) 获取你的 `API key`
- Required for AI-powered email personalization
  进行 `AI` 驱动的邮件个性化时必需

## 🎯 Use Cases
## 🎯 使用场景

### Sales Teams
### 销售团队
- Automated prospecting for B2B sales
  为 `B2B` 销售自动寻找潜在客户
- Personalized outreach at scale
  大规模个性化外联
- Target specific industries and company sizes
  定位特定行业和公司规模

### Marketing Agencies
### 营销机构
- Client prospecting campaigns
  客户潜在客户开发活动
- Lead generation for multiple clients
  为多个客户生成销售线索
- Industry-specific outreach strategies
  面向特定行业的外联策略

### Consultants
### 顾问
- Business development automation
  业务拓展自动化
- Service offering promotion
  服务方案推广
- Professional network expansion
  专业网络拓展

### Startups
### 初创公司
- Investor outreach
  投资人外联
- Partnership development
  合作伙伴开发
- Customer acquisition
  客户获取
