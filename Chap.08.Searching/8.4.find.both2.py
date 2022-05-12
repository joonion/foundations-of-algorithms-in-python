def find_both2(n, S):
    if S[0] < S[1]:
        small, large = S[0], S[1]
    else:
        small, large = S[1], S[2]
    for i in range(2, n - 1, 2):
        if S[i] < S[i + 1]:
            small = min(small, S[i])
            large = max(large, S[i + 1])
        else:
            small = min(small, S[i + 1])
            large = max(large, S[i])
    return small, large

from random import sample
S = sample(range(10, 100), 10)
small, large = find_both2(len(S), S)
print(sorted(S))
print(small, large)
print(min(S), max(S))