#!/usr/bin/env python3
"""this module contains a function that takes a list mxd_list of integers
and floats and returns their sum as a float
"""


from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """this funciton adds a list of ints and floats and returns the sum

    Args:
        mxd_list (List[Union[int, float]]): list of ints and floats

    Returns:
        float: the sum of all the list's items
    """
    total: float = 0
    for x in mxd_list:
        total += x
    return total
