"""
BOOKING REPOSITORY (DAO)
only SQL here for bookings.
"""

from app.infrastructure_persistence.db_manager import DatabaseManager


class BookingRepository:
    def __init__(self) -> None:
        self._db = DatabaseManager.get_instance().connection

    def has_overlap(self, car_id: int, start_date: str, end_date: str) -> bool:
        # overlap rule: block PENDING and APPROVED bookings
        cur = self._db.cursor()
        cur.execute(
            "SELECT 1 FROM bookings WHERE car_id=? AND status IN ('PENDING','APPROVED') "
            "AND NOT (end_date < ? OR start_date > ?) LIMIT 1",
            (int(car_id), start_date, end_date),
        )
        return cur.fetchone() is not None

    def create_booking(self, booking_data: dict) -> int:
        cur = self._db.cursor()
        try:
            cur.execute(
                "INSERT INTO bookings (customer_id, car_id, start_date, end_date, status, total_fee, estimated_km, "
                "auto_approved, decided_by_admin_id, decided_at, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))",
                (
                    int(booking_data["customer_id"]),
                    int(booking_data["car_id"]),
                    booking_data["start_date"],
                    booking_data["end_date"],
                    booking_data["status"],
                    float(booking_data["total_fee"]),
                    int(booking_data["estimated_km"]),
                    int(booking_data["auto_approved"]),
                    booking_data["decided_by_admin_id"],
                    booking_data["decided_at"],
                ),
            )
            self._db.commit()
            return int(cur.lastrowid)
        except Exception:
            self._db.rollback()
            raise

    def get_by_id(self, booking_id: int):
        cur = self._db.cursor()
        cur.execute("SELECT * FROM bookings WHERE booking_id=?", (int(booking_id),))
        return cur.fetchone()

    def list_by_status(self, status: str):
        cur = self._db.cursor()
        cur.execute("SELECT * FROM bookings WHERE status=? ORDER BY booking_id", (status,))
        return cur.fetchall()

    def list_by_customer(self, customer_id: int):
        cur = self._db.cursor()
        cur.execute(
            "SELECT * FROM bookings WHERE customer_id=? ORDER BY booking_id DESC",
            (int(customer_id),),
        )
        return cur.fetchall()

    def update_status(self, booking_id: int, status: str, admin_id: int | None) -> None:
        cur = self._db.cursor()
        try:
            cur.execute(
                "UPDATE bookings SET status=?, decided_by_admin_id=?, decided_at=datetime('now') WHERE booking_id=?",
                (status, admin_id, int(booking_id)),
            )
            self._db.commit()
        except Exception:
            self._db.rollback()
            raise

    def customer_has_rejection_history(self, customer_id: int) -> bool:
        cur = self._db.cursor()
        cur.execute(
            "SELECT 1 FROM bookings WHERE customer_id=? AND status='REJECTED' LIMIT 1",
            (int(customer_id),),
        )
        return cur.fetchone() is not None

    def car_has_active_bookings(self, car_id: int) -> bool:
        cur = self._db.cursor()
        cur.execute(
            "SELECT 1 FROM bookings WHERE car_id=? AND status IN ('PENDING','APPROVED') LIMIT 1",
            (int(car_id),),
        )
        return cur.fetchone() is not None
