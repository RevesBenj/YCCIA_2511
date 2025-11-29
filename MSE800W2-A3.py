# -------------------------------------------------------
# Recursive Functions
# Author: Benjelyn Reves Patiag
# Description: Convert the Fibonacci and Factorial to Recursive Function.
# -------------------------------------------------------

# Recursive Fibonacci function (returns a list of length n)
def fibonacci_recursive(n):

    # Generate an N-length Fibonacci series recursively.  Returns a list containing the first n Fibonacci numbers.
    # Case when n is zero or negative → return empty list
    # No recursion happens here
    if n <= 0:
        return []

    # Base case: if n is 1 → only the first Fibonacci number
    # When base case is reached, function starts returning (popping from stack)
    elif n == 1:
        return [0]

    # Base case: if n is 2 → first two Fibonacci numbers
    elif n == 2:
        return [0, 1]

    # This calls the function again. Each CALL STACK is stored in memory.
    # Keeps stacking calls until it reaches the base case.
    # Then it solves them one by one from bottom to top.
    fib_list = fibonacci_recursive(n - 1)  # stack PUSH

    # After reaching the simplest case, starts going back up and solving each step.
    # Now values begin to POP from the stack and combine results.
    next_value = fib_list[-1] + fib_list[-2]  # Get next value

    # Add the next Fibonacci number to the list.
    fib_list.append(next_value)

    # Send back the answer and remove (POPS) this step from memory.
    return fib_list  # stack POP


# Recursive factorial function
def factorial_recursive(x):

    # Calculate factorial of a number recursively.
    # Check for invalid input (negative numbers)
    if x < 0:
        return "Error: Factorial is defined for positive numbers only."

    # Base case: factorial of 0 or 1 is 1
    # When base case is reached → recursion stops and values pop back up.
    if x == 0 or x == 1:
        return 1


    # RECURSIVE STEPS:
    # Multiply x by factorial of (x-1)
    # Each call is like adding a new task on a stack, each step until it reaches the base case.
    # Then it starts solving each step from the bottom, combining results one by one like unstacking tasks.
    return x * factorial_recursive(x - 1)  # stack PUSH


# ---------------- CALL MAIN PROGRAM ----------------
if __name__ == "__main__":
    try:
        # Take user input
        n = int(input("Enter a positive number (N) for the length of the Fibonacci series: "))

        # Display Fibonacci series (recursive)
        print(f"\nFibonacci series of length {n} (recursive):")
        print(fibonacci_recursive(n))

        # Display factorial (recursive)
        print(f"\nFactorial of {n} (recursive):")
        print(factorial_recursive(n))

    except ValueError as e:
        print(f"Error: Invalid input. Please enter a positive integer. {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
