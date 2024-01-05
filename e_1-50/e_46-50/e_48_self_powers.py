def power(n):
    return n**n

n= 1000

print(sum(power(n) for n in range(1,n+1)))