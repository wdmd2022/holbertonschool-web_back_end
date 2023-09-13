#!/usr/bin/env python3
"""this module contains a function index_range and a class Server which
serves to paginate a CSV for us into manageable chunks (after all, who
wants to read 10,000 baby names at once?)"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this helpful little function helps us determine the start and end index
    for our particular pagination parameters

    Args:
        page (int): the page we wish to start on
        page_size (int): the number of records in a page

    Returns:
        Tuple[int, int]: a tuple containing the start and end indexes
    """
    tup_start: int = page_size * (page - 1)
    tup_end: int = tup_start + page_size
    return (tup_start, tup_end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """this function uses a helper function index_range to get the actual
        page desired from the data file defined as DATA_FILE. It raises errors
        if the inputs are not positive integers.

        Args:
            page (int, optional): the page to start on. Defaults to 1.
            page_size (int, optional): number of records per. Defaults to 10.

        Returns:
            List[List]: the list of records, or an empty list if request is
            out of range for the records that exist
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        self.dataset()
        index_tuple = index_range(page, page_size)
        if index_tuple[1] <= len(self.__dataset):
            return self.__dataset[index_tuple[0]:index_tuple[1]]
        else:
            return []
