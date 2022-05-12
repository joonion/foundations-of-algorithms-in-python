from heapq import heappush, heappop

class Item:
    def __init__(self, id, weight, profit):
        self.id = id
        self.weight = weight
        self.profit = profit
        self.profit_per_weight = profit // weight
        
def knapsack(n, W, w, p):
    heap = []
    for i in range(n):
        item = Item(i + 1, w[i], p[i])
        heappush(heap, (-item.profit_per_weight, item))
    maxprofit = totweight = 0
    stolen = []
    while len(heap) > 0:
        item = heappop(heap)[1]
        if totweight + item.weight <= W:
            totweight += item.weight
            maxprofit += item.profit
            stolen.append((item.id, item.weight, item.profit))
        else:
            profit = (W - totweight) * item.profit_per_weight
            maxprofit += profit
            stolen.append((item.id, W - totweight, profit))
            break # Need not to go further
    return maxprofit, stolen
        
n, W = map(int, input().split())
w = list(map(int, input().split()))
p = list(map(int, input().split()))
print(n, W, w, p)
maxprofit, stolen = knapsack(n, W, w, p)
print(maxprofit)
print(stolen)

