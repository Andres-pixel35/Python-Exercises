import helpers
import random

# you can change this constant if you want to do the experiment with a different number of doors. Although, it has to be at least three to work.
NUMBER_DOORS = 3

doors = [x for x in range(1,NUMBER_DOORS + 1)]

winner = random.randint(1,NUMBER_DOORS)

original_choice = ""

print(f"Welcome to the Monty Hall game, in front of you are {NUMBER_DOORS}, behind one of them is waiting a fancy travel to Norway for you and all your family "
      "and in the other doors, there is a cute goat. Please choose one of the following doors.\n")

choice = helpers.get_choice(doors, original_choice)

new_doors = helpers.open_rest_doors(doors, choice, winner)

print("\nNow there are only two doors left to be opened: ")
for x in new_doors:
    print(f"Door {x}")

while True:
    valid_choices = ['y', 'n']
    change_door = input(f"\nYou chose the door {choice}, do you want to change your choice? (y/n):  ")

    if change_door.lower() not in valid_choices:
        print(f"You must enter 'y' or 'n', but you entered '{change_door}'. Please try again.")
        continue
    break

if change_door.lower() == 'y':
    for x in new_doors:
        if choice != x:
            choice = x
            break

if choice == winner:
    print("\nCongratulations, you've won the travel to Norway.")
else:
    print("\nUnfortunately you haven't won the travel to Norway, but now you have a cute goat all for yourself.\n"
          f"The winner door was {winner}, but you chose {choice}.")




