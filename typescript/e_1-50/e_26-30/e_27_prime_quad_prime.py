import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *


def gen_prime_quad(a: int, b: int):
    """
    Generates a quadratic function of the form f(n) = n^2 + a*n + b.

    Args:
        a (int): The coefficient of the linear term.
        b (int): The constant term.

    Returns:
        function: A quadratic function that takes an integer argument and returns the corresponding value.
    """
    def f(n):
        return n**2 + a*n + b
    return f

primes_under_1000 = sieve_of_eratosthenese(1000)
for a in range(-1000, 1001):
    for b in primes_under_1000:
        for sign in [-1, 1]:
            f = gen_prime_quad(a, sign*b)
            primes = []
            n = 0
            while f(n) > 0 and f(n) in primes_under_1000:
                primes.append(f(n))
                n += 1
            if len(primes) > 40:
                print(a, sign*b, len(primes))
print(primes)