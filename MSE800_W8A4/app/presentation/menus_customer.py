"""
CUSTOMER MENU
only UI prints and input, no SQL.
"""

from app.presentation.input_helpers import read_date, read_float, read_int
from app.domain.users import Customer
from app.application.services.auth_service import AuthService
from app.application.services.car_service import CarService
from app.application.services.booking_service import BookingService


def customer_menu(customer: Customer, auth: AuthService, cars: CarService, bookings: BookingService) -> None:
    while True:  # only stop when user choose Logout (return)
        # refresh customer so points always accurate
        customer = auth.refresh_customer(customer.user_id)

        print("\n--- CUSTOMER MENU ---")
        print("1) View available cars")
        print("2) Request booking")
        print("3) View my bookings")
        print("0) Logout")

        choice = read_int("Choose: ", 0, 3)

        if choice == 0: # Logout
            return

        if choice == 1: # View available cars
            rows = cars.list_available_now()
            if not rows:
                print("No cars available now.")
                continue

            print("\nAvailable cars:")
            for r in rows:
                print(
                    f"ID {r['car_id']} | {r['car_type']} | {r['make']} {r['model']} {r['year']} | "
                    f"mileage={r['mileage']} | min={r['min_rent_days']} max={r['max_rent_days']} | "
                    f"rate={r['daily_rate']} | next service at {r['next_service_mileage']}"
                )

        if choice == 2: # Request booking
            try:
                car_id = read_int("Car ID: ", 1, None)
                start = read_date("Start date (YYYY-MM-DD): ")
                end = read_date("End date (YYYY-MM-DD): ")
                km = read_int("Estimated trip km (0 if none): ", 0, None)
                extra = read_float("Extra charges (0 if none): ", 0.0)

                print(f"Your loyalty points: {customer.loyalty_points}")
                redeem = read_int("Redeem points? (0 or multiples of 100): ", 0, None)

                booking_id, status, total = bookings.create_booking(
                    customer=customer,
                    car_id=car_id,
                    start_date=start,
                    end_date=end,
                    estimated_km=km,
                    extra=extra,
                    redeem_points=redeem,
                )

                print(f"Booking created! id={booking_id} status={status} total=${total}")
                if status == "APPROVED":
                    print("✅ Auto-approved (fast confirm for low-risk booking).")
                else:
                    print("⏳ Pending admin approval.")

            except Exception as exc:
                print(f"Booking error: {exc}")

        if choice == 3: # View my bookings
            rows = bookings.list_customer_bookings(customer.user_id)
            if not rows:
                print("No bookings yet.")
                continue

            print("\nMy bookings:")
            for r in rows:
                print(
                    f"Booking {r['booking_id']} | car={r['car_id']} | {r['start_date']} to {r['end_date']} | "
                    f"status={r['status']} | fee={r['total_fee']} | auto={r['auto_approved']} | km={r['estimated_km']}"
                )
