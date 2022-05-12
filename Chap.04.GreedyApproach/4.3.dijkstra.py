def dijkstra(n, W):
    global INF, touch, length
    F = []
    for i in range(2, n + 1):
        touch[i] = 1
        length[i] = W[1][i]
    for _ in range(n - 1):
        min = INF
        for i in range(2, n + 1):
            if 0 <= length[i] < min:
                min = length[i]
                vnear = i
        e = (touch[vnear], vnear, W[touch[vnear]][vnear])
        F.append(e)
        for i in range(2, n + 1):
            if length[vnear] + W[vnear][i] < length[i]:
                length[i] = length[vnear] + W[vnear][i]
                touch[i] = vnear
        length[vnear] = -1 # move vnear to Y from V - Y
    return F
                
INF = 999
n, m = map(int, input().split())
touch = [0] * (n + 1)
length = [0] * (n + 1)
W = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w
    
F = dijkstra(n, W)
print(F)