#!/usr/bin/env python3
"""Module that defines a function to print a string in uppercase."""


def uppercase(str):
    """Print the given string converted to uppercase using ASCII logic."""
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
