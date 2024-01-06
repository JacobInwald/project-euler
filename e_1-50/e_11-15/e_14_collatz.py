def collatz_seq(n: int) -> list[int]:
    """
    Generates the Collatz sequence starting from the given number.

    Args:
        n (int): The starting number.

    Yields:
        int: The next number in the Collatz sequence.

    Returns:
        list[int]: The Collatz sequence starting from the given number.
    """
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        yield n

max = 0
starter=0
for i in range(1, 1000000):
    seq = list(collatz_seq(i))
    if max <= len(seq):
        max = len(seq)
        starter = i
print(starter, max)