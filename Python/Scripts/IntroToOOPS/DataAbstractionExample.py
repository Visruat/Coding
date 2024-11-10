class Rectangle:
    def __init__(self, length, width):
        self.__length = length  # Private attribute
        self.__width = width    # Private attribute

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")          # Output: Area: 15
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 16

# print(rect.__length)  # This will raise an AttributeError as length and width are private attributes