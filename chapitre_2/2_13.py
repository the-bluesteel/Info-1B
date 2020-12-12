from chapitre_2.sorting import selection_sort, insertion_sort
from random import randint
from time import time_ns

a = b = [randint(1, 101) for _ in range(12000)]

before = time_ns()

selection_sort(a)

print(f"{time_ns() - before} ns (Selection Sort)")

before = time_ns()
insertion_sort(b)
print(f"{time_ns() - before} ns (Insertion Sort)")

"""
n= 6000 -> 1.7 seconds to 0 seconds
n = 120000 -> 7 seconds to 0 seconds


"""