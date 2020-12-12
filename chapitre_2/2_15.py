from chapitre_2.sorting import quicksort as qs
from time import time_ns
from random import randint

def partition(a, g, d):
    p = a[d]
    if d - g >= 10:
        p = get_pivot(a[g], a[(d - g) // 2], a[d])
    else:
        return -200
    i, j = g, d - 1
    while True:
        while i <= j and a[i] < p:
            i += 1
        while i <= j and a[j] > p:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            a[i], a[d] = p, a[i]
            return i


def quicksort(a, g=0, d=""):
    if d == "":
        d = len(a) - 1
    if g >= d:
        return
    p = partition(a, g, d)
    if p == -200:
        return
    quicksort(a, g, p - 1)
    quicksort(a, p + 1, d)


def get_pivot(a, b, c):
    if a >= b >= c or a <= b <= c:
        return b
    if a >= c >= b or a <= c <= b:
        return c
    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        x, j = a[i], i
        while j > 0 and a[j - 1] > x:
            a[j] = a[j - 1]
            j -= 1
        if j < i:
            a[j] = x


def modified_quicksort(a):
    quicksort(a)
    insertion_sort(a)

a = [randint(1, 100) for _ in range(1000000)]
b = a[:]

before = time_ns()
modified_quicksort(a)
print(f"{time_ns() - before} ns - Modified")


before = time_ns()
qs(b)
print(f"{time_ns() - before} ns - Original")


"""
Modified: n = 1000000 -> 1.5 sec

Original: n = 1000000 -> 1.7 sec

"""