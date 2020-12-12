import math


def longest_string(a, b, c):
    if len(a) > len(b) and len(a) > len(c):
        return a
    if len(b) > len(a) and len(b) > len(c):
        return b
    if len(c) > len(b) and len(c) > len(a):
        return c
    return a


def check_vowels(s):
    vowels = "iueoa"
    s = s.lower()
    for c in s:
        if c in vowels:
            return True

    return False


def count_of_numbers(s):
    numbers = "1234567890"
    counter = 0
    for c in s:
        if c in numbers:
            counter += 1

    return counter


def count_average(*a):
    l = []
    for _ in a:
        if 1 <= _ <= 60:
            l.append(_)
    return math.ceil(sum(l) / len(l))


def change_s(a):
    a = a.replace("S", "$")
    a = a.replace("s", "$")
    return a
