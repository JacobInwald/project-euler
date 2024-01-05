def d(n: int) -> int:
    """
    Returns the nth digit of the Champernowne's constant.

    Parameters:
    n (int): The index of the digit to retrieve.

    Returns:
    int: The nth digit of the Champernowne's constant.
    """
    const = ''.join([str(i) for i in range(0, n+1)])
    return int(const[n])

prod = 1
arr =[d(10**i) for i in range(7)]
for a in arr:
    prod *= a
print(prod)
