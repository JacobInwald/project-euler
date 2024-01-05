# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

n = 1000000
primes = sieve_of_eratosthenese(n)
max_length = 0

for i in range(n//2):
    for j in range(i+1, int(m.sqrt(n+1))):
        s = sum(primes[i:j])
        if j-i > max_length and s < n and s in primes:
            print(j-i, s)
            max_length = j-i
            continue