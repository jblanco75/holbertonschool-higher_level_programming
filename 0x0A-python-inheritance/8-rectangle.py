#!/usr/bin/python3
"""class BaseGeometry
   with methods and attr"""


class BaseGeometry:
    """Defines a geometry class"""
    def area(self):
        """Defines area of geometric object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Constructor method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
