from random import randint


def selection_sort(l, p=0):
    if p >= len(l):
        return
    d = l[p]
    i = p
    for c in range(p + 1, len(l)):
        if l[c] < d:
            d = l[c]
            i = c
    l[p], l[i] = l[i], l[p]
    selection_sort(l, p + 1)


l = [randint(1, 1000) for _ in range(10)]
print(l)
selection_sort(l)
print(l)
