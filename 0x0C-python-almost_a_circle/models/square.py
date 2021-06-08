#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor method"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """Represents the class objects as a string"""
        message = "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)
        return message
