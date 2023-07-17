#!/usr/bin/python3
"""
Base class
"""

import json


class Base:
    """Base class for managing id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int): The ID of the object. If not provided,
            the ID is automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Create a new JSON representation"""
        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Create a new file with JSON representation of objects"""
        filename = cls.__name__ + '.json'
        obj_list = []

        if list_objs is not None:
            obj_list = [cls.to_dictionary(obj) for obj in list_objs]

        with open(filename, 'w') as file:
            json.dump(obj_list, file)
