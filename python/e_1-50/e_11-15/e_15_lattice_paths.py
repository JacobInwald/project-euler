n = 20

n += 1
lattice = [[1 for i in range(n)] for i in range(n)]

for y in range(1, n):
    for x in range(1, n):
        lattice[y][x] = lattice[y][x-1] + lattice[y-1][x]

print(lattice[20][20])