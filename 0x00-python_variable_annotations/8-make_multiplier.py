#!/usr/bin/env python3
"""
Module to demostrate Complex types annotations.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Typed-Annotated function that return a function

    Args:
        multiplier (float): the first argument

    Return:
        a function that multiplies a float by multiplier arg
    """
    def float_multiplier(fl: float) -> float:
        return fl * multiplier
    
    return float_multiplier
