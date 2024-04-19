#!/usr/bin/env python3
"""
Module to demostrate Complex types annotations.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """
    Typed-Annotated function that return a mixed-types tuple.

    Args:
        k (str): the first argument
        v (int | float): the second argument

    Return:
        a tuple of a string and square of the float number.
    """

    return (k, (v * v))
