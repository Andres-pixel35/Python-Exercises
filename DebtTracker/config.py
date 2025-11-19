# Here will be store all the constants.

# Here will be all the constants that can be MODIFIED to fit the user's needs
MAX_DEBTS = 50
FILENAME = "debt_records.csv"
BASE_PATH = "."
# END

# If the user decide to not enter a name, then '二百五' will be their name.
DEFAULT_USER_NAME = "二百五"

FIELDNAMES = ["user_name", "debt_name", "start_date", "deadline", "monthly_payment", "instalments", "total_amount", "remaining_amount", "interest_rate"]

OPTIONS_OLD_USER = ["Add a new debt", "View interest rate", "Adjust monthly payment", "Pay off now", "Exit"]
OPTIONS_NEW_USER = ["Continue", "Exit"]
OPTIONS_INTEREST_RATE = ["View all", "Choose one"]
