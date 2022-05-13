def euclid(n, m):
    if m == 0:
        return n, 1, 0
    else:
        gcd, i, j = euclid(m, n % m)
        return gcd, j, i - (n // m) * j

n = int(input())
m = int(input())
gcd, i, j = euclid(n, m)
print(gcd, i, j)