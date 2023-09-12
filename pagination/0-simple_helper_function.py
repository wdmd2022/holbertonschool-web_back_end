#!/usr/bin/env python3
"""this module contains a simple helper function we will use in our
pagination-based tasks, called index_range. The function should return
a tuple of size 2, containing a start index and an end index corresponding
to the range of indexes to return in a list for those particular pagination
parameters. Page numbers are 1-indexed, i.e., the first page is page 1."""


from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    if page == 1:
        tup_start: int = 0
    else:
        tup_start: int = page_size * page
    tup_end: int = tup_start + page_size
    return (tup_start, tup_end)
