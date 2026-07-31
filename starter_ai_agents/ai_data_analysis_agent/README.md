# AI Data Analysis Agent
# AI 数据分析代理

This Streamlit app analyzes CSV and Excel files with natural language queries.
这个 Streamlit 应用可以用自然语言查询分析 CSV 和 Excel 文件。

It uses the Agno framework, OpenAI GPT-4o, and DuckDB for fast data processing.
它使用 Agno 框架、OpenAI GPT-4o 和 DuckDB 来完成高效数据处理。

## Features
## 功能特性

- Upload CSV and Excel files.
- 上传 CSV 和 Excel 文件。
- Ask questions in natural language.
- 用自然语言提问。
- Convert questions into SQL and return answers quickly.
- 将问题转成 SQL 并快速返回结果。
- Show charts and summaries in a simple UI.
- 在简洁界面中展示图表和摘要。

## Run
## 运行

1. Clone the repository.
1. 克隆仓库。
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/starter_ai_agents/ai_data_analysis_agent
   ```
2. Install dependencies.
2. 安装依赖。
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app.
3. 运行应用。
   ```bash
   streamlit run ai_data_analyst.py
   ```

## Usage
## 使用方式

1. Add your OpenAI API key in the sidebar.
1. 在侧边栏中填写 OpenAI API Key。
2. Upload a data file.
2. 上传数据文件。
3. Ask a question about the data.
3. 输入关于数据的问题。
4. Review the answer and any generated visuals.
4. 查看答案和生成的可视化结果。
