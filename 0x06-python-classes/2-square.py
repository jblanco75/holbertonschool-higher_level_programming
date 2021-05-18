#!/usr/bin/python3
"""Square Class"""


class Square:
    """Create private instance __size"""
    def __init__(self, size=0):
        if size != type(int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
