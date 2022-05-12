class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit

def boundof(u, n, W, w, p):
    if u.weight >= W:
        return 0
    else:
        totweight = u.weight
        bound = u.profit
        j = u.level + 1
        while j <= n and totweight + w[j] <= W:
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if k <= n:
            bound += (W - totweight) * (p[k] // w[k])
        return bound

def knapsack2(n, W, w, p):
    queue = [] # Initialize Queue
    v = Node(0, 0, 0)
    bound = boundof(v, n, W, w, p)
    maxprofit = 0
    queue.append(v)
    print(v.level, v.weight, v.profit, bound, maxprofit, True)
    while len(queue) != 0:
        v = queue.pop(0)
        nlevel = v.level + 1
        u = Node(nlevel, v.weight + w[nlevel], v.profit + p[nlevel])
        if u.weight <= W and u.profit > maxprofit:
            maxprofit = u.profit
        bound = boundof(u, n, W, w, p)
        if bound > maxprofit:
            queue.append(u)
        print(u.level, u.weight, u.profit, bound, maxprofit, bound > maxprofit)
        u = Node(nlevel, v.weight, v.profit)
        bound = boundof(u, n, W, w, p)
        if bound > maxprofit:
            queue.append(u)
        print(u.level, u.weight, u.profit, bound, maxprofit, bound > maxprofit)
    return maxprofit

n, W = map(int, input().split())
items = []
w = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
print(n, W)
print(w)
print(p)

maxprofit = knapsack2(n, W, w, p)
print(maxprofit)