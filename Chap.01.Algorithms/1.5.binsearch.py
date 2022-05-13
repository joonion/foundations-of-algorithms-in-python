def binsearch(n, S, x):
    low, high = 1, n
    location = 0
    while low <= high and location == 0:
        mid = (low + high) // 2
        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return location

n = int(input())
S = list(map(int, input().split()))
x = int(input())
location = binsearch(n, [0] + S, x)
print(location)