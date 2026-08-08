# Life Insurance Coverage Advisor Agent
# 人寿保险保额顾问代理

This Streamlit app estimates term life insurance coverage and suggests policy options.

这个 Streamlit 应用可以估算定期寿险保额，并给出可选方案建议。

It uses Agno, OpenAI GPT-5, E2B, and Firecrawl.

它使用 Agno、OpenAI GPT-5、E2B 和 Firecrawl。

## Highlights
## 亮点

- Estimate coverage from income, debt, dependents, assets, and horizon.
- 根据收入、负债、家属、资产和期限估算保障额度。
- Run the calculation inside an E2B sandbox.
- 在 E2B 沙箱中执行计算。
- Research current insurance options from the web.
- 从网页上检索最新的保险产品信息。
- Show a concise breakdown with source links.
- 展示简洁的计算过程和来源链接。

## Installation
## 安装

1. Clone the repository.
1. 克隆仓库。
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   ```
2. Install dependencies.
2. 安装依赖。
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app.
3. 运行应用。
   ```bash
   streamlit run life_insurance_advisor_agent.py
   ```

## Usage
## 使用方式

1. Enter OpenAI, Firecrawl, and E2B API keys.
1. 输入 OpenAI、Firecrawl 和 E2B 的 API Key。
2. Fill in the financial details.
2. 填写财务信息。
3. Generate coverage and options.
3. 生成保额和产品建议。
4. Review the explanation and suggested policies.
4. 查看计算说明和推荐方案。

## Disclaimer
## 免责声明

This project is for educational and prototyping purposes only and is not financial advice.
本项目仅用于学习和原型验证，不构成金融建议。
