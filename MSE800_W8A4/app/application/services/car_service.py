"""
CAR SERVICE
admin CRUD for cars.
"""

from app.config.logging_config import get_logger
from app.domain.cars import CarFactory
from app.application.validators import (
    require_non_empty,
    require_non_negative_int,
    require_positive_int,
    require_year_range,
)
from app.infrastructure_persistence.repositories.car_repo import CarRepository
from app.infrastructure_persistence.repositories.booking_repo import BookingRepository

log = get_logger("car_service") 


class CarService: # This class is "service layer". UI/CLI talk to this. UI do not talk directly to SQL/repo. Service hide business rules + workflow.
    def __init__(self) -> None:
        self._cars = CarRepository() # Abstraction: repo hide SQL queries
        self._bookings = BookingRepository()

    def add_car(
        self,
        car_type: str,
        make: str,
        model: str,
        year: int,
        mileage: int,
        available_now: bool,
        min_days: int,
        max_days: int,
        daily_rate: float | None,
        service_interval_km: int | None,
    ) -> int:
        # validate and apply business rule here, UI just send input.
        require_non_empty(make, "Make")
        require_non_empty(model, "Model")
        require_year_range(year)
        require_non_negative_int(mileage, "Mileage")
        require_positive_int(min_days, "Min rent days")
        require_positive_int(max_days, "Max rent days")

        if int(min_days) > int(max_days): # keep data consistent, avoid wrong min/max days
            raise ValueError("Min rent days cannot exceed max rent days.")
        # service decide what is valid for pricing/service settings
        if daily_rate is not None and float(daily_rate) <= 0:
            raise ValueError("Daily rate must be > 0.")
        if service_interval_km is not None and int(service_interval_km) <= 0:
            raise ValueError("Service interval must be > 0.")
        
        # POLYMORPHISM (via Factory) + ABSTRACTION: CarFactory.create() can return different Car subclass based on car_type
        car = CarFactory.create(
            car_type=car_type,
            make=make,
            model=model,
            year=year,
            mileage=mileage,
            min_rent_days=min_days,
            max_rent_days=max_days,
            daily_rate=daily_rate,
            service_interval_km=service_interval_km,
            available_now=available_now,
        )

        car_data = {
            "car_type": car.car_type,
            "make": car.make,
            "model": car.model,
            "year": car.year,
            "mileage": car.mileage,
            "available_now": 1 if car.available_now else 0,
            "min_rent_days": car.min_rent_days,
            "max_rent_days": car.max_rent_days,
            "daily_rate": car.daily_rate,
            "service_interval_km": car.service_interval_km,
            "next_service_mileage": car.next_service_mileage,
        }

        car_id = self._cars.add_car(car_data)
        log.info("Car added car_id=%s type=%s", car_id, car.car_type)
        return car_id

    def list_all_cars(self):
        # service method, UI calls this (not repo)
        return self._cars.list_all()

    def update_car(self, car_id: int, fields: dict) -> None:
        if self._cars.get_by_id(car_id) is None:
            raise ValueError("Car not found.")

        if "min_rent_days" in fields and "max_rent_days" in fields:
            if int(fields["min_rent_days"]) > int(fields["max_rent_days"]):
                raise ValueError("Min rent days cannot exceed max rent days.")

        self._cars.update_fields(car_id, fields)
        log.info("Car updated car_id=%s fields=%s", car_id, list(fields.keys()))

    def delete_car(self, car_id: int) -> None:
        if self._cars.get_by_id(car_id) is None:
            raise ValueError("Car not found.")

        # safety: cannot delete if active bookings exist
        if self._bookings.car_has_active_bookings(car_id):
            raise ValueError("Cannot delete car: it has pending/approved bookings.")

        self._cars.delete_car(car_id)
        log.info("Car deleted car_id=%s", car_id)

    def list_available_now(self):
        return self._cars.list_available_now()

    def get_car(self, car_id: int):
        return self._cars.get_by_id(car_id)
