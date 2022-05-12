def promising(i, n, col):
    for j in range(1, i):
        if col[i] == col[j] or abs(col[i] - col[j]) == i - j:
            return False
    return True

def nqueens(i, n, col):
    if promising(i, n, col):
        if i == n:
            print(col[1:])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                nqueens(i + 1, n, col)

n = int(input())
col = [0] * (n + 1)
nqueens(0, n, col)
