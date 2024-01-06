import math as m

n = 1000

end = False
for a in range(1, n):
    for b in range(a, n):
        c = m.sqrt(a**2 + b**2)
        if a + b + c == n:
            print(int(a*b*c))
            end = True
            break
    if end:
        break
