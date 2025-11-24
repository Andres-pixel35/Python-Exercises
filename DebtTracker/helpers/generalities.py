from datetime import date, datetime
import helpers.debts_functions as hd

def calculate_months(start_date: date) -> int:
    current_date = date.today()

    if current_date < start_date:
        return 0
    else:
        months = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)
        months = months + 1 # since my program counts the start_date as the first instalment, i need to make this change here to ensure all the payments are count

        if current_date.day < start_date.day:
            months = months - 1

        return months

def check_name_debt(debt_name: str, debts: list) -> bool:
    for dictionary in debts:
        if dictionary["debt_name"] == debt_name.lower():
            return False

    return True

def create_list_dict(keys: list, values: list, debts: list) -> dict:
    temp_dict = {keys[i]: values[i] for i in range (len(keys))}

    debts.append(temp_dict)

    return temp_dict

def show_interest_rate_loop(debts: list):
    print("\nDebt name: insterest rate")
    for debt in debts:
        print(f"{debt["debt_name"].title()}: {debt["interest_rate"]}%")

def show_remaining_amount(debt: dict):
    start_date = datetime.strptime(debt["start_date"], "%Y/%m/%d").date()
    months = calculate_months(start_date)
    months_left = int(debt["instalments"]) - months
    monthly_payment = float(debt["monthly_payment"])
    insterest_rate = round(float(debt["interest_rate"]) / 100, 2)

    remaining_amount = hd.calculate_remaining_balance(monthly_payment, insterest_rate, months_left)

    print(f"{debt["debt_name"].title()}: "
          f"You still owe {remaining_amount["principal"]} of the loan balance, and you will pay {remaining_amount["interest"]} in interest over the remaining months.")






