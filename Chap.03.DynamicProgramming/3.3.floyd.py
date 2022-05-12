def floyd(n, W):
    global INF
    D = W
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

INF = 999
n, m = map(int, input().split())
W = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    W[i][i] = 0 
for _ in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w
for i in range(1, n + 1):
    print(W[i][1:])
    
D = floyd(n, W)
print("D = ")
for i in range(1, n + 1):
    print(D[i][1:])
