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

    @property
    def width(self):
        """Width property"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width Setter"""
        self.validate_positive_integer("width", width)
        self.__width = width

    @property
    def height(self):
        """Height property"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height Setter"""
        self.validate_positive_integer("height", height)
        self.__height = height

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, x):
        """x Setter"""
        self.validate_non_negative_integer("x", x)
        self.__x = x

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, y):
        """y Setter"""
        self.validate_non_negative_integer("y", y)
        self.__y = y

    def validate_positive_integer(self, name, value):
        """
        Validate that the given value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def validate_non_negative_integer(self, name, value):
        """
        Validate that the given value is a non-negative integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """
        Display the rectangle with '#' representing the shape.

        The rectangle is displayed with the specified 'x' and 'y' offsets.
        The 'x' offset represents the number of spaces before the shape
            starts horizontally.
        The 'y' offset represents the number of newlines before the shape
            starts vertically.
        """
        newline_count = self.__y
        while newline_count > 0:
            print("")
            newline_count -= 1

        height_count = self.__height
        while height_count > 0:
            x_offset = self.__x
            while x_offset > 0:
                print(" ", end="")
                x_offset -= 1

            width_count = self.__width - 1
            while width_count > 0:
                print("#", end="")
                width_count -= 1

            print("#")
            height_count -= 1

    def __str__(self):
        """String representation"""
        result = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return result

    def update(self, *args, **kwargs):
        """Updating data"""
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key in kwargs:
                if key in attributes:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Create a dictionary representation of the Rectangle."""
        dictionary = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return dictionary
