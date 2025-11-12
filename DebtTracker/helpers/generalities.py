import numpy_financial as npf
from datetime import date

def get_interest_rate(monthly_payment: float, total_amount: float, number_payments: int) -> float:
    rate = npf.rate(number_payments, -monthly_payment, total_amount, 0)
    rate = float(rate)
    return rate

def get_remaining_amount(monthly_payment: float, total_amount: float, number_payments: int, start_date: date) -> float:
    current_date = date.today()
    real_total_amount = monthly_payment * number_payments

    if (start_date.year, start_date.month) == (current_date.year, current_date.month):
        if current_date.day < start_date.day:
            return real_total_amount
        elif current_date.day >= start_date.day:
            return real_total_amount - monthly_payment
    elif current_date < start_date:
        return real_total_amount

    months = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)

    if current_date.day < start_date.day:
        months = months - 1

    if months >= number_payments:
        print("Congrutulations, your debt is already completly paid since it has been more months since the start date than your monthly payents."
              f"\nThere were {number_payments} monthly payments, but it has been {months} months since the first payment.\n")
        return -1
    
    debt_paid_by_now = monthly_payment * months

    if debt_paid_by_now > real_total_amount:
        print(f"There is an error either with the number of payments, '{number_payments}', with the amount of your monthly payment, '{monthly_payment}'"
              f", or with the total amount debt, '{total_amount}'. Since the money paid by now, '{debt_paid_by_now}' is bigger than the money you owed with interest,"
              f"'{real_total_amount}'.\n")
        return -1

    remaining_amount = real_total_amount - debt_paid_by_now

    return remaining_amount

