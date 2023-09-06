#!/usr/bin/env python3
"""this module contains a function a type-annotated function sum_list which
takes a list input_list of floats as argument and returns their sum as a float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """this function takes a list of floats and returns their sum

    Args:
        input_list (List[float]): this is a list of floats we will operate on

    Returns:
        float: the sum of the list's items
    """
    total: float = 0
    for x in input_list:
        total += x
    return total
