#!/usr/bin/env python3
"""
Module to demostrate basic variable annotations.
"""


def to_str(n: float) -> str:
    """
    Typed-Annotated function that returns a string representation of the float

    Args:
        n (float): the float number to convert to a string

    Return:
        the string representation of the float
    """
    return '{}'.format(n)
