#!/usr/bin/python3

"""
Class that defines a Student
"""


class Student():
    """
    Represents a student object.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with the specified attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        Attributes:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student object.

        Args:

        attrs (list): Optional. A list of attribute names to include in
                      the dictionary representation.
            If not provided, all attributes will be included.

        Returns:

        dict: A dictionary representing the student object with attribute names
                as keys and attribute values as values.
        If attrs is specified, only the specified attributes will be included
        in the dictionary.
        """
        if attrs is None:
            return self.__dict__
        return {attr: self.__dict__[attr] for attr in attrs
                if attr in self.__dict__}

    def reload_from_json(self, json):

        """
        Reload the Student object from a JSON dictionary.

        Args:
            json (dict): A JSON dictionary containing attribute-value pairs.

        """
        if json is not None:
            for attr, value in json.items():
                setattr(self, attr, value)
