#!/usr/bin/python3
"""Child class from Base"""
from models.base import Base


class Rectangle(Base):
    """Class inherited from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints a Rectangle with '#'"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """Represents the class objects as a string"""
        message = ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))
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
                    self.width = arg
                elif elem == 2:
                    self.height = arg
                elif elem == 3:
                    self.x = arg
                elif elem == 4:
                    self.y = arg
                elem += 1

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

        def to_dictionary(self):
            """Returns dictionary representation of Rectangle"""
            return {"id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y}
