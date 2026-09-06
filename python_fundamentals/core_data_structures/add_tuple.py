#!/usr/bin/env python3
"""Module that adds two tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Return a new tuple with the sum of the first two elements of
    tuple_a and tuple_b, treating missing values as 0."""
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a0 + b0, a1 + b1)
