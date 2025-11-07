#Here will been all the funtions to general things, like asking and storing inputs, some math and things like that

from datetime import datetime

# it allows the user to enter their debts and it creates a list of dictionaries, the user can enter up to MAX_DEBTS debts.
# some information is automatically fill up since there is no need for the user to manually enter that kind of information.
def get_debts(MAX_DEBTS: int, user_name: str) -> list:
    debts = []
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
                end_date = datetime.strptime(input("Enter the deadline (YYYY/MM/DD): "), "%Y/%m/%d").date()

                if start_date > end_date:
                    print("The deadline cannot be prior to the start date. Please try again.\n")
                    continue
                break
            except ValueError:
                print("Invalid format. Please try again (example: 2023/06/10).\n")

        while True:
            try:
                payment_monthly = float(input("Please enter the amount of money due monthly: "))
                total_amount = float(input("Please enter the original amount borrowed: "))

                if payment_monthly < 0 or total_amount < 0:
                    raise ValueError
                break
            except ValueError:
                print("You must enter a positive integer or float, but you did not. Please try again.\n")

        next_debt = input("Do you want to add another debt? (y/n): ")
        if next_debt.lower() in valid_options:
            match next_debt.lower():
                case ('y'):
                    continue
                case ('n'):
                    break
        else:
            print(f"Molto malo, {user_name}.\nClosing.\n")
            break

    return debts

        

