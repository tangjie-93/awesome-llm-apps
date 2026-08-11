import asyncio
import io
import json
import logging
import os
import re
import shutil
import tempfile
import time
import traceback
import uuid
import zipfile
from typing import Dict, List, Optional

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field

from openai_optimizer import DEFAULT_MODEL, OpenAISkillOptimizer


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MAX_UPLOAD_SIZE = 10 * 1024 * 1024
MAX_FILE_SIZE = 1 * 1024 * 1024
MAX_FILE_COUNT = 50
SESSION_TTL = 3600
ALLOWED_EXTENSIONS = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".py", ".js", ".ts",
    ".html", ".css", ".xml", ".toml", ".cfg", ".ini", ".sh",
}

app = FastAPI(title="Self-Improving Agent Skills OpenAI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions: Dict[str, dict] = {}


class OpenAIKeyMixin(BaseModel):
    """统一承载前端传入的模型和 API Key 配置。"""

    api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    model: Optional[str] = DEFAULT_MODEL

    @property
    def api_key_value(self) -> str:
        """按兼容顺序返回可用的 API Key。"""
        return self.openai_api_key or self.api_key or self.gemini_api_key or ""


class AnalyzeRequest(OpenAIKeyMixin):
    """分析技能时的请求参数。"""

    session_id: str


class RegenerateRequest(OpenAIKeyMixin):
    """重新生成评测配置时的请求参数。"""

    session_id: str


class StartRequest(OpenAIKeyMixin):
    """启动优化任务时的请求参数。"""

    max_rounds: Optional[int] = Field(default=20, gt=0, le=50)


class SessionConfig(BaseModel):
    """前端确认后的场景和评测配置。"""

    session_id: str
    scenarios: List[dict]
    evals: List[dict]


def parse_skill_frontmatter(content: str) -> dict:
    """解析 SKILL.md 顶部的 YAML 风格元数据。"""
    if not content.startswith("---"):
        return {}
    try:
        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}
        metadata = {}
        for line in parts[1].strip().split("\n"):
            # 只处理最简单的 key: value 顶层字段，避免误读多行 YAML 内容。
            if ":" in line and not line.startswith(" "):
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip().strip('"')
        return metadata
    except Exception:
        return {}


def create_session_from_files(skill_files: dict, file_list: list) -> dict:
    """基于上传或示例文件创建一个内存会话。"""
    skill_md = next((content for name, content in skill_files.items() if name.endswith("SKILL.md")), None)
    if not skill_md:
        raise HTTPException(status_code=400, detail="No SKILL.md found")
    metadata = parse_skill_frontmatter(skill_md)
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "skill_files": skill_files,
        "file_list": file_list,
        "metadata": metadata,
        "status": "uploaded",
        "scenarios": None,
        "evals": None,
        "experiments": [],
        "changelog": [],
        "current_skill_md": skill_md,
        "original_skill_md": skill_md,
        "created_at": time.time(),
    }
    return {"session_id": session_id, "file_list": file_list, "metadata": metadata}


def _is_allowed_file(name: str) -> bool:
    """检查文件扩展名是否在允许处理的文本类型范围内。"""
    _, ext = os.path.splitext(name)
    return ext.lower() in ALLOWED_EXTENSIONS


def _is_safe_path(name: str) -> bool:
    """拒绝绝对路径和目录穿越路径，避免写入或读取到技能目录外。"""
    return ".." not in name and not os.path.isabs(name)


def _normalize_uploaded_paths(skill_files: dict, file_list: list) -> tuple[dict, list]:
    """去掉上传文件的共同父目录，让前端看到稳定的相对路径。"""
    if not file_list:
        return skill_files, file_list
    common = os.path.commonpath(file_list)
    if common and common != file_list[0]:
        return (
            {os.path.relpath(name, common): content for name, content in skill_files.items()},
            [os.path.relpath(name, common) for name in file_list],
        )
    return skill_files, file_list


def _build_optimizer(request: OpenAIKeyMixin) -> OpenAISkillOptimizer:
    """根据请求参数或环境变量创建 OpenAI 技能优化器。"""
    api_key = request.api_key_value or os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        raise HTTPException(status_code=400, detail="OpenAI API key is required")
    return OpenAISkillOptimizer(api_key=api_key, model=request.model or DEFAULT_MODEL)


@app.post("/api/upload")
async def upload_skill(file: UploadFile = File(...)):
    """上传 zip 格式技能包并创建优化会话。"""
    if not (file.filename or "").endswith(".zip"):
        raise HTTPException(status_code=400, detail="Only .zip files are accepted")
    content = await file.read()
    if len(content) > MAX_UPLOAD_SIZE:
        raise HTTPException(status_code=413, detail=f"Upload exceeds {MAX_UPLOAD_SIZE // (1024 * 1024)}MB limit")

    try:
        with zipfile.ZipFile(io.BytesIO(content)) as zf:
            skill_files = {}
            file_list = []
            for name in zf.namelist():
                # 跳过目录、系统隐藏文件以及不在白名单内的文件，降低无关内容干扰。
                if name.endswith("/") or name.startswith("__MACOSX") or "/.DS_Store" in name or name.endswith(".DS_Store"):
                    continue
                if not _is_safe_path(name) or not _is_allowed_file(name):
                    continue
                raw = zf.read(name)
                # 单文件过大时直接忽略，避免一次上传占用过多内存。
                if len(raw) > MAX_FILE_SIZE:
                    continue
                if len(file_list) >= MAX_FILE_COUNT:
                    break
                skill_files[name] = raw.decode("utf-8", errors="ignore")
                file_list.append(name)

        skill_files, file_list = _normalize_uploaded_paths(skill_files, file_list)
        return create_session_from_files(skill_files, file_list)
    except zipfile.BadZipFile:
        raise HTTPException(status_code=400, detail="Invalid zip file")
    except HTTPException:
        raise
    except Exception:
        logger.error("Upload error: %s", traceback.format_exc())
        raise HTTPException(status_code=500, detail="Error processing file")


@app.post("/api/upload-files")
async def upload_files(files: List[UploadFile] = File(...)):
    """上传多个散文件并创建优化会话。"""
    if len(files) > MAX_FILE_COUNT:
        raise HTTPException(status_code=413, detail=f"Too many files (max {MAX_FILE_COUNT})")
    skill_files = {}
    file_list = []
    total_size = 0
    for uploaded in files:
        name = uploaded.filename or "unknown"
        # 忽略隐藏文件和系统目录，保留真正参与优化的技能源码。
        if name.startswith(".") or "/.DS_Store" in name or "__MACOSX" in name:
            continue
        if not _is_safe_path(name) or not _is_allowed_file(name):
            continue
        content = await uploaded.read()
        total_size += len(content)
        if total_size > MAX_UPLOAD_SIZE:
            raise HTTPException(status_code=413, detail=f"Total upload exceeds {MAX_UPLOAD_SIZE // (1024 * 1024)}MB limit")
        if len(content) > MAX_FILE_SIZE:
            continue
        skill_files[name] = content.decode("utf-8", errors="ignore")
        file_list.append(name)

    skill_files, file_list = _normalize_uploaded_paths(skill_files, file_list)
    return create_session_from_files(skill_files, file_list)


@app.post("/api/analyze")
async def analyze_skill(request: AnalyzeRequest):
    """分析当前技能，生成可编辑的场景和评测用例。"""
    if request.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[request.session_id]
    try:
        optimizer = _build_optimizer(request)
        analysis = await optimizer.analyze_skill(session["skill_files"])
        session["scenarios"] = analysis["scenarios"]
        session["evals"] = analysis["evals"]
        session["status"] = "analyzed"
        return {"scenarios": analysis["scenarios"], "evals": analysis["evals"]}
    except HTTPException:
        raise
    except Exception:
        logger.error("Analysis error: %s", traceback.format_exc())
        raise HTTPException(status_code=500, detail="Analysis failed. Check your OpenAI API key and try again.")


@app.post("/api/regenerate")
async def regenerate_config(request: RegenerateRequest):
    """复用分析逻辑重新生成场景和评测配置。"""
    return await analyze_skill(AnalyzeRequest(**request.model_dump()))


@app.post("/api/update-config")
async def update_config(config: SessionConfig):
    """保存前端编辑后的场景和评测配置。"""
    if config.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[config.session_id]
    session["scenarios"] = config.scenarios
    session["evals"] = config.evals
    session["status"] = "configured"
    return {"status": "ok"}


@app.get("/api/stream/{session_id}")
async def stream_progress(session_id: str):
    """通过 Server-Sent Events 向前端推送优化进度。"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[session_id]

    async def event_generator():
        """从会话事件队列中持续取出事件并写入 SSE 响应。"""
        if "event_queue" not in session:
            session["event_queue"] = asyncio.Queue()
        queue = session["event_queue"]
        try:
            while True:
                event = await queue.get()
                if event is None:
                    break
                # SSE 每条消息以 data: 开头，并用空行分隔事件。
                yield f"data: {json.dumps(event)}\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            # 客户端断开后删除队列，避免旧连接继续积压事件。
            if "event_queue" in session:
                del session["event_queue"]

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )


@app.post("/api/start/{session_id}")
async def start_optimization(session_id: str, request: StartRequest):
    """启动后台技能优化任务，并立即返回启动状态。"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[session_id]
    if not session.get("scenarios") or not session.get("evals"):
        raise HTTPException(status_code=400, detail="Must configure scenarios and evals first")
    if session.get("status") == "running":
        raise HTTPException(status_code=400, detail="Optimization already running")

    session["status"] = "running"
    session["stop_requested"] = False
    session["event_queue"] = asyncio.Queue()

    async def run_optimization():
        """在后台执行优化循环，并把过程事件同步到会话状态。"""
        try:
            optimizer = _build_optimizer(request)

            async def callback(event):
                """接收优化器回调事件，更新前端需要展示的实验列表。"""
                if "event_queue" in session:
                    await session["event_queue"].put(event)
                if event["type"] == "baseline":
                    # baseline 表示未修改技能前的基准评分。
                    session["experiments"].append({
                        "experiment_id": 0,
                        "pass_rate": event["data"].get("score", 0),
                        "status": "baseline",
                        "per_eval": event["data"].get("per_eval", []),
                    })
                elif event["type"] == "experiment_result":
                    # 每轮实验结果会标记保留或丢弃，供前端绘制历史记录。
                    session["experiments"].append({
                        "experiment_id": event["data"].get("round", len(session["experiments"])),
                        "pass_rate": event["data"].get("score", 0),
                        "status": "keep" if event["data"].get("kept") else "discard",
                        "per_eval": event["data"].get("per_eval", []),
                        "description": event["data"].get("description", ""),
                        "strategy": event["data"].get("strategy", ""),
                    })
                elif event["type"] == "complete":
                    # 完成事件会生成最终结果，并用 None 通知 SSE 流结束。
                    session["status"] = "complete"
                    session["final_result"] = _frontend_result(session, event["data"])
                    session["current_skill_md"] = event["data"].get("improved_skill_md", "")
                    if "event_queue" in session:
                        await session["event_queue"].put(None)

            result = await optimizer.optimize(
                skill_files=session["skill_files"],
                scenarios=session["scenarios"],
                evals=session["evals"],
                max_rounds=request.max_rounds or 20,
                callback=callback,
            )
            if not session.get("final_result"):
                # 兼容优化器没有发送 complete 事件但正常返回结果的情况。
                session["final_result"] = _frontend_result(session, result)
                session["current_skill_md"] = result.get("improved_skill_md", "")
                session["status"] = "complete"
        except Exception as exc:
            logger.error("Optimization error: %s", traceback.format_exc())
            session["status"] = "error"
            session["error"] = str(exc)
            if "event_queue" in session:
                await session["event_queue"].put({"type": "error", "data": {"message": str(exc)}})
                await session["event_queue"].put(None)

    asyncio.create_task(run_optimization())
    return {"status": "started"}


def _frontend_result(session: dict, data: dict) -> dict:
    """把优化器结果转换为前端展示和下载所需的数据结构。"""
    mutation_log = data.get("mutation_log", [])
    return {
        "baseline_score": data.get("baseline_score", 0),
        "final_score": data.get("final_score", 0),
        "improved_skill_md": data.get("improved_skill_md", ""),
        "original_skill_md": session.get("original_skill_md", ""),
        "score_history": data.get("score_history", []),
        "experiments_run": len(mutation_log),
        "kept": sum(1 for item in mutation_log if item.get("kept")),
        "discarded": sum(1 for item in mutation_log if not item.get("kept")),
        "changelog": [
            {
                "description": item.get("description", item.get("diagnosis", "")),
                "reasoning": item.get("diagnosis", ""),
                "status": "keep" if item.get("kept") else "discard",
                "score_before": item.get("score_before", 0),
                "score_after": item.get("score_after", 0),
                "strategy": item.get("strategy_type", ""),
            }
            for item in mutation_log
        ],
        "mutation_log": mutation_log,
        "strategy_stats": data.get("strategy_stats", {}),
    }


@app.post("/api/stop/{session_id}")
async def stop_optimization(session_id: str):
    """标记当前会话停止，并结束前端 SSE 连接。"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[session_id]
    session["stop_requested"] = True
    session["status"] = "stopped"
    if "event_queue" in session:
        await session["event_queue"].put(None)
    return {"status": "stopped"}


@app.get("/api/download/{session_id}")
async def download_skill(session_id: str):
    """把优化后的 SKILL.md 和原始辅助文件重新打包为 zip。"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[session_id]
    if not session.get("current_skill_md"):
        raise HTTPException(status_code=400, detail="No improved skill available")
    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, "improved_skill.zip")
    try:
        with zipfile.ZipFile(zip_path, "w") as zf:
            for filename, content in session["skill_files"].items():
                # 只替换 SKILL.md，其他文件按上传时的内容原样保留。
                zf.writestr(filename, session["current_skill_md"] if filename.endswith("SKILL.md") else content)
            if session.get("final_result"):
                zf.writestr("CHANGELOG.json", json.dumps(session["final_result"]["changelog"], indent=2))
        return FileResponse(zip_path, media_type="application/zip", filename="improved_skill.zip")
    finally:
        # FileResponse 返回后异步清理临时目录，避免下载过程中文件被提前删除。
        asyncio.create_task(cleanup_temp_dir(temp_dir))


async def cleanup_temp_dir(temp_dir: str):
    """延迟删除下载接口创建的临时目录。"""
    await asyncio.sleep(60)
    try:
        shutil.rmtree(temp_dir)
    except Exception:
        pass


@app.get("/api/examples")
async def list_examples():
    """扫描仓库中的示例技能，并返回可加载的示例列表。"""
    examples_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    examples = []
    if os.path.exists(examples_dir):
        for name in sorted(os.listdir(examples_dir)):
            skill_dir = os.path.join(examples_dir, name)
            skill_md_path = os.path.join(skill_dir, "SKILL.md")
            if os.path.isdir(skill_dir) and os.path.exists(skill_md_path):
                # 读取示例技能的 frontmatter，用于在列表中展示名称和说明。
                with open(skill_md_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                metadata = parse_skill_frontmatter(content)
                examples.append({
                    "name": metadata.get("name", name),
                    "description": metadata.get("description", ""),
                    "path": name,
                })
    return {"examples": examples}


@app.post("/api/examples/{example_name}/load")
async def load_example(example_name: str):
    """按示例名称加载仓库内置技能，并创建一个新的优化会话。"""
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", example_name):
        raise HTTPException(status_code=400, detail="Invalid example name")
    examples_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    skill_dir = os.path.realpath(os.path.join(examples_dir, example_name))
    # 双重校验示例目录位于 examples_dir 内，防止路径穿越。
    if not skill_dir.startswith(examples_dir + os.sep):
        raise HTTPException(status_code=400, detail="Invalid example name")
    if not os.path.isdir(skill_dir):
        raise HTTPException(status_code=404, detail="Example skill not found")

    skill_files = {}
    file_list = []
    for root, _, files in os.walk(skill_dir):
        for filename in files:
            if filename.startswith("."):
                continue
            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, skill_dir)
            if not _is_allowed_file(rel_path):
                continue
            # 示例文件已经在本地仓库中，按文本读取后复用统一的会话创建逻辑。
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                skill_files[rel_path] = f.read()
            file_list.append(rel_path)
    return create_session_from_files(skill_files, file_list)


@app.get("/api/status/{session_id}")
async def get_status(session_id: str):
    """查询当前会话状态、实验记录、错误信息和最终结果。"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[session_id]
    return {
        "status": session.get("status", "unknown"),
        "experiments": session.get("experiments", []),
        "error": session.get("error"),
        "final_result": session.get("final_result"),
    }


@app.get("/health")
async def health_check():
    """健康检查接口，用于确认服务进程和 OpenAI 后端类型。"""
    return {"status": "healthy", "provider": "openai"}


async def _cleanup_expired_sessions():
    """定期清理超过 TTL 且不在运行中的内存会话。"""
    while True:
        await asyncio.sleep(300)
        now = time.time()
        # 运行中的会话不清理，避免后台优化任务状态被提前删除。
        expired = [
            sid for sid, session in sessions.items()
            if now - session.get("created_at", now) > SESSION_TTL and session.get("status") != "running"
        ]
        for sid in expired:
            del sessions[sid]
        if expired:
            logger.info("Cleaned up %s expired session(s)", len(expired))


@app.on_event("startup")
async def startup():
    """应用启动后创建会话清理后台任务。"""
    asyncio.create_task(_cleanup_expired_sessions())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8892)
