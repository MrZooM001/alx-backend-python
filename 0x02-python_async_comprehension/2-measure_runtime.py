#!/usr/bin/env python3
"""
Module to demostrate an async comprehension.
"""
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """
    Coroutine that executes async_comprehension() four times in parallel using asyncio.gather,
    measures the total runtime and return it.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    total_runtime = asyncio.get_event_loop().time() - start_time

    return total_runtime
