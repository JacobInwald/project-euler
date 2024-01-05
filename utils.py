import os
import math as m


def divisible(n: int, primes: list[int]) -> bool:
    """Checks if n is divisible by numbers in the given list"""
    for i in primes:
        if (n // i) * i == n:
            return False
    return True


def sieve_of_eratosthenese(n):
    numbers = {i:False for i in range(2,n+1,1)}
    primes = []
    for k in numbers.keys():
        if numbers[k]:
            continue
        else:
            primes.append(k)

        i = k
        while i <= n:
            numbers[i] = True
            i += k
    
    return primes


def is_prime(n: int, primes: list[int]=None) -> bool:
    if not primes:
        primes = sieve_of_eratosthenese(n)
    for i in primes:
        if i < n and n % i == 0:
            return False
    return True

def isPan(n: int, upto=9) -> bool:
    n = str(n)
    if len(n) != upto:
        return False
    for i in range(1, upto+1):
        if str(i) not in n:
            return False
    return True

def gen_tri(n):
    return n*(n+1)//2

def is_tri(n):
    return ((m.sqrt(8*n+1) - 1) / 2) % 1 == 0

def gen_pent(n):
    return n*(3*n-1)//2

def is_pent(n):
    return ((m.sqrt(24*n+1) + 1) / 6) % 1 == 0

def gen_hex(n):
    return n*(2*n-1)

def is_hex(n):
    return ((m.sqrt(8*n+1) + 1) / 4) % 1 == 0

def is_circle_prime(n, primes):
    if n < 10:
        return True
    isTrue = True
    for i in range(len(str(n))):
        isTrue = is_prime(n, primes) and isTrue
        n =  int(str(n)[-1] + str(n)[0:-1])

    return isTrue


def prime_factorize(n, primes=None):
    if not primes:
        primes = sieve_of_eratosthenese(n)
    
    for p in primes:
        if p > n:
            return []
        
        if n % p == 0:
            return [p] + prime_factorize(n//p, primes)
    
    return []
    



def gen_mill_primes():
    mill_primes = sieve_of_eratosthenese(1000000)

    with open(os.path.join(os.path.dirname(__file__), 'data/million_primes.txt'), 'w') as f:
        nums = ''
        for n in mill_primes:
            nums += str(n) + ','
        f.writelines(nums)

def read_mill_primes():
    with open(os.path.join(os.path.dirname(__file__), 'data/million_primes.txt'), 'r') as f:
        nums = f.readline().split(',')
        return [int(n) for n in nums if n != '']
