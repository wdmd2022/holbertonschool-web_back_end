#!/usr/bin/env python3
"""this module contains a function make_multiplier which takes a float
'multiplier' as an argument and returns a function that multiplies a float
by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """this function returns another function that multiplies a new number
    by a multiplier

    Args:
        multiplier (float): the float we will use in the returning function

    Returns:
        Callable[[float], float]: a function that mutlplies a float by the
        so-called multiplier float
    """
    def returned_multiplier(x: float) -> float:
        """this is the function we are creating to return from the main one

        Args:
            x (float): a float that the user will later supply

        Returns:
            float: x multiplied by the multiplier given when we created it
        """
        return x * multiplier
    return returned_multiplier
