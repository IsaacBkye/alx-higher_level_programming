#!/usr/bin/python3


"""Base Class for project"""


import json


class Base:
    '''Private attributes for class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor of id for Base Class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Method to return the JSON string representation of function'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Method to write JSON string representation to file'''
        new = []
        if list_objs:
            for i in list_objs:
                new.append(cls.to_dictionary(i))
        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        '''Method to return the list of JSON string representation'''
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''classmethod to print instances'''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Classmethod to return a list of instances'''
        newList = []
        try:
            with open("{}.json".format(cls.__name__), 'r') as o:
                new = cls.from_json_string(o.read())
        except IOError:
            return []

        for i in new:
            newList.append(cls.create(**i))
        return newList
