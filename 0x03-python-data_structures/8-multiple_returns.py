#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence):
        length = len(sentence)
        letty = sentence[0]
        return((length, letty))
    return ((0, None))
