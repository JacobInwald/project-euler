import math

def c(a, b): return math.sqrt((a**2)+(b**2))

def isTriplet(a, b, c): return a**2 + b**2 == int(c)**2

for a in range(0,1000):
     for b in range(a,1000):
             c1 = c(a, b)
             if(isTriplet(a,b,c1) and a+b+c1 == 1000):
                             print(a,b,c1)
