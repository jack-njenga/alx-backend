#!/usr/bin/env python3
"""
hypermedia Pagination
"""
from typing import List, Dict
import csv


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ init """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """

        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            self.__dataset = data[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ Dataset indexing starting at 0 """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            x_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns page data with index and next index
        """
        ind = self.indexed_dataset().keys()
        assert (index <= max(ind) and index >= 0)
        trueind = index
        while (trueind not in ind) and (trueind <= max(ind)):
            trueind += 1
        data = []
        while (len(data) < page_size) and (trueind <= max(ind)):
            row = self.indexed_dataset().get(trueind)
            if row:
                data.append(row)
            trueind += 1
        while (trueind not in ind) and (trueind <= max(ind)):
            trueind += 1
        return {
            'index': index,
            'next_index': trueind if (trueind <= max(ind))else None,
            'page_size': len(data),
            'data': data
        }
