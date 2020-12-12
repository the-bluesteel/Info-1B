from random import randint

def selection_sort(a):
    comparaisons = 0
    affections = 0
    for i in range(len(a) - 1):
        p = i
        for j in range(i + 1, len(a)):
            comparaisons += 1
            if a[j] < a[p]:
                p = j
            comparaisons += 1
            if p > i:
                affections += 1
                a[i], a[p] = a[p], a[i]
    return affections, comparaisons

def partition(a, g, d, comparaisons, affections):
    p = a[d]
    i, j = g, d - 1
    while True:
        while i <= j and a[i] < p:
            comparaisons += 1
            i += 1
        while i <= j and a[j] > p:
            comparaisons += 1
            j -= 1
        comparaisons += 1
        if i <= j:
            affections += 1
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            affections += 1
            a[i], a[d] = p, a[i]
            return i, affections, comparaisons


def quicksort(a, g=0, d="", comparaisons = 0, affections = 0):
    if d == "":
        d = len(a) - 1
    if g >= d:
        return affections, comparaisons
    p, affections, comparaisons = partition(a, g, d, comparaisons, affections)
    quicksort(a, g, p - 1, comparaisons, affections)
    quicksort(a, p + 1, d, comparaisons, affections)


def insertion_sort(a):
    affections = 0
    comparaisons = 0
    for i in range(1, len(a)):
        x, j = a[i], i
        while j > 0 and a[j - 1] > x:
            comparaisons += 1
            affections += 1
            a[j] = a[j - 1]
            j -= 1
        comparaisons += 1
        if j < i:
            affections += 1
            a[j] = x
    return affections, comparaisons


a = b = c = [randint(1, 1000) for _ in range(100)]
n = selection_sort(a)
m = insertion_sort(b)
print(f"Selection Sort: {n[0]} affections and {n[1]} comparisons")
print(f"Insertion Sort: {m[0]} affections and {m[1]} comparisons")

"""
Selection Sort: n = 100 -> 4941 / 9900
Insertion Sort: n = 100 -> 27 / 123

"""