import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

primes = sieve_of_eratosthenese(1000000)

print(primes[10000])