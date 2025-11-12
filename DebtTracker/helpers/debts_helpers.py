#Here will been all the funtions to general things, like asking and storing inputs, some math and things like that

from config import MAX_DEBTS #type: ignore
from datetime import datetime
from dateutil.relativedelta import relativedelta
from helpers.generalities import get_interest_rate, get_remaining_amount #type: ignore

# it allows the user to enter their debts and it creates a list of dictionaries, the user can enter up to MAX_DEBTS debts.
# some information is automatically fill up since there is no need for the user to manually enter that kind of information.
def get_debts(user_name: str, debts: list) -> list:
    valid_options = ['y', 'n']
    print(f"Now, please enter the following information related to your debts.\nRemeber that you can only enter up to {MAX_DEBTS} differents debts.\n")

    while True:
        number_debts = len(debts)
        if number_debts == MAX_DEBTS:
            print("You have reached the maximum amount of debts you can record.\n")
            return debts

        debt_name = input(f"Please enter the name of your debt number {number_debts + 1}: ")

        if debt_name.strip() == "":
            print("You must enter a name for each one of your debts. Please try again.\n")
            continue
        
        while True:
            try:
                start_date = datetime.strptime(input("Enter the start date (YYYY/MM/DD): "), "%Y/%m/%d").date()
                break
            except ValueError:
                print("Invalid format. Please try again (example: 2023/06/10).\n")

        while True:
            try:
                payments = int(input("Please enter the total number of monthly payments: "))
                payment_monthly = float(input("Please enter the amount of money due monthly: "))
                total_amount = float(input("Please enter the original amount borrowed: "))

                if payment_monthly < 1 or total_amount < 1 or payments < 1:
                    raise ValueError

                deadline = start_date + relativedelta(months=payments)
                break
            except ValueError:
                print("You must enter a positive integer or float greater than zero (0), but you did not. Please try again.\n")

        interest_rate = get_interest_rate(payment_monthly, total_amount, payments)

        remaining_amount = get_remaining_amount(payment_monthly, total_amount, payments, start_date)
        
        next_debt = input("Do you want to add another debt? (y/n): ")
        if next_debt.lower() in valid_options:
            match next_debt.lower():
                case ('y'):
                    continue
                case ('n'):
                    print("Closing.\n")
                    break
        else:
            print(f"Molto malo, {user_name}.\nClosing.\n")
            break

    return debts
