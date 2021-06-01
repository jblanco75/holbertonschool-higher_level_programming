#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets dict representation"""
        names = [i for i in self.__dict__ if type(attrs) == str]
        if attrs is None:
            return (self.__dict__)
        retrv = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                retrv[key] = value
        return (retrv)
