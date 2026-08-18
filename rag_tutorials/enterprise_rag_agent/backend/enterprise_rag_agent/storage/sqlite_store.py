from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timedelta, timezone
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
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS audit_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actor_id TEXT NOT NULL,
                        action TEXT NOT NULL,
                        resource TEXT NOT NULL,
                        detail TEXT NOT NULL,
                        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS usage_events (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actor_id TEXT NOT NULL,
                        event_type TEXT NOT NULL,
                        endpoint TEXT NOT NULL,
                        input_tokens INTEGER NOT NULL DEFAULT 0,
                        output_tokens INTEGER NOT NULL DEFAULT 0,
                        model_calls INTEGER NOT NULL DEFAULT 0,
                        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        external_id TEXT NOT NULL UNIQUE,
                        display_name TEXT NOT NULL,
                        email TEXT,
                        groups TEXT NOT NULL DEFAULT '[]',
                        is_active INTEGER NOT NULL DEFAULT 1,
                        metadata TEXT NOT NULL DEFAULT '{}',
                        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        last_seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS roles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE,
                        description TEXT NOT NULL DEFAULT '',
                        permissions TEXT NOT NULL DEFAULT '[]',
                        is_system INTEGER NOT NULL DEFAULT 0,
                        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS user_roles (
                        user_id INTEGER NOT NULL,
                        role_id INTEGER NOT NULL,
                        PRIMARY KEY (user_id, role_id),
                        FOREIGN KEY(user_id) REFERENCES users(id),
                        FOREIGN KEY(role_id) REFERENCES roles(id)
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actor_id TEXT NOT NULL,
                        answer_log_id INTEGER,
                        rating INTEGER NOT NULL,
                        comment TEXT NOT NULL DEFAULT '',
                        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                default_roles = (
                    ("admin", "系统管理员", ["manage_users", "manage_roles", "manage_audit"]),
                    ("editor", "知识库编辑者", ["manage_documents", "run_ingest"]),
                    ("viewer", "只读用户", ["read_documents", "ask_questions"]),
                    ("auditor", "审计查看者", ["read_audit"]),
                )
                connection.executemany(
                    """
                    INSERT OR IGNORE INTO roles (name, description, permissions, is_system)
                    VALUES (?, ?, ?, 1)
                    """,
                    [
                        (name, description, json.dumps(permissions, ensure_ascii=False))
                        for name, description, permissions in default_roles
                    ],
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

    def get_operation_log(self, operation_id: int) -> dict[str, object] | None:
        connection = self._connect()
        try:
            row = connection.execute(
                """
                SELECT id, operation, status, path, knowledge_base, allowed_groups, detail, created_at
                FROM operation_logs
                WHERE id = ?
                """,
                (operation_id,),
            ).fetchone()
        finally:
            connection.close()
        if not row:
            return None
        return {
            "id": row["id"],
            "operation": row["operation"],
            "status": row["status"],
            "path": row["path"],
            "knowledge_base": row["knowledge_base"],
            "allowed_groups": json.loads(row["allowed_groups"]),
            "detail": json.loads(row["detail"]),
            "created_at": row["created_at"],
        }

    def log_audit(self, actor_id: str, action: str, resource: str, detail: dict[str, object]) -> None:
        """记录需要管理员追踪的业务动作。"""
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    "INSERT INTO audit_logs (actor_id, action, resource, detail) VALUES (?, ?, ?, ?)",
                    (actor_id, action, resource, json.dumps(detail, ensure_ascii=False)),
                )
        finally:
            connection.close()

    def list_audit_logs(self, limit: int = 500) -> list[dict[str, object]]:
        connection = self._connect()
        try:
            rows = connection.execute(
                "SELECT id, actor_id, action, resource, detail, created_at FROM audit_logs ORDER BY id DESC LIMIT ?",
                (limit,),
            ).fetchall()
        finally:
            connection.close()
        return [
            {
                "id": row["id"],
                "actor_id": row["actor_id"],
                "action": row["action"],
                "resource": row["resource"],
                "detail": json.loads(row["detail"]),
                "created_at": row["created_at"],
            }
            for row in rows
        ]

    def delete_audit_logs(self, before: str | None = None) -> int:
        connection = self._connect()
        try:
            with connection:
                if before:
                    cursor = connection.execute("DELETE FROM audit_logs WHERE created_at < ?", (before,))
                else:
                    cursor = connection.execute("DELETE FROM audit_logs")
        finally:
            connection.close()
        return cursor.rowcount

    def purge_audit_logs(self, retention_days: int) -> int:
        cutoff = (datetime.now(timezone.utc) - timedelta(days=retention_days)).strftime("%Y-%m-%d %H:%M:%S")
        return self.delete_audit_logs(cutoff)

    def log_usage(
        self,
        actor_id: str,
        event_type: str,
        endpoint: str,
        input_tokens: int = 0,
        output_tokens: int = 0,
        model_calls: int = 0,
    ) -> None:
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    """
                    INSERT INTO usage_events
                    (actor_id, event_type, endpoint, input_tokens, output_tokens, model_calls)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (actor_id, event_type, endpoint, input_tokens, output_tokens, model_calls),
                )
        finally:
            connection.close()

    def usage_stats(self) -> dict[str, int]:
        connection = self._connect()
        try:
            row = connection.execute(
                """
                SELECT COALESCE(SUM(CASE WHEN event_type = 'request' THEN 1 ELSE 0 END), 0) AS requests,
                       COALESCE(SUM(input_tokens + output_tokens), 0) AS tokens,
                       COALESCE(SUM(model_calls), 0) AS model_calls
                FROM usage_events
                """
            ).fetchone()
        finally:
            connection.close()
        model_row = self._connect()
        try:
            calls = model_row.execute("SELECT COALESCE(SUM(model_calls), 0) FROM usage_events").fetchone()[0]
        finally:
            model_row.close()
        return {"requests": int(row["requests"]), "tokens": int(row["tokens"]), "model_calls": int(calls)}

    def upsert_user_profile(
        self,
        external_id: str,
        display_name: str,
        email: str | None,
        groups: list[str],
    ) -> dict[str, object]:
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    """
                    INSERT INTO users (external_id, display_name, email, groups)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(external_id) DO UPDATE SET
                        display_name = excluded.display_name,
                        email = excluded.email,
                        groups = excluded.groups,
                        last_seen_at = CURRENT_TIMESTAMP,
                        updated_at = CURRENT_TIMESTAMP
                    """,
                    (external_id, display_name, email, json.dumps(groups, ensure_ascii=False)),
                )
            row = connection.execute(
                "SELECT id, external_id, display_name, email, groups, is_active, metadata, created_at, updated_at, last_seen_at FROM users WHERE external_id = ?",
                (external_id,),
            ).fetchone()
        finally:
            connection.close()
        return self._user_row_to_dict(row)

    def user_role_names(self, user_id: int) -> list[str]:
        connection = self._connect()
        try:
            rows = connection.execute(
                """
                SELECT roles.name
                FROM roles
                JOIN user_roles ON user_roles.role_id = roles.id
                WHERE user_roles.user_id = ?
                ORDER BY roles.name
                """,
                (user_id,),
            ).fetchall()
        finally:
            connection.close()
        return [str(row["name"]) for row in rows]

    def user_permissions(self, user_id: int) -> set[str]:
        connection = self._connect()
        try:
            rows = connection.execute(
                """
                SELECT roles.permissions
                FROM roles
                JOIN user_roles ON user_roles.role_id = roles.id
                WHERE user_roles.user_id = ?
                """,
                (user_id,),
            ).fetchall()
        finally:
            connection.close()
        return {
            permission
            for row in rows
            for permission in json.loads(row["permissions"])
            if isinstance(permission, str) and permission
        }

    def log_feedback(self, actor_id: str, answer_log_id: int | None, rating: int, comment: str) -> dict[str, object]:
        connection = self._connect()
        try:
            with connection:
                cursor = connection.execute(
                    "INSERT INTO feedback (actor_id, answer_log_id, rating, comment) VALUES (?, ?, ?, ?)",
                    (actor_id, answer_log_id, rating, comment),
                )
                feedback_id = cursor.lastrowid
            row = connection.execute(
                "SELECT id, actor_id, answer_log_id, rating, comment, created_at FROM feedback WHERE id = ?",
                (feedback_id,),
            ).fetchone()
        finally:
            connection.close()
        return {
            "id": row["id"],
            "actor_id": row["actor_id"],
            "answer_log_id": row["answer_log_id"],
            "rating": row["rating"],
            "comment": row["comment"],
            "created_at": row["created_at"],
        }

    def feedback_summary(self) -> dict[str, float | int]:
        connection = self._connect()
        try:
            row = connection.execute(
                "SELECT COUNT(*) AS count, COALESCE(AVG(rating), 0) AS average_rating FROM feedback"
            ).fetchone()
        finally:
            connection.close()
        return {"count": int(row["count"]), "average_rating": round(float(row["average_rating"]), 2)}

    def count_low_confidence_answers(self, threshold: float) -> int:
        connection = self._connect()
        try:
            row = connection.execute(
                "SELECT COUNT(*) AS count FROM answer_logs WHERE confidence < ?",
                (threshold,),
            ).fetchone()
        finally:
            connection.close()
        return int(row["count"])

    def list_users(self) -> list[dict[str, object]]:
        connection = self._connect()
        try:
            rows = connection.execute(
                "SELECT id, external_id, display_name, email, groups, is_active, metadata, created_at, updated_at, last_seen_at FROM users ORDER BY display_name, id"
            ).fetchall()
        finally:
            connection.close()
        users = [self._user_row_to_dict(row) for row in rows]
        for user in users:
            user["roles"] = self.user_role_names(int(user["id"]))
        return users

    def create_user(
        self,
        external_id: str,
        display_name: str,
        email: str | None,
        groups: list[str],
        role_ids: list[int],
    ) -> dict[str, object]:
        user = self.upsert_user_profile(external_id, display_name, email, groups)
        self.set_user_roles(int(user["id"]), role_ids)
        return next(item for item in self.list_users() if item["id"] == user["id"])

    def update_user(
        self,
        user_id: int,
        display_name: str,
        email: str | None,
        groups: list[str],
        is_active: bool,
        role_ids: list[int],
    ) -> dict[str, object] | None:
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    """
                    UPDATE users
                    SET display_name = ?, email = ?, groups = ?, is_active = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                    """,
                    (display_name, email, json.dumps(groups, ensure_ascii=False), int(is_active), user_id),
                )
        finally:
            connection.close()
        self.set_user_roles(user_id, role_ids)
        return next((item for item in self.list_users() if item["id"] == user_id), None)

    def delete_user(self, user_id: int) -> bool:
        connection = self._connect()
        try:
            with connection:
                connection.execute("DELETE FROM user_roles WHERE user_id = ?", (user_id,))
                cursor = connection.execute("DELETE FROM users WHERE id = ?", (user_id,))
        finally:
            connection.close()
        return cursor.rowcount > 0

    def set_user_roles(self, user_id: int, role_ids: list[int]) -> None:
        connection = self._connect()
        try:
            with connection:
                connection.execute("DELETE FROM user_roles WHERE user_id = ?", (user_id,))
                connection.executemany(
                    "INSERT OR IGNORE INTO user_roles (user_id, role_id) VALUES (?, ?)",
                    [(user_id, role_id) for role_id in role_ids],
                )
        finally:
            connection.close()

    def list_roles(self) -> list[dict[str, object]]:
        connection = self._connect()
        try:
            rows = connection.execute(
                "SELECT id, name, description, permissions, is_system, created_at, updated_at FROM roles ORDER BY is_system DESC, name"
            ).fetchall()
        finally:
            connection.close()
        return [
            {
                "id": row["id"],
                "name": row["name"],
                "description": row["description"],
                "permissions": json.loads(row["permissions"]),
                "is_system": bool(row["is_system"]),
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
            }
            for row in rows
        ]

    def create_role(self, name: str, description: str, permissions: list[str]) -> dict[str, object]:
        connection = self._connect()
        try:
            with connection:
                cursor = connection.execute(
                    "INSERT INTO roles (name, description, permissions) VALUES (?, ?, ?)",
                    (name, description, json.dumps(permissions, ensure_ascii=False)),
                )
                role_id = cursor.lastrowid
        finally:
            connection.close()
        return next(item for item in self.list_roles() if item["id"] == role_id)

    def update_role(self, role_id: int, name: str, description: str, permissions: list[str]) -> dict[str, object] | None:
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    """
                    UPDATE roles
                    SET name = ?, description = ?, permissions = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                    """,
                    (name, description, json.dumps(permissions, ensure_ascii=False), role_id),
                )
        finally:
            connection.close()
        return next((item for item in self.list_roles() if item["id"] == role_id), None)

    def delete_role(self, role_id: int) -> bool:
        connection = self._connect()
        try:
            with connection:
                system = connection.execute("SELECT is_system FROM roles WHERE id = ?", (role_id,)).fetchone()
                if not system or system["is_system"]:
                    return False
                connection.execute("DELETE FROM user_roles WHERE role_id = ?", (role_id,))
                cursor = connection.execute("DELETE FROM roles WHERE id = ?", (role_id,))
        finally:
            connection.close()
        return cursor.rowcount > 0

    def _user_row_to_dict(self, row: sqlite3.Row) -> dict[str, object]:
        return {
            "id": row["id"],
            "external_id": row["external_id"],
            "display_name": row["display_name"],
            "email": row["email"],
            "groups": json.loads(row["groups"]),
            "is_active": bool(row["is_active"]),
            "metadata": json.loads(row["metadata"]),
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
            "last_seen_at": row["last_seen_at"],
        }
