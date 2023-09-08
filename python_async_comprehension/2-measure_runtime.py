#!/usr/bin/env python3
"""this module containsa a coroutine measure_runtime that executes
async_comprehension four times in parallel using asyncio.gather,
measures the runtime, and returns it"""


import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """this coroutine measures the runtime to run async_comprehension
    four times in parallel using asyncio.gather

    Returns:
        float: the runtime, which is around 10 seconds
    """
    start_time = perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = perf_counter()
    return end_time - start_time
