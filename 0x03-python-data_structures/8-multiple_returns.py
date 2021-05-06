#!/usr/bin/python3
def multiple_returns(sentence):
    first = None
    if sentence:
        length = len(sentence)
        first = sentence[0]
        return length, first
    else:
        return length, None
