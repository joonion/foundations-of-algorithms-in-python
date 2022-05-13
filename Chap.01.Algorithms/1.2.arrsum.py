def arrsum(n, S):
    result = 0
    for i in range(1, n + 1):
        result += S[i]
    return result

n = int(input())
S = list(map(int, input().split()))
sum = arrsum(n, [0] + S)
print(sum)