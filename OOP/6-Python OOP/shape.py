from math import pi


class Shape:
    def __init__(self, name) -> None:
        self.name = name


class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius**2


r = Rectangle("Rectangle", 500, 400)
c = Circle("Circle", 600)

print(r.area())
print(c.area())
