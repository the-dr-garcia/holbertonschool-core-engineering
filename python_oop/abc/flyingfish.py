#!/usr/bin/env python3
"""Module demonstrating multiple inheritance and method resolution order."""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print swimming behavior for a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat information for a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print flying behavior for a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat information for a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish inheriting from both Fish and Bird."""

    def fly(self):
        """Print flying behavior for a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print swimming behavior for a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print habitat information for a flying fish."""
        print("The flying fish lives both in water and the sky!")
