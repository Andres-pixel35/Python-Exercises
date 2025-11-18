import os
import csv

# searchs from the search path a file that match with filename, if found returns true, false otherwise
def file_exists(filename: str, search_path: str) -> bool:
    for _, _, files in os.walk(search_path):
        if filename in files:
            return True
    return False

# Only when it's the first time of the user using this program tha headers shall be written
def update_csv(fieldnames: list, debts: list, filename: str, old_user: bool):
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if not old_user:
            writer.writeheader()

        for debt in debts:
            writer.writerow(debt)

def read_csv(filename: str) -> list:
    with open(filename, mode="r", encoding="utf-8") as file:
        tmp_list = []
        csv_reader = csv.DictReader(file)

        for debt in csv_reader:
            tmp_list.append(debt)

        return tmp_list

