from chapitre_2.sorting import quicksort
from time import time_ns
l = [_ for _ in range(900)]


before = time_ns()

quicksort(l)

print(time_ns() - before)

# -> algorithm chooses a pivot and goes through every element and selects it as the pivot
# -> O(n*(n-1))