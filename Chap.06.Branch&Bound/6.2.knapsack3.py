from heapq import heappush, heappop
class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = 0

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

def knapsack3(n, W, w, p):
    heap = [] # Initialize Priority Queue
    v = Node(0, 0, 0)
    v.bound = boundof(v, n, W, w, p)
    maxprofit = 0
    heappush(heap, (-v.bound, v))
    print(v.level, v.weight, v.profit, v.bound, maxprofit, True)
    while len(heap) != 0:
        v = heappop(heap)[1]
        # print(v.level, v.weight, v.profit, v.bound)
        if v.bound > maxprofit:
            nlevel = v.level + 1
            u = Node(nlevel, v.weight + w[nlevel], v.profit + p[nlevel])
            if u.weight <= W and u.profit > maxprofit:
                maxprofit = u.profit
            u.bound = boundof(u, n, W, w, p)
            if u.bound > maxprofit:
                heappush(heap, (-u.bound, u))
            print(u.level, u.weight, u.profit, u.bound, maxprofit, u.bound > maxprofit)
            u = Node(nlevel, v.weight, v.profit)
            u.bound = boundof(u, n, W, w, p)
            if u.bound > maxprofit:
                heappush(heap, (-u.bound, u))
            print(u.level, u.weight, u.profit, u.bound, maxprofit, u.bound > maxprofit)
    return maxprofit

n, W = map(int, input().split())
items = []
w = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
print(n, W)
print(w)
print(p)

maxprofit = knapsack3(n, W, w, p)
print(maxprofit)