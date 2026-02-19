"""
AUTH SERVICE
handles register and login.
"""

from app.application.validators import require_email_like, require_min_length, require_non_empty
from app.config.logging_config import get_logger
from app.domain.users import Admin, Customer
from app.infrastructure_persistence.security import hash_password
from app.infrastructure_persistence.repositories.user_repo import UserRepository

log = get_logger("auth_service")


class AuthService:
    def __init__(self) -> None:
        self._users = UserRepository()

    def register_customer(self, name: str, email: str, password: str) -> int:
        require_non_empty(name, "Name")
        require_email_like(email)
        require_min_length(password, 6, "Password")

        email_clean = email.strip().lower()
        if self._users.find_by_email(email_clean) is not None:
            raise ValueError("Email already registered.")

        user_id = self._users.create_user(name.strip(), email_clean, hash_password(password), "CUSTOMER")
        log.info("Customer registered user_id=%s email=%s", user_id, email_clean)
        return user_id

    def register_admin(self, name: str, email: str, password: str) -> int:
        require_non_empty(name, "Name")
        require_email_like(email)
        require_min_length(password, 8, "Admin password")

        email_clean = email.strip().lower()
        if self._users.find_by_email(email_clean) is not None:
            raise ValueError("Email already registered.")

        user_id = self._users.create_user(name.strip(), email_clean, hash_password(password), "ADMIN")
        log.info("Admin registered user_id=%s email=%s", user_id, email_clean)
        return user_id

    def login(self, email: str, password: str): # return Admin | Customer
        require_non_empty(email, "Email")
        require_non_empty(password, "Password")

        email_clean = email.strip().lower()
        row = self._users.find_by_email(email_clean)

        if row is None or row["password_hash"] != hash_password(password):
            raise ValueError("Invalid email or password.")

        # polymorphism: return different object based on role
        if row["role"] == "ADMIN":
            return Admin(int(row["user_id"]), row["name"], row["email"])

        return Customer(int(row["user_id"]), row["name"], row["email"], int(row["loyalty_points"]))

    def refresh_customer(self, customer_id: int) -> Customer:
        row = self._users.get_by_id(customer_id)
        if row is None or row["role"] != "CUSTOMER":
            raise ValueError("Customer not found.")
        return Customer(int(row["user_id"]), row["name"], row["email"], int(row["loyalty_points"]))

    def list_customers(self, admin): 
        # only admin allowed
        if not admin.is_admin():
            raise PermissionError("Only admin can view customers.")

        return self._users.list_customers()
