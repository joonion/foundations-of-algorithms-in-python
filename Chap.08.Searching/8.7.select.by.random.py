from random import randint

def partition3(low, high, S):
    randspot = randint(low, high)
    pivotitem = S[randspot]
    S[low], S[randspot] = S[randspot], S[low]
    j = low
    for i in range(low + 1, high + 1):
        if S[i] < pivotitem:
            j += 1
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint

def selection3(k, low, high, S):
    if low == high:
        return S[low]
    else:
        pivotpoint = partition3(low, high, S)
        if k == pivotpoint:
            return S[pivotpoint]
        elif k < pivotpoint:
            return selection3(k, low, pivotpoint - 1, S)
        else:
            return selection3(k, pivotpoint + 1, high, S)
        
from random import sample
n, k = 10, 5
S = [0] + sample(range(10, 100), n)
kth = selection3(k, 1, n, S)
print(S[1:])
print(kth)
print(sorted(S[1:])[k - 1])
