#!/usr/bin/env python3
"""Pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Paginating with Simple Page and Page Size Parameters"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
