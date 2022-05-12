def promising(i, weight, profit):
    global n, W, w, p, maxprofit
    if weight >= W:
        return False
    else:
        j = i + 1
        totweight = weight
        bound = profit
        while j <= n and totweight + w[j] <= W:
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if k <= n:
            bound += (W - totweight) * (p[k]//w[k])
    return bound > maxprofit
            
def knapsack(i, weight, profit):
    global n, W, w, p, bestset, include, maxprofit
    if weight <= W and profit > maxprofit:
        maxprofit = profit
        bestset = include[:]
    if promising(i, weight, profit):
        include[i + 1] = 1
        knapsack(i + 1, weight + w[i+1], profit + p[i+1])
        include[i + 1] = 0
        knapsack(i + 1, weight, profit)

n, W = map(int, input().split())
w = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
bestset, include = [0] * (n + 1), [0] * (n + 1)
maxprofit = 0
knapsack(0, 0, 0)
print(maxprofit)
for i in range(1, n + 1):
    if bestset[i] == 1:
        print(i, end = " ")
