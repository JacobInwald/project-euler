# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *
import math as m

def gen_composite_nums(n: int) -> list[int]:
    comps = set()
    for i in range(2, n):
        for j in range(i, n//i):
            comps.add(i*j)
    return comps

def gold_conjec(n, primes):
    for p in primes:
        if p > n-1:
            return False
        
        sub = (n-p) / 2
        if sub % 1 == 0 and m.sqrt(sub) % 1 == 0:
            return True
        
    return False

n = 10000
primes = sieve_of_eratosthenese(n)
odd_comps = [i for i in gen_composite_nums(n) if i % 2 != 0 and not gold_conjec(i, primes)]

print(odd_comps[0] if len(odd_comps) > 0 else "not found")