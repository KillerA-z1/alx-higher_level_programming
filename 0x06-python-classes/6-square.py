#!/usr/bin/python3
"""Square is a class"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square object with a given size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If the size is not an integer or
                    the position is not a tuple.
            ValueError: If the size or position values are invalid.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Set the size of the square.

        Args:
            size (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Set the position of the square.

        Args:
            position (tuple): The new position of the square.

        Raises:
        TypeError:If the position is not a tuple or contains invalid values.
        ValueError: If the position values are less than 0.
        """
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) for coord in position):
            raise TypeError("position values must be integers")
        elif any(coord < 0 for coord in position):
            raise ValueError("position values must be >= 0")
        else:
            self.__position = position

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print a square pattern using '#'.

        The square is printed with the specified position and size.

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
