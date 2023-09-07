#!/usr/bin/env python3
"""this module updates wait_n, which contains an async routine that spawns
wait_random n times with a specified max_delay, and modifies it to instead
call task_wait_random
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function that calls task_wait_random n times

    Args:
        n (int): how many times to call task_wait_random
        max_delay (int): parameter fed to task_wait_random

    Returns:
        List[float]: natually ascending list of complete times
    """
    to_do_list = [task_wait_random(max_delay) for _ in range(n)]
    result_list = []
    for task in asyncio.as_completed(to_do_list):
        result = await task
        result_list.append(result)
    return result_list
