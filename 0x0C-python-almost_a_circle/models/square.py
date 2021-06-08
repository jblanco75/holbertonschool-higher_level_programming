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
        return self.width

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

    def update(self, *args, **kwargs):
        """Updates the class assigning a key/value
        argument to attributes"""
        elem = 0
        if args is not None and len(args) != 0:
            for arg in args:
                if elem == 0:
                    self.id = arg
                elif elem == 1:
                    self.size = arg
                elif elem == 2:
                    self.x = arg
                elif elem == 3:
                    self.y = arg
                elem += 1

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of the Square"""
        return ({"id": self.id, "size": self.width,
                 "x": self.x, "y": self.y})
