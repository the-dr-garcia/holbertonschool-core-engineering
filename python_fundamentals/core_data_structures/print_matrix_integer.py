#!/usr/bin/env python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix, one row per line, values separated by a space."""
    for row in matrix:
        print(" ".join("{:d}".format(value) for value in row))
