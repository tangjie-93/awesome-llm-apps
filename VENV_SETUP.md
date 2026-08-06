# Python 虚拟环境使用指令

项目根目录：

```text
D:\study\awesome-llm-apps
```

macOS/Linux 用户需要把路径替换为自己本机的项目路径。

## Windows PowerShell

### 1. 进入项目根目录

```powershell
cd D:\study\awesome-llm-apps
```

### 2. 创建虚拟环境

```powershell
python -m venv .venv
```

如果 `.venv` 已经存在，可以跳过这一步。

### 3. 激活虚拟环境

```powershell
.\.venv\Scripts\Activate.ps1
```

激活成功后，命令行前面通常会出现：

```powershell
(.venv)
```

如果 PowerShell 提示脚本执行策略不允许运行，执行：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

然后重新激活：

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. 验证 Python 路径

```powershell
python --version
where python
```

`where python` 的第一行应该类似：

```powershell
D:\study\awesome-llm-apps\.venv\Scripts\python.exe
```

### 5. 安装当前教程依赖

```powershell
pip install -r ai_agent_framework_crash_course\openai_sdk_crash_course\1_starter_agent\requirements.txt
```

### 6. 配置 OpenAI API Key

```powershell
cd D:\study\awesome-llm-apps\ai_agent_framework_crash_course\openai_sdk_crash_course\1_starter_agent
Copy-Item env.example .env
```

然后打开 `.env`，填入：

```text
OPENAI_API_KEY=你的_API_Key
```

### 7. 运行 Streamlit 应用

```powershell
streamlit run app.py
```

### 8. 测试个人助理 Agent

```powershell
cd D:\study\awesome-llm-apps\ai_agent_framework_crash_course\openai_sdk_crash_course\1_starter_agent\1_personal_assistant_agent
python
```

进入 Python 交互环境后执行：

```python
from agent import sync_example

print(sync_example())
```

### 9. 退出虚拟环境

```powershell
deactivate
```

## Windows Git Bash

如果终端提示符里有 `MINGW64`，说明你正在使用 Git Bash。此时虚拟环境仍然是 Windows 结构，目录是 `.venv/Scripts`，但激活方式要使用 Bash 的 `source`。

### 1. 进入项目根目录

```bash
cd /d/study/awesome-llm-apps
```

### 2. 创建虚拟环境

```bash
python -m venv .venv
```

如果 `.venv` 已经存在，可以跳过这一步。

### 3. 激活虚拟环境

```bash
source .venv/Scripts/activate
```

不要使用下面两个命令：

```bash
.\.venv\Scripts\Activate.ps1
source .venv/bin/activate
```

原因：

- `.\.venv\Scripts\Activate.ps1` 是 PowerShell 命令，Git Bash 不能直接执行。
- `.venv/bin/activate` 是 macOS/Linux 虚拟环境路径，Windows venv 没有这个目录。

### 4. 验证 Python 路径

```bash
python --version
which python
```

`which python` 的输出应该类似：

```bash
/d/study/awesome-llm-apps/.venv/Scripts/python
```

### 5. 安装当前教程依赖

```bash
pip install -r ai_agent_framework_crash_course/openai_sdk_crash_course/1_starter_agent/requirements.txt
```

### 6. 配置 OpenAI API Key

```bash
cd /d/study/awesome-llm-apps/ai_agent_framework_crash_course/openai_sdk_crash_course/1_starter_agent
cp env.example .env
```

然后打开 `.env`，填入：

```text
OPENAI_API_KEY=你的_API_Key
```

### 7. 运行 Streamlit 应用

```bash
streamlit run app.py
```

### 8. 退出虚拟环境

```bash
deactivate
```

## macOS/Linux

### 1. 进入项目根目录

把下面路径替换为你的项目实际路径：

```bash
cd /path/to/awesome-llm-apps
```

### 2. 创建虚拟环境

```bash
python3 -m venv .venv
```

如果 `.venv` 已经存在，可以跳过这一步。

### 3. 激活虚拟环境

```bash
source .venv/bin/activate
```

激活成功后，命令行前面通常会出现：

```bash
(.venv)
```

### 4. 验证 Python 路径

```bash
python --version
which python
```

`which python` 的输出应该类似：

```bash
/path/to/awesome-llm-apps/.venv/bin/python
```

### 5. 安装当前教程依赖

```bash
pip install -r ai_agent_framework_crash_course/openai_sdk_crash_course/1_starter_agent/requirements.txt
```

### 6. 配置 OpenAI API Key

```bash
cd /path/to/awesome-llm-apps/ai_agent_framework_crash_course/openai_sdk_crash_course/1_starter_agent
cp env.example .env
```

然后打开 `.env`，填入：

```text
OPENAI_API_KEY=你的_API_Key
```

### 7. 运行 Streamlit 应用

```bash
streamlit run app.py
```

### 8. 测试个人助理 Agent

```bash
cd /path/to/awesome-llm-apps/ai_agent_framework_crash_course/openai_sdk_crash_course/1_starter_agent/1_personal_assistant_agent
python
```

进入 Python 交互环境后执行：

```python
from agent import sync_example

print(sync_example())
```

### 9. 退出虚拟环境

```bash
deactivate
```

## Git 忽略说明

根目录 `.gitignore` 已配置：

```gitignore
.venv/
env
env/
```

所以虚拟环境目录和任意目录下名为 `env` 的文件或文件夹不会被提交。
