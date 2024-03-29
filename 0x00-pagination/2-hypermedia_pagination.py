#!/usr/bin/env python3
"""
Pagination
"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ init """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """

        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            self.__dataset = data[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ data pages """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page > 0
        start, end = index_range(page, page_size)
        if start > len(self.dataset()):
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns data page
        """
        pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': (page + 1) if (page + 1 <= pages) else None,
            'prev_page': (page - 1) if (page - 1 > 0) else None,
            'total_pages': pages
        }
