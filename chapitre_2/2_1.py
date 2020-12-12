from functools import lru_cache
from time import time_ns
from math import sqrt


def fibo_iter(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 1, 0
    for _ in range(n - 1):
        a, b = a + b, a

    return a


@lru_cache(maxsize=1280, typed=False)
def fibo_recu(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo_recu(n - 1) + fibo_recu(n - 2)


def fibo_formule(n):
    p = (1+sqrt(5))/2
    q = (1-sqrt(5))/2

    return (1/sqrt(5)) * (p**n - q**n)

before = time_ns()
print(fibo_iter(400))
print(time_ns() - before)
before = time_ns()
print(fibo_recu(400))
print(time_ns()-before)

print(fibo_formule(1000))