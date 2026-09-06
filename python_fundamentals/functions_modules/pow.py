#!/usr/bin/env python3
"""Module that defines a function to compute a raised to the power of b."""


def pow(a, b):
    """Return a raised to the power of b using a manual loop."""
    result = 1
    for i in range(b):
        result *= a
    return result
