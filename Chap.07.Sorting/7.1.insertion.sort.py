def insertionsort(S):
    n = len(S)
    for i in range(1, n):
        x = S[i]
        j = i - 1
        while j >= 0 and S[j] > x:
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = x

from random import sample
S = sample(range(10, 100), 10)
insertionsort(S)
print(S)
print(sorted(S))
