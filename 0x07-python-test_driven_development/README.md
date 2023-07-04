# 0x07-python-test driven development
---

# Function Examples

This repository provides examples of Python functions with corresponding test cases. Each function is implemented in a separate module and has associated tests written using the doctest module.

## Functions

- [Add Integer](./0-add_integer.py): A function that adds two integers and returns the result.
- [Divide Matrix](./1-divide_matrix.py): A function that divides each element of a matrix by a given divisor and returns a new matrix.
- [Divide Matrix (Improved)](./2-matrix_divided.py): An improved version of the matrix division function with additional validation and error handling.
- [Say My Name](./3-say_my_name.py): A function that prints a person's name.
- [Print Square](./4-print_square.py): A function that prints a square of '#' characters.
- [text indentation](./5-text_indentation.py): A function that prints a text with 2 new lines after each of these characters '.',' ?',and ':'.".

## Test Cases

Test cases for each function are provided in separate text files in the `tests` directory. The test cases cover various scenarios to ensure the functions work correctly and handle different input cases.

## Running Tests

To run the tests for a specific function, you can use the `python3 -m doctest -v` command followed by the path to the test file. For example:

```bash
python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
