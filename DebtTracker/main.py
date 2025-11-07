from helpers import files_helpers, debts_helpers

MAX_DEBTS = 50
FILENAME = "debt_records.csv"
BASE_PATH = "."

# If the user decide to not enter a name, then '二百五' will be their name.
DEFAULT_USER_NAME = "二百五"

old_user = files_helpers.file_exists(FILENAME, BASE_PATH)

if not old_user:
    print(
        "=== Welcome to your personal debt tracker! ===\n\nHere, you can not only record your debts but also automatically view their interest rates,"
        " see how much you could save by paying them off now, and how much youcould save by increasing your monthly payments.\nMoreover,"
        " your information will be automatically updated each time you run this programme.\n"
    )

    user_name = input(f"Please enter your name (default '{DEFAULT_USER_NAME}'): ").capitalize()

    if user_name.strip() == "":
        user_name = DEFAULT_USER_NAME

    debts = debts_helpers.get_debts(MAX_DEBTS, user_name)
    print(debts)
