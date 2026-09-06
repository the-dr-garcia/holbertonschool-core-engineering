#!/usr/bin/env python3
"""Module that updates or adds a key/value pair in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Replace the value of key if it exists, otherwise add it."""
    a_dictionary[key] = value
    return a_dictionary
