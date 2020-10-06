#!/usr/bin/python3
"""
My class list that inherits from list
"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """ Initializace all instance of method"""
        super().__init__
    """metod to print my list ascending sort"""
    def print_sorted(self):
        print(sorted(self))
