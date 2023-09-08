#!/usr/bin/env python3
"""this module contains a coroutine that takes no arguments and loops
10 times, each time asynchronously waiting 1 second, then yielding a
random number between 0 and 10 with the help of the random module.
"""


import asyncio
from random import uniform as silly_number
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """this coroutine loops 10 times, each time waiting a second before
    yielding a random float between 0 and 10

    Returns:
        Generator[float, None, None]: the asynchronous generator

    Yields:
        Generator[float, None, None]: generator functionality
        for getting floats
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield silly_number(0, 10)
