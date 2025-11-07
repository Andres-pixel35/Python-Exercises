# Here will been all the functions related to the use and manipulation of files, like read and write.

import os

# searchs from the search path a file that match with filename, if found returns true, false otherwise
def file_exists(filename: str, search_path: str) -> bool:
    for _, _, files in os.walk(search_path):
        if filename in files:
            return True
    return False

