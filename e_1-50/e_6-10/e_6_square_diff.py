n = 100

sum_square = sum(i**2 for i in range(1, n+1))
square_sum = sum(i for i in range(1, n+1))**2

print(square_sum - sum_square)