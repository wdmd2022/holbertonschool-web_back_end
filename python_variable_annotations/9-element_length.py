#!/usr/bin/env python3
"""this module contains a function that we will annotate with
the appropriate duck types. The beginning function was:
def element_length(lst):
    return [(i, len(i)) for i in lst]
"""


from typing import Sequence, List, Tuple


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """this function takes a list-like object and returns a new list
    of tuples, with each tuple containing an iterable, sequence-like
    object and the length of that object.

    Args:
        lst (Sequence): this is any type of list-like object that can use len

    Returns:
        List[Tuple[Sequence, int]]: a list filled with tuples, with each tuple
        consisting of a sequence-like object from lst, and its length
    """
    return [(i, len(i)) for i in lst]
