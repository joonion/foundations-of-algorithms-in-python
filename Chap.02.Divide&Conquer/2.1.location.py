def location(low, high, S, x):
    if low > high:
        return 0
    else:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            return location(low, mid - 1, S, x)
        else:
            return location(mid + 1, high, S, x)
        
n = int(input())
S = [0] + list(map(int, input().split()))
x = int(input())
print(location(1, n, S, x))
