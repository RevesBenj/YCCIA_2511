# MSE800W1Activity2.py
# Week 1 – Activity 2: Gross Pay + Tax Deduction
# This script asks for hours worked and hourly rate (Part 1),
# then estimates annual income and uses NZ tax brackets (Part 2)
# to calculate income tax and final net pay.

def calculate_annual_tax(annual_income):
    """
    Calculates the annual income tax based on NZ tax brackets.
    Brackets from 1 April 2025:
      0–15,600 → 10.5%
      15,601–53,500 → 17.5%
      53,501–78,100 → 30%
      78,101–180,000 → 33%
      180,001+ → 39%
    Source: IRD tax rates for individuals. :https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals
    """
    tax = 0.0
    remaining = annual_income

    # 1st bracket
    bracket1 = 15_600
    if remaining > 0:
        taxed = min(bracket1, remaining)
        tax += taxed * 0.105
        remaining -= taxed

    # 2nd bracket
    bracket2 = 53_500 - 15_600
    if remaining > 0:
        taxed = min(bracket2, remaining)
        tax += taxed * 0.175
        remaining -= taxed

    # 3rd bracket
    bracket3 = 78_100 - 53_500
    if remaining > 0:
        taxed = min(bracket3, remaining)
        tax += taxed * 0.30
        remaining -= taxed

    # 4th bracket
    bracket4 = 180_000 - 78_100
    if remaining > 0:
        taxed = min(bracket4, remaining)
        tax += taxed * 0.33
        remaining -= taxed

    # 5th bracket
    if remaining > 0:
        tax += remaining * 0.39

    return tax

def main():
    # Part 1: get inputs from user
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate ($): "))

    # compute gross pay for this period
    gross_pay = hours_worked * hourly_rate
    print(f"Gross pay for period: ${gross_pay:.2f}")

    # For simplicity: assume this period is one week
    # Estimate annual income by multiplying by 52 weeks
    annual_income = gross_pay * 52
    print(f"Estimated annual income: ${annual_income:.2f}")

    # Part 2: compute annual tax
    annual_tax = calculate_annual_tax(annual_income)
    print(f"Estimated annual income tax: ${annual_tax:.2f}")

    # Compute net annual income
    net_annual_income = annual_income - annual_tax
    print(f"Estimated net annual income: ${net_annual_income:.2f}")

    # Also show net for the period (this week) after tax pro-rated
    weekly_tax = annual_tax / 52
    net_weekly_pay = gross_pay - weekly_tax
    print(f"Estimated net pay for period (after tax): ${net_weekly_pay:.2f}")

if __name__ == "__main__":

    main()