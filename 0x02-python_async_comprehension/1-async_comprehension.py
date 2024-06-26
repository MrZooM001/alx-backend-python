#!/usr/bin/env python3
"""
Module to demostrate an async comprehension.
"""
import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    random_nums = [i async for i in async_generator()]
    return random_nums
