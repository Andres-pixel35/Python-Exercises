def open_rest_doors(doors: list, choice: int, winner: int) -> list:
    new_doors = doors[:]
 
    for x in doors:
        if len(new_doors) > 2:
            if not x == choice and not x == winner:
                new_doors.remove(x)

    return new_doors

def get_choice(doors: list, original_choice: str) -> int:
    while True:
        try:
            for i in doors:
                print(f"Door {i}")

            # I'm doing this because I want to reflect in the error message what was exactly the user's input
            original_choice = input("\nChoose a door: ")

            choice = int(original_choice)

            if choice not in doors:
                raise ValueError
            return choice

        except ValueError:
            print(f"You must enter a number related to a door, but you entered '{original_choice}'. Please try again.")


