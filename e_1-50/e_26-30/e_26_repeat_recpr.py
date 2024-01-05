from decimal import Decimal as d

def find_recpr(n: int) -> int:
    """
    Finds the length of the repeating reciprocal of a given number.

    Parameters:
    n (int): The number for which to find the repeating reciprocal length.

    Returns:
    int: The length of the repeating reciprocal.

    """
    if (n & (n - 1)) == 0 or n % 5 == 0:
        return 0
    if n % 2 == 0:
        return find_recpr(n // 2)
    
    nines = 9
    while (nines // n)*n != nines:
        nines = nines * 10 + 9
    return len(str(nines))


m = max(find_recpr(i) for i in range(1,1001))

for i in range(1,1001):
    if find_recpr(i) == m:
        print(i, m)
        break