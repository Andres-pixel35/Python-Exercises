import os
import csv
from config import FILENAME, FILENAME_PATH, BASE_PATH, FIELDNAMES

# searchs from the search path a file that match with filename, if found returns true, false otherwise
def file_exists() -> bool:
    for _, _, files in os.walk(BASE_PATH):
        if FILENAME in files:
            return True
    return False

# Only when it's the first time of the user using this program tha headers shall be written
def update_csv(debts: list):
    with open(FILENAME_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        
        writer.writeheader()

        for debt in debts:
            writer.writerow(debt)

def read_csv() -> list:
    with open(FILENAME_PATH, mode="r", encoding="utf-8") as file:
        tmp_list = []
        csv_reader = csv.DictReader(file)

        for debt in csv_reader:
            tmp_list.append(debt)

        return tmp_list

