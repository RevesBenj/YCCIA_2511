"""
DOMAIN: BOOKING
booking is record, we freeze it so no accidental change.
Once confirmed, details must NOT change accidentally.
All changes (approve, reject, complete) must go through services.
"""

# dataclass is used to quickly create a data-only object
# frozen=True is the IMPORTANT part → it "freezes" the object  meaning once created, its values CANNOT be changed
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Booking:
    booking_id: int
    customer_id: int
    car_id: int
    start_date: str
    end_date: str
    status: str
    total_fee: float
    estimated_km: int
    auto_approved: bool

    def duration_days(self) -> int:
        s = datetime.strptime(self.start_date, "%Y-%m-%d").date()
        e = datetime.strptime(self.end_date, "%Y-%m-%d").date()
        return (e - s).days + 1
