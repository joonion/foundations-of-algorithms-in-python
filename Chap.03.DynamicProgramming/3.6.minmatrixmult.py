def minimum(i, j, M, d):
    global INF
    minvalue, mink = INF, 0
    for k in range(i, j):
        value = M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]
        if value < minvalue:
            minvalue, mink = value, k
    return minvalue, mink

def minmult(n, d):
    global INF
    M = [[INF] * (n + 1) for _ in range(n + 1)]
    P = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][i] = 0
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i][j], P[i][j] = minimum(i, j, M, d)
    return M[1][n], M, P

def order(i, j, P):
    if i == j:
        return "A" + str(i)
    else:
        k = P[i][j]
        left = order(i, k, P)
        right = order(k + 1, j, P)
        return "(" + left + right + ")"        

INF = 999
n = int(input())
d = list(map(int, input().split()))
minvalue, M, P = minmult(n, d)
print("M = ")
for i in range(1, n + 1):
    print(M[i][i:])
print("P = ")
for i in range(1, n + 1):
    print(P[i][i:])
print("minmult = ", minvalue)

multorder = order(1, n, P)
print(multorder)