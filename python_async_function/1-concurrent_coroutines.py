#!/usr/bin/env python3
"""this module contains an async routine that spawns wait_random n times
with a specified max_delay
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function that calls wait_random n times

    Args:
        n (int): how many times to call wait_random
        max_delay (int): parameter fed to wait_random

    Returns:
        List[float]: natually ascending list of complete times
    """
    to_do_list = [wait_random(max_delay) for _ in range(n)]
    result_list = []
    for task in asyncio.as_completed(to_do_list):
        result = await task
        result_list.append(result)
    return result_list
