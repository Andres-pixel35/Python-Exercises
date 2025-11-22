import os
import csv
from config import FILENAME, FILENAME_PATH, BASE_PATH, FIELDNAMES, HISTORY_PATH

# searchs from the search path a file that match with filename, if found returns true, false otherwise
def file_exists() -> bool:
    for _, _, files in os.walk(BASE_PATH):
        if FILENAME in files:
            return True
    return False

# the following tho functions will handle the functionalities of read and write for 'debt_records.csv' 
def update_records(debts: list):
    with open(FILENAME_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        
        writer.writeheader()

        for debt in debts:
            writer.writerow(debt)

def read_records() -> list:
    with open(FILENAME_PATH, mode="r", newline="", encoding="utf-8") as file:
        tmp_list = []
        csv_reader = csv.DictReader(file)

        for debt in csv_reader:
            tmp_list.append(debt)

        return tmp_list

# the following two functions are related to the functionalities read and write of debts_history
def write_history(new_debts: list, old_user: bool):
    if not old_user:
        try:
            os.remove(HISTORY_PATH)
        except FileNotFoundError:
            pass

    with open(HISTORY_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not old_user:
            writer.writeheader()

        for debt in new_debts:
            writer.writerow(debt)

def read_history() -> str:
    try:
        with open(HISTORY_PATH, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            first_row = next(reader)

            return first_row["user_name"]

    except FileNotFoundError:
        raise FileNotFoundError
    except StopIteration:
        raise FileNotFoundError



