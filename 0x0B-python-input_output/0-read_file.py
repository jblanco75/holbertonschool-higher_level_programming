#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """File UTF-8 reader"""
    with open(filename, mode='r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
