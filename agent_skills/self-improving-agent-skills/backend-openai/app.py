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
    api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    model: Optional[str] = DEFAULT_MODEL

    @property
    def api_key_value(self) -> str:
        return self.openai_api_key or self.api_key or self.gemini_api_key or ""


class AnalyzeRequest(OpenAIKeyMixin):
    session_id: str


class RegenerateRequest(OpenAIKeyMixin):
    session_id: str


class StartRequest(OpenAIKeyMixin):
    max_rounds: Optional[int] = Field(default=20, gt=0, le=50)


class SessionConfig(BaseModel):
    session_id: str
    scenarios: List[dict]
    evals: List[dict]


def parse_skill_frontmatter(content: str) -> dict:
    if not content.startswith("---"):
        return {}
    try:
        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}
        metadata = {}
        for line in parts[1].strip().split("\n"):
            if ":" in line and not line.startswith(" "):
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip().strip('"')
        return metadata
    except Exception:
        return {}


def create_session_from_files(skill_files: dict, file_list: list) -> dict:
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
    _, ext = os.path.splitext(name)
    return ext.lower() in ALLOWED_EXTENSIONS


def _is_safe_path(name: str) -> bool:
    return ".." not in name and not os.path.isabs(name)


def _normalize_uploaded_paths(skill_files: dict, file_list: list) -> tuple[dict, list]:
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
    api_key = request.api_key_value or os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        raise HTTPException(status_code=400, detail="OpenAI API key is required")
    return OpenAISkillOptimizer(api_key=api_key, model=request.model or DEFAULT_MODEL)


@app.post("/api/upload")
async def upload_skill(file: UploadFile = File(...)):
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
                if name.endswith("/") or name.startswith("__MACOSX") or "/.DS_Store" in name or name.endswith(".DS_Store"):
                    continue
                if not _is_safe_path(name) or not _is_allowed_file(name):
                    continue
                raw = zf.read(name)
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
    if len(files) > MAX_FILE_COUNT:
        raise HTTPException(status_code=413, detail=f"Too many files (max {MAX_FILE_COUNT})")
    skill_files = {}
    file_list = []
    total_size = 0
    for uploaded in files:
        name = uploaded.filename or "unknown"
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
    return await analyze_skill(AnalyzeRequest(**request.model_dump()))


@app.post("/api/update-config")
async def update_config(config: SessionConfig):
    if config.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[config.session_id]
    session["scenarios"] = config.scenarios
    session["evals"] = config.evals
    session["status"] = "configured"
    return {"status": "ok"}


@app.get("/api/stream/{session_id}")
async def stream_progress(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[session_id]

    async def event_generator():
        if "event_queue" not in session:
            session["event_queue"] = asyncio.Queue()
        queue = session["event_queue"]
        try:
            while True:
                event = await queue.get()
                if event is None:
                    break
                yield f"data: {json.dumps(event)}\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            if "event_queue" in session:
                del session["event_queue"]

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )


@app.post("/api/start/{session_id}")
async def start_optimization(session_id: str, request: StartRequest):
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
        try:
            optimizer = _build_optimizer(request)

            async def callback(event):
                if "event_queue" in session:
                    await session["event_queue"].put(event)
                if event["type"] == "baseline":
                    session["experiments"].append({
                        "experiment_id": 0,
                        "pass_rate": event["data"].get("score", 0),
                        "status": "baseline",
                        "per_eval": event["data"].get("per_eval", []),
                    })
                elif event["type"] == "experiment_result":
                    session["experiments"].append({
                        "experiment_id": event["data"].get("round", len(session["experiments"])),
                        "pass_rate": event["data"].get("score", 0),
                        "status": "keep" if event["data"].get("kept") else "discard",
                        "per_eval": event["data"].get("per_eval", []),
                        "description": event["data"].get("description", ""),
                        "strategy": event["data"].get("strategy", ""),
                    })
                elif event["type"] == "complete":
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
                zf.writestr(filename, session["current_skill_md"] if filename.endswith("SKILL.md") else content)
            if session.get("final_result"):
                zf.writestr("CHANGELOG.json", json.dumps(session["final_result"]["changelog"], indent=2))
        return FileResponse(zip_path, media_type="application/zip", filename="improved_skill.zip")
    finally:
        asyncio.create_task(cleanup_temp_dir(temp_dir))


async def cleanup_temp_dir(temp_dir: str):
    await asyncio.sleep(60)
    try:
        shutil.rmtree(temp_dir)
    except Exception:
        pass


@app.get("/api/examples")
async def list_examples():
    examples_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    examples = []
    if os.path.exists(examples_dir):
        for name in sorted(os.listdir(examples_dir)):
            skill_dir = os.path.join(examples_dir, name)
            skill_md_path = os.path.join(skill_dir, "SKILL.md")
            if os.path.isdir(skill_dir) and os.path.exists(skill_md_path):
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
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", example_name):
        raise HTTPException(status_code=400, detail="Invalid example name")
    examples_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    skill_dir = os.path.realpath(os.path.join(examples_dir, example_name))
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
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                skill_files[rel_path] = f.read()
            file_list.append(rel_path)
    return create_session_from_files(skill_files, file_list)


@app.get("/api/status/{session_id}")
async def get_status(session_id: str):
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
    return {"status": "healthy", "provider": "openai"}


async def _cleanup_expired_sessions():
    while True:
        await asyncio.sleep(300)
        now = time.time()
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
    asyncio.create_task(_cleanup_expired_sessions())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8892)
