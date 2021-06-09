#!/usr/bin/python3
"""Class Base"""
import json


class Base:
    """Main class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method of class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of dictionary"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file"""
        filename = cls.__name__ + ".json"
        list_to_save = []
        if list_objs is not None:
            for elem in list_objs:
                list_to_save.append(cls.to_dictionary(elem))
        with open(filename, mode="w", encoding="utf-8") as json_file:
            json_file.write(cls.to_json_string(list_to_save))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
