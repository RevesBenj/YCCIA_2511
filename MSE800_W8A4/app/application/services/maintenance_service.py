"""
MAINTENANCE SERVICE (Innovation)

- when booking completed, mileage increase
- if mileage hit service target, make alert and lock car
"""

from app.config.logging_config import get_logger
from app.infrastructure_persistence.repositories.car_repo import CarRepository
from app.infrastructure_persistence.repositories.maintenance_repo import MaintenanceRepository

log = get_logger("maintenance_service")


class MaintenanceService:
    def __init__(self) -> None:
        self._cars = CarRepository() # connect to car data (read / update mileage, availability)
        self._alerts = MaintenanceRepository() # connect to maintenance alert data

    def apply_mileage_and_check(self, car_id: int, added_km: int):
        if int(added_km) <= 0: # safety check: if no mileage added, nothing to do
            return None

        car = self._cars.get_by_id(car_id) # get car record from database
        if car is None: # if car not exist, stop process
            raise ValueError("Car not found.")

        new_mileage = int(car["mileage"]) + int(added_km) # add booking km to existing mileage
        self._cars.update_fields(car_id, {"mileage": new_mileage}) # update car mileage in database

        # INNOVATION:  if new mileage reach or exceed service target, means car need maintenance
        if new_mileage >= int(car["next_service_mileage"]): # service due
            if not self._alerts.has_open_alert_for_car(car_id):# check if alert already exist, avoid duplicate maintenance alert
                msg = f"Service due: mileage {new_mileage} reached target {car['next_service_mileage']}."  # create maintenance message for admin
                alert_id = self._alerts.create_alert(car_id, new_mileage, msg) # create maintenance alert record
                self._cars.update_fields(car_id, {"available_now": 0}) # lock the car so user cannot book              
                log.info( # log for monitoring and audit
                    "Maintenance alert created alert_id=%s car_id=%s",
                    alert_id,
                    car_id
                )
                return alert_id

        return None # if no maintenance needed, return nothing

    def list_open_alerts(self): # admin can view all open maintenance alerts
        return self._alerts.list_open_alerts()

    def mark_serviced(self, car_id: int) -> None:
        car = self._cars.get_by_id(car_id)
        if car is None:
            raise ValueError("Car not found.")

        # close all open maintenance alerts for this car, means service already done
        self._alerts.close_alerts_for_car(car_id)

        # reset next service target + unlock car
        next_target = int(car["mileage"]) + int(car["service_interval_km"])

         # update next service mileage and unlock car
        self._cars.update_fields(
            car_id,
            {
                "next_service_mileage": next_target,
                "available_now": 1
            }
        )

         # log service completion
        log.info(
            "Car serviced, unlocked car_id=%s next_service=%s",
            car_id,
            next_target
        )