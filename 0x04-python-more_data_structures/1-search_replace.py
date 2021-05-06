#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = my_list[:]
        for i in my_list:
            new_list[search] = replace
        return new_list
