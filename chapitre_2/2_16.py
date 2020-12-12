from time import time_ns
from chapitre_2.sorting import quicksort
from random import randint

l = [randint(1, 199) for _ in range(1000000)]
a = l[:]
b = l[:]


before = time_ns()

sorted(a)

print(f"{time_ns() - before} - sorted function")


before = time_ns()

quicksort(b)

print(f"{time_ns() - before} - quicksort function")

before = time_ns()

l.sort()

print(f"{time_ns() - before} - .sort() function")

"""
sorted() -> n = 1000000 -> 78789300 ns
quicksort() -> n = 1000000 -> 1793732900 ns
.sort() -> n = 1000000 -> 75798600 ns

"""