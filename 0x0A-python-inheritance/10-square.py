#!/usr/bin/python3
"""Square class that inherits from
   Rectangle (9-rectangle.py)"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits from class Rectangle"""
    def __init__(self, size):
        """Constructor of Instantiation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size
