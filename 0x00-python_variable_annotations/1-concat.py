#!/usr/bin/env python3
"""
Module to demostrate basic variable annotations.
"""


def concat(str1: str, str2: str) -> str:
    """
    Typed-Annotated function that returns a concat of two strings.

    Args:
        str1 (str): the first string to concat
        str2 (str): the second string to concat

    Return:
        Concatenated string of str1 and str2
    """
    return str1 + str2
