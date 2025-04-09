"""
Author: Braulio
Date: 7-4-2025
"""

import math
import random


def get_score(range:int) -> float:
    num = random.uniform(0.0, 90)
    return math.trunc(num * 100) / 100
