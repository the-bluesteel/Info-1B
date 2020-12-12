from math import factorial, sqrt


class Number:
    def __init__(self, value):
        self.v = value

    def __str__(self):
        return f"value is {self.v}"

    def set_value(self, new_v):
        self.v = new_v

    def factorial(self):
        assert self.v >= 0, "Factorial - Error"
        return factorial(self.v)

    def sum_of_divisors(self):
        sum = 0
        for i in range(1, self.v):
            if self.v % i == 0:
                sum += i
        sum += self.v
        return sum

    def reverse(self):
        reversed_v = 0
        for index, c in enumerate(str(self.v)):
            reversed_v += int(c) * (10 ** index)
        self.v = reversed_v

    def is_square(self):
        return sqrt(self.v).is_integer()

    def is_prime(self):
        if self.v % 2 == 0 and self.v != 2:
            return False
        for i in range(3, int(sqrt(self.v) + 1), 2):
            if self.v % 2 == 0:
                return False
        return True

    def is_perfect(self):
        return True if self.sum_of_divisors() == 2 * self.v else False

    def is_palindrome(self):
        reversed_v = 0
        for index, c in enumerate(str(self.v)):
            reversed_v += int(c) * (10 ** index)
        return True if reversed_v == self.v else False

    def is_amicable_to(self, n):
        return True if self.sum_of_divisors() == n.sum_of_divisors == n.v + self.v else False



"""
n = Number(606)
print(n)
print(n.factorial())
print(n.sum_of_divisors())
n.reverse()
print(n)
print(n.is_square())
print(f"{n.is_prime()} - prime?")
print(f"{n.is_palindrome()} - palindrome?")
"""

