def d(n: int) -> int:
    const = ''.join([str(i) for i in range(0, n+1)])
    return int(const[n])

prod = 1
arr =[d(10**i) for i in range(7)]
for a in arr:
    prod *= a
print(prod)
