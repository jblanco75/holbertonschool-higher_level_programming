#!/usr/bin/python3
"""Function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """Encodes Python object into a JSON String"""
    return json.dumps(my_obj)
