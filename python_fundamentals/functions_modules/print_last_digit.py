#!/usr/bin/env python3
"""Module that defines a function to print and return the last digit."""


def print_last_digit(number):
    """Print and return the last digit of number as a positive value."""
    last_digit = number % 10
    if last_digit < 0:
        last_digit += 10
    print("{}".format(last_digit))
    return last_digit
