# -------------------------------------------------------
# W2-A4.3 Python OOP DEBUGGING
# Author: Benjelyn Reves Patiag
# Date Created: 30-Nov-2025
# Description: Update the code to be bug free. Explain your understanding of Self into the code. and adding __init__ function for n=5.
# -------------------------------------------------------

class MathSeries:

    def __init__(self, n):
        # init for accessibility
        self.n = n

    def factorial_recursive(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        # use self
        return n * self.factorial_recursive(n - 1)

    def fibonacci_recursive(self, n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        # use self
        return (self.fibonacci_recursive(n - 1) +
                self.fibonacci_recursive(n - 2))

    # Generate Fibonacci series from 0 to n
    def fibonacci_series(self):
        series = []
        for i in range(self.n + 1):
            series.append(self.fibonacci_recursive(i))
        return series


if __name__ == "__main__":
    n = 5
    # Create an object
    obj1 = MathSeries(n)

    print("Factorial (recursive):", obj1.factorial_recursive(obj1.n))
    print("Fibonacci (recursive):", obj1.fibonacci_recursive(obj1.n))

    # Print the entire Fibonacci series
    print(f"Fibonacci series (0 to {obj1.n}):", obj1.fibonacci_series())
