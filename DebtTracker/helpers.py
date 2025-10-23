import os

MAX_DEBTS = 50

# searchs from the search path a file that match with filename, if found returns true, false otherwise
def file_exists(filename: str, search_path: str) -> bool:
    for _, _, files in os.walk(search_path):
        if filename in files:
            return True
    return False

# it allows the user to enter their debts and it creates a list of dictionaries, the user can enter up to MAX_DEBTS debts.
# some information is automatically fill up since there is no need for the user to manually enter that kind the information.
def get_debts(number_debts: int) -> list:
    return "not yet implemented"
