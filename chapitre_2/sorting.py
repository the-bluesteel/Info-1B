def selection_sort(a):
    for i  in range(len(a) -1):
        p = i
        for j in range(i + 1, len(a)):
            if a[j] < a[p]:
                p = j
            if p > i:
                a[i], a[p] = a[p], a[i]

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
    if g >= d:
        return
    p = partition(a, g, d)
    quicksort(a, g, p - 1)
    quicksort(a, p+1, d)


def insertion_sort(a):
    for i in range(1, len(a)):
        x, j = a[i], i
        while j > 0 and a[j - 1] > x:
            a[j] = a[j - 1]
            j -= 1
        if j < i:
            a[j] = x
            