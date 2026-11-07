#!/usr/bin/env python3
"""Module: Experimenting with Async in Python"""

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats representing the time delays"""
    task_wait_random = __import__('3-tasks').task_wait_random

    results = []

    time = [task_wait_random(max_delay) for i in range(n)]
    for delay in asyncio.as_completed(time):
        result = await delay
        results.append(result)

    return results
