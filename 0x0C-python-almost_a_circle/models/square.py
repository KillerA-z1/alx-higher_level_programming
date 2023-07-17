#!/usr/bin/python3
"""
Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size : The size of the square.
            x : The x-coordinate of the square's position.
            y : The y-coordinate of the square's position.
            id : The ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size of the square.
        """
        self.width = self.height = value

    def __str__(self):
        """
        String representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
