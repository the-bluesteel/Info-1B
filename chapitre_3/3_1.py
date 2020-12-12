from my_main_functions import pgcd


class Fraction:
    def __init__(self, new_n: int, new_d: int):
        self.d = new_d if new_d != 0 else 1
        self.n = new_n

    def __str__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"

    def simplify(self):
        p = pgcd(self.n, self.d)
        self.n = self.n // p
        self.d = self.d // p

    def invert(self):
        if self.n != 0:
            self.n, self.d = self.d, self.n

    def add(self, f):
        p = f.d
        m = f.n
        if self.d == p:
            self.n += f.n
        else:
            m *= self.d
            p *= self.d
            self.n *= p
            self.d *= p
            self.n += m
        self.simplify()

    def multiply_by(self, f):
        self.n *= f.n
        self.d *= f.d
        self.simplify()

    def divide_y(self, f):
        self.n *= f.d
        self.d *= f.n
        self.simplify()


"""
f = Fraction(6, 12)
print(f)
f.simplify()
print(f)
f.invert()
print(f)
f1 = Fraction(9, 2)
f.add(f1)
print(f)
f.multiply_by(f1)
print(f)
f.divide_y(f1)
print(f)
"""
