# 0x0C. Python - Almost a circle
---
# Almost a Circle

This project is part of the ALX Higher Level Programming curriculum. It focuses on object-oriented programming concepts in Python.

## Base Class

The `Base` class manages the `id` attribute and avoids duplicating code.

## First Rectangle

The `Rectangle` class inherits from the `Base` class and adds attributes specific to a rectangle.

## Validate Attributes

Update the `Rectangle` class by adding validation to the setter methods and instantiation.

## Area

The `Rectangle` class includes a method `area()` that returns the area of the rectangle.

## Display

The `Rectangle` class includes a method `display()` that prints a representation of the rectangle using the `#` character.

## String Representation

The `Rectangle` class overrides the `__str__` method to return a string representation of the rectangle.

## Square Inheritance

The `Square` class inherits from the `Rectangle` class and adds attributes specific to a square.

## Save and Load JSON

The `Base` class includes methods to save and load instances to/from a JSON file.

## Save and Load CSV

The `Base` class includes methods to save and load instances to/from a CSV file.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Example Usage

Here are a few examples of how to use the classes:

1. Creating and manipulating rectangles:

```python
from models.rectangle import Rectangle

# Create a rectangle with width 4 and height 6
rectangle = Rectangle(4, 6)

# Print the area of the rectangle
print(rectangle.area())

# Display the rectangle
rectangle.display()

# Update the rectangle's width and height
rectangle.width = 8
rectangle.height = 10

# Print the updated area of the rectangle
print(rectangle.area())

# Display the updated rectangle
rectangle.display()
```
2. Creating and manipulating squares:

```python

from models.square import Square

# Create a square with side length 5
square = Square(5)

# Print the area of the square
print(square.area())

# Display the square
square.display()

# Update the square's side length
square.size = 7

# Print the updated area of the square
print(square.area())

# Display the updated square
square.display()
```
