from random import randint
from my_main_functions import Stack


def partition(a, g, d):
    p  = a[d]
    i, j  = g, d-1
    while True:
        while i <= j and a[i] < p:
            i+= 1
        while i <= j and a[j] > p:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            a[i], a[d] = p, a[i]
            return i


def quicksort(a, g = 0, d =""):
    if d == "":
        d = len(a) -1
    stack = Stack()

    stack.push(g)
    stack.push(d)

    while not stack.is_empty():
        h = stack.pop()
        l = stack.pop()

        p = partition(a,l,h)

        if p -1 > l:
            stack.push(l)
            stack.push(p - 1)

        if p + 1 < h:
            stack.push(p + 1)
            stack.push(h)

"""
l = [randint(1,1000) for _ in range(10)]
print(l)
quicksort(l)
print(l)
"""
