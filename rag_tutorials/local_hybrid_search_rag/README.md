# 🖥️ Local RAG App with Hybrid Search
# 🖥️ 使用混合搜索的本地 `RAG` 应用

A powerful document Q&A application that leverages Hybrid Search (RAG) and local LLMs for comprehensive answers. Built with RAGLite for robust document processing and retrieval, and Streamlit for an intuitive chat interface, this system combines document-specific knowledge with local LLM capabilities to deliver accurate and contextual responses.
这是一个强大的文档问答应用，利用 `Hybrid Search (RAG)` 和本地 `LLM` 提供全面答案。该系统使用 `RAGLite` 实现稳健的文档处理与检索，并使用 `Streamlit` 提供直观的聊天界面，将文档专属知识与本地 `LLM` 能力结合起来，生成准确且具备上下文的响应。

## Demo:
## 演示：


https://github.com/user-attachments/assets/375da089-1ab9-4bf4-b6f3-733f44e47403


## Quick Start
## 快速开始

For immediate testing, use these tested model configurations:
如需立即测试，请使用以下已经验证的模型配置：
```bash
# LLM Model
bartowski/Llama-3.2-3B-Instruct-GGUF/Llama-3.2-3B-Instruct-Q4_K_M.gguf@4096

# Embedder Model
lm-kit/bge-m3-gguf/bge-m3-Q4_K_M.gguf@1024
```
These models offer a good balance of performance and resource usage, and have been verified to work well together even on a MacBook Air M2 with 8GB RAM.
这些模型在性能和资源使用之间提供了良好平衡，并且已验证即使在配备 `8GB RAM` 的 `MacBook Air M2` 上也能很好地协同工作。

## Features
## 功能

- **Local LLM Integration**:
- **本地 `LLM` 集成**：
  - Uses llama-cpp-python models for local inference
  - 使用 `llama-cpp-python` 模型进行本地推理
  - Supports various quantization formats (Q4_K_M recommended)
  - 支持多种量化格式（推荐 `Q4_K_M`）
  - Configurable context window sizes
  - 可配置上下文窗口大小

- **Document Processing**:
- **文档处理**：
  - PDF document upload and processing
  - 上传并处理 `PDF` 文档
  - Automatic text chunking and embedding
  - 自动文本切块和嵌入
  - Hybrid search combining semantic and keyword matching
  - 结合语义匹配和关键词匹配的混合搜索
  - Reranking for better context selection
  - 通过重排序改进上下文选择

- **Multi-Model Integration**:
- **多模型集成**：
  - Local LLM for text generation (e.g., Llama-3.2-3B-Instruct)
  - 使用本地 `LLM` 进行文本生成（例如 `Llama-3.2-3B-Instruct`）
  - Local embeddings using BGE models
  - 使用 `BGE` 模型生成本地嵌入
  - FlashRank for local reranking
  - 使用 `FlashRank` 进行本地重排序

## Prerequisites
## 前置条件

1. **Install spaCy Model**:
1. **安装 `spaCy` 模型**：
   ```bash
   pip install https://github.com/explosion/spacy-models/releases/download/xx_sent_ud_sm-3.7.0/xx_sent_ud_sm-3.7.0-py3-none-any.whl
   ```

2. **Install Accelerated llama-cpp-python** (Optional but recommended):
2. **安装加速版 `llama-cpp-python`**（可选但推荐）：
   ```bash
   # Configure installation variables
   LLAMA_CPP_PYTHON_VERSION=0.3.2
   PYTHON_VERSION=310 # 3.10, 3.11, 3.12
   ACCELERATOR=metal  # For Mac
   # ACCELERATOR=cu121  # For NVIDIA GPU
   PLATFORM=macosx_11_0_arm64  # For Mac
   # PLATFORM=linux_x86_64  # For Linux
   # PLATFORM=win_amd64  # For Windows

   # Install accelerated version
   pip install "https://github.com/abetlen/llama-cpp-python/releases/download/v$LLAMA_CPP_PYTHON_VERSION-$ACCELERATOR/llama_cpp_python-$LLAMA_CPP_PYTHON_VERSION-cp$PYTHON_VERSION-cp$PYTHON_VERSION-$PLATFORM.whl"
   ```

3. **Install Dependencies**:
3. **安装依赖**：
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/rag_tutorials/local_hybrid_search_rag
   pip install -r requirements.txt
   ```

## Model Setup
## 模型设置

RAGLite extends LiteLLM with support for llama.cpp models using llama-cpp-python. To select a llama.cpp model (e.g., from bartowski's collection), use a model identifier of the form "llama-cpp-python/<hugging_face_repo_id>/<filename>@<n_ctx>", where n_ctx is an optional parameter that specifies the context size of the model.
`RAGLite` 扩展了 `LiteLLM`，通过 `llama-cpp-python` 支持 `llama.cpp` 模型。要选择 `llama.cpp` 模型（例如来自 `bartowski` 的模型集合），请使用形如 `llama-cpp-python/<hugging_face_repo_id>/<filename>@<n_ctx>` 的模型标识符，其中 `n_ctx` 是一个可选参数，用于指定模型的上下文大小。

1. **LLM Model Path Format**:
1. **`LLM` 模型路径格式**：
   ```
   llama-cpp-python/<repo>/<model>/<filename>@<context_length>
   ```
   Example:
   示例：
   ```
   bartowski/Llama-3.2-3B-Instruct-GGUF/Llama-3.2-3B-Instruct-Q4_K_M.gguf@4096
   ```

2. **Embedder Model Path Format**:
2. **嵌入模型路径格式**：
   ```
   llama-cpp-python/<repo>/<model>/<filename>@<dimension>
   ```
   Example:
   示例：
   ```
   lm-kit/bge-m3-gguf/bge-m3-Q4_K_M.gguf@1024
   ```

## Database Setup
## 数据库设置

The application supports multiple database backends:
该应用支持多个数据库后端：

- **PostgreSQL** (Recommended):
- **`PostgreSQL`**（推荐）：
  - Create a free serverless PostgreSQL database at [Neon](https://neon.tech) in a few clicks
  - 只需点击几下，即可在 [Neon](https://neon.tech) 创建免费的无服务器 `PostgreSQL` 数据库
  - Get instant provisioning and scale-to-zero capability
  - 获得即时配置和缩容到零的能力
  - Connection string format: `postgresql://user:pass@ep-xyz.region.aws.neon.tech/dbname`
  - 连接字符串格式：`postgresql://user:pass@ep-xyz.region.aws.neon.tech/dbname`


## How to Run
## 如何运行

1. **Start the Application**:
1. **启动应用**：
   ```bash
   streamlit run local_main.py
   ```

2. **Configure the Application**:
2. **配置应用**：
   - Enter LLM model path
   - 输入 `LLM` 模型路径
   - Enter embedder model path
   - 输入嵌入模型路径
  - Set database URL
  - 设置数据库 `URL`
  - Click "Save Configuration"
   - 点击 `Save Configuration`

3. **Upload Documents**:
3. **上传文档**：
   - Upload PDF files through the interface
   - 通过界面上传 `PDF` 文件
   - Wait for processing completion
   - 等待处理完成

4. **Start Chatting**:
4. **开始聊天**：
   - Ask questions about your documents
   - 针对你的文档提问
   - Get responses using local LLM
   - 使用本地 `LLM` 获取响应
   - Fallback to general knowledge when needed
   - 在需要时回退到通用知识

## Notes
## 注意事项

- Context window size of 4096 is recommended for most use cases
- 对大多数使用场景，建议上下文窗口大小为 `4096`
- Q4_K_M quantization offers good balance of speed and quality
- `Q4_K_M` 量化在速度和质量之间提供了良好平衡
- BGE-M3 embedder with 1024 dimensions is optimal
- 维度为 `1024` 的 `BGE-M3` 嵌入器是较优选择
- Local models require sufficient RAM and CPU/GPU resources
- 本地模型需要足够的 `RAM` 和 `CPU/GPU` 资源
- Metal acceleration available for Mac, CUDA for NVIDIA GPUs
- `Mac` 可使用 `Metal` 加速，`NVIDIA GPU` 可使用 `CUDA`

## Contributing
## 贡献

Contributions are welcome! Please feel free to submit a Pull Request.
欢迎贡献！请随时提交 `Pull Request`。
