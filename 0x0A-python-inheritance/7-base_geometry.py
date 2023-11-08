#!/usr/bin/python3
"""
Module: BaseGeometry
"""


class BaseGeometry:
    """
    Base class for geometry-related classes.
    It also provides a method `integer_validator()` for validating
    integer values.
    """
    def area(self):
        """
        Calculate the area of the geometry object.
        Raises:
            Exception: Indicates that the area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        This method validates that the given value is an integer and,
        greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
