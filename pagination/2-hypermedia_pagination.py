#!/usr/bin/env python3
"""this module contains a function index_range and a class Server which
serves to paginate a CSV for us into manageable chunks (after all, who
wants to read 10,000 baby names at once?) -- it also goes further to
implement a method get_hyper that takes the same arguments as get_page
and returns a dictionary including a bunch of cool new key-value pairs"""

import csv
import math
from typing import List, Tuple, Dict, Union


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

    def get_hyper(
            self, page: int = 1,
            page_size: int = 10
            ) -> Dict[str, Union[int, List[List], None]]:
        """this function is like get_page but instead of just getting
        a page, it returns an entire dictionary of cool info along with it

        Args:
            page (int, optional): page # to grab. Defaults to 1.
            page_size (int, optional): how many rows of data. Defaults to 10.

        Returns:
            Dict[str, Union[int, List[List], None]]: a dictionary detailing:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as integer
        """
        gotten_page = self.get_page(page, page_size)
        return_page_size = len(gotten_page)
        return_page_number = page
        next_page = (
            page + 1 if self.get_page(page + 1, page_size)
            else None
        )
        prev_page = (
            page - 1 if page - 1 > 0
            else None
        )
        total_pages = len(self.__dataset) // page_size
        return {
            "page_size": return_page_size,
            "page": return_page_number,
            "data": gotten_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }
