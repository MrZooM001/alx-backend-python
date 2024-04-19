#!/usr/bin/env python3
"""
Module to demostrate Complex types annotations.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Typed-Annotated function that returns the sum of list's elements as float.

    Args:
        input_list (list[float]): list of float numbers

    Return:
        the sum of list's elements as a float.
    """
    return sum(num for num in input_list)
