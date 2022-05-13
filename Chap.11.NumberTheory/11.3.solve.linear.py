def euclid(n, m):
    if m == 0:
        return n, 1, 0
    else:
        gcd, i, j = euclid(m, n % m)
        return gcd, j, i - (n // m) * j
    
def solve_linear(n, m, k):
    d, i, j = euclid(n, m)
    if k % d == 0:
        solutions = []
        for l in range(d):
            solutions.append((j*k//d + l*n//d) % n)
        return solutions
            
n, m, k = map(int, input().split())
solutions = solve_linear(n, m, k)
print(solutions)