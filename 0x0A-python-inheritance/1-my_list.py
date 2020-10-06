#!/usr/bin/python3
"""
class list that inherits from list
"""


class MyList(list):
    """
    Subclass of list
    """
    def __init__(self):
        """
        Initializace all instance of method
        """
        super().__init__

    def print_sorted(self):
        """
        method to print my list ascending sort
        """
        print(sorted(self))
