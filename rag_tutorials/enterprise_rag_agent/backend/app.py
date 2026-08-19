from __future__ import annotations

import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from api.app import create_app
from application.service import EnterpriseRAGService
from core.config import load_config


def build_parser() -> argparse.ArgumentParser:
    """构建命令行参数解析器，统一管理启动、导入和问答入口。"""
    parser = argparse.ArgumentParser(description="Enterprise RAG Agent")
    subparsers = parser.add_subparsers(dest="command")

    ingest = subparsers.add_parser("ingest", help="Ingest a file or directory")
    ingest.add_argument("path", type=str)
    ingest.add_argument("--kb", type=str, default=None)
    ingest.add_argument("--groups", type=str, default=None)

    ask = subparsers.add_parser("ask", help="Ask a question")
    ask.add_argument("question", type=str)
    ask.add_argument("--kb", type=str, default=None)
    ask.add_argument("--groups", type=str, default=None)
    ask.add_argument("--top-k", type=int, default=None)

    search = subparsers.add_parser("search", help="Show retrieved chunks")
    search.add_argument("question", type=str)
    search.add_argument("--kb", type=str, default=None)
    search.add_argument("--groups", type=str, default=None)
    search.add_argument("--top-k", type=int, default=None)

    subparsers.add_parser("stats", help="Show database stats")
    subparsers.add_parser("serve", help="Start the API server")

    return parser


def main() -> None:
    """命令行主入口：按子命令执行导入、检索、问答或启动服务。"""
    load_dotenv()
    config = load_config()
    service = EnterpriseRAGService(config)
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        args.command = "serve"

    if args.command == "ingest":
        result = service.ingest_path(
            Path(args.path),
            knowledge_base=args.kb,
            allowed_groups=_parse_groups(args.groups),
        )
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
        return

    if args.command == "ask":
        result = service.agent.answer(
            args.question,
            knowledge_base=args.kb,
            user_groups=_parse_groups(args.groups),
            top_k=args.top_k,
        )
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
        return

    if args.command == "search":
        results = service.search(
            args.question,
            knowledge_base=args.kb,
            user_groups=_parse_groups(args.groups),
            top_k=args.top_k,
        )
        print(json.dumps([item.to_dict() for item in results], ensure_ascii=False, indent=2))
        return

    if args.command == "stats":
        print(json.dumps(service.stats(), ensure_ascii=False, indent=2))
        return

    if args.command == "serve":
        import uvicorn

        uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)


def _parse_groups(value: str | None) -> list[str] | None:
    """把逗号分隔的组字符串解析成干净的组列表。"""
    if value is None:
        return None
    groups = [item.strip() for item in value.split(",")]
    return [group for group in groups if group]


app = create_app()


if __name__ == "__main__":
    main()
