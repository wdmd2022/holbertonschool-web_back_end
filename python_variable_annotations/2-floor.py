#!/usr/bin/env python3
"""this module contains a function to get the floor of a float
"""


def floor(n: float) -> int:
    """this function takes a float and returns its floor

    Args:
        n (float): the number we are rounding down

    Returns:
        int: the floor of the float. Though integer division returns
        an int, we cast it to remove the '.0'
    """
    return int(n // 1)
