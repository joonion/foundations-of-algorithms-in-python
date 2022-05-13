def prod(u, v):
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
        p = prod(x, w)
        q = prod(x, z) + prod(w, y)
        r = prod(y, z)
        return p * (10 ** (2*m)) + q * (10 ** m) + r

threshold = int(input())
u = int(input())
v = int(input())
print(u * v)
print(prod(u, v))
