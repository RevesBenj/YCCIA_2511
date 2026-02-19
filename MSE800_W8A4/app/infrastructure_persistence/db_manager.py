"""
DB MANAGER (Singleton)
Only one DB instance, so stable.
Auto create schema and seed default admin.
"""

from __future__ import annotations

import os
import sqlite3
from datetime import datetime
from typing import Optional

from app.config.logging_config import get_logger
from app.config.settings import (
    DB_PATH,
    DEFAULT_ADMIN_EMAIL,
    DEFAULT_ADMIN_PASSWORD,
    DEFAULT_ADMIN_NAME,
)
from app.infrastructure_persistence.schema import SCHEMA_SQL
from app.infrastructure_persistence.security import hash_password

log = get_logger("db_manager")


class DatabaseManager:
    _instance: Optional["DatabaseManager"] = None

    def __init__(self, db_path: str) -> None:
        self._db_path = db_path
        self._conn = sqlite3.connect(self._db_path)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA foreign_keys = ON")

        self._init_schema()
        self._seed_default_admin()

    @classmethod
    def get_instance(cls, db_path: str = DB_PATH) -> "DatabaseManager":
        if cls._instance is None:
            os.makedirs(os.path.dirname(db_path), exist_ok=True)  # auto create /data
            cls._instance = DatabaseManager(db_path)
            log.info("DB ready at %s", db_path)
        return cls._instance

    @property
    def connection(self) -> sqlite3.Connection:
        return self._conn

    def _init_schema(self) -> None:
        cur = self._conn.cursor()
        cur.executescript(SCHEMA_SQL)
        self._conn.commit()

    def _seed_default_admin(self) -> None:
        cur = self._conn.cursor()
        cur.execute("SELECT 1 FROM users WHERE email=?", (DEFAULT_ADMIN_EMAIL,))
        if cur.fetchone() is None:
            cur.execute(
                "INSERT INTO users (name, email, password_hash, role, loyalty_points, created_at) "
                "VALUES (?, ?, ?, 'ADMIN', 0, ?)",
                (
                    DEFAULT_ADMIN_NAME,
                    DEFAULT_ADMIN_EMAIL,
                    hash_password(DEFAULT_ADMIN_PASSWORD),
                    datetime.utcnow().isoformat(),
                ),
            )
            self._conn.commit()
            log.info("Default admin created (admin@local.com / sysad1$).")
