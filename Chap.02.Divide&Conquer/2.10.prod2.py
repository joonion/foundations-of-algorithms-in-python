def prod2(u, v):
    global threshold
    n = max(len(str(u)), len(str(v)))
    if u == 0 or v == 0:
        return 0
    elif n <= threshold:
        return u * v
    else:
        m = n // 2
        x, y = u // (10 ** m), u % (10 ** m)
        w, z = v // (10 ** m), v % (10 ** m)
        r = prod2(x + y, w + z)
        p = prod2(x, w)
        q = prod2(y, z)
        return p * (10 ** (2*m)) + (r - p - q) * (10 ** m) + q

threshold = int(input())
u = int(input())
v = int(input())
print(u * v)
print(prod2(u, v))
