import sqlite3
import json
from pathlib import Path
from datetime import datetime, timezone

class MemoryStore:
    def __init__(self, path="data/researchpilot.db"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                """CREATE TABLE IF NOT EXISTS searches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    query TEXT NOT NULL,
                    result_json TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )"""
            )

    def save(self, query, result):
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                "INSERT INTO searches(query,result_json,created_at) VALUES(?,?,?)",
                (
                    query,
                    json.dumps(result),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )

    def recent(self, limit=5):
        with sqlite3.connect(self.path) as connection:
            rows = connection.execute(
                "SELECT query,result_json,created_at "
                "FROM searches ORDER BY id DESC LIMIT ?",
                (limit,),
            ).fetchall()

        return [
            {"query": q, "result": json.loads(r), "created_at": created}
            for q, r, created in rows
        ]
