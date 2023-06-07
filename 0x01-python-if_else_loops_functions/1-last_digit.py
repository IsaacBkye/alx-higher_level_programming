#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if number < 0:
    num = -number
if num % 10 > 5:
    print(f"Last digit of {number} is {num % 10} and is greater than 5")
elif num % 10 < 6 and num % 10 != 0:
    print(f"Last digit of {number} is {-(num % 10)} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {num % 10} and is is 0")
