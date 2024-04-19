#!/usr/bin/env python3
"""11. More involved type annotations"""
from typing import TypeVar, Mapping, Any, Union

U = TypeVar("U")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[U, None] = None) -> Union[Any, U]:
    """type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
