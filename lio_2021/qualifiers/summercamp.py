from string import ascii_letters, ascii_uppercase
import sys

# get amount of first names
n = int(input())

# dict that maps a letter to a value, here mapping first caracter to how many names start with it
letter_with_value = {}

# read first names while checking of constraints are being met correctly
for _ in range(int(n)):
    name = input()
    starting_letter = name[0].upper()
    # add one to how often a name with a specific first character appears
    if starting_letter in letter_with_value.keys():
        letter_with_value[starting_letter] += 1
    else:
        letter_with_value[starting_letter] = 1

# store all first characters that appear at least 5 times
organised = [c for c, value in letter_with_value.items() if value >= 5]

# return stored first characters in alphabetic order
print("".join(sorted(organised)) if len(organised) > 0 else "/")
