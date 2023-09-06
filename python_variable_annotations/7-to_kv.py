#!/usr/bin/env python3
"""this module contains a type-annotated function 'to_kv' that takes
a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v and should be annotated
as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """this function takes a string and a number and returns a tuple
    with the string and the number squared, as a float

    Args:
        k (str): the string we will eventually return with a squared number
        v (Union[int, float]): a number, either an int or float, we will ^2

    Returns:
        Tuple[str, float]: our original string in a tuple with the v^2 float
    """
    return (k, float(v*v))
