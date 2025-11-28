from config import OPTIONS_OLD_USER, OPTIONS_NEW_USER, OPTIONS_VIEW
from helpers import files_helpers, user_input, debts_functions, generalities

def main():
    debts: list[dict] = []
    old_user = files_helpers.file_exists()

    if not old_user:
        print("=== PLEASE READ THE README FILE BEFORE EXECUTING THIS PROGRAM ===\n")
        print(
            "=== Welcome to your personal debt tracker! ===\n\nHere, you can not only record your debts but also automatically view their interest rates,"
            " see how much you could save by paying them off now, and simulate how much you could save by increasing your monthly payments.\nMoreover,"
            " your information will be automatically updated each time you run this programme.\n"
        )

        user_name = user_input.ask_users_name()

        debts = user_input.get_debts(user_name, debts, old_user)

        files_helpers.update_records(debts)

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
        user_name = ""
        debts = files_helpers.read_records()

        if debts and debts[0].get("user_name"):
            user_name = debts[0]["user_name"] 
        else:
            try:
                user_name = files_helpers.read_history()
            except FileNotFoundError:
                print("We beg your pardon, due to an error we cannot longer recall your name.")
                user_name = user_input.ask_users_name()
                old_user = False

        print(f"Welcome back, {user_name.title()}.")

        debts = debts_functions.update_debt(debts)
        files_helpers.update_records(debts)
        
        if len(debts) == 0:
            print(f"\nCongratulations, {user_name.title()}. You have paid off all your previous debts.\n\n"
                  "Do you want to add a new one? ", end="")
            choice = user_input.get_choice()
            if choice == 'y':
                debts = user_input.get_debts(user_name, debts, old_user)
            else:
                print("Closing.")
                return 0

        while True:
            print("\nWhat do you want to do?")
            choice = user_input.get_choice_2(OPTIONS_OLD_USER)
            match choice:
                case 1:
                    debts = user_input.get_debts(user_name, debts, old_user)

                    if not user_input.ask_continue(debts):
                        break
                    continue

                case 2:
                    print("\nHere you can choose to either view the interest rate of all your debts or choose one specifically. What do you want to do?")
                    choice = user_input.get_choice_2(OPTIONS_VIEW)
                    match choice:
                        case 1:
                            generalities.show_interest_rate_loop(debts)

                        case 2:
                            debt = user_input.ask_debt_name(debts, "interest rate")
                            rate = round(float(debt["interest_rate"]) * 100, 2)
                            print(f"\nThe insterest rate of {debt["debt_name"].title()} is {rate}%")

                    if not user_input.ask_continue(debts):
                        break
                    continue

                case 3:
                    print("\nHere you can choose to either view the remaining amount of all your debts or choose one specifically. What do you want to do?")
                    choice = user_input.get_choice_2(OPTIONS_VIEW)
                    print("")
                    match choice:
                        case 1:
                            for debt in debts:
                                balance = generalities.calculate_balance(debt)
                                print(f"{debt["debt_name"].title()}: "
                                    f"You still owe ${round(balance["principal"], 2)} of the loan balance, and you will pay ${round(balance["interest"], 2)} "
                                    "in interest over the remaining months.")
                        case 2:
                            debt = user_input.ask_debt_name(debts, "principal remaining")
                            balance = generalities.calculate_balance(debt)
                            print(f"{debt["debt_name"].title()}: "
                                f"You still owe ${round(balance["principal"], 2)} of the loan balance, and you will pay ${round(balance["interest"], 2)} "
                                "in interest over the remaining months.")

                    if not user_input.ask_continue(debts):
                        break
                    continue

                case 4:
                    print("\nHere you can simulate how much could you save if you were to increase your monthly payments.")
                    debt = user_input.ask_debt_name(debts, "payments")
                    generalities.show_change_payments(debt)

                    if not user_input.ask_continue(debts):
                        break
                    continue
                
                case 5:
                    print("\nHere you can pay off any debt now and see how much you could save by doing that")
                    debt = user_input.ask_debt_name(debts, "principal remaining")  

                    principal = generalities.calculate_balance(debt)
                    monthly_rate = float(debt["interest_rate"])
                    days, fine_amount = user_input.get_days_fine(principal["principal"])

                    payoff = debts_functions.calculate_interim_payoff(principal["principal"], monthly_rate, days, fine_amount)

                    money_saved = round(float(debt["remaining_amount"]) - payoff, 2)

                    print(f"\nIn order to pay off {debt["debt_name"].title()} you need ${payoff}."
                          f" If you pay off your debt today you can save ${money_saved}. \nDo you want to pay off your debt? ", end="")
                    choice = user_input.get_choice()
                    if choice == 'y':
                        debts.remove(debt)
                        if debts:
                            if not user_input.ask_continue(debts):
                                break
                            continue
                        else:
                            print("\nRight know you don't have any debt recorded. Do you want to add one?", end="")
                            choice2 = user_input.get_choice()
                            if choice2 == 'n':
                                files_helpers.update_records(debts)
                                print("Thank you for using my program.\nCosing")
                                break
                            else:
                                debts = user_input.get_debts(user_name, debts, old_user)
                                continue
                    else:
                        if not user_input.ask_continue(debts):
                            break
                        continue
                
                case 6:
                    files_helpers.update_records(debts)
                    print("\nThank you for using my program.\nClosing")
                    break
            break

if __name__ == "__main__":
    main()
