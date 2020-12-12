from my_main_functions import Stack
from string import ascii_uppercase


def convert_to_any_base(i, b):
    s = Stack()
    assert 2<=b<=36
    while i != 0:
        p = i % b
        if p >= 10:
            p = ascii_uppercase[p - 10]
        s.push(str(p))
        i //= b
    result = ""
    while not s.is_empty():
        result += s.pop()
    return result


def convert_to_decimal(i, b):
    assert 2<=b<=36
    result = 0
    for index, c in enumerate(reversed(i)):
        if c in ascii_uppercase:
            c = ascii_uppercase.index(c) + 10

        result += int(c) * b ** index

    return result



i = int(input("Entrez un nombre en base 10: "))
print(f"({i})_10 = ({convert_to_any_base(i, 2)})_2")
b = int(input("Entrez la base: "))
print(f"({i})_10 = ({convert_to_any_base(i, b)})_{b}")
i2 = input(f"Entrez un nombre en base {b}: ")
print(f"({i2})_{b} = ({convert_to_decimal(i2, b)})_10")