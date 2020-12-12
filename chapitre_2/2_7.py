from random import randint
from time import time_ns
from chapitre_2.sorting import quicksort, selection_sort

n = int(input("Enter n: "))

l = [randint(1, 10000) for _ in range(n)]


a, b = l, l


before = time_ns()
selection_sort(b)
print(time_ns() - before)

# n=4500 -> 1 sec
# n=6500 -> 2 sec
# n=9000 -> 4 sec
# n=13000 -> 9 sec
# n=18000 -> 17 sec
# n=36000 -> 68 sec