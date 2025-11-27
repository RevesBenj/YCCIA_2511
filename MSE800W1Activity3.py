# -------------------------------------------------------
# Fibonacci Series & Factorial
# Author: Benjelyn Reves Patiag
# Description:
#   Part1 details - Develop a Python program that uses functions to generate an N-length Fibonacci series and compute the factorial of N.
#       Do not use any external packages in this version. Include clear inline comments to show your understanding, then upload your code to GitHub and share the link.
#   Part2 details: For the second version, update your program by using built-in packages such as "Math" to enhance or simplify your calculations. Upload this updated version to GitHub as well.
# -------------------------------------------------------

import math  # Part 2 Solution: Using math.factorial() to simplify calculations


#  Function to generate Fibonacci sequence
def fibonacci(n):
    """Generate an N-length Fibonacci series."""
    # If N is 0 or negative, return an empty list
    if n <= 0:
        return []  # Return empty list for invalid input

    # First two numbers of Fibonacci
    fib_list = [0, 1]

    # Loop to generate the next values
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    # Return only N numbers
    return fib_list[:n]


# Part 1 Solution: Function to calculate factorial of x using a loop
def factorial(x):
    # Factorial is not defined for negative numbers
    if x < 0:
        return "Error: Factorial is  defined for positive numbers only."

    result = 1
    # Multiply all numbers from 1 to x
    for i in range(1, x + 1):
        result *= i
    return result

#  Part 2 Solution: Function to calculate factorial using built-in math package
def factorialMath(n):
    """Compute factorial using math.factorial()."""
    try:
        return math.factorial(n)  # Faster than manual multiplication
    except ValueError:
        return "Error: Factorial is not defined for negative numbers."




# ---------------- CALL MAIN PROGRAM ----------------
if __name__ == "__main__":
    try:
        # Take user input
        n = int(input("Enter a positive number (N) for the length of the Fibonacci series: "))

        # Display Fibonacci series
        print(f"\nFibonacci series of length {n}:")
        print(fibonacci(n))

        # Display factorial
        print(f"\nFactorial of {n}: (calculated without packages)")
        print(factorial(n))
        print(f"\nFactorial of {n}: (calculated with the built-in math package)")
        print(factorialMath(n))


    except ValueError as e:
        print(f"Error: Invalid input. Please enter a positive integer. {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")