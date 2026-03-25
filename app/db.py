import sqlite3
from datetime import datetime, timezone
from pathlib import Path


class MemoryStore:
    def __init__(self, db_path: str = "/app/data/memory.db") -> None:
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                user_id TEXT PRIMARY KEY,
                rolling_summary TEXT DEFAULT '',
                updated_at TEXT NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                token_estimate INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()

    def ensure_session(self, user_id: str) -> None:
        self.conn.execute(
            """
            INSERT INTO sessions(user_id, rolling_summary, updated_at)
            VALUES(?, '', ?)
            ON CONFLICT(user_id) DO UPDATE SET updated_at=excluded.updated_at
            """,
            (user_id, self._now()),
        )
        self.conn.commit()

    def get_summary(self, user_id: str) -> str:
        row = self.conn.execute(
            "SELECT rolling_summary FROM sessions WHERE user_id=?",
            (user_id,),
        ).fetchone()
        return row["rolling_summary"] if row else ""

    def update_summary(self, user_id: str, summary: str) -> None:
        self.conn.execute(
            "UPDATE sessions SET rolling_summary=?, updated_at=? WHERE user_id=?",
            (summary, self._now(), user_id),
        )
        self.conn.commit()

    def add_message(self, user_id: str, role: str, content: str, token_estimate: int) -> None:
        self.conn.execute(
            """
            INSERT INTO messages(user_id, role, content, token_estimate, created_at)
            VALUES(?, ?, ?, ?, ?)
            """,
            (user_id, role, content, token_estimate, self._now()),
        )
        self.conn.commit()

    def list_messages(self, user_id: str) -> list[dict]:
        rows = self.conn.execute(
            """
            SELECT id, role, content, token_estimate, created_at
            FROM messages
            WHERE user_id=?
            ORDER BY id ASC
            """,
            (user_id,),
        ).fetchall()
        return [dict(row) for row in rows]

    def replace_with_compacted(self, user_id: str, kept_message_ids: list[int]) -> None:
        if not kept_message_ids:
            self.conn.execute("DELETE FROM messages WHERE user_id=?", (user_id,))
        else:
            placeholders = ",".join("?" for _ in kept_message_ids)
            params = [user_id, *kept_message_ids]
            self.conn.execute(
                f"DELETE FROM messages WHERE user_id=? AND id NOT IN ({placeholders})",
                params,
            )
        self.conn.commit()
