def merge2(low, mid, high, S):
    U = [0] * (high - low + 1)
    i, j, k = low, mid + 1, 0
    while i <= mid and j <= high:
        if S[i] < S[j]:
            U[k], i = S[i], i + 1
        else:
            U[k], j = S[j], j + 1
        k += 1
    if i > mid:
        while j <= high:
            U[k], k, j = S[j], k + 1, j + 1
    else:
        while i <= mid:
            U[k], k, i = S[i], k + 1, i + 1
    for k in range(len(U)):
        S[low + k] = U[k]

def mergesort2(low, high, S):
    if low < high:
        mid = (low + high) // 2
        mergesort2(low, mid, S)
        mergesort2(mid + 1, high, S)
        merge2(low, mid, high, S)

from random import sample
S = sample(range(10, 100), 10)
mergesort2(0, len(S)-1, S)
print(S)
print(sorted(S))
