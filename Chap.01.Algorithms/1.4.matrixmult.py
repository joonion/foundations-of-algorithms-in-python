def matrixmult(n, A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
B = []
for _ in range(n):
    B.append(list(map(int, input().split())))

C = matrixmult(n, A, B)
for i in range(n):
    print(C[i])