# Here will be store all the constants.

# Here will be all the constants that can be MODIFIED to match the user's needs
MAX_DEBTS = 50 
FILENAME = "debt_records.csv" #this must be a csv file, otherwise the program won't work
FILENAME_PATH = "./data" + "/" + FILENAME # make sure you know what you are doing when changing relative paths
BASE_PATH = "." # here the same
HISTORY_FILENAME = "debts_history.csv"
HISTORY_PATH = "./data" + "/" + HISTORY_FILENAME
DAYS_IN_YEAR = 365 # Only if you know what are you doing
# END

# If the user decide to not enter a name, then '二百五' will be their name.
DEFAULT_USER_NAME = "二百五" # I mean, you could change this one as well if you like, but it is not my intention for you to do so.

FIELDNAMES = ["user_name", "debt_name", "start_date", "deadline", "monthly_payment", "instalments", "principal", "remaining_amount", "interest_rate"]

OPTIONS_OLD_USER = ["Add a new debt", "View interest rate", "View the remaining balance", "Adjust monthly payment", "Pay off now", "Exit"]
OPTIONS_NEW_USER = ["Continue", "Exit"]
OPTIONS_VIEW = ["View all", "Choose one"]
