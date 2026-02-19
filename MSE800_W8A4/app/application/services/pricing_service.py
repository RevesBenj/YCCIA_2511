"""
PRICING SERVICE
compute rental fee.
"""

from app.domain.cars import Car
from app.application.validators import require_non_negative_float


class PricingService:
    def calculate_fee(self, car: Car, days: int, extra: float, discount: float) -> float:
        if int(days) <= 0:  # Validation logic is inside service, UI does not check business rules.      
            raise ValueError("Days must be at least 1.")
        require_non_negative_float(extra, "Extra charges")
        require_non_negative_float(discount, "Discount")

        # polymorphism: effective_daily_rate depends on car type multiplier
        daily = car.effective_daily_rate()
        # total price = daily rate * days + extras - discounts
        total = (daily * int(days)) + float(extra) - float(discount)

        if total < 0: # rental fee cannot be negative
            total = 0.0

        return round(total, 2)
