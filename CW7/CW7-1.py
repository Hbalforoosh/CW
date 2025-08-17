from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("The input radius must be positive.")
        self.r = r

    def perimeter(self):
        return math.pi * 2 * self.r

    def area(self):
        return math.pi * self.r**2


class Rectangle(Shape):
    def __init__(self, width, length):
        if width <= 0:
            raise ValueError("The input width must be positive.")
        self.width = width
        if length <= 0:
            raise ValueError("The input lenght must be positive.")
        self.length = length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("The input side must be positive.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        semi_perimeter = self.perimeter() / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (semi_perimeter - self.c))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


c = Circle(5)
r = Rectangle(5, 6)
t = Triangle(6, 8, 10)

print("Circle shape:")
print(f'Area is : {c.area()}')
print(f'Perimeter is : {c.perimeter()}')

print("Rectangle shape:")
print(f'Area is : {r.area()}')
print(f'Perimeter is : {r.perimeter()}')

print("Triangle shape:")
print(f'Area is : {t.area()}')
print(f'Perimeter is : {t.perimeter()}')
