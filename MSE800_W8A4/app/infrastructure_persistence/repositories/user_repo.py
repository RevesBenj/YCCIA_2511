"""
USER REPOSITORY (DAO)
only SQL here for users.
"""

from app.infrastructure_persistence.db_manager import DatabaseManager


class UserRepository:
    def __init__(self) -> None:
        self._db = DatabaseManager.get_instance().connection

    def find_by_email(self, email: str):
        cur = self._db.cursor()
        cur.execute("SELECT * FROM users WHERE email=?", (email,))
        return cur.fetchone()

    def get_by_id(self, user_id: int):
        cur = self._db.cursor()
        cur.execute("SELECT * FROM users WHERE user_id=?", (int(user_id),))
        return cur.fetchone()

    def list_customers(self):
        # return all customers only, for admin
        cur = self._db.cursor()
        cur.execute(
            "SELECT user_id, name, email, loyalty_points, created_at "
            "FROM users WHERE role='CUSTOMER' ORDER BY user_id"
        )
        return cur.fetchall()

    def create_user(self, name: str, email: str, password_hash: str, role: str) -> int:
        cur = self._db.cursor()
        try:
            cur.execute(
                "INSERT INTO users (name, email, password_hash, role, loyalty_points, created_at) "
                "VALUES (?, ?, ?, ?, 0, datetime('now'))",
                (name, email, password_hash, role),
            )
            self._db.commit()
            return int(cur.lastrowid)
        except Exception:
            self._db.rollback()
            raise

    def update_loyalty_points(self, user_id: int, new_points: int) -> None:
        cur = self._db.cursor()
        try:
            cur.execute(
                "UPDATE users SET loyalty_points=? WHERE user_id=?",
                (int(new_points), int(user_id)),
            )
            self._db.commit()
        except Exception:
            self._db.rollback()
            raise
