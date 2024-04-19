#!/usr/bin/env python3
"""
Module to demostrate Complex types annotations.
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list or tuples"""
    return [(i, len(i)) for i in lst]
