#!/usr/bin/env python3
"""Module: Experimenting with Async in Python"""

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats representing the time delays"""
    wait_random = __import__('0-basic_async_syntax').wait_random

    results = []

    time = [wait_random(max_delay) for i in range(n)]
    for delay in asyncio.as_completed(time):
        result = await delay
        results.append(result)

    return results
