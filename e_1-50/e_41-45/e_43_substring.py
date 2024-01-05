# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *
from itertools import permutations


def get_all_pan() -> list[int]:
    """
    Returns a list of all pandigital numbers with 10 digits.

    A pandigital number is a number that contains all the digits from 0 to 9 exactly once.

    Returns:
        A list of all pandigital numbers with 10 digits.
    """
    digits = "0123456789"
    perms = [int(''.join(p)) for p in permutations(digits, 10)]
    return [p for p in perms if len(str(p)) == 10]


def is_sub_divisible(n: int) -> bool:
    """
    Checks if a number satisfies the substring divisibility property.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number satisfies the substring divisibility property, False otherwise.
    """
    str_n = str(n)
    divisors = [2, 3, 5, 7, 11, 13, 17]
    all_true = True
    for i in range(len(divisors)):
        div = divisors[i]
        sub = str_n[i+1] + str_n[i+2] + str_n[i+3]
        all_true = all_true and int(sub) % div == 0

    return all_true

print(sum(p for p in get_all_pan() if is_sub_divisible(p)))