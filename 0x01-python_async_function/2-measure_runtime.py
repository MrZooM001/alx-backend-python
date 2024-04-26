#!/usr/bin/env python3
"""
Module to demostrate an asynchronous coroutine.
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n, max_delay):
    """
     Function with integers n and max_delay as arguments that measures
     the total execution time for wait_n(n, max_delay),
     and returns total_time / n.
    Args:
        n (int): time amount to be passed to wait_n()
        max_delay (int): delay to wait for
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
