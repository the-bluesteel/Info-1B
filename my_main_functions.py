import math


def pgcd(a, b):
    assert a > 0 and b > 0, ""
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def max3(a, b, c):
    l = [a, b, c]
    l.sort(reverse=True)
    print(l)
    return l[0]


def geo3(a, b, c):
    if 0 not in [a, b, c] and (a > 0) == (b > 0) == (c > 0):
        return (a * b * c) * (1 / 3)
    else:
        return 0


def sum_of_integer(a, b):
    if a == b:
        return 0
    if a < b:
        a, b = b, a
    sum = 0
    for i in range(math.ceil(b), math.floor(a) + 1):
        sum += i

    return sum


def fact(a):
    assert a > 0, ""
    f = 1
    for x in range(1, a + 1):
        f *= x
    return f


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        print("Empty Stack")

    def top(self):
        if len(self.items) > 0:
            return self.items[-1]
        print("Empty Stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        s = "Stack (from top to bottom): [ "
        for x in reversed(self.items):
            s += f"{x} "
        s += "]"
        return s


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, x):
        self.items.insert(0, x)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            print("Empty Queue")

    def pop(self):
        if len(self.items)>0:
            return self.items.pop()
        else:
            print("Empty Queue")

    def size(self):
        return len(self.items)

    def get_queue(self):
        return self.items

    def __str__(self):
        s = "Queue ==> : ["
        for x in self.items:
            s += f"{x} "
        s += "]"
        return s

    def empty(self):
        self.items = []

    def remove(self, x):
        if x in self.items:
            self.items.remove(x)
