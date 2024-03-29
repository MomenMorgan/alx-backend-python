#!/usr/bin/env python3

""" 1. Let's execute multiple coroutines at the same time with async  """

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int = 0, max_delay: int = 10) -> list:
    """ spawn wait_random n times with the specified max_delay """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
