import numpy_financial as npf

def get_interest_rate(monthly_payment: float, total_amount: float, number_payments: int) -> float:
    rate = npf.rate(number_payments, -monthly_payment, total_amount, 0)
    rate = float(rate)
    return rate

