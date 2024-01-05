# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *
from itertools import permutations

def gen_perms(n):
    n = str(n)
    return [int(''.join(x)) for x in permutations(n, len(n))]

primes = sieve_of_eratosthenese(10000)
explored_perms = set()

for p in range(1000, 10000): 
    if p in primes and p not in explored_perms:
        if '0' in str(p):
            continue
        prime_permutations = []
        for perm in gen_perms(p):
            if perm in primes:
                prime_permutations.append(perm)
        prime_permutations = set(prime_permutations)
        explored_perms.update(prime_permutations)

        if len(prime_permutations) >= 3:
            for triplet in permutations(prime_permutations, 3):
                triplet = sorted(triplet)
                diffs = [triplet[i+1] - triplet[i] for i in range(2)]
                if diffs[0] == diffs[1]:
                    print(triplet, diffs)
