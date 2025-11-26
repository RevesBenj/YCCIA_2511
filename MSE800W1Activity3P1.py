# -------------------------------------------------------
# PART 1 – Fibonacci Series & Factorial (Without Packages)
# Author: Benjelyn Reves Patiag
# -------------------------------------------------------

# Function to generate an N-length Fibonacci series
def fibonacci(n):
    # If N is 0 or negative, return an empty list
    if n <= 0:
        return []

    # The first two values of the Fibonacci sequence
    fib_list = [0, 1]

    # Loop to generate the next values
    for i in range(2, n):
        # Each number is the sum of the previous two numbers
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list[:n]   # Return only N numbers


# Function to calculate factorial of x using a loop
def factorial(x):
    # Factorial is not defined for negative numbers
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."

    result = 1
    # Multiply all numbers from 1 to x
    for i in range(1, x + 1):
        result *= i
    return result


# ---------------- CALL MAIN PROGRAM ----------------
if __name__ == "__main__":
    # Take user input
    n = int(input("Enter a positive integer N: "))

    # Display Fibonacci series
    print(f"\nFibonacci series of length {n}:")
    print(fibonacci(n))

    # Display factorial
    print(f"\nFactorial of {n}:")
    print(factorial(n))
