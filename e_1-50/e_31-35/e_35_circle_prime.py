# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

def is_circle_prime(n, primes):
    if n < 10:
        return True
    isTrue = True
    for i in range(len(str(n))):
        isTrue = is_prime(n, primes) and isTrue
        n =  int(str(n)[-1] + str(n)[0:-1])

    return isTrue

primes = read_mill_primes()
print(is_circle_prime(197, primes))

counter = 0
length = 0
for p in primes:
    if is_circle_prime(p, primes):
        counter += 1
        print(p, counter)
