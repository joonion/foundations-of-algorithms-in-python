from math import ceil, floor

def median(first, last, S):
    s = S[first:last+1]
    return sorted(s)[len(s)//2]
    
def partition2(low, high, S):
    arraysize = high - low + 1
    r = ceil(arraysize / 5)
    T = [0] * (r + 1) 
    for i in range(1, r + 1):
        first = low + 5*i - 5
        last = min(low + 5*i - 1, low + arraysize - 1)
        T[i] = median(first, last, S)
    pivotitem = select(floor((r + 1) / 2), r, T)
    j = low
    for i in range(low, high + 1):
        if S[i] == pivotitem:
            S[i], S[j] = S[j], S[i]
            mark = j
            j += 1
        elif S[i] < pivotitem:
            S[i], S[j] = S[j], S[i]
            j += 1
    pivotpoint = j - 1
    S[mark], S[pivotpoint] = S[pivotpoint], S[mark]
    return pivotpoint

def selection2(k, low, high, S):
    if low == high:
        return S[low]
    else:
        pivotpoint = partition2(low, high, S)
        if k == pivotpoint:
            return S[pivotpoint]
        elif k < pivotpoint:
            return selection2(k, low, pivotpoint - 1, S)
        else:
            return selection2(k, pivotpoint + 1, high, S)
        
def select(k, n, S):
    return selection2(k, 1, n, S)

from random import sample, randint
n = randint(1, 90)
k = randint(1, n)
S = [0] + sample(range(10, 100), n)
# S = [0, 2, 3, 5, 8, 12, 1, 7, 10, 13, 30, 6, 14, 15, 18, 22]
kth = select(k, len(S) - 1, S)
print(sorted(S[1:]))
print(kth, n, k)
print(sorted(S[1:])[k - 1])
