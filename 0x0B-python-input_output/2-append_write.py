#!/usr/bin/python3
"""Append text at rhe end"""


def append_write(filename="", text=""):
    """Appends UTF-8 text to a file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
