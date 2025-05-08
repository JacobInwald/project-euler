import math
import tqdm

def get_divs(n):
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            yield i
            yield n // i
    
    if math.sqrt(n) % 1 == 0:
        yield math.sqrt(n)

abundant = [n for n in range(28124-12) if sum(get_divs(n)) - n > n]
print(abundant[0:10])

sums = []
for x in tqdm.tqdm(range(len(abundant))):
    for y in abundant[x:]:
        sums.append(abundant[x]+y)

sums = set(sums) 
n = [i for i in range(1,28124)]
n = set(n)
print(list(n.difference(sums))[0:20])
print(sum(n.difference(sums)))
