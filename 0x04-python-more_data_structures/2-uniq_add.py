#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique_list = dict(zip(my_list, ['unique'] * len(my_list))).keys()
    for item in unique_list:
        result += item
    return (result)
