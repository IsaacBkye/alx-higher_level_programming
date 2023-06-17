#!/usr/bin/python3
def roman_to_int(roman_string):
    digit = 0
    if (roman_string.__class__ == str):
        rString = len(roman_string)
        rD = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rValue = [rD.get(_value) for _value in roman_string]
        for item, _value in enumerate(rValue):
            if (item < rString - 1):
                if (_value < rValue[item + 1]):
                    digit -= _value
                else:
                    digit += _value
            else:
                digit += _value
    return (digit)
