def exchangesort(n, S):
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if S[i] > S[j]:
                S[i], S[j] = S[j], S[i]

from random import sample
S = [0] + sample(range(10, 100), 10)
print(sorted(S[1:]))
exchangesort(len(S) - 1, S)
print(S[1:])