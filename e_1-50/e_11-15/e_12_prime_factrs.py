import collections
import itertools


def gen_triag_num(n):
    return int(n * (n + 1) / 2)

def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1
    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factors(n)
    pf_with_multiplicity = collections.Counter(pf)
    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]
    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)

for i in range(100000):
    num = gen_triag_num(i)
    if len([i for i in get_divisors(num)]) > 500:
        print(num)
        break