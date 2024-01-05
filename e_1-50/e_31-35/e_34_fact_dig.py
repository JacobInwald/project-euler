def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n-1)

def sumFactDigits(n: int) -> int:
    return sum([fact(int(d)) for d in str(n)])

print(max([i for i in range(3 , 1000000) if sumFactDigits(i) == i]))