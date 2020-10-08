#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    list of lists of integers representing the Pascal’s triangle
    """
    _list = []
    if n <= 0:
        return _list
    for row in range(n):
        if row == 0:
            _list.append([1])
        elif row == 1:
            _list.append([1, 1])
        else:
            _list2 = []
            for colm in range(row + 1):
                _list2.append(colm)
            for colm in range(row):
                _list2[0], _list2[row] = 1, 1
                _list2[colm] = _list[row - 1][colm - 1] + _list[row - 1][colm]
            _list.append(_list2)
    return _list
