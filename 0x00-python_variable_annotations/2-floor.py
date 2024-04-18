#!/usr/bin/env python3
"""
Module to demostrate basic variable annotations.
"""
import math


def floor(n: float) -> int:
    """
    Typed-Annotated function that returns a floor number of a float number.

    Args:
        n (float): the float number to floor

    Return:
        the floor number of a float number
    """
    return math.floor(n)
