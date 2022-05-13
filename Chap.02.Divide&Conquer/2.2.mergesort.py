def merge(h, m, U, V, S):
    i = j = k = 0
    while i < h and j < m:
        if U[i] < V[j]:
            S[k], i = U[i], i + 1
        else:
            S[k], j = V[j], j + 1
        k += 1
    if i >= h:
        while j < m:
            S[k], k, j = V[j], k + 1, j + 1
    else:
        while i < h:
            S[k], k, i = U[i], k + 1, i + 1

def mergesort(n, S):
    h = n // 2
    m = n - h
    if n > 1:
        U, V = S[:h], S[h:]
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)

from random import sample
S = sample(range(10, 100), 10)
mergesort(len(S), S)
print(S)
print(sorted(S))
