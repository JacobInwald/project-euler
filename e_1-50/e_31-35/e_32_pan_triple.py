import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

def tripletIsPan(a: int, b: int, c: int) -> bool:
    """
    Check if the concatenation of three numbers forms a pandigital number.

    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.

    Returns:
        bool: True if the concatenation is a pandigital number, False otherwise.
    """
    return isPan(str(a) + str(b) + str(c))

triplets = []

for i in range(1, 100):
    for j in range(i, 10000):
        if tripletIsPan(i, j, i*j):
            triplets.append((i, j, i*j))
            print(i, j, i*j)

set_of_pans = set([t[2] for t in triplets])

print(sum(set_of_pans))