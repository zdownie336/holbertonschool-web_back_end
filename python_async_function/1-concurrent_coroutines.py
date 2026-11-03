#!/usr/bin/env python3
"""Module for concurrent coroutines"""

import asyncio


def wait_n(n: int, max_delay: int) -> list[float]:
    """returning a list of floats between n and max_delay"""
    wait_random = __import__('0-basic_async_syntax').wait_random

    results = []

    waits = [wait_random(max_delay) for i in range(n)]
    for delays in asyncio.as_completed(waits):
        exec = await delays
        results.append(exec)

    return results
