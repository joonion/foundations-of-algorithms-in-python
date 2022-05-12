def knapsack(n, W, DP):
    global w, p
    if n == 0 or W <= 0:
        DP[(n, W)] = 0
    else:
        if (n, W) not in DP:
            if w[n] > W:
                DP[n, W] = knapsack(n-1, W, DP)
            else:
                DP[n, W] = max(knapsack(n-1, W-w[n], DP) + p[n],
                               knapsack(n-1, W, DP))
    return DP[(n, W)]
        
n, W = map(int, input().split())
w = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
print(n, W, w, p)
DP = {}
maxprofit = knapsack(n, W, DP)
print(maxprofit)
print(DP)
