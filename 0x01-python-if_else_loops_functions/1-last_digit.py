#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nummod = number % 10
num = number
if number < 0:
    num = -number
    nummod = -(num % 10)
if nummod > 5:
    print(f"Last digit of {number} is {nummod} and is greater than 5")
elif nummod == 0:
    print(f"Last digit of {number} is {nummod} and is 0")
else:
    print(f"Last digit of {number} is {nummod} and is less than 6 and not 0")
