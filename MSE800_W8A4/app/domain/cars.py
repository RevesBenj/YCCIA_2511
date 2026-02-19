"""
DOMAIN: CARS
OOP:
- Abstraction: Car abstract class
- Inheritance: Economy/Standard/Premium car types
- Polymorphism: rate_multiplier differs per car type
Design Pattern:
- Factory Method: CarFactory.create()
"""

from __future__ import annotations  # allow class name before define
from abc import ABC, abstractmethod  # tool for base class rule


class Car(ABC): # base car, cannot create direct
    def __init__(
        self,
        car_id: int | None,
        car_type: str,
        make: str,
        model: str,
        year: int,
        mileage: int,
        available_now: bool,
        min_rent_days: int,
        max_rent_days: int,
        daily_rate: float,
        service_interval_km: int,
        next_service_mileage: int,
    ) -> None:
        self._car_id = car_id # save car id
        self._car_type = car_type.strip().upper() # clean car type
        self._make = make.strip()
        self._model = model.strip()
        self._year = int(year)
         # ENCAPSULATION: Car details are protected to prevent invalid changes such as negative mileage.
        self._mileage = int(mileage)

        # available_now is "fleet availability", not schedule availability
        # schedule conflicts handled by booking overlap logic
        self._available_now = bool(available_now)

        self._min_rent_days = int(min_rent_days) # min rent rule
        self._max_rent_days = int(max_rent_days) # max rent rule
         # ENCAPSULATION: Car details are protected to prevent invalid changes such as wrong prices.
        self._daily_rate = float(daily_rate)

        # maintenance innovation
        self._service_interval_km = int(service_interval_km) # service gap
        self._next_service_mileage = int(next_service_mileage) # next service target
    #expose read-only access using @property
    @property
    def car_id(self) -> int | None:
        return self._car_id

    @property
    def car_type(self) -> str:
        return self._car_type

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @property
    def mileage(self) -> int:
        return self._mileage

    @property
    def available_now(self) -> bool:
        return self._available_now

    @property
    def min_rent_days(self) -> int:
        return self._min_rent_days

    @property
    def max_rent_days(self) -> int:
        return self._max_rent_days

    @property
    def daily_rate(self) -> float:
        return self._daily_rate

    @property
    def service_interval_km(self) -> int:
        return self._service_interval_km

    @property
    def next_service_mileage(self) -> int:
        return self._next_service_mileage

    @abstractmethod
    def rate_multiplier(self) -> float:  # each car type must say price multiplier
        raise NotImplementedError

    def effective_daily_rate(self) -> float:
        return round(self._daily_rate * self.rate_multiplier(), 2)


class EconomyCar(Car):  # cheap car
    def rate_multiplier(self) -> float:
        return 0.90


class StandardCar(Car):  # normal car
    def rate_multiplier(self) -> float:
        return 1.00


class PremiumCar(Car): # expensive car
    def rate_multiplier(self) -> float:
        return 1.20


class CarFactory:
    """
    Factory Method pattern.
    give car_type, it create correct Car object.
    """

    @staticmethod
    def create(
        car_type: str,
        make: str,
        model: str,
        year: int,
        mileage: int,
        min_rent_days: int,
        max_rent_days: int,
        daily_rate: float | None = None,
        service_interval_km: int | None = None,
        car_id: int | None = None,
        available_now: bool = True,
        next_service_mileage: int | None = None,
    ) -> Car:
        ct = car_type.strip().upper()

        # safe defaults
        if daily_rate is None:
            daily_rate = 50.0
        if service_interval_km is None:  # set default service interval if empty
            service_interval_km = 10_000
        if next_service_mileage is None:
            next_service_mileage = int(mileage) + int(service_interval_km) # auto calculate next service if empty
        # decide which car object to create
        if ct == "ECONOMY":
            return EconomyCar(
                car_id, "ECONOMY", make, model, year, mileage, available_now,
                min_rent_days, max_rent_days, daily_rate, service_interval_km, next_service_mileage
            )
        if ct == "PREMIUM":
            return PremiumCar(
                car_id, "PREMIUM", make, model, year, mileage, available_now,
                min_rent_days, max_rent_days, daily_rate, service_interval_km, next_service_mileage
            )

        return StandardCar(
            car_id, "STANDARD", make, model, year, mileage, available_now,
            min_rent_days, max_rent_days, daily_rate, service_interval_km, next_service_mileage
        )
