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

def quicksort(low, high, S):
    if low < high:
        pivotpoint = partition(low, high, S)
        quicksort(low, pivotpoint - 1, S)
        quicksort(pivotpoint + 1, high, S)
        
from random import sample
S = sample(range(10, 100), 10)
quicksort(0, len(S)-1, S)
print(S)
print(sorted(S))