#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (my_list):
        index = 0
        length = len(my_list)
        boolList = [False] * length
        for cnt in my_list:
            if (cnt % 2 == 0):
                boolList[index] = True
            index += 1
        return (boolList)
    return (list())
