class Shape:
    def __init__(self):
        pass

    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return (self.radius ** 2) * 3.14

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

원1 = Circle(2)
print(원1.get_area())
사각형1 = Rectangle(3, 4)
print(사각형1.get_area())
