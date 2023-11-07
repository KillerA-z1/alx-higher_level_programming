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

    def to_json(self):
        """
        Returns a dictionary representation of the student object.

        Returns:
            dict: A dictionary representing the student object with
                attribute names as keys and attribute values as values.
        """
        return self.__dict__
