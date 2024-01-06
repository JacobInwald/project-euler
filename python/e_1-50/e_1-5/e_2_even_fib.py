def fib_upto(n: int) -> list[int]:
    """
    Generate a list of Fibonacci numbers up to a given limit.

    Args:
        n (int): The limit up to which Fibonacci numbers should be generated.

    Returns:
        list[int]: A list of Fibonacci numbers up to the given limit.
    """
    list = [0] * n
    list[0] = 1
    list[1] = 1
    for i in range(2, n):
        list[i] = list[i-1] + list[i-2]
    return list

print(sum(n for n in fib_upto(100) if n % 2 == 0 and n < 4000000))