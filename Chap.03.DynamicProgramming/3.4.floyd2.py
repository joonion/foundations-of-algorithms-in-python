def floyd2(n, W):
    global INF
    P = [[0] * (n + 1) for _ in range(n + 1)]
    D = W
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k
    return D, P

def path(i, j):
    k = P[i][j]
    if k != 0:
        path(i, k)
        print("v" + str(k), end = " ")
        path(k, j)
    
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
    
D, P = floyd2(n, W)
print("D = ")
for i in range(1, n + 1):
    print(D[i][1:])
print("P = ")
for i in range(1, n + 1):
    print(P[i][1:])

path(5, 3)