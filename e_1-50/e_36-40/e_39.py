import numpy as np

def x(a, b):
    c = np.sqrt(a*a + b*b)
    if c % 1 == 0:
        return np.sqrt(a*a + b*b) + a + b
    else:
        return -1

p_counts = {k:0 for k in range(1,1001)}

for a in range(1, 1000):
    for b in range(a, 1000):
        p = x(a,b)
        if p <= 1000 and p > 0:
            p_counts[p] += 1

max = 0
p_max = 0
for k,v in p_counts.items():
    if v > max:
        max = v
        p_max = k
print(p_max)