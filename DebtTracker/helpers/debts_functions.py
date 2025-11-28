import numpy_financial as npf
from datetime import date, datetime
import helpers.user_input as hu
from helpers.generalities import calculate_months
from config import DAYS_IN_YEAR

def calculate_interest_rate(monthly_payment: float, principal: float, instalments: int) -> float:
    rate = npf.rate(instalments, -monthly_payment, principal, 0)
    rate = float(rate)
    if abs(rate) < 1e-8:
        return 0.0
    return rate 

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
def calculate_remaining_amount(monthly_payment: float, instalments: int, start_date: date) -> float:
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

    new_remaining_amount = real_total_amount - debt_paid_by_now

    return round(new_remaining_amount,2)

def update_debt(debts: list) -> list:
    updated_list = []
    for debt in debts:
        start_date = datetime.strptime(debt["start_date"], "%Y/%m/%d").date()
        monthly_payment = float(debt["monthly_payment"])
        instalments = int(debt["instalments"])

        remaining_amount = calculate_remaining_amount(monthly_payment, instalments, start_date)

        if remaining_amount > 0:
            debt["remaining_amount"] = remaining_amount
            updated_list.append(debt)
        else:
            name = debt["debt_name"]
            print(f"Congratulations for paying off your debt {name.title()}\n")

    return updated_list

# Return remaining principal and total future interest
def calculate_remaining_balance(monthly_payment: float, monthly_rate: float, months_left: int) -> dict:
    r = monthly_rate
    a = monthly_payment
    n = months_left

    if r == 0:
        principal = a * n
        future_interest = 0.0

    else:
        principal = npf.pv(r, n, -a, fv=0, when="end")

        principal = abs(principal)

        total_remaining_payments = a * n
        future_interest = total_remaining_payments - principal

    return {
        "principal": principal,
        "interest": future_interest,
    }

def compare_payments(monthly_rate: float, principal: float, old_payment: float):
    while True:
        new_payment = 0
        try:
            new_payment = float(input("Please enter the amount of the new payment: "))
            if new_payment < 0:
                raise ValueError
            elif new_payment <= old_payment:
                print(f"The new payment must be higher than the previous ({old_payment}). Please try again.\n")
                continue
        except ValueError:
            print(f"You must enter a positive float, but you entered: {new_payment}. Please try again.\n")
            continue

        def simulate(payment: float, is_new_payment: bool):
            last_payment = 0
            bal = principal
            months = 0
            interest_sum = 0.0

            while True:
                if bal <= 0:
                    return months, interest_sum, last_payment

                i = bal * monthly_rate
                c = payment - i

                if c <= 0:
                    print("Payment too small to cover even the monthly interest. Please try again.\n")
                    return None

                if c > bal:
                    # this is the final payment
                    last_payment = i + bal
                    bal = 0
                    interest_sum += i
                    if is_new_payment:
                        months += 1
                        continue
                    continue 

                last_payment = payment
                bal -= c
                interest_sum += i
                months += 1

        result_old = simulate(old_payment, False)
        result_new = simulate(new_payment, True)

        if result_old is None or result_new is None:
            continue

        old_months, old_interest, old_last_payment = result_old
        new_months, new_interest, new_last_payment = result_new

        print(f"\nOld finish: {old_months} months, interest ${old_interest:.2f}, last payment ${old_last_payment:.2f}")
        print(f"New finish: {new_months} months, interest ${new_interest:.2f}, last payment ${new_last_payment:.2f}")
        print(f"Months saved: {old_months - new_months}")
        print(f"Money saved: ${old_interest - new_interest:.2f}")

        break

def calculate_interim_payoff(remaining_principal: float, monthly_rate: float, days_since_last_payment: int, prepayment_fine: float) -> float:
    if days_since_last_payment == 0:
        accrued_interest = 0.0
    else:
        monthly_rate_decimal = monthly_rate 

        nominal_annual_rate = monthly_rate_decimal * 12
        
        daily_rate_decimal = nominal_annual_rate / DAYS_IN_YEAR

        accrued_interest = remaining_principal * daily_rate_decimal * days_since_last_payment

    total_payoff_amount = round(remaining_principal + accrued_interest + prepayment_fine, 2)

    return total_payoff_amount
