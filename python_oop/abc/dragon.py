#!/usr/bin/env python3
"""Module implementing mixins and a composite class."""


class SwimMixin:
    """Mixin class providing swimming capability."""

    def swim(self):
        """Print swimming behavior for the creature."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying capability."""

    def fly(self):
        """Print flying behavior for the creature."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon inheriting from multiple mixins."""

    def roar(self):
        """Print roaring behavior for the dragon."""
        print("The dragon roars!")
