"""1) Create a class named Shape. Add an instance method called area. But don't define the method, just raise
NotImplementedError() exception with a suitable message.

2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC)
Make the area method an abstract method by decorating it with abstractmethod decorator (import this also from
abc).

3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
Define constructor for each of them to assign the necessary parameters required for calculating the area.
Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it.
Create an object for each of the subclasses and call the area method on the objects.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Subclasses must implement the area")



class Square(Shape):
    """ Square area."""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    """ Circle area."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    """Triangle area."""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height




class Pentagon(Shape):
    """Pentagon area."""

    def __init__(self, side):
        self.side = side

    def area(self):
        return (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side ** 2) / 4




square = Square(5)
circle = Circle(5)
triangle = Triangle(5, 5)
pentagon = Pentagon(5)

print("Square area:", square.area())
print("Circle area:", circle.area())
print("Triangle area:", triangle.area())
print("Pentagon area:", pentagon.area())
