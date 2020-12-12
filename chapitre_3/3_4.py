from random import randint
from string import ascii_uppercase
from math import sqrt

class Point:

    def __init__(self, name, x, y):
        if name != "random":
            self.name = name
            self.x = x
            self.y = y
        else:
            self.name = ascii_uppercase[randint(0, len(ascii_uppercase)-1)]
            self.x = randint(x, y+1)
            self.y = randint(x, y+1)

    def __str__(self):
        return f"{self.name}({self.x},{self.y})"

    def distance_to(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


class Triangle:
    def __init__(self, p1:Point, p2:Point, p3:Point):
        self.p1, self.p2, self.p3 = p1, p2, p3

    def __str__(self):
        return f"triangle: {self.p1}, {self.p2}, {self.p3}"

    def set_random_data(self, min, max):
        self.p1, self.p2, self.p3 = Point("random", min, max), Point("random", min, max), Point("random", min, max)

    def calculate_circumference(self):
        return self.p1.distance_to(self.p2) + self.p1.distance_to(p3) + self.p2.distance_to(p3)

    def show_type(self):
        type = "scalène"
        if self.p1.distance_to(self.p2) == self.p1.distance_to(self.p3) == self.p2.distance_to(self.p3):
            type = "equilateral"
        elif self.p1.distance_to(self.p2) == self.p1.distance_to(p3) or self.p1.distance_to(self.p2) == self.p2.distance_to(p3)  \
                or self.p2.distance_to(self.p3) == self.p1.distance_to(self.p3):
            type = "isosceles"

        angle = "."
        if self.p2.distance_to(self.p3)**2 == self.p2.distance_to(self.p1)**2 + self.p1.distance_to(self.p3)**2:
            angle = f" and right-angled at {self.p1.name}."
        elif self.p1.distance_to(self.p3) ** 2 == self.p2.distance_to(self.p1) ** 2 + self.p2.distance_to(self.p3)**2:
            angle = f" and right-angled at {self.p2.name}."
        elif self.p1.distance_to(self.p2)**2 == self.p3.distance_to(self.p1) ** 2 + self.p3.distance_to(self.p2) ** 2:
            angle = f" and right-angled at {self.p3.name}."

        return f"The triangle: ({self.p1}, {self.p2}, {self.p3}) is {type}{angle}"



"""
p = Point("R", 1, 5)
p2 = Point("X", 2, 6)
p3 = Point("random", 1, 7)
print(p)
print(p.distance_to(p2))
t = Triangle(p, p2, p3)
print(t)
t.set_random_data(1, 6)
print(t)
print(t.calculate_circumference())
print(t.show_type())
"""
