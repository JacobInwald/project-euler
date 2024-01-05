# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *


primes = read_mill_primes()
print(is_truncate_prime(3797, primes))

sum = 0
length = 0
for p in primes:
    if is_truncate_prime(p, primes):
        sum += p
        print(p, sum)
