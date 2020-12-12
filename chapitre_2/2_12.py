from random import randint

def insertion_sort(a, start=1):
    if start >= len(a):
        return
    x, j = a[start], start
    while j > 0 and a[j - 1] > x:
        a[j] = a[j - 1]
        j -= 1
    if j < start:
        a[j] = x
    return insertion_sort(a, start+1)


l = [randint(1, 100) for _ in range(20)]

print(l)
insertion_sort(l)
print(l)
