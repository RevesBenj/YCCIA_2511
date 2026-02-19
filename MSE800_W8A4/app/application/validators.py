"""
VALIDATORS - Common validation functions.
common checks in one file to reduce repeat code.
"""


def require_non_empty(value: str, field_name: str) -> None:
    if not value or not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")


def require_email_like(value: str) -> None:
    if not value or "@" not in value or "." not in value:
        raise ValueError("Email format looks invalid.")


def require_min_length(value: str, min_len: int, field_name: str) -> None:
    if not value or len(value) < min_len:
        raise ValueError(f"{field_name} must be at least {min_len} characters.")


def require_positive_int(value: int, field_name: str) -> None:
    if int(value) <= 0:
        raise ValueError(f"{field_name} must be > 0.")


def require_non_negative_int(value: int, field_name: str) -> None:
    if int(value) < 0:
        raise ValueError(f"{field_name} cannot be negative.")


def require_non_negative_float(value: float, field_name: str) -> None:
    if float(value) < 0:
        raise ValueError(f"{field_name} cannot be negative.")


def require_year_range(year: int, min_year: int = 1980, max_year: int = 2100) -> None:
    if int(year) < min_year or int(year) > max_year:
        raise ValueError("Year out of range.")
