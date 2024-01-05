
def isPan(n: int) -> bool:
    n = str(n)
    if len(n) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in n:
            return False
    return True

def tripletIsPan(a: int, b: int, c: int) -> bool:
    return isPan(str(a) + str(b) + str(c))

triplets = []

for i in range(1, 100):
    for j in range(i, 10000):
        if tripletIsPan(i, j, i*j):
            triplets.append((i, j, i*j))
            print(i, j, i*j)

set_of_pans = set([t[2] for t in triplets])

print(sum(set_of_pans))