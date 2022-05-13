def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
    
n = int(input())
m = int(input())
print(gcd(n, m))