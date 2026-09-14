#!/usr/bin/env python3
"""Module implementing a custom list class with notification messages on modification."""


class VerboseList(list):
    """Custom list class that prints messages when items are added or removed."""

    def append(self, item):
        """Append an item to the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with elements and print a notification."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
