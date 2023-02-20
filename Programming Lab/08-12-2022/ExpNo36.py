class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()

rect1 = Rectangle(4, 7)
rect2 = Rectangle(4, 5)

print("Area of rectangle 1 :",rect1.area())
print("Area of rectangle 2 :",rect2.area())

if rect1<rect2:
    print("Area of rectangle 1 less than Rectangle 2")
else:
    print("Area of rectangle 2 is less than rectangle 1")