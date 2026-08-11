# Vision RAG with Cohere Embed-4 🖼️
# 使用 `Cohere Embed-4` 的 `Vision RAG` 🖼️

A powerful visual Retrieval-Augmented Generation (RAG) system that utilizes Cohere's state-of-the-art Embed-4 model for multimodal embedding and Google's efficient Gemini 2.5 Flash model for answering questions about images and PDF pages.
一个强大的视觉检索增强生成（`RAG`）系统，使用 `Cohere` 最先进的 `Embed-4` 模型进行多模态嵌入，并使用 `Google` 高效的 `Gemini 2.5 Flash` 模型回答有关图片和 `PDF` 页面的问题。

## Features
## 功能

- **Multimodal Search**: Leverages Cohere Embed-4 to find the most semantically relevant image (or PDF page image) for a given text question.
  **多模态搜索**：利用 `Cohere Embed-4` 为给定文本问题查找语义上最相关的图片（或 `PDF` 页面图片）。
- **Visual Question Answering**: Employs Google Gemini 2.5 Flash to analyze the content of the retrieved image/page and generate accurate, context-aware answers.
  **视觉问答**：使用 `Google Gemini 2.5 Flash` 分析检索到的图片/页面内容，并生成准确、上下文感知的答案。
- **Flexible Content Sources**:
  **灵活的内容来源**：
    - Use pre-loaded sample financial charts and infographics.
      使用预加载的示例财务图表和信息图。
    - Upload your own custom images (PNG, JPG, JPEG).
      上传你自己的自定义图片（`PNG`、`JPG`、`JPEG`）。
    - **Upload PDF documents**: Automatically extracts pages as images for analysis.
      **上传 `PDF` 文档**：自动将页面提取为图片以进行分析。
- **No OCR Required**: Directly processes complex images and visual elements within PDF pages without needing separate text extraction steps.
  **无需 `OCR`**：直接处理 `PDF` 页面中的复杂图片和视觉元素，无需单独的文本提取步骤。
- **Interactive UI**: Built with Streamlit for easy interaction, including content loading, question input, and result display.
  **交互式 `UI`**：使用 `Streamlit` 构建，便于进行内容加载、问题输入和结果展示。
- **Session Management**: Remembers loaded/uploaded content (images and processed PDF pages) within a session.
  **会话管理**：在一个会话中记住已加载/上传的内容（图片和处理后的 `PDF` 页面）。

## Requirements
## 要求

- Python 3.8+
  `Python 3.8+` 环境
- Cohere API key
  `Cohere API key` 密钥
- Google Gemini API key
  `Google Gemini API key` 密钥

## How to Run
## 如何运行

Follow these steps to set up and run the application:
按照以下步骤设置并运行应用：

1.  **Clone and Navigate to Directory** :
    **克隆并进入目录**：
    ```bash
    git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
    cd awesome-llm-apps/rag_tutorials/vision_rag
    ```

2.  **Install Dependencies**:
    **安装依赖**：
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure you have the latest `PyMuPDF` installed along with other requirements)*
    *（确保你已随其他依赖一起安装最新的 `PyMuPDF`）*

3.  **Set up your API keys**:
    **设置你的 `API keys`**：
    - Get a Cohere API key from: [https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)
      从这里获取 `Cohere API key`：[https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)
    - Get a Google API key from: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
      从这里获取 `Google API key`：[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

4.  **Run the Streamlit app**:
    **运行 `Streamlit app`**：
    ```bash
    streamlit run vision_rag.py
    ```

5.  **Access the Web Interface**:
    **访问 `Web` 界面**：
    - Streamlit will provide a local URL (usually `http://localhost:8501`) in your terminal.
      `Streamlit` 会在终端中提供一个本地 `URL`（通常是 `http://localhost:8501`）。
    - Open this URL in your web browser.
      在你的网页浏览器中打开此 `URL`。

## How It Works
## 工作原理

The application follows a two-stage RAG process:
该应用遵循两阶段 `RAG` 流程：

1.  **Retrieval**:
    **检索**：
    - When you load sample images or upload your own images/PDFs:
      当你加载示例图片或上传自己的图片/`PDF` 时：
        - Regular images are converted to base64 strings.
          普通图片会被转换为 `base64` 字符串。
        - **PDFs are processed page by page**: Each page is rendered as an image, saved temporarily, and converted to a base64 string.
          **`PDF` 会逐页处理**：每一页都会被渲染为图片、临时保存，并转换为 `base64` 字符串。
    - Cohere's `embed-v4.0` model (with `input_type="search_document"`) is used to generate a dense vector embedding for each image or PDF page image.
      使用 `Cohere` 的 `embed-v4.0` 模型（带 `input_type="search_document"`）为每张图片或 `PDF` 页面图片生成密集向量嵌入。
    - When you ask a question, the text query is embedded using the same `embed-v4.0` model (with `input_type="search_query"`).
      当你提问时，文本查询会使用同一个 `embed-v4.0` 模型（带 `input_type="search_query"`）进行嵌入。
    - Cosine similarity is calculated between the question embedding and all image embeddings.
      计算问题嵌入与所有图片嵌入之间的余弦相似度。
    - The image with the highest similarity score (which could be a regular image or a specific PDF page image) is retrieved as the most relevant context.
      检索相似度得分最高的图片作为最相关上下文（可能是普通图片，也可能是特定的 `PDF` 页面图片）。

2.  **Generation**:
    **生成**：
    - The original text question and the retrieved image/page image are passed as input to the Google `gemini-2.5-flash-preview-04-17` model.
      原始文本问题和检索到的图片/页面图片会作为输入传递给 `Google` 的 `gemini-2.5-flash-preview-04-17` 模型。
    - Gemini analyzes the image content in the context of the question and generates a textual answer.
      `Gemini` 会在问题语境下分析图片内容并生成文本答案。

## Usage
## 用法

1.  Enter your Cohere and Google API keys in the sidebar.
    在侧边栏输入你的 `Cohere` 和 `Google API keys`。
2.  Load content:
    加载内容：
    - Click **"Load Sample Images"** to download and process the built-in examples.
      点击 **"Load Sample Images"** 下载并处理内置示例。
    - *OR/AND* Use the **"Upload Your Images or PDFs"** section to upload your own image or PDF files.
      *或/和* 使用 **"Upload Your Images or PDFs"** 部分上传你自己的图片或 `PDF` 文件。
3.  Once content is loaded and processed (embeddings generated), the **"Ask a Question"** section will be enabled.
    内容加载并处理完成后（已生成嵌入），**"Ask a Question"** 部分会启用。
4.  Optionally, expand **"View Loaded Images"** to see thumbnails of all images and processed PDF pages currently in the session.
    可选择展开 **"View Loaded Images"**，查看当前会话中所有图片和已处理 `PDF` 页面的缩略图。
5.  Type your question about the loaded content into the text input field.
    在文本输入框中输入关于已加载内容的问题。
6.  Click **"Run Vision RAG"**.
    点击 **"Run Vision RAG"**。
7.  View the results:
    查看结果：
    - The **Retrieved Image/Page** deemed most relevant to your question (caption indicates source PDF and page number if applicable).
      被认为与你的问题最相关的 **Retrieved Image/Page**（如果适用，标题会指示来源 `PDF` 和页码）。
    - The **Generated Answer** from Gemini based on the image and question.
      `Gemini` 基于图片和问题生成的 **Generated Answer**。

## Use Cases
## 使用场景

- Analyze financial charts and extract key figures or trends.
  分析财务图表并提取关键数字或趋势。
- Answer specific questions about diagrams, flowcharts, or infographics within images or PDFs.
  回答关于图片或 `PDF` 中图示、流程图或信息图的具体问题。
- Extract information from tables or text within screenshots or PDF pages without explicit OCR.
  在无需显式 `OCR` 的情况下，从截图或 `PDF` 页面中的表格或文本提取信息。
- Build and query visual knowledge bases (from images and PDFs) using natural language.
  使用自然语言构建并查询视觉知识库（来源于图片和 `PDF`）。
- Understand the content of various complex visual documents, including multi-page reports.
  理解各种复杂视觉文档的内容，包括多页报告。

## Note
## 注意

- Image and PDF processing (page rendering + embedding) can take time, especially for many items or large files. Sample images are cached after the first load; PDF processing currently happens on each upload within a session.
  图片和 `PDF` 处理（页面渲染 + 嵌入）可能需要时间，尤其是在项目很多或文件很大时。示例图片会在首次加载后缓存；`PDF` 处理目前会在会话内每次上传时执行。
- Ensure your API keys have the necessary permissions and quotas for the Cohere and Gemini models used.
  确保你的 `API keys` 对所用的 `Cohere` 和 `Gemini` 模型具备必要权限和配额。
- The quality of the answer depends on both the relevance of the retrieved image and the capability of the Gemini model to interpret the image based on the question.
  答案质量同时取决于检索图片的相关性，以及 `Gemini` 模型基于问题解读图片的能力。
