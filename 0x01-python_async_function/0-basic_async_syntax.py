#!/usr/bin/env python3
"""
Module to demostrate an asynchronous coroutine.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    an asynchronous coroutine that takes in an integer argument,
    waits for a random delay between 0 and max_delay

    Args:
        max_delay (int): delay to wait for if provided, default is 10
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
