#!/usr/bin/python3
"""
Module: BaseGeometry
"""


class BaseGeometry:
    """
    Base class for geometry-related classes.

    """
    def area(self):
        """
        Calculate the area of the geometry object.
        Raises:
            Exception: Indicates that the area calculation is not implemented.
        """
        raise Exception("area() is not implemented")
