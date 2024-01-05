import collections
import itertools
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

def gen_triag_num(n: int) -> int:
    """
    Generates the nth triangular number.
    
    Parameters:
    n (int): The index of the triangular number to generate.
    
    Returns:
    int: The nth triangular number.
    """
    return int(n * (n + 1) / 2)


def prod(iterable: list[int]) -> int:
    """
    Calculates the product of all the elements in the given iterable.

    Args:
        iterable (list[int]): The list of integers to calculate the product from.

    Returns:
        int: The product of all the elements in the iterable.
    """
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factorize(n)
    pf_with_multiplicity = collections.Counter(pf)
    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]
    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)

for i in range(100000):
    num = gen_triag_num(i)
    if len([i for i in get_divisors(num)]) > 500:
        print(num)
        break