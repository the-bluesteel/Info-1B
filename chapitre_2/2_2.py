from functools import lru_cache
from time import time_ns

@lru_cache(maxsize=128, typed=False)
def collatz_r(u, n):
    if n <= 0:
        return u
    return collatz_r(u * (1 / 2), n - 1) if u % 2 == 0 else collatz_r(3 * u + 1, n - 1)


def collatz_i(u, n):
    for _ in range(n):
        if u % 2 == 0:
            u = u * (1 / 2)
        else:
            u = 3 * u + 1
    return u


def collatz_counter(u):
    counter = 0
    while u != 1:
        counter += 1
        if u % 2 == 0:
            u = u * (1 / 2)
        else:
            u = 3 * u + 1
    return counter

before = time_ns()

for _ in range(1, 5000):
    collatz_counter(_)



print(time_ns()-before)

# 10000 -> around 1 second
# O(n)
# 8 h = 28800 seconds
# -> 288000000 = N