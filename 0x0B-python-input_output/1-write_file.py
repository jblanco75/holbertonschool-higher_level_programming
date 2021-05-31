#!/usr/bin/python3
"""Write a line to a file"""


def write_file(filename="", text=""):
    """Write a UTF-8 line to a file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
