from config import FILENAME, BASE_PATH, DEFAULT_USER_NAME
from helpers import files_helpers, user_input

debts: list[dict] = []
old_user = files_helpers.file_exists(FILENAME, BASE_PATH)

if not old_user:
    print(
        "=== Welcome to your personal debt tracker! ===\n\nHere, you can not only record your debts but also automatically view their interest rates,"
        " see how much you could save by paying them off now, and how much you could save by increasing your monthly payments.\nMoreover,"
        " your information will be automatically updated each time you run this programme.\n"
    )

    user_name = input(f"Please enter your name (default '{DEFAULT_USER_NAME}'): ").lower()

    if user_name.strip() == "":
        user_name = DEFAULT_USER_NAME

    debts = user_input.get_debts(user_name, debts)
