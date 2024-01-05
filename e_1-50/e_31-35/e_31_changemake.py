
def branch(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    num_ways_for_amt = {k : [0 for i in coins] for k in range(0, n+1)}

    for amt in range(1, n+1):
        for i in range(len(coins)):
            if coins[i] == amt:
                num_ways_for_amt[amt][i] = 1
            elif coins[i] < amt:
                for j in range(len(coins)):
                    if coins[j] <= coins[i]:
                        num_ways_for_amt[amt][i] += num_ways_for_amt[amt - coins[i]][j]
    for k in num_ways_for_amt.keys():
        num_ways_for_amt[k] = sum(num_ways_for_amt[k])
    return num_ways_for_amt

print(branch(200))
