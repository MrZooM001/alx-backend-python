#!/usr/bin/env python3
"""
Module to demostrate an asynchronous coroutine.
"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    an asynchronous coroutine that takes in two integer arguments,
    and spawn task_wait_random for n times with the specified max_delay
    and return a sorted List of all delays as floats

    Args:
        n (int): time amount to spawn a function
        max_delay (int): delay to wait for
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    all_delays = await asyncio.gather(*(tasks))
    return sorted(all_delays)
