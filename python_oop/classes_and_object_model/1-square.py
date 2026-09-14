chmod +x 1-square.py
git add 1-square.py
git commit -m "Add 1-square.py script"0;276;0c#!/usr/bin/env python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
