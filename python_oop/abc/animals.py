#!/usr/bin/env python3
"""Module providing an abstract base class and concrete animal implementations."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing a generic animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be overridden by subclasses."""
        pass


class Dog(Animal):
    """Dog class representing a canine."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class representing a feline."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
