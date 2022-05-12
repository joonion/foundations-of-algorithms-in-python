def promising(i):
    global n, W, vindex
    if i == n - 1 and not W[vindex[n-1]][vindex[0]]:
        return False
    elif i > 0 and not W[vindex[i-1]][vindex[i]]:
        return False
    else:
        for j in range(1, i):
            if vindex[i] == vindex[j]:
                return False
    return True

def hamiltonian(i):
    global n, vindex
    if promising(i):
        if i == n - 1:
            print(vindex)
        else:
            for j in range(2, n + 1):
                vindex[i + 1] = j
                hamiltonian(i + 1)

n, m = map(int, input().split())
vindex = [0] * n
W = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    W[u][v] = W[v][u] = 1
vindex[0] = 1
hamiltonian(0)