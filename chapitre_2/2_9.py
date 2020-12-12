from random import randint


def partition(a, g, d):
    p = a[d]
    if d - g >= 3:
        p = get_pivot(a[g], a[(d-g)//2], a[d])

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
    quicksort(a, g, p - 1)
    quicksort(a, p + 1, d)


def get_pivot(a, b, c):
    if a >= b >= c or a <= b <= c:
        return b
    if a >= c >= b or a <= c <= b:
        return c
    return a


l = [randint(1, 1000) for _ in range(50)]
print(l)
quicksort(l)
print(l)
