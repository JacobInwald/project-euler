# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *


def distinct_prime_factors(xs: list[int], primes: list[int] = None) -> int:
    """
    Returns the set of distinct prime factors of the numbers in the given list.

    Args:
        xs (list[int]): The list of numbers.
        primes (list[int], optional): The list of prime numbers. If not provided, it will be generated using the sieve of Eratosthenes algorithm.

    Returns:
        set[int]: The set of distinct prime factors.
    """
    if primes == None:
        primes = sieve_of_eratosthenese(max(xs))
    distinct_factors = set()
    for x in xs:
        x_fac = prime_factorize(x, primes)
        distinct_factors.update(x_fac)

    return distinct_factors

n =1000000
primes = sieve_of_eratosthenese(n)
num_distinct = 4

for i in range(1, n):
    check = True
    for x in range(num_distinct):
        check = check and len(distinct_prime_factors([i+x], primes)) == num_distinct
    
    if check:
        print(i)
        break
