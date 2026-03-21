# ============================================
# Extended decorator example 
# Features:
# 1. execution time tracking
# 2. basic error handling
# 3. saving logs to a file
# ============================================

import time
from datetime import datetime

LOG_FILE = "decorator_log.txt"


def save_log(message):
    """Save log message into text file."""
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")


# decorator function

def log_decorator(func):
    """Decorator for logging, timing, and basic error handling."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        start_message = (
            f"[{timestamp}] Calling {func.__name__} "
            f"with args={args}, kwargs={kwargs}"
        )
        print(start_message)
        save_log(start_message)

        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            success_message = (
                f"[{timestamp}] {func.__name__} returned {result} "
                f"| execution time: {execution_time:.6f} seconds"
            )
            print(success_message)
            save_log(success_message)
            return result

        except Exception as error:  # basic error handling
            end_time = time.time()
            execution_time = end_time - start_time

            error_message = (
                f"[{timestamp}] ERROR in {func.__name__}: {error} "
                f"| execution time: {execution_time:.6f} seconds"
            )
            print(error_message)
            save_log(error_message)
            return None

    return wrapper


# ============================================
# function 1: add
# ============================================
@log_decorator
def add(a, b):
    # add two numbers
    return a + b


# ============================================
# function 2: multiply
# ============================================
@log_decorator
def multiply(a, b):
    # multiply two numbers
    return a * b


# ============================================
# function 3: divide
# this one added to show error handling
# ============================================
@log_decorator
def divide(a, b):
    # divide two numbers
    return a / b


# ============================================
# main test code
# ============================================
if __name__ == "__main__":
    print("---- TEST ADD ----")
    add(3, 5)

    print()
    print("---- TEST MULTIPLY ----")
    multiply(2, 6)

    print()
    print("---- TEST DIVIDE OK ----")
    divide(10, 2)

    print()
    print("---- TEST DIVIDE ERROR ----")
    divide(10, 0)
