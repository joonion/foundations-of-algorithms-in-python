def subsets_containing_k_vertices(n, k):
    S = []
    for A in range(2 ** (n-1)):
        if bin(A).count("1") == k:
            S.append(A)
    return S

def not_in_A(n, A):
    S = []
    for i in range(n - 1):
        if A & (1 << i) == 0:
            S.append(2 + i)
    return S

def in_A(n, A):
    S = []
    for i in range(n - 1):
        if A & (1 << i) != 0:
            S.append(2 + i)
    return S

def diff(A, j):
    return A & ~(1 << (j - 2))

def minimum(n, i, A, W, D):
    global INF
    minvalue, minj = INF, 0
    for j in in_A(n, A):
        value = W[i][j] + D[j][diff(A, j)]
        if value < minvalue:
            minvalue, minj = value, j
    return minvalue, minj
    
def travel(n, W):
    global INF
    D = [[INF] * (2**(n-1)) for _ in range(n + 1)]
    P = [[0] * (2**(n-1)) for _ in range(n + 1)]
    for i in range(2, n + 1):
        D[i][0] = W[i][1]
        
    for k in range(1, n - 1):
        for A in subsets_containing_k_vertices(n, k):
            for i in not_in_A(n, A):
                D[i][A], P[i][A] = minimum(n, i, A, W, D)
                
    A = 2 ** (n - 1) - 1 # A = V - {v1}
    D[1][A], P[1][A] = minimum(n, 1, A, W, D)
    return D[1][A], D, P

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

minlength, D, P = travel(n, W)
print("D = ")
for i in range(1, n + 1):
    print(D[i])
print("P = ")
for i in range(1, n + 1):
    print(P[i])
print("minlength = ", minlength)

    