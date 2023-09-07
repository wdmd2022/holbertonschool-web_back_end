#!/usr/bin/env python3
"""module requirements: Write an asynchronous coroutine that takes in an
integer argument (max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay (included and
float value) seconds and eventually returns it.
Use the random module.
"""


import asyncio
from random import uniform as thats_so_random


async def wait_random(max_delay: int = 10) -> float:
    """this coroutine takes an int argument. waits for a random delay
    between 0 and max_delay, and returns how long it waited

    Args:
        max_delay (int, optional): Upper bound of delay. Defaults to 10.

    Returns:
        float: the amount of time it randomly waited for
    """
    random_delay_time = thats_so_random(0, max_delay)
    await asyncio.sleep(random_delay_time)
    return random_delay_time
