#!/usr/bin/env python3
"""
Module to demostrate Complex types annotations.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Typed-Annotated function that sum mixed-types elements of a list.

    Args:
        input_list (list[float]): list of float numbers

    Return:
        the sum of list's mixed elements as a float.
    """
    
    return sum(num for num in mxd_lst)
