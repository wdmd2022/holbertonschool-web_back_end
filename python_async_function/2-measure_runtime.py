#!/usr/bin/env python3
"""this module imports wait_n and measures execution time.
"""

import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """this function is a synchronous function that uses a nested event loop
    to run asynchronous code whose execution time we measure and return

    Args:
        n (int): number of times wait_n will execute
        max_delay (int): delay variable for setting range of wait times on
        wait_n executions

    Returns:
        float: seconds it took to run the async code
    """
    async def nested_async_wait() -> None:
        """nested async function definition which thereby allows us to call
        wait_n function, which is asynchronous, from the synchronous
        measure_time function we will ultimately import into our main file
        """
        await wait_n(n, max_delay)
    start_time = perf_counter()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(nested_async_wait())
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
