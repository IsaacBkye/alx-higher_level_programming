#!/usr/bin/python3


"""Module for saving arguments to file"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arg = load_from_json_file("add_item.json")
except:
    arg = []
for i in range(1, len(argv)):
    arg.append(argv[i])

save_to_json_file(arg, "add_item.json")
