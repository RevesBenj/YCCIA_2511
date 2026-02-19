"""
MAINTENANCE REPOSITORY (DAO)
only SQL here for alerts.
"""

from app.infrastructure_persistence.db_manager import DatabaseManager


class MaintenanceRepository:
    def __init__(self) -> None:
        self._db = DatabaseManager.get_instance().connection

    def has_open_alert_for_car(self, car_id: int) -> bool:
        cur = self._db.cursor()
        cur.execute(
            "SELECT 1 FROM maintenance_alerts WHERE car_id=? AND status='OPEN' LIMIT 1",
            (int(car_id),),
        )
        return cur.fetchone() is not None

    def create_alert(self, car_id: int, triggered_mileage: int, message: str) -> int:
        cur = self._db.cursor()
        try:
            cur.execute(
                "INSERT INTO maintenance_alerts (car_id, triggered_mileage, message, status, created_at) "
                "VALUES (?, ?, ?, 'OPEN', datetime('now'))",
                (int(car_id), int(triggered_mileage), message),
            )
            self._db.commit()
            return int(cur.lastrowid)
        except Exception:
            self._db.rollback()
            raise

    def list_open_alerts(self):
        cur = self._db.cursor()
        cur.execute("SELECT * FROM maintenance_alerts WHERE status='OPEN' ORDER BY alert_id DESC")
        return cur.fetchall()

    def close_alerts_for_car(self, car_id: int) -> None:
        cur = self._db.cursor()
        try:
            cur.execute(
                "UPDATE maintenance_alerts SET status='CLOSED', closed_at=datetime('now') "
                "WHERE car_id=? AND status='OPEN'",
                (int(car_id),),
            )
            self._db.commit()
        except Exception:
            self._db.rollback()
            raise
