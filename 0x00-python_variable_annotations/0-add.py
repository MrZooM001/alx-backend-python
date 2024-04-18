#!/usr/bin/env python3
"""
Module to demostrate basic variable annotations.
"""


def add(a: float, b: float) -> float:
    """
    Typed-Annotated function that returns sum of two float numbers.

    Args:
        a (float): the first float number
        b (float): the second float number

    Return:
        Sum of a and b as float
    """
    return a + b
