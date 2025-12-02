# -------------------------------------------------------
# Week 2 - Activity 5 Temperature converter
# Author: Benjelyn Reves Patiag
# Date Created: 2-Dec-2025
# Description: Temperature converter - transforms user-entered temperatures between Fahrenheit and Celsius
# Should the user enter an incorrect format or use the wrong prefix, the program should prompt
# them with: "Invalid input. Please enter the temperature with the correct 'C' or F' prefix.
# -------------------------------------------------------


class TempConverter:
    def __init__(self):
        self.user_input = ""

    def get_input(self):
        # Keep looping until the input is valid
        while True:
            self.user_input = input("Enter a temperature value (e.g., F51 or C11). Use only uppercase 'C' or 'F': ").strip()

            if self.validate_input():
                return self.user_input
            else:
                print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")

    def validate_input(self):
        # Must be at least 2 characters
        if len(self.user_input) < 2:
            return False

        prefix = self.user_input[0]
        number_part = self.user_input[1:]

        # Check prefix
        if prefix not in ("C", "F"):
            return False

        # Check the numeric part
        try:
            float(number_part)
        except ValueError:
            return False

        return True

    def tempConvertCalc(self):
        prefix = self.user_input[0]
        value = float(self.user_input[1:])

        if prefix == "F":
            # Fahrenheit → Celsius
            celsius = (value - 32) * 5 / 9
            return f"F{value:.0f} degrees Fahrenheit = {celsius:.2f} degrees Celsius"

        elif prefix == "C":
            # Celsius → Fahrenheit
            fahrenheit = (value * 9 / 5) + 32
            return f"C{value:.0f} degrees Celsius = {fahrenheit:.2f} degrees Fahrenheit"


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    converter = TempConverter()
    converter.get_input()  # Will loop until input is valid
    print(converter.tempConvertCalc())
