"""
AUTO-APPROVE RULES (Innovation)
low risk booking, system approve automatically.
"""

from app.config.settings import (
    AUTO_APPROVE_MAX_DAYS,
    AUTO_APPROVE_MAX_EXTRA,
    AUTO_APPROVE_MAX_DAILY_RATE,
)
from app.infrastructure_persistence.repositories.booking_repo import BookingRepository


class ApprovalRulesService:
    def __init__(self) -> None:
        self._bookings = BookingRepository() # Other classes cannot access booking history directly.

    def should_auto_approve(self, customer_id: int, car_row, days: int, extra: float) -> bool:
        if int(days) > AUTO_APPROVE_MAX_DAYS: # If rental days too long, risk is higher, no auto approve
            return False
        if float(extra) > float(AUTO_APPROVE_MAX_EXTRA): # If extra charges too high, risk is higher, no auto approve
            return False
        if float(car_row["daily_rate"]) > float(AUTO_APPROVE_MAX_DAILY_RATE): # If car daily rate too high, risk is higher, no auto approve
            return False
        if self._bookings.customer_has_rejection_history(customer_id): # If customer has rejection history, no auto approve
            return False

        return True
