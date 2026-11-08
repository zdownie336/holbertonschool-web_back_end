#!/usr/bin/env python3
"""Module: async comprehension"""
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """returning a list of random numbers"""

    async_generator = __import__('0-async_generator').async_generator

    return [i async for i in async_generator()]
