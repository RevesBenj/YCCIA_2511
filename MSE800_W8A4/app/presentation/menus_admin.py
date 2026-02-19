"""
ADMIN MENU
only UI and calling service.
"""

from app.presentation.input_helpers import read_int, read_float, read_yes_no
from app.domain.users import Admin
from app.application.services.auth_service import AuthService
from app.application.services.car_service import CarService
from app.application.services.booking_service import BookingService


def admin_menu(admin: Admin, auth: AuthService, cars: CarService, bookings: BookingService) -> None:
    while True:
        print("\n--- ADMIN MENU ---")
        print("1) Add car")
        print("2) Update car")
        print("3) Delete car")
        print("4) View pending bookings")
        print("5) Approve/Reject booking")
        print("6) Complete booking (apply mileage + maintenance check)")
        print("7) View open maintenance alerts")
        print("8) Mark car serviced (unlock car)")
        print("9) Register another admin")
        print("10) View all cars")
        print("11) View all customers")
        print("0) Logout")

        choice = read_int("Choose: ", 0, 11)

        if choice == 0:
            return

        if choice == 1: # Add car
            try:
                car_type = input("Car type (ECONOMY/STANDARD/PREMIUM): ").strip().upper() or "STANDARD"
                make = input("Make: ").strip()
                model = input("Model: ").strip()
                year = read_int("Year: ", 1980, 2100)
                mileage = read_int("Mileage: ", 0, None)
                available_now = read_int("Available now? (1 yes / 0 no): ", 0, 1) == 1
                min_days = read_int("Min rent days: ", 1, None)
                max_days = read_int("Max rent days: ", 1, None)

                rate_raw = input("Daily rate (blank default): ").strip()
                daily_rate = float(rate_raw) if rate_raw else None

                interval_raw = input("Service interval km (blank 10000): ").strip()
                interval_km = int(interval_raw) if interval_raw else None

                car_id = cars.add_car(
                    car_type=car_type,
                    make=make,
                    model=model,
                    year=year,
                    mileage=mileage,
                    available_now=available_now,
                    min_days=min_days,
                    max_days=max_days,
                    daily_rate=daily_rate,
                    service_interval_km=interval_km,
                )
                print(f"Car added! car_id={car_id}")
            except Exception as exc:
                print(f"Add car error: {exc}")

        if choice == 2: # Update car
            try:
                car_id = read_int("Car ID: ", 1, None)
                fields = {}

                print("Leave blank to skip update field.")
                make = input("New make: ").strip()
                model = input("New model: ").strip()
                year = input("New year: ").strip()
                mileage = input("New mileage: ").strip()
                avail = input("Available now (1/0): ").strip()
                min_days = input("Min rent days: ").strip()
                max_days = input("Max rent days: ").strip()
                daily_rate = input("Daily rate: ").strip()
                next_service = input("Next service mileage: ").strip()

                if make:
                    fields["make"] = make
                if model:
                    fields["model"] = model
                if year:
                    fields["year"] = int(year)
                if mileage:
                    fields["mileage"] = int(mileage)
                if avail in ("0", "1"):
                    fields["available_now"] = int(avail)
                if min_days:
                    fields["min_rent_days"] = int(min_days)
                if max_days:
                    fields["max_rent_days"] = int(max_days)
                if daily_rate:
                    fields["daily_rate"] = float(daily_rate)
                if next_service:
                    fields["next_service_mileage"] = int(next_service)

                cars.update_car(car_id, fields)
                print("Car updated.")
            except Exception as exc:
                print(f"Update error: {exc}")

        if choice == 3: # Delete car
            try:
                car_id = read_int("Car ID: ", 1, None)
                cars.delete_car(car_id)
                print("Car deleted.")
            except Exception as exc:
                print(f"Delete error: {exc}")

        if choice == 4:# View pending bookings
            rows = bookings.list_pending_bookings()
            if not rows:
                print("No pending bookings.")
                continue

            print("\nPending bookings:")
            for r in rows:
                print(
                    f"Booking {r['booking_id']} | customer={r['customer_id']} | car={r['car_id']} | "
                    f"{r['start_date']} to {r['end_date']} | fee={r['total_fee']} | km={r['estimated_km']}"
                )

        if choice == 5: # Approve/Reject booking
            try:
                booking_id = read_int("Booking ID: ", 1, None)
                approve = read_yes_no("Approve booking? (y/n): ")
                bookings.decide_booking(admin, booking_id, approve=approve)
                print("Booking decision saved.")
            except Exception as exc:
                print(f"Decision error: {exc}")

        if choice == 6: # Complete booking
            try:
                booking_id = read_int("Booking ID to complete: ", 1, None)
                alert_id = bookings.complete_booking(admin, booking_id)
                print("Booking completed.")
                if alert_id is not None:
                    print(f"⚠️ Maintenance alert created: alert_id={alert_id} (car locked until serviced)")
            except Exception as exc:
                print(f"Complete error: {exc}")

        if choice == 7: # View open maintenance alerts
            try:
                rows = bookings.list_open_alerts(admin)
                if not rows:
                    print("No open alerts.")
                    continue

                print("\nOpen maintenance alerts:")
                for r in rows:
                    print(f"Alert {r['alert_id']} | car={r['car_id']} | {r['message']}")
            except Exception as exc:
                print(f"Alerts error: {exc}")

        if choice == 8: # Mark car serviced
            try:
                car_id = read_int("Car ID serviced: ", 1, None)
                bookings.mark_car_serviced(admin, car_id)
                print("Car serviced. Alerts closed. Car unlocked.")
            except Exception as exc:
                print(f"Service error: {exc}")

        if choice == 9: # Register another admin
            try:
                name = input("New admin name: ").strip()
                email = input("New admin email: ").strip()
                password = input("New admin password (min 8): ").strip()
                user_id = auth.register_admin(name, email, password)
                print(f"Admin created user_id={user_id}")
            except Exception as exc:
                print(f"Register admin error: {exc}")

        if choice == 10: # View all cars
            rows = cars.list_all_cars()

            if not rows:
                print("No cars found.")
            else:
                print("\n--- All Cars ---")
                for r in rows:
                    print(
                        f"ID={r['car_id']} | {r['car_type']} {r['make']} {r['model']} {r['year']} | "
                        f"mileage={r['mileage']} | available={r['available_now']} | "
                        f"min={r['min_rent_days']} max={r['max_rent_days']} | "
                        f"rate={r['daily_rate']} | next_service={r['next_service_mileage']}"
                    )

        if choice == 11: # View all customers
            rows = auth.list_customers(admin)

            if not rows:
                print("No customers found.")
            else:
                print("\n--- All Customers ---")
                for r in rows:
                    print(
                        f"ID={r['user_id']} | name={r['name']} | email={r['email']} | "
                        f"points={r['loyalty_points']} | created={r['created_at']}"
                    )


