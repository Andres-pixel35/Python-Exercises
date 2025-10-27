import random

# number of times you want to throw the coin REPEAT_EVENT times
NUMBER_TRIALS = 1000000
# number of times it will throw the coin
REPEAT_EVENT = 6
# number of times it has to be either 'H' ot 'T' in a row
REPEATED_EVENT = 5

t_five_times = 0
h_five_times = 0
sixth_h_AH = 0
sixth_t_AH = 0
sixth_h_AT = 0
sixth_t_AT = 0

for _ in range(NUMBER_TRIALS):
    results = [random.choice(['H', 'T']) for _ in range(REPEAT_EVENT)]

    if results[:REPEATED_EVENT] == ['H']*REPEATED_EVENT:
        h_five_times = h_five_times + 1
        
        if results[REPEATED_EVENT] == 'H':
            sixth_h_AH = sixth_h_AH + 1
        else:
            sixth_t_AH = sixth_t_AH + 1

    elif results[:REPEATED_EVENT] == ['T']*REPEATED_EVENT:
        t_five_times = t_five_times + 1
        
        if results[REPEATED_EVENT] == 'H':
            sixth_h_AT = sixth_h_AT + 1
        else:
            sixth_t_AT = sixth_t_AT + 1

print(f"\n=== H ===\n\nThe number of times 'H' was the result five times in a row: {h_five_times}\n"
      f"And the number of times 'H' was the result again on the sixth throw: {sixth_h_AH} and for 'T' it was: {sixth_t_AH}\n")

print(f"\n=== T ===\n\nThe number of times 'T' was the result five times in a row: {t_five_times}\n"
      f"And the number of times 'T' was the result again on the sixth throw: {sixth_t_AT} and for 'H' it was: {sixth_h_AT}\n")


percentage_h = float((h_five_times/NUMBER_TRIALS) * 100)
percentage_t = float((t_five_times/NUMBER_TRIALS) * 100)

percentage_sixth_h_AH = ((sixth_h_AH/h_five_times) * 100)
percentage_sixth_t_AH = ((sixth_t_AH/h_five_times) * 100)

percentage_sixth_h_AT = ((sixth_h_AT/t_five_times) * 100)
percentage_sixth_t_AT = ((sixth_t_AT/t_five_times) * 100)

print(f"Out of the {NUMBER_TRIALS} trials where the coin was threw {REPEAT_EVENT} times, there was a {percentage_h:.2f}% chance of 'H' being the result 5 times in a row"
      f" and a {percentage_t:.2f}% chance for 'T'.\n\nWhen the case was 'H', there was a {percentage_sixth_h_AH:.2f}% chance of 'H' being the sixth result and "
      f"a {percentage_sixth_t_AH:.2f}% chance for 'T'.\n\nFor the case of 'T', there was a {percentage_sixth_h_AT:.2f}% chance of 'H' being the sixth result and "
      f"a {percentage_sixth_t_AT:.2f}% chance for 'T'.\n")
