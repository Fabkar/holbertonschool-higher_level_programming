#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list):
        return
    if idx < 0:
        return
    return my_list[idx]
