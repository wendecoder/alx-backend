#!/usr/bin/env python3
"""A script that contains index_range function"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a
    start index and an end index"""
    begin = (page - 1) * page_size
    return (begin, begin + page_size)
