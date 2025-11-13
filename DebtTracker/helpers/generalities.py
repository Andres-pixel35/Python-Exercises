from datetime import date

def calculate_months(start_date: date) -> int:
    current_date = date.today()
    months = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)

    if current_date.day < start_date.day:
        months = months - 1

    return months
