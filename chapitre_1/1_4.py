from my_main_functions import fact
from my_string_functions import count_of_numbers
from my_other_functions import get_stars

s = input("Enter a string: ")
n = count_of_numbers(s)
f = fact(n)
print(n, f)
print(get_stars(n), get_stars(f))