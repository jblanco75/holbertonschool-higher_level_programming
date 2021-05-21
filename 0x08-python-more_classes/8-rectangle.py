#!/usr/bin/python3
"""Rectangle class"""


class Rectangle():
    """Attribute init for Rectangle class"""

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """width of Rectangle"""
        self.__width = width
        """height of Rectangle"""
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Prints a square with '#' """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """Return string representation of Rectangle"""
        return "Rectangle(" + str(self.__width) + ", " + \
            str(self.__height) + ")"

    def __del__(self):
        """Destructor method for instances"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Staticmethod for comparing areas"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
