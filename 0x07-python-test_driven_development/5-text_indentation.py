#!/usr/bin/python3
"""Function: text_indentation(text):"""


def text_indentation(text):
    """
    Print text
    2 new lines after each of these characters: ., ? and :
    Args:
        text (str): text
    Raise
        TypeError: when text is not str
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in [':', '.', '?']:
            print(text[i])
            print()
        else:
            print(text[i], end='')
