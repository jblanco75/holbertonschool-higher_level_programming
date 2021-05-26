#!/usr/bin/python3
"""Function: say_my_name"""


def say_my_name(first_name, last_name=""):
    """ Function to print name.
    Args:
        first_name (string): first name to print. Required
        last_name (string): last name to print. Optional
    Raises:
        TypeError raised if anything other than strings are passed
    Return: None
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    return print("My name is {:s} {:s}".format(first_name, last_name))
