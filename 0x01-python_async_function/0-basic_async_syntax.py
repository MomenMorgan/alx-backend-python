#!/usr/bin/env python3

import asyncio
import random


def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and max_delay """
    delay = random.uniform(0, max_delay)
    asyncio.sleep(delay)
    return delay