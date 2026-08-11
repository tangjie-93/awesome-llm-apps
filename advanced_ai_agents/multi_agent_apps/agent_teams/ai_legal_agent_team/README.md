# 👨‍⚖️ AI Legal Agent Team
# 👨‍⚖️ `AI` 法律智能体团队

### 🎓 FREE Step-by-Step Tutorial
### 🎓 免费分步教程

**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-ai-legal-team-run-by-ai-agents) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**
**👉 [点击这里查看完整分步教程](https://www.theunwindai.com/p/build-an-ai-legal-team-run-by-ai-agents)，通过详细的代码讲解、说明和最佳实践，学习如何从零构建这个项目。**

A Streamlit application that simulates a full-service legal team using multiple AI agents to analyze legal documents and provide comprehensive legal insights. Each agent represents a different legal specialist role, from research and contract analysis to strategic planning, working together to provide thorough legal analysis and recommendations.
这是一个 `Streamlit` 应用，使用多个 `AI` 智能体模拟全方位法律团队，用于分析法律文档并提供全面的法律洞察。每个智能体代表不同的法律专家角色，涵盖研究、合同分析到战略规划，并协同提供深入的法律分析和建议。

## Features
## 功能

- **Specialized Legal AI Agent Team**
- **专门的法律 `AI` 智能体团队**
  - **Legal Researcher**: Equipped with DuckDuckGo search tool to find and cite relevant legal cases and precedents. Provides detailed research summaries with sources and references specific sections from uploaded documents.
  - **`Legal Researcher`**：配备 `DuckDuckGo` 搜索工具，用于查找并引用相关法律案例和判例。提供带来源的详细研究摘要，并引用上传文档中的具体章节。

  - **Contract Analyst**: Specializes in thorough contract review, identifying key terms, obligations, and potential issues. References specific clauses from documents for detailed analysis.
  - **`Contract Analyst`**：专注于全面合同审查，识别关键条款、义务和潜在问题。引用文档中的具体条款进行详细分析。

  - **Legal Strategist**: Focuses on developing comprehensive legal strategies, providing actionable recommendations while considering both risks and opportunities.
  - **`Legal Strategist`**：专注于制定全面法律策略，在同时考虑风险和机会的基础上提供可执行建议。

  - **Team Lead**: Coordinates analysis between team members, ensures comprehensive responses, properly sourced recommendations, and references to specific document parts. Acts as an Agent Team coordinator for all three agents.
  - **`Team Lead`**：协调团队成员之间的分析，确保回复全面、建议有适当来源，并引用文档的具体部分。作为全部三个智能体的 `Agent Team` 协调者。

- **Document Analysis Types**
- **文档分析类型**
  - Contract Review - Done by Contract Analyst
  - 合同审查 - 由 `Contract Analyst` 完成
  - Legal Research - Done by Legal Researcher
  - 法律研究 - 由 `Legal Researcher` 完成
  - Risk Assessment - Done by Legal Strategist, Contract Analyst
  - 风险评估 - 由 `Legal Strategist`、`Contract Analyst` 完成
  - Compliance Check - Done by Legal Strategist, Legal Researcher, Contract Analyst
  - 合规检查 - 由 `Legal Strategist`、`Legal Researcher`、`Contract Analyst` 完成
  - Custom Queries - Done by Agent Team - Legal Researcher, Legal Strategist, Contract Analyst
  - 自定义查询 - 由 `Agent Team` 完成，包括 `Legal Researcher`、`Legal Strategist`、`Contract Analyst`

## How to Run
## 如何运行

1. **Setup Environment**
1. **设置环境**

   ```bash
   # Clone the repository
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_legal_agent_team

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
2. **配置 `API Keys`**

   - Get OpenAI API key from [OpenAI Platform](https://platform.openai.com)
   - 从 [OpenAI Platform](https://platform.openai.com) 获取 `OpenAI API key`
   - Get Qdrant API key and URL from [Qdrant Cloud](https://cloud.qdrant.io)
   - 从 [Qdrant Cloud](https://cloud.qdrant.io) 获取 `Qdrant API key` 和 `URL`

3. **Run the Application**
3. **运行应用**

   ```bash
   streamlit run legal_agent_team.py
   ```

4. **Use the Interface**
4. **使用界面**

   - Enter API credentials
   - 输入 `API` 凭据
   - Upload a legal document (PDF)
   - 上传法律文档（`PDF`）
   - Select analysis type
   - 选择分析类型
   - Add custom queries if needed
   - 如有需要，添加自定义查询
   - View analysis results
   - 查看分析结果

## Notes
## 说明

- Supports PDF documents only
- 仅支持 `PDF` 文档
- Uses GPT-4o for analysis
- 使用 `GPT-4o` 进行分析
- Uses text-embedding-3-small for embeddings
- 使用 `text-embedding-3-small` 生成嵌入
- Requires stable internet connection
- 需要稳定的互联网连接
- API usage costs apply
- 会产生 `API` 使用费用
