from config import MAX_DEBTS, FIELDNAMES 
from datetime import datetime
from dateutil.relativedelta import relativedelta
from helpers.debts_functions import get_interest_rate, get_remaining_amount, check_debt 
from helpers.generalities import create_list_dict, check_name_debt

# to check out that when the user is asked to enter 'y/n', they actually do that
def get_choice() -> str:
    valid_options = ['y', 'n']
    while True:
        choice = input("(y/n): ").lower()
        if choice not in valid_options:
            continue
        return choice

# it allows the user to enter their debts and it creates a list of dictionaries, the user can enter up to MAX_DEBTS debts.
# some information is automatically fill up since there is no need for the user to manually enter that kind of information.    
def get_debts(user_name: str, debts: list) -> list:
    print(f"Now, please enter the following information related to your debts.\nRemeber that you can only enter up to {MAX_DEBTS} different debts.\n")

    while True:
        number_debts = len(debts)
        if number_debts == MAX_DEBTS:
            print("You have reached the maximum amount of debts you can record.\n\nClosing")
            return debts

        debt_name = input(f"Please enter the name of your debt number {number_debts + 1}: ")

        if debt_name.strip() == "":
            print("You must enter a name for each one of your debts. Please try again.\n")
            continue
        elif not check_name_debt(debt_name, debts):
            print(f"A debt called {debt_name.title()} already exists. Please try again.\n")
            continue
        
        while True:
            try:
                start_date = datetime.strptime(input("Enter the start date (YYYY/MM/DD): "), "%Y/%m/%d").date()
                instalments = int(input("Please enter the number of your instalments: "))
                payment_monthly = float(input("Please enter the amount of money due monthly: "))
                total_amount = float(input("Please enter the original amount borrowed: "))

                if payment_monthly < 1 or total_amount < 1 or instalments < 1:
                    print("You must enter a positive number greater than 0. Please try again.\n")
                    continue

                if not check_debt(payment_monthly, total_amount, instalments, start_date):
                    print("")
                    continue

                deadline = start_date + relativedelta(months=instalments)

                break
            except ValueError:
                print("An error occurred with the data you entered. Please check and try again.\n")

        interest_rate = get_interest_rate(payment_monthly, total_amount, instalments)

        remaining_amount = get_remaining_amount(payment_monthly, instalments, start_date)

        start_date = start_date.strftime("%Y-%m-%d")
        deadline = deadline.strftime("%Y-%m-%d")

        temp_list = [user_name, debt_name, start_date, deadline, payment_monthly, instalments, total_amount, remaining_amount, interest_rate]

        debts = create_list_dict(FIELDNAMES, temp_list, debts)

        print(f"\nYour debt {debt_name.title()} has been added successfully.\nDo you want to add another debt? ", end="")
        choice = get_choice()
        if choice == 'y':
            print("")
            continue

        print("Closing.")
        break
    return debts
