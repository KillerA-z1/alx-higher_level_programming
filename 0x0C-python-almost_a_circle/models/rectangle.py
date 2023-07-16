#!/usr/bin/python3
"""
Rectangle class that inherits from the Base class.
"""
from .base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from the Base class and representing
    a rectangle with two Attributes :
        width : The width of the rectangle.
        height : The height of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object with the specified attributes.

        Args:
            width : The width of the rectangle.
            height : The height of the rectangle.
            x : The x-coordinate of the rectangle's position.
            y : The y-coordinate of the rectangle's position.
            id : The ID of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
