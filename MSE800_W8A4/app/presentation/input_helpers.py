"""
INPUT HELPERS
safe input so no crash when user type wrong.
"""

from datetime import datetime


def read_int(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if min_val is not None and val < min_val:
                print(f"Too small, must be >= {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"Too big, must be <= {max_val}")
                continue
            return val
        except ValueError:
            print("Not a valid number. Please try again.")


def read_float(prompt: str, min_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if min_val is not None and val < min_val:
                print(f"Too small, must be >= {min_val}")
                continue
            return val
        except ValueError:
            print("Not a valid number. Please try again.")


def read_date(prompt: str):
    while True:
        raw = input(prompt).strip()
        try:
            return datetime.strptime(raw, "%Y-%m-%d").date()
        except ValueError:
            print("Wrong date format. Use YYYY-MM-DD.")


def read_yes_no(prompt: str) -> bool:
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("Please type y/n.")
