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

def sumFactDigits(n: int) -> int:
    """
    Calculates the sum of the factorials of the digits of a given number.

    Args:
        n (int): The number for which to calculate the sum of factorial digits.

    Returns:
        int: The sum of the factorials of the digits of the given number.
    """
    return sum([fact(int(d)) for d in str(n)])

print(max([i for i in range(3 , 1000000) if sumFactDigits(i) == i]))