import helpers

FILENAME = 'debt_records.csv'
BASE_PATH = '.'

old_user = helpers.file_exists(FILENAME, BASE_PATH)

print("=== Welcome to your personal debt tracker! ===\n\nHere, you can not only record your debts but also automatically view their interest rates," 
    " see how much you could save by paying them off now, and how much youcould save by increasing your monthly payments.\nMoreover," 
    " your information will be automatically updated each time you run this programme.")

   

