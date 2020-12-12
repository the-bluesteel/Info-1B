from random import randint
from math import sqrt


class Point:

    def __init__(self, x=randint(-10, 10), y=randint(-10, 10)):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def distance(self, p):
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def is_identical(self, p):
        return True if self.y == p.y and self.x == p.x else False

    def __str__(self):
        return f"({self.x},{self.y})"


class Segment:
    def __init__(self, p1=Point(), p2=Point()):
        self.p1 = p1
        self.p2 = p2

    def get_boundary(self):
        return self.p2

    def get_origin(self):
        return self.p1

    def set_boundary(self, p2):
        self.p2 = p2

    def set_origin(self, p1):
        self.p1 = p1

    def get_length(self):
        return self.p1.distance(self.p2)

    def get_midpoint(self):
        return Point((self.p1.x + self.p2.x) / 2, (self.p2.y + self.p1.y) / 2)

    def __str__(self):
        return f"Segment : {self.p1} - {self.p2}"


class Quadrilateral:
    def __init__(self, d1: Segment, d2: Segment):
        self.d1 = d1
        self.d2 = d2

    def get_diagonal1(self):
        return self.d1

    def get_diagonal2(self):
        return self.d2

    def set_diagonal1(self, d):
        self.d1 = d

    def set_diagonal2(self, d):
        self.d2 = d

    def is_parallelogram(self):
        return True if self.d1.get_midpoint().is_identical(self.d2.get_midpoint()) else False

    def is_rectangle(self):
        return True if self.is_parallelogram() and self.d1.get_length() == self.d2.get_length() else False

    def __str__(self):
        return f"quad [ {self.d1.get_origin()}, {self.d1.get_boundary()}, {self.d2.get_origin()}, {self.d2.get_boundary()} ]"


"""
p1 = Point(1, 9)
p2 = Point(2, 5)
print(p1)
print(p2)
print(Point())
p1.set_x(p2.get_y())
print(p1)
print(p1.distance(p2))
print(p2.is_identical(Point(2, 5)))
s1 = Segment(p1, p2)
print(s1.get_boundary())
print(s1)
s1.set_origin(Point(3, 7))
print(s1)
print(f"{s1.get_length():.3f}")
print(s1.get_midpoint())
print(Segment())
s2 = Segment(Point(7, 8), Point(5, 1))
q1 = Quadrilateral(s1, s2)
print(q1)
print(q1.is_parallelogram())
q1.set_diagonal1(Segment(Point(7, 1), Point(5, 8)))
print(q1)
print(q1.is_rectangle())
"""

