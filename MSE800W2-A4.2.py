# -------------------------------------------------------
# W2-A4 Python OOP
# Author: Benjelyn Reves Patiag
# Date Created: 30-Nov-2025
# Description: Instantiation - Create object of the class
# -------------------------------------------------------


class MathSeries:

    @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)

    @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2)

    @staticmethod
    def fibonacci_series(n):
        series = []
        for i in range(n):
            series.append(MathSeries.fibonacci_recursive(i))
        return series


if __name__ == "__main__":
    n = 5

    # Instantiate the class.
    ms = MathSeries()

    print("Factorial (recursive):", ms.factorial_recursive(n))
    print("Fibonacci recursive series:", ms.fibonacci_series(n))
