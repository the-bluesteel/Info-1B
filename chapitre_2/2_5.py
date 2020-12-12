from functools import lru_cache
from time import time_ns
from math import factorial

def pascal_r(n, k):
    if n < 0 or False == (0 <= k <= n):
        return 0

    if k == 0 or k == n:
        return 1

    return pascal_r(n - 1, k - 1) + pascal_r(n - 1, k)


@lru_cache(maxsize=128, typed=False)
def pascal_rc(n, k):
    if n < 0 or False == (0 <= k <= n):
        return 0

    if k == 0 or k == n:
        return 1

    return pascal_rc(n - 1, k - 1) + pascal_rc(n - 1, k)
before = time_ns()
for n in range(1, 20):
    for k in range(0, n+1):
        pascal_r(n, k)
"""
print(f"{time_ns() - before} ns")

before = time_ns()
for n in range(1, 20):
    for k in range(0, n + 1):
        pascal_rc(n, k)

print(f"{time_ns() - before} ns")
"""

def pascal_i(n, k):
    if n < 0 or not (0<=k<=n):
        return 0
    if k == 0 or k == n:
        return 1
    triangle = []
    for row in range(n + 1):
        l = []
        for element in range(row+1):
            if element == 0 or element == row:
                l.append(1)
            else:
                l.append(triangle[row - 1][element - 1] + triangle[row-1][element])
        triangle.append(l)
    return triangle[n][k]


def pascal_f(n, k):
    return factorial(n) / (factorial(k)*factorial(n-k))


n = int(input("Enter n: "))
assert n > 0, "n > 0"

for a in range(n):
    for k in range(a+1):
        print(pascal_rc(a, k), end=" ")
    print("")

for a in range(n, n+10):
    sum = 0
    for k in range(a+1):
        sum += pascal_rc(a, k)
    print(sum)

a = int(input("Enter a: "))
m = int(input("Enter m: "))

for b in range(m):
    for k in range(b+1):
        if pascal_rc(b, k) % a == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print("")