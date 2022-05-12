def bin(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return bin(n - 1, k - 1) + bin(n - 1, k)
    
n, k = map(int, input().split())
print(bin(n, k))