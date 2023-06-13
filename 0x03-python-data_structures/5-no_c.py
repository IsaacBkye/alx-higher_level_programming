#!/usr/bin/python3
def no_c(my_string):
    strr = my_string
    strr = strr.translate({ord('c'): None})
    strr = strr.translate({ord('C'): None})
    return (strr)
