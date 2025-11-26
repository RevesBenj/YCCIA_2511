# ---------------------------------------------------------------
# PART 2 – Fibonacci & Factorial (Using Built-in Package: math)
# Author: Your Name
# ---------------------------------------------------------------

import math  # Using math.factorial() to simplify calculations


# Function to generate Fibonacci sequence
def fibonacci(n):
    """Generate an N-length Fibonacci series."""
    if n <= 0:
        return []  # Return empty list for invalid input

    # First two numbers of Fibonacci
    fib_list = [0, 1]

    # Generate remaining values
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list[:n]


# Function to calculate factorial using built-in math package
def factorial(n):
    """Compute factorial using math.factorial()."""
    try:
        return math.factorial(n)  # Faster than manual multiplication
    except ValueError:
        return "Error: Factorial is not defined for negative numbers."


# ----------------- MAIN PROGRAM (ENTRY POINT) -----------------
if __name__ == "__main__":
    n = int(input("Enter a positive integer N: "))

    print(f"\nFibonacci series of length {n}:")
    print(fibonacci(n))

    print(f"\nFactorial of {n} (using math package):")
    print(factorial(n))
