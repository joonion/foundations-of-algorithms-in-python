def find_both(n, S):
    small = large = S[0]
    for i in range(1, n):
        if S[i] < small:
            small = S[i]
        elif S[i] > large:
            large = S[i]
    return small, large

from random import sample
S = sample(range(10, 100), 10)
small, large = find_both(len(S), S)
print(sorted(S))
print(small, large)
print(min(S), max(S))