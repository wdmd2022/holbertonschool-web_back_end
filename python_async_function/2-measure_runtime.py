#!/usr/bin/env python3
"""this module imports wait_n and measures execution time.
"""

import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    async def nested_async_wait():
        await wait_n(n, max_delay)
    start_time = perf_counter()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(nested_async_wait())
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
