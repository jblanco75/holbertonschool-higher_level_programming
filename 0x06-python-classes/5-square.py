#!/usr/bin/python3
"""Square Class"""


class Square:
    """Create private instance __size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square with '#' """
        if size != 0:
            for i in range(self.__size):
                print('#' * self.__size)
        else:
            print()

    @property
    def size(self):
        """Gets property value"""
        return self.__size

    @size.setter
    def size(self, val):
        """Sets property value"""
        if type(val) != int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
