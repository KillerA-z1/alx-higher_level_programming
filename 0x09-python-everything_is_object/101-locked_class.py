#!/usr/bin/python3
"""Creating class LockedClass"""


class LockedClass:
    """
    LockedClass allows only the 'first_name' attribute
    """
    # Define the __slots__ attribute to restrict allowed instance attributes
    __slots__ = ['first_name']
