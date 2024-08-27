#!/usr/bin/env python3
"""Pagination"""

from typing import Tuple, List, Dict, Any
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """Paginating with Simple Page and Page Size Parameters"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Hypermedia pagination; returns a dict containing paginated
        data info
        """
        data = self.get_page(page, page_size)

        next_page = page + 1
        prev_page = page - 1
        total_pages = int(math.ceil(len(self.dataset()) / page_size))
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page if next_page < total_pages else None,
            "prev_page": prev_page if prev_page >= 1 else None,
            "total_pages": total_pages
        }
