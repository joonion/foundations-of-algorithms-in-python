def find_largest(n, S):
    large = S[0]
    for i in range(1, n):
        if S[i] > large:
            large = S[i]
    return large

from random import sample
S = sample(range(10, 100), 10)
large = find_largest(len(S), S)
print(sorted(S))
print(large)
print(max(S))