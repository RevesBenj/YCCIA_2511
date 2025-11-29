# -------------------------------------------------------
# Python OOP
# Author: Benjelyn Reves Patiag
# Date Created: 30-Nov-2025
# Description: Python OOP. A class that provides recursive methods for Fibonacci
#     and factorial calculations.
# -------------------------------------------------------


class MathRecursion:

    def fibonacci(self, n):
        # Recursive Fibonacci function that returns
        # a list containing the first n Fibonacci numbers.


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

        # RECURSIVE CALL:
        # Each function call is PUSHED onto the call stack.
        fib_list = self.fibonacci(n - 1)  # stack PUSH

        # After reaching simplest case, recursion starts to POP
        next_value = fib_list[-1] + fib_list[-2]

        # Append the newly computed number
        fib_list.append(next_value)

        # Returning completes this stack frame → stack POP
        return fib_list


    def factorial(self, x):
        """
        Recursive factorial function.
        """

        # Negative value check
        if x < 0:
            return "Error: Factorial is defined for positive numbers only."

        # Base case (FACTORIAL OF 0 OR 1 = 1)
        # When base case is reached → recursion stops and returns start popping.
        if x == 0 or x == 1:
            return 1

        # RECURSIVE CALL:
        # Multiply x by factorial(x-1)
        # Each call is stacked until base case is hit.
        return x * self.factorial(x - 1)  # stack PUSH


# ---------------- CLASS MAIN PROGRAM ----------------
if __name__ == "__main__":
    try:
        # Create an object of the MathRecursion class
        math_obj = MathRecursion()

        # User input
        n = int(input("Enter a positive number (N) for Fibonacci and factorial: "))

        # Display Fibonacci
        print(f"\nFibonacci series of length {n} (recursive):")
        print(math_obj.fibonacci(n))

        # Display factorial
        print(f"\nFactorial of {n} (recursive):")
        print(math_obj.factorial(n))

    except ValueError as e:
        print(f"Error: Invalid input. Please enter a positive integer. {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
