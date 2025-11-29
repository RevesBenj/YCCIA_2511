# -------------------------------------------------------
# DEBUGGING
# Author: Benjelyn Reves Patiag
# Date Created: 29-Nov-2025
# Description: Week 2- Activity 4 - Debugging
# -------------------------------------------------------

def factorial(n):
    # Base case: if n is 0, factorial is 1
    if n == 0:
        return 1
    # Recursive case: multiply n by factorial of (n-1)
    return n * factorial(n - 1)
    # FIX EXPLANATION: This function is correct, but it needs a number `n` to work.
    # BUG: Calling factorial() without an argument (in main) will cause a TypeError.


def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    # Recursive case: sum of previous two Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)
    # FIX EXPLANATION: This function is correct, but also requires a number `n`.
    # BUG: Calling fibonacci() without an argument (in main) will cause a TypeError.
    # Note: This returns the nth Fibonacci number, not the full sequence.


if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        # BUG: Missing argument for factorial(), required positional argument: 'n'
        # FIX: Ask user for a number and pass it as an argument
        n = int(input("Enter a number for factorial: "))
        ans = factorial(n)

    elif choice == "2":
        # BUG: Missing argument for fibonacci(), required positional argument: 'n'
        # FIX: Ask user for a number and pass it as an argument
        n = int(input("Enter a number for fibonacci: "))
        ans = fibonacci(n)

    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)
    # FIX EXPLANATION: Now the program correctly asks the user for a number
    # and passes it to the recursive functions, preventing TypeError.
