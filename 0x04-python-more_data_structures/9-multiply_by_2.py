#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_a_dictionary = a_dictionary.copy()
    for key in n_a_dictionary:
        n_a_dictionary[key] *= 2
    return n_a_dictionary
