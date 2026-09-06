#!/usr/bin/env python3
"""Module that defines a function to print and return the last digit."""


def print_last_digit(number):
    """Print and return the last digit of number as a positive value."""
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit), end="")
    return last_digit
