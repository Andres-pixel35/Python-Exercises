from datetime import date

def calculate_months(start_date: date) -> int:
    current_date = date.today()

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

def create_list_dict(keys: list, values: list, debts: list) -> list:
    temp_dict = {keys[i]: values[i] for i in range (len(keys))}

    debts.append(temp_dict)

    return debts


