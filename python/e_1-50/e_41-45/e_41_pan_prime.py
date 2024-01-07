# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

primes = sieve_of_eratosthenese(10000000)
for p in primes:
    for i in range(1,9):
        if isPan(p, i):
            print(p)

