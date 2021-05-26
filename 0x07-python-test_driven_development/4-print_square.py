#!/usr/bin/python3
"""Function: print_square"""


def print_square(size):
        """Prints a square with '#'
        'size' is the size length of the square
        'size' must be an integer"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if size > 0:
            for i in range(size):
                print('#' * size)
        else:
            print()
