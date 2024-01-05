# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

def is_circle_prime(n, primes):
    if n < 10:
        return True
    
    for i in range(len(str(n))):
        if n not in primes:
            return False
        n =  int(str(n)[-1] + str(n)[0:-1])

    return True


n=10000
primes = sieve_of_eratosthenese(n)

counter = 0
length = 0
for p in primes:
    if is_circle_prime(p, primes):
        counter += 1
        print(p, counter)

