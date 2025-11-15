from config import FILENAME, BASE_PATH, DEFAULT_USER_NAME, FIELDNAMES
from helpers import files_helpers, user_input

def main():
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

        files_helpers.update_csv(FIELDNAMES, debts, FILENAME, old_user)

        print("All your debts have been recorded successfully.\n\nWhat do you want to do now?")
        options = ["Continue", "Exit"]

        choice = user_input.get_choice_2(options)
        match choice:
            case 1:
                old_user = True
            case 2:
                print("\nThank you for using my program.\nClosing")
                return 0

    if old_user:
        print("sayonara")

if __name__ == "__main__":
    main()


