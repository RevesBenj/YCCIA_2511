"""
BOOKING SERVICE

- customer request booking
- admin approve / reject
- admin complete booking (apply mileage + check maintenance)
"""

from datetime import date
from app.config.logging_config import get_logger
from app.config.settings import (
    LOYALTY_REDEEM_BLOCK,
    LOYALTY_REDEEM_VALUE,
    LOYALTY_EARN_PER_DOLLAR,
)
from app.domain.users import Admin, Customer
from app.domain.cars import CarFactory
from app.application.validators import require_non_negative_float, require_non_negative_int
from app.infrastructure_persistence.repositories.booking_repo import BookingRepository
from app.infrastructure_persistence.repositories.car_repo import CarRepository
from app.infrastructure_persistence.repositories.user_repo import UserRepository
from app.application.services.pricing_service import PricingService
from app.application.services.approval_rules import ApprovalRulesService
from app.application.services.maintenance_service import MaintenanceService

log = get_logger("booking_service")


class BookingService:
    def __init__(self) -> None:
        self._bookings = BookingRepository()
        self._cars = CarRepository()
        self._users = UserRepository()

        self._pricing = PricingService()
        self._rules = ApprovalRulesService()
        self._maintenance = MaintenanceService()

    def create_booking(
        self,
        customer: Customer,
        car_id: int,
        start_date: date,
        end_date: date,
        estimated_km: int,
        extra: float = 0.0,
        redeem_points: int = 0,
    ):
       # ----Begin: date validation (Cannot book in the past) ----
        from datetime import date  # make sure this import exists

        today = date.today()  # get today date from system clock

        # start date must be today or future
        if start_date < today:
            raise ValueError("Start date must be today or later.")
        # end date must be today or future
        if end_date < today:
            raise ValueError("End date must be today or later.")
        # ----End: date validation (Cannot book in the past) ----

        # basic validation
        if end_date < start_date:
            raise ValueError("End date cannot be before start date.")
        require_non_negative_int(estimated_km, "Estimated km")
        require_non_negative_float(extra, "Extra charges")
        require_non_negative_int(redeem_points, "Redeem points")

        car_row = self._cars.get_by_id(car_id)
        if car_row is None:
            raise ValueError("Car ID not found.")

        # if locked by maintenance, block booking
        if int(car_row["available_now"]) != 1:
            raise ValueError("Car is unavailable now (maintenance lock).")

        s_txt = start_date.isoformat()
        e_txt = end_date.isoformat()

        # critical: block overlap for PENDING and APPROVED
        if self._bookings.has_overlap(car_id, s_txt, e_txt):
            raise ValueError("Date conflict: car already booked in that range.")

        days = (end_date - start_date).days + 1

        # enforce min/max rental period requirement
        if days < int(car_row["min_rent_days"]) or days > int(car_row["max_rent_days"]):
            raise ValueError(
                f"Rental days must be between {car_row['min_rent_days']} and {car_row['max_rent_days']}."
            )

        # create domain car object for pricing (polymorphism)
        car_obj = CarFactory.create(
            car_type=car_row["car_type"],
            make=car_row["make"],
            model=car_row["model"],
            year=int(car_row["year"]),
            mileage=int(car_row["mileage"]),
            min_rent_days=int(car_row["min_rent_days"]),
            max_rent_days=int(car_row["max_rent_days"]),
            daily_rate=float(car_row["daily_rate"]),
            service_interval_km=int(car_row["service_interval_km"]),
            car_id=int(car_row["car_id"]),
            available_now=bool(car_row["available_now"]),
            next_service_mileage=int(car_row["next_service_mileage"]),
        )

        # loyalty redeem logic
        discount = 0.0
        if redeem_points > 0:
            if redeem_points % LOYALTY_REDEEM_BLOCK != 0:
                raise ValueError(f"Redeem points must be multiples of {LOYALTY_REDEEM_BLOCK}.")
            if customer.loyalty_points < redeem_points:
                raise ValueError("Not enough loyalty points.")
            discount = (redeem_points / LOYALTY_REDEEM_BLOCK) * LOYALTY_REDEEM_VALUE

        total_fee = self._pricing.calculate_fee(car_obj, days, extra=extra, discount=discount)

        # innovation: auto-approve
        auto_ok = self._rules.should_auto_approve(customer.user_id, car_row, days, extra)
        status = "APPROVED" if auto_ok else "PENDING"

        booking_id = self._bookings.create_booking(
            {
                "customer_id": customer.user_id,
                "car_id": car_id,
                "start_date": s_txt,
                "end_date": e_txt,
                "status": status,
                "total_fee": total_fee,
                "estimated_km": int(estimated_km),
                "auto_approved": 1 if auto_ok else 0,
                "decided_by_admin_id": None,
                "decided_at": None,
            }
        )

        # apply redeemed points now
        if redeem_points > 0:
            self._users.update_loyalty_points(customer.user_id, customer.loyalty_points - redeem_points)

        # award points if already approved
        if status == "APPROVED":
            add_pts = int(total_fee // LOYALTY_EARN_PER_DOLLAR)
            row = self._users.get_by_id(customer.user_id)
            self._users.update_loyalty_points(customer.user_id, int(row["loyalty_points"]) + add_pts) # add points

        log.info("Booking created booking_id=%s status=%s fee=%s", booking_id, status, total_fee)
        return booking_id, status, total_fee

    def list_customer_bookings(self, customer_id: int):
        return self._bookings.list_by_customer(customer_id)

    def list_pending_bookings(self):
        return self._bookings.list_by_status("PENDING")

    def decide_booking(self, admin: Admin, booking_id: int, approve: bool) -> None:
        if not admin.is_admin():
            raise PermissionError("Only admin can approve/reject.")

        row = self._bookings.get_by_id(booking_id)
        if row is None:
            raise ValueError("Booking not found.")
        if row["status"] != "PENDING":
            raise ValueError("Only PENDING bookings can be decided.")

        # if approving, ensure car not locked by maintenance
        if approve:
            car_row = self._cars.get_by_id(int(row["car_id"]))
            if car_row is None:
                raise ValueError("Car not found for booking.")
            if int(car_row["available_now"]) != 1:
                raise ValueError("Cannot approve: car is locked due to maintenance.")

        new_status = "APPROVED" if approve else "REJECTED"
        self._bookings.update_status(booking_id, new_status, admin.user_id)

        # award points on approval
        if approve:
            add_pts = int(float(row["total_fee"]) // LOYALTY_EARN_PER_DOLLAR)
            u = self._users.get_by_id(int(row["customer_id"]))
            self._users.update_loyalty_points(int(row["customer_id"]), int(u["loyalty_points"]) + add_pts)

        log.info("Admin decided booking_id=%s status=%s", booking_id, new_status)

    def complete_booking(self, admin: Admin, booking_id: int):
        if not admin.is_admin():
            raise PermissionError("Only admin can complete bookings.")

        row = self._bookings.get_by_id(booking_id)
        if row is None:
            raise ValueError("Booking not found.")
        if row["status"] != "APPROVED":
            raise ValueError("Only APPROVED bookings can be completed.")

        # mark completed
        self._bookings.update_status(booking_id, "COMPLETED", admin.user_id)

        # apply mileage and check maintenance
        alert_id = self._maintenance.apply_mileage_and_check(int(row["car_id"]), int(row["estimated_km"]))
        log.info("Booking completed booking_id=%s alert_id=%s", booking_id, alert_id)
        return alert_id

    def list_open_alerts(self, admin: Admin):
        if not admin.is_admin():
            raise PermissionError("Only admin can view alerts.")
        return self._maintenance.list_open_alerts()

    def mark_car_serviced(self, admin: Admin, car_id: int) -> None:
        if not admin.is_admin():
            raise PermissionError("Only admin can mark serviced.")
        self._maintenance.mark_serviced(car_id)
