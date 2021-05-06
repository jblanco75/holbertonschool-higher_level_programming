#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list:
        if idx < 0:
            return None
        if idx < len(my_list):
            my_list[idx] = element
            return my_list
        else:
            return my_list
