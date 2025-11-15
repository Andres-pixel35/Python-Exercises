import numpy_financial as npf
from datetime import date
import helpers.user_input as hu
from helpers.generalities import calculate_months


#using numpy_financial i can get the monthly interes rate
def get_interest_rate(monthly_payment: float, total_amount: float, instalments: int) -> float:
    rate = npf.rate(instalments, -monthly_payment, total_amount, 0)
    rate = float(rate)
    return round(rate * 100, 2)

# it will make sure that the data entered is likely to be a real debt and that the user did not make any huge mistake entering the data
def check_debt(monthly_payment: float, total_amount: float, instalments: int, start_date: date) -> bool:
    months = calculate_months(start_date)

    if months >= instalments:
        print(f"Since the beginning of the debt has passed {months} months, which is equal or greater that your instalments ({instalments})."
              "\nPlease check the data and try again.")
        return False

    ratio = (instalments * monthly_payment) / total_amount
    if ratio < 0.9:
        print("The total of instalments is too low to cover the debt — data may be incorrect.\n"
            "If you are sure of the data, you may continue. Are you sure? ", end="")
        choice = hu.get_choice()
        if choice == 'y':
            return True
        return False
    elif ratio > 1.6:
        print("The total of instalments is much higher than the debt — This might be due to interest rate.\n"
              "If you know that you have a high interest rate per month, you may continue. Are you sure? ", end="")
        choice = hu.get_choice()
        if choice == 'y':
            return True
        return False

    return True

# it calculates the remaining amount of the debt each time the program is execute.
# this is thanks to take the current date and compare it with the start_date
def get_remaining_amount(monthly_payment: float, instalments: int, start_date: date) -> float:
    current_date = date.today()
    real_total_amount = monthly_payment * instalments

    if (start_date.year, start_date.month) == (current_date.year, current_date.month):
        if current_date.day < start_date.day:
            return real_total_amount
        elif current_date.day >= start_date.day:
            return real_total_amount - monthly_payment
    elif current_date < start_date:
        return real_total_amount

    months = calculate_months(start_date)

    debt_paid_by_now = monthly_payment * months

    remaining_amount = real_total_amount - debt_paid_by_now

    return remaining_amount

