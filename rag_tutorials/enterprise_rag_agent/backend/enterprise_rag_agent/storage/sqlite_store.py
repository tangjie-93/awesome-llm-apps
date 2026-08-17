from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from ..core.models import ChunkRecord, SourceDocument


class SQLiteRAGStore:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS documents (
                        source_id TEXT PRIMARY KEY,
                        knowledge_base TEXT NOT NULL,
                        path TEXT NOT NULL,
                        title TEXT NOT NULL,
                        content_type TEXT NOT NULL,
                        content_hash TEXT NOT NULL DEFAULT '',
                        version TEXT NOT NULL,
                        allowed_groups TEXT NOT NULL,
                        risk_level TEXT NOT NULL DEFAULT 'low',
                        metadata TEXT NOT NULL,
                        content TEXT NOT NULL,
                        indexed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS chunks (
                        chunk_id TEXT PRIMARY KEY,
                        source_id TEXT NOT NULL,
                        knowledge_base TEXT NOT NULL,
                        path TEXT NOT NULL,
                        title TEXT NOT NULL,
                        section_path TEXT NOT NULL,
                        chunk_index INTEGER NOT NULL,
                        text TEXT NOT NULL,
                        token_count INTEGER NOT NULL,
                        embedding TEXT NOT NULL DEFAULT '[]',
                        allowed_groups TEXT NOT NULL,
                        risk_level TEXT NOT NULL DEFAULT 'low',
                        metadata TEXT NOT NULL,
                        FOREIGN KEY(source_id) REFERENCES documents(source_id)
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS answer_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        question TEXT NOT NULL,
                        answer TEXT NOT NULL,
                        confidence REAL NOT NULL,
                        citations TEXT NOT NULL,
                        metadata TEXT NOT NULL,
                        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS evaluation_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        question TEXT NOT NULL,
                        expected_answer TEXT,
                        actual_answer TEXT NOT NULL,
                        score REAL NOT NULL,
                        notes TEXT NOT NULL,
                        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS operation_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        operation TEXT NOT NULL,
                        status TEXT NOT NULL,
                        path TEXT,
                        knowledge_base TEXT,
                        allowed_groups TEXT NOT NULL,
                        detail TEXT NOT NULL,
                        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                self._ensure_column(connection, "documents", "content_hash", "TEXT NOT NULL DEFAULT ''")
                self._ensure_column(connection, "documents", "risk_level", "TEXT NOT NULL DEFAULT 'low'")
                self._ensure_column(connection, "documents", "indexed_at", "TEXT NOT NULL DEFAULT ''")
                self._ensure_column(connection, "chunks", "embedding", "TEXT NOT NULL DEFAULT '[]'")
                self._ensure_column(connection, "chunks", "risk_level", "TEXT NOT NULL DEFAULT 'low'")
                connection.execute("CREATE INDEX IF NOT EXISTS idx_chunks_kb ON chunks(knowledge_base)")
                connection.execute("CREATE INDEX IF NOT EXISTS idx_chunks_source ON chunks(source_id)")
                connection.execute("CREATE INDEX IF NOT EXISTS idx_docs_kb ON documents(knowledge_base)")
                connection.execute(
                    "CREATE INDEX IF NOT EXISTS idx_docs_content_hash ON documents(content_hash)"
                )
        finally:
            connection.close()

    def _ensure_column(
        self,
        connection: sqlite3.Connection,
        table: str,
        column: str,
        definition: str,
    ) -> None:
        rows = connection.execute(f"PRAGMA table_info({table})").fetchall()
        if column not in {row["name"] for row in rows}:
            connection.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")

    def replace_document(self, document: SourceDocument, chunks: list[ChunkRecord]) -> None:
        connection = self._connect()
        try:
            with connection:
                connection.execute("DELETE FROM chunks WHERE source_id = ?", (document.source_id,))
                connection.execute("DELETE FROM documents WHERE source_id = ?", (document.source_id,))
                connection.execute(
                    """
                    INSERT INTO documents
                    (source_id, knowledge_base, path, title, content_type, content_hash, version, allowed_groups, risk_level, metadata, content)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        document.source_id,
                        document.knowledge_base,
                        document.path,
                        document.title,
                        document.content_type,
                        document.content_hash,
                        document.version,
                        json.dumps(document.allowed_groups, ensure_ascii=False),
                        document.risk_level,
                        json.dumps(document.metadata, ensure_ascii=False),
                        document.content,
                    ),
                )
                connection.executemany(
                    """
                    INSERT INTO chunks
                    (chunk_id, source_id, knowledge_base, path, title, section_path, chunk_index, text, token_count, embedding, allowed_groups, risk_level, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    [
                        (
                            chunk.chunk_id,
                            chunk.source_id,
                            chunk.knowledge_base,
                            chunk.path,
                            chunk.title,
                            chunk.section_path,
                            chunk.chunk_index,
                            chunk.text,
                            chunk.token_count,
                            json.dumps(chunk.embedding),
                            json.dumps(chunk.allowed_groups, ensure_ascii=False),
                            chunk.risk_level,
                            json.dumps(chunk.metadata, ensure_ascii=False),
                        )
                        for chunk in chunks
                    ],
                )
        finally:
            connection.close()

    def delete_document(self, source_id: str) -> bool:
        connection = self._connect()
        try:
            with connection:
                connection.execute("DELETE FROM chunks WHERE source_id = ?", (source_id,))
                cursor = connection.execute("DELETE FROM documents WHERE source_id = ?", (source_id,))
        finally:
            connection.close()
        return cursor.rowcount > 0

    def prune_documents_under_path(
        self,
        root_path: Path,
        keep_source_ids: set[str],
        knowledge_base: str | None = None,
    ) -> int:
        root = str(root_path.resolve())
        query = "SELECT source_id, path FROM documents"
        params: tuple[object, ...] = ()
        if knowledge_base:
            query += " WHERE knowledge_base = ?"
            params = (knowledge_base,)

        connection = self._connect()
        try:
            rows = connection.execute(query, params).fetchall()
            stale_source_ids = [
                row["source_id"]
                for row in rows
                if row["source_id"] not in keep_source_ids and self._is_under_path(row["path"], root)
            ]
            with connection:
                for source_id in stale_source_ids:
                    connection.execute("DELETE FROM chunks WHERE source_id = ?", (source_id,))
                    connection.execute("DELETE FROM documents WHERE source_id = ?", (source_id,))
        finally:
            connection.close()
        return len(stale_source_ids)

    def _is_under_path(self, value: str, root: str) -> bool:
        try:
            Path(value).resolve().relative_to(root)
        except ValueError:
            return False
        return True

    def load_chunks(self, knowledge_bases: list[str] | None = None) -> list[ChunkRecord]:
        query = """
            SELECT chunk_id, source_id, knowledge_base, path, title, section_path,
                   chunk_index, text, token_count, embedding, allowed_groups, risk_level, metadata
            FROM chunks
        """
        params: tuple[object, ...] = ()
        if knowledge_bases:
            placeholders = ",".join("?" for _ in knowledge_bases)
            query += f" WHERE knowledge_base IN ({placeholders})"
            params = tuple(knowledge_bases)
        query += " ORDER BY knowledge_base, path, chunk_index"
        connection = self._connect()
        try:
            rows = connection.execute(query, params).fetchall()
        finally:
            connection.close()
        return [
            ChunkRecord(
                chunk_id=row["chunk_id"],
                source_id=row["source_id"],
                knowledge_base=row["knowledge_base"],
                path=row["path"],
                title=row["title"],
                section_path=row["section_path"],
                chunk_index=row["chunk_index"],
                text=row["text"],
                token_count=row["token_count"],
                embedding=json.loads(row["embedding"]),
                allowed_groups=tuple(json.loads(row["allowed_groups"])),
                risk_level=row["risk_level"],
                metadata=json.loads(row["metadata"]),
            )
            for row in rows
        ]

    def list_documents(self, knowledge_base: str | None = None) -> list[dict[str, object]]:
        query = """
            SELECT source_id, knowledge_base, path, title, content_type, content_hash, version, allowed_groups, risk_level, metadata, indexed_at
            FROM documents
        """
        params: tuple[object, ...] = ()
        if knowledge_base:
            query += " WHERE knowledge_base = ?"
            params = (knowledge_base,)
        query += " ORDER BY knowledge_base, path"
        connection = self._connect()
        try:
            rows = connection.execute(query, params).fetchall()
        finally:
            connection.close()
        return [
            {
                "source_id": row["source_id"],
                "knowledge_base": row["knowledge_base"],
                "path": row["path"],
                "title": row["title"],
                "content_type": row["content_type"],
                "content_hash": row["content_hash"],
                "version": row["version"],
                "allowed_groups": json.loads(row["allowed_groups"]),
                "risk_level": row["risk_level"],
                "metadata": json.loads(row["metadata"]),
                "indexed_at": row["indexed_at"],
            }
            for row in rows
        ]

    def get_document(self, source_id: str) -> dict[str, object] | None:
        connection = self._connect()
        try:
            row = connection.execute(
                """
                SELECT source_id, knowledge_base, path, title, content_type,
                       content_hash, version, allowed_groups, risk_level, metadata, indexed_at
                FROM documents
                WHERE source_id = ?
                """,
                (source_id,),
            ).fetchone()
        finally:
            connection.close()
        return self._document_row_to_dict(row) if row else None

    def find_duplicate_document(
        self,
        content_hash: str,
        exclude_source_id: str,
    ) -> dict[str, object] | None:
        connection = self._connect()
        try:
            row = connection.execute(
                """
                SELECT source_id, knowledge_base, path, title, content_type,
                       content_hash, version, allowed_groups, risk_level, metadata, indexed_at
                FROM documents
                WHERE content_hash = ? AND source_id != ?
                ORDER BY knowledge_base, path
                LIMIT 1
                """,
                (content_hash, exclude_source_id),
            ).fetchone()
        finally:
            connection.close()
        return self._document_row_to_dict(row) if row else None

    def _document_row_to_dict(self, row: sqlite3.Row) -> dict[str, object]:
        return {
            "source_id": row["source_id"],
            "knowledge_base": row["knowledge_base"],
            "path": row["path"],
            "title": row["title"],
            "content_type": row["content_type"],
            "content_hash": row["content_hash"],
            "version": row["version"],
            "allowed_groups": json.loads(row["allowed_groups"]),
            "risk_level": row["risk_level"],
            "metadata": json.loads(row["metadata"]),
            "indexed_at": row["indexed_at"],
        }

    def list_knowledge_bases(self) -> list[str]:
        connection = self._connect()
        try:
            rows = connection.execute(
                "SELECT DISTINCT knowledge_base FROM documents ORDER BY knowledge_base"
            ).fetchall()
        finally:
            connection.close()
        return [row["knowledge_base"] for row in rows]

    def stats(self) -> dict[str, int]:
        connection = self._connect()
        try:
            documents = connection.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
            chunks = connection.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
            answer_logs = connection.execute("SELECT COUNT(*) FROM answer_logs").fetchone()[0]
            evaluation_logs = connection.execute("SELECT COUNT(*) FROM evaluation_logs").fetchone()[0]
            operation_logs = connection.execute("SELECT COUNT(*) FROM operation_logs").fetchone()[0]
        finally:
            connection.close()
        return {
            "documents": documents,
            "chunks": chunks,
            "answer_logs": answer_logs,
            "evaluation_logs": evaluation_logs,
            "operation_logs": operation_logs,
        }

    def log_answer(
        self,
        question: str,
        answer: str,
        confidence: float,
        citations: list[dict[str, object]],
        metadata: dict[str, object],
    ) -> None:
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    """
                    INSERT INTO answer_logs (question, answer, confidence, citations, metadata)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        question,
                        answer,
                        confidence,
                        json.dumps(citations, ensure_ascii=False),
                        json.dumps(metadata, ensure_ascii=False),
                    ),
                )
        finally:
            connection.close()

    def log_evaluation(self, question: str, expected_answer: str | None, actual_answer: str, score: float, notes: str) -> None:
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    """
                    INSERT INTO evaluation_logs (question, expected_answer, actual_answer, score, notes)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (question, expected_answer, actual_answer, score, notes),
                )
        finally:
            connection.close()

    def log_operation(
        self,
        operation: str,
        status: str,
        path: str | None,
        knowledge_base: str | None,
        allowed_groups: list[str] | None,
        detail: dict[str, object],
    ) -> None:
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    """
                    INSERT INTO operation_logs (operation, status, path, knowledge_base, allowed_groups, detail)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        operation,
                        status,
                        path,
                        knowledge_base,
                        json.dumps(allowed_groups or [], ensure_ascii=False),
                        json.dumps(detail, ensure_ascii=False),
                    ),
                )
        finally:
            connection.close()

    def list_answer_logs(self) -> list[dict[str, object]]:
        connection = self._connect()
        try:
            rows = connection.execute(
                """
                SELECT id, question, answer, confidence, citations, metadata, created_at
                FROM answer_logs
                ORDER BY id DESC
                """
            ).fetchall()
        finally:
            connection.close()
        return [
            {
                "id": row["id"],
                "question": row["question"],
                "answer": row["answer"],
                "confidence": row["confidence"],
                "citations": json.loads(row["citations"]),
                "metadata": json.loads(row["metadata"]),
                "created_at": row["created_at"],
            }
            for row in rows
        ]

    def list_evaluation_logs(self) -> list[dict[str, object]]:
        connection = self._connect()
        try:
            rows = connection.execute(
                """
                SELECT id, question, expected_answer, actual_answer, score, notes, created_at
                FROM evaluation_logs
                ORDER BY id DESC
                """
            ).fetchall()
        finally:
            connection.close()
        return [
            {
                "id": row["id"],
                "question": row["question"],
                "expected_answer": row["expected_answer"],
                "actual_answer": row["actual_answer"],
                "score": row["score"],
                "notes": row["notes"],
                "created_at": row["created_at"],
            }
            for row in rows
        ]

    def list_operation_logs(self) -> list[dict[str, object]]:
        connection = self._connect()
        try:
            rows = connection.execute(
                """
                SELECT id, operation, status, path, knowledge_base, allowed_groups, detail, created_at
                FROM operation_logs
                ORDER BY id DESC
                """
            ).fetchall()
        finally:
            connection.close()
        return [
            {
                "id": row["id"],
                "operation": row["operation"],
                "status": row["status"],
                "path": row["path"],
                "knowledge_base": row["knowledge_base"],
                "allowed_groups": json.loads(row["allowed_groups"]),
                "detail": json.loads(row["detail"]),
                "created_at": row["created_at"],
            }
            for row in rows
        ]
