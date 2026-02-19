"""
CAR REPOSITORY (DAO)
only SQL here for cars.
"""

from app.infrastructure_persistence.db_manager import DatabaseManager


class CarRepository:
    def __init__(self) -> None:
        self._db = DatabaseManager.get_instance().connection

    def add_car(self, car_data: dict) -> int:
        cur = self._db.cursor()
        try:
            cur.execute(
                "INSERT INTO cars (car_type, make, model, year, mileage, available_now, min_rent_days, max_rent_days, "
                "daily_rate, service_interval_km, next_service_mileage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    car_data["car_type"],
                    car_data["make"],
                    car_data["model"],
                    int(car_data["year"]),
                    int(car_data["mileage"]),
                    int(car_data["available_now"]),
                    int(car_data["min_rent_days"]),
                    int(car_data["max_rent_days"]),
                    float(car_data["daily_rate"]),
                    int(car_data["service_interval_km"]),
                    int(car_data["next_service_mileage"]),
                ),
            )
            self._db.commit()
            return int(cur.lastrowid)
        except Exception:
            self._db.rollback()
            raise

    def list_all(self):
        # get all cars from database (admin view)
        cur = self._db.cursor()
        cur.execute("SELECT * FROM cars ORDER BY car_id")
        return cur.fetchall()

    def get_by_id(self, car_id: int):
        cur = self._db.cursor()
        cur.execute("SELECT * FROM cars WHERE car_id=?", (int(car_id),))
        return cur.fetchone()

    def list_available_now(self):
        cur = self._db.cursor()
        cur.execute("SELECT * FROM cars WHERE available_now=1 ORDER BY car_id")
        return cur.fetchall()

    def update_fields(self, car_id: int, fields: dict) -> None:
        allowed = {
            "car_type", "make", "model", "year", "mileage", "available_now",
            "min_rent_days", "max_rent_days", "daily_rate",
            "service_interval_km", "next_service_mileage",
        }
        clean = {k: v for k, v in fields.items() if k in allowed}
        if not clean:
            return

        set_sql = ", ".join([f"{k}=?" for k in clean.keys()])
        values = list(clean.values()) + [int(car_id)]

        cur = self._db.cursor()
        try:
            cur.execute(f"UPDATE cars SET {set_sql} WHERE car_id=?", tuple(values))
            self._db.commit()
        except Exception:
            self._db.rollback()
            raise

    def delete_car(self, car_id: int) -> None:
        cur = self._db.cursor()
        try:
            cur.execute("DELETE FROM cars WHERE car_id=?", (int(car_id),))
            self._db.commit()
        except Exception:
            self._db.rollback()
            raise
