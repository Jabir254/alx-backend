#!/usr/bin/env python3
'''Simple helper functions'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''return a tuple containing a start and end index'''
    if page <= 0 or page_size <= 0:
        return None

    start_index, end_index = 0, 0
    for i in range(page):
        start_index = end_index
        end_index += page_size

    return (start_index, end_index)
