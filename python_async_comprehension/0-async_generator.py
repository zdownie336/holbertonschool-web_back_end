#!/usr/bin/env python3
"""Module for making async comprehension and understanding"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """This function is around async generation and comprehension"""

    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
