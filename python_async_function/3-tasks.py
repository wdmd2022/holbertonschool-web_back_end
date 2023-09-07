#!/usr/bin/env python3
"""this module contains a function (non-async) that takes an int and returns
an ayncio.Task
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """this non-async function returns a coroutine (wait_random) wrapped
    in an asyncio Task object

    Args:
        max_delay (int): max delay to be passed to wait_random

    Returns:
        asyncio.Task: an asyncio Task object
    """
    return asyncio.create_task(wait_random(max_delay))
