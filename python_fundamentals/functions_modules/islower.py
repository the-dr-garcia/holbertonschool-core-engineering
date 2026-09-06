#!/usr/bin/env python3
"""Module that defines a function to check if a character is lowercase."""


def islower(c):
    """Check if a character is a lowercase letter using ASCII logic."""
    return ord(c) >= 97 and ord(c) <= 122
