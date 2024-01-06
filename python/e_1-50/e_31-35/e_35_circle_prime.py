# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

n=1000000
primes = sieve_of_eratosthenese(n)

counter = 0
length = 0
for p in primes:
    if is_circle_prime(p, primes):
        counter += 1
        print(p, counter)

