#!/usr/bin/python3
"""Square Class"""


class Square:
    """Create private instance __size"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) != int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square with '#' """
        if self.size != 0:
            if self.position > 0:
                print("\n" * self.position[1], end='')
            for i in range(self.size):
                print(" " * self.position[0], end='')
                print('#' * self.size)
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

    @property
    def position(self):
        """Gets property value"""
        return self.__position

    @position.setter
    def position(self, val):
        """Sets property value"""
        if type(val) != tuple or len(val) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(val[0]) != int or val[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(val[1]) != int or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val
