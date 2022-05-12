def prim(n, W):
    global INF, nearest, distance
    F = []
    for i in range(2, n + 1):
        nearest[i] = 1
        distance[i] = W[1][i]
    for _ in range(n - 1):
        min = INF
        for i in range(2, n + 1):
            if 0 <= distance[i] < min:
                min = distance[i]
                vnear = i
        e = (nearest[vnear], vnear, W[nearest[vnear]][vnear])
        F.append(e)
        distance[vnear] = -1 # move vnear to Y from V - Y
        for i in range(2, n + 1):
            if W[i][vnear] < distance[i]:
                distance[i] = W[i][vnear]
                nearest[i] = vnear
    return F
                
INF = 999
n, m = map(int, input().split())
nearest = [0] * (n + 1)
distance = [0] * (n + 1)
W = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = W[v][u] = w
    
F = prim(n, W)
print(F)