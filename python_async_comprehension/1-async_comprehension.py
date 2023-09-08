#!/usr/bin/env python3
"""this module contains a coroutine async_comprehension that takes
no arguments, collecting 10 random numbers using an async comprehensing
over async_generator, and then returning the 10 random numbers"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """this coroutine collects 10 random numbers through async comprehensing
    of async_generator, and then returns all the numbers it collects

    Returns:
        List[float]: a list of random-ish floats between 0 and 10
    """
    return [generated_number async for generated_number in async_generator()]
