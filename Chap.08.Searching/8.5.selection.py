def partition(low, high, S):
    pivotitem = S[low]
    j = low
    for i in range(low + 1, high + 1):
        if S[i] < pivotitem:
            j += 1
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint
    
def selection(k, low, high, S):
    if low == high:
        return S[low]
    else:
        pivotpoint = partition(low, high, S)
        if k == pivotpoint:
            return S[pivotpoint]
        elif k < pivotpoint:
            return selection(k, low, pivotpoint - 1, S)
        else:
            return selection(k, pivotpoint + 1, high, S)
    
from random import sample
n, k = 10, 5
S = [0] + sample(range(10, 100), n)
kth = selection(k, 1, n, S)
print(S[1:])
print(kth)
print(sorted(S[1:])[k - 1])