# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

def panMultiple(n: int) -> int:
    """
    Finds the smallest pandigital multiple of n.

    Parameters:
    n (int): The number to find the pandigital multiple of.

    Returns:
    int: The smallest pandigital multiple of n, or 0 if none is found.
    """

    mag_order = len(str(n))
    for i in range(1, mag_order+1):
        str_check = ""
        for mul in range(1, i+1):
            str_check += str(n*mul)
        if isPan(int(str_check)):
            return int(str_check)
    return 0

max = 0
for i in range(0,1000000):
    if panMultiple(i) > max:
        print(i, panMultiple(i))