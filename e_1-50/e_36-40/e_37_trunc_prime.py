# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

def is_truncate_prime(n, primes):
    str_n = str(n)
    if len(str_n) <= 1 or n not in primes:
        return False
    for i in range(1, len(str_n)):
        if int(str_n[0:i]) not in primes:
            return False
        if int(str_n[i:]) not in primes:
            return False
    return True

primes = read_mill_primes()
print(is_truncate_prime(3797, primes))

sum = 0
length = 0
for p in primes:
    if is_truncate_prime(p, primes):
        sum += p
        print(p, sum)
