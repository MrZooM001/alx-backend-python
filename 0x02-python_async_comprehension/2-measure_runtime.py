#!/usr/bin/env python3
"""
Module to demostrate an async comprehension.
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension() four times in parallel using asyncio.gather,
    measures the total runtime and return it.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_runtime = time.time() - start_time

    return total_runtime
