#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets dict representation"""
        return (self.__dict__)
