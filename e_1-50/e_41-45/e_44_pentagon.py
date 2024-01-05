import math as m

def gen_pent(n):
    return n*(3*n-1)//2

def is_pent(n):
    return (m.sqrt(24*n+1) + 1) /6 % 1 == 0

sum = 0
diff = 0
min_pair = (0, 0)
min_diff = 100000000
for i in range(1, 10000):
    for j in range(i, 10000):
        sum = gen_pent(i) + gen_pent(j)
        diff = gen_pent(j) - gen_pent(i)
        if is_pent(sum) and is_pent(diff) and diff < min_diff:
            min_pair = (i, j)
            min_diff = diff            
            print(gen_pent(i), gen_pent(j), diff)

print("")
print(min_pair, min_diff)