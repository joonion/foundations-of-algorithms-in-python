def seqsearch(n, S, x):
    location = 1
    while location <= n and S[location] != x:
        location += 1
    if location > n:
        location = 0
    return location

n = int(input())
S = list(map(int, input().split()))
x = int(input())
location = seqsearch(n, [0] + S, x)
print(location)
        