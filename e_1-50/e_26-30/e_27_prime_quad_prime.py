def divisible(n, primes):
    for i in primes:
        if n % i == 0:
            return False
    return True

def prime_sieve(n):
    """Returns a list of primes <= n."""
    primes = [2]
    for i in range(3, n+1):
         if divisible(i, primes):
                primes.append(i)
    return primes

def gen_prime_quad(a, b):
    def f(n):
        return n**2 + a*n + b
    return f

primes_under_1000 = prime_sieve(1000)
for a in range(-1000, 1001):
    for b in primes_under_1000:
        for sign in [-1, 1]:
            f = gen_prime_quad(a, sign*b)
            primes = []
            n = 0
            while f(n) > 0 and f(n) in primes_under_1000:
                primes.append(f(n))
                n += 1
            if len(primes) > 40:
                print(a, sign*b, len(primes))
print(primes)