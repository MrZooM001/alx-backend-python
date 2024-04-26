#!/usr/bin/env python3
"""
Module to demostrate an asynchronous coroutine.
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns a asyncio.Task

    Args:
        max_delay (int): delay to wait for
    """
    return asyncio.create_task(wait_random(max_delay))
