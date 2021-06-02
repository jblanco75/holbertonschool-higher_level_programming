#!/usr/bin/python3
"""class BaseGeometry (based on 5-base_geometry.py)
   with method"""


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
