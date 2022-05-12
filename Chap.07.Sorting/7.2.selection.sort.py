def selectionsort(n, S):
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if S[j] < S[smallest]:
                smallest = j
        S[i], S[smallest] = S[smallest], S[i]

from random import sample
S = sample(range(10, 100), 10)
selectionsort(len(S), S)
print(S)
print(sorted(S))
