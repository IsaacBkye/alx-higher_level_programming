#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if (idx >= 0 or idx < length):
        for i, e in enumerate(my_list):
            if (i == idx):
                my_list[i] = element
    return (my_list)
