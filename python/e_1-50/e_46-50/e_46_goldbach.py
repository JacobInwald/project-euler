# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *
import math as m

def gen_composite_nums(n: int) -> list[int]:
    """
    Generates a list of composite numbers up to a given limit.

    Args:
        n (int): The upper limit for generating composite numbers.

    Returns:
        list[int]: A list of composite numbers.

    """
    comps = set()
    for i in range(2, n):
        for j in range(i, n//i):
            comps.add(i*j)
    return comps

import math

def gold_conjec(n: int, primes: list[int]) -> bool:
    """
    Checks if the given number `n` can be expressed as the sum of a prime number and twice a square number.

    Args:
        n (int): The number to be checked.
        primes (list[int]): List of prime numbers.

    Returns:
        bool: True if `n` satisfies the Goldbach's conjecture, False otherwise.
    """
    for p in primes:
        if p > n-1:
            return False
        
        sub = (n-p) / 2
        if sub % 1 == 0 and math.sqrt(sub) % 1 == 0:
            return True
        
    return False

n = 10000
primes = sieve_of_eratosthenese(n)
odd_comps = [i for i in gen_composite_nums(n) if i % 2 != 0 and not gold_conjec(i, primes)]

print(odd_comps[0] if len(odd_comps) > 0 else "not found")