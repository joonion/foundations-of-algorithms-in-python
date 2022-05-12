def promising(i):
    global W, vcolor
    for j in range(1, i):
        if W[i][j] != 0 and vcolor[i] == vcolor[j]:
            return False
    return True
    
def mcoloring(i, m):
    global n, vcolor
    if promising(i):
        if i == n:
            print(vcolor[1:])
        else:
            for color in range(1, m + 1):
                vcolor[i + 1] = color
                mcoloring(i + 1, m)

m = int(input())
n, k = map(int, input().split())
vcolor = [0] * (n + 1)
W = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    u, v = map(int, input().split())
    W[u][v] = W[v][u] = 1
mcoloring(0, m)