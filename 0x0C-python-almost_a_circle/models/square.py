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

    def update(self, *args, **kwargs):
        """Updating data"""
        if args:
            attributes = ['id', 'width', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key in ['id', 'size', 'x', 'y']:
                setattr(self, key, kwargs.get(key, getattr(self, key)))

    def to_dictionary(self):
        """Create a dictionary representation of the Square."""
        dictionary = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return dictionary
