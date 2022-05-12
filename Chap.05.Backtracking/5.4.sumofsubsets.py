def promising(i, weight, total):
    global n, W, w, include
    return weight + total >= W and (weight == W or weight + w[i+1] <= W)

def sumofsubsets(i, weight, total):
    global n, W, w, include
    if promising(i, weight, total):
        if weight == W:
            print(include[1:])
        else:
            include[i + 1] = 1
            sumofsubsets(i + 1, weight + w[i+1], total - w[i+1])
            include[i + 1] = 0
            sumofsubsets(i + 1, weight, total - w[i+1])
    
n, W = map(int, input().split())
w = [0] + list(map(int, input().split()))
include = [0] * (n + 1)
sumofsubsets(0, 0, sum(w[1:]))
