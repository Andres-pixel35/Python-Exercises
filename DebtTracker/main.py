from config import DEFAULT_USER_NAME, OPTIONS_OLD_USER, OPTIONS_NEW_USER, OPTIONS_INTEREST_RATE
from helpers import files_helpers, user_input, debts_functions, generalities

def main():
    debts: list[dict] = []
    old_user = files_helpers.file_exists()

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

        files_helpers.update_csv(debts)

        print("All your debts have been recorded successfully.\n\nWhat do you want to do now?")

        choice = user_input.get_choice_2(OPTIONS_NEW_USER)
        match choice:
            case 1:
                old_user = True
                print("")
            case 2:
                print("\nThank you for using my program.\nClosing")
                return 0

    if old_user:
        debts = files_helpers.read_csv()
        user_name = debts[0]["user_name"]
        print(f"Welcome back, {user_name.title()}.")

        debts = debts_functions.update_debt(debts)
        
        if len(debts) == 0:
            print(f"\nCongratulations, {user_name.title()}. You have paid off all your previous debts.\n\n"
                  "Do you want to add a new one? ", end="")
            choice = user_input.get_choice()
            if choice == 'y':
                debts = user_input.get_debts(user_name, debts)
            else:
                files_helpers.update_csv(debts)
                print("Closing.")
                return 0

        while True:
            print("\nWhat do you want to do?")
            choice = user_input.get_choice_2(OPTIONS_OLD_USER)
            match choice:
                case 1:
                    debts = user_input.get_debts(user_name, debts)

                    print("\nDo you want to continue? ", end="")
                    choice = user_input.get_choice()
                    if choice == 'n':
                        files_helpers.update_csv(debts)
                        print("Thank you for using my program.\nClosing.")
                        break
                    continue

                case 2:
                    print("\nHere you can choose to either view the interest rate of all your debts or choose one specifically. What do you want to do?")
                    choice = user_input.get_choice_2(OPTIONS_INTEREST_RATE)
                    match choice:
                        case 1:
                            generalities.show_interest_rate(debts)

                            print("\nDo you want to do something else? ", end="")
                            choice = user_input.get_choice()
                            if choice == 'n':
                                files_helpers.update_csv(debts)
                                print("Thank you for using my program.\nClosing.")
                                break
                            continue

                        case 2:
                            user_input.ask_debt_name_for_interest(debts)

                            print("\nDo you want to do something else? ", end="")
                            choice = user_input.get_choice()
                            if choice == 'n':
                                files_helpers.update_csv(debts)
                                print("Thank you for using my program.\nClosing.")
                                break
                            continue
            break



if __name__ == "__main__":
    main()


