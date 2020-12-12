from random import randint
from time import time_ns


def insertionsort(a):
    """Best case O(n) - Average Case O(n^2)"""
    if len(a) > 0:
        for i in range(1, len(a)):
            x, j = a[i], i
            while j > 0 and a[j - 1] > x:
                a[j] = a[j - 1]
                j -= 1
            if j < i:
                a[j] = x


def random_list(n, m):
    return [randint(0, n) for _ in range(m)]


def selection_sort(a):
    """Time complexity = O(n^2)"""
    if len(a) > 0:
        for i in range(len(a) - 1):
            p = i
            for j in range(i + 1, len(a)):
                if a[j] < a[p]:
                    p = j
            if p > i:
                (a[p], a[i]) = (a[i], a[p])


def test_algorithm(algorithm):
    current_time = time_ns()
    l1 = random_list(randint(1, 1000), randint(1, 1000))
    print("Using algorithm {}".format(algorithm.__name__))
    print(l1)
    algorithm(l1)
    print(l1)
    print("Time spent:", time_ns() - current_time)
    print(l1 == sorted(l1))


def quicksort(li, start=0, end=""):
    if end == "":
        end = len(li) - 1
    if start >= end:  # stop the sorting
        return
    p = partition(li, start, end)
    quicksort(li, start, p - 1)  # sort list on the left of the pivot
    quicksort(li, p + 1, end)  # sort list on the right of the pivot


def partition(li, start, end):
    pivot = li[end]
    i, j = start, end - 1
    while True:
        while i <= j and li[i] < pivot:  # li[i] smaller than pivot and is already on the left side
            i += 1
        while i <= j and li[j] > pivot:  # checking if li[j] is larger than the pivot
            j -= 1
        if i <= j:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
        else:
            li[i], li[end] = pivot, li[i]
            return i


def mergesort(li):
    if len(li) > 1:
        mid = len(li) // 2
        left = li[:mid]
        right = li[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li[k] = left[i]
                i += 1
            else:
                li[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            li[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    """Uncomment the following code to test sorting algorithms"""
    test_algorithm(insertionsort)
    test_algorithm(selection_sort)
    test_algorithm(quicksort)
    test_algorithm(mergesort)
