"""
CLI router
this file decide main menu and send user to admin/customer menu.
"""

from app.application.services.auth_service import AuthService
from app.application.services.car_service import CarService
from app.application.services.booking_service import BookingService
from app.presentation.input_helpers import read_int
from app.presentation.menus_admin import admin_menu
from app.presentation.menus_customer import customer_menu


def run_app() -> None:
    # Create services once (app scope)
    auth = AuthService()
    cars = CarService()
    bookings = BookingService()

    print("\n=== Hello! Welcome to the BS CAR RENTAL SYSTEM (CUI). ===")
    print("To get you started, we've set up a default admin account for your first login:")
    print("Email: admin@local.com | Password: sysad1$")

    while True:
        print("\n--- 🛠️  BS Car Rental: Main Menu ---")
        print("How can we help you today?")
        print("1) Create a New Customer")
        print("2) Login to Your Dashboard")
        print("0) Exit")

        choice = read_int("Enter your choice (0-2): ", 0, 2)

        if choice == 0:
            print("Thank you, Goodbye!")
            return

        if choice == 1:
            try:
                name = input("Name: ").strip()
                email = input("Email: ").strip()
                password = input("Password (min 6): ").strip()
                user_id = auth.register_customer(name, email, password)
                print(f"Registered customer. user_id={user_id}")
            except Exception as exc:
                print(f"Register error: {exc}")

        if choice == 2:
            try:
                email = input("Email: ").strip()
                password = input("Password: ").strip()
                user = auth.login(email, password)

                print(f"Welcome {user.name} ({user.role})")

                # polymorphism: object decides menu
                if user.is_admin():
                    admin_menu(user, auth, cars, bookings)
                else:
                    customer_menu(user, auth, cars, bookings)

            except Exception as exc:
                print(f"Login failed: {exc}")
