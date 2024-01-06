def fact(n: int) -> int:
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number for which factorial needs to be calculated.

    Returns:
    int: The factorial of the given number.
    """

    if n == 0:
        return 1
    return n * fact(n-1)

n = 100
print(sum([int(d) for d in str(fact(n))]))