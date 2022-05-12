class Node:
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def preorder(self, path):
        path.append(self.key)
        if self.left != None:
            self.left.preorder(path)
        if self.right != None:
            self.right.preorder(path)

    def inorder(self, path):
        if self.left != None:
            self.left.inorder(path)
        path.append(self.key)
        if self.right != None:
            self.right.inorder(path)
                
def minimum(i, j, A, p):
    global INF
    minvalue, mink = INF, 0
    for k in range(i, j + 1):
        value = A[i][k - 1] + A[k + 1][j]
        for m in range(i, j + 1):
            value += p[m]
        if value < minvalue:
            minvalue, mink = value, k
    return minvalue, mink

def optsearchtree(n, p):
    global INF
    A = [[INF] * (n + 1) for _ in range(n + 2)]
    R = [[0] * (n + 1) for _ in range(n + 2)]
    for i in range(1, n + 1):
        A[i][i - 1] = R[i][i - 1] = 0
        A[i][i], R[i][i] = p[i], i
    A[n + 1][n] = R[n + 1][n] = 0

    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            A[i][j], R[i][j] = minimum(i, j, A, p)
    return A[1][n], A, R

def tree(i, j, K, R):
    k = R[i][j]
    if k == 0:
        return None
    else:
        p = Node(K[k])
        p.left = tree(i, k - 1, K, R)
        p.right = tree(k + 1, j, K, R)
        return p

INF = 999
n = int(input())
K = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
minavg, A, R = optsearchtree(n, p)
print("A = ")
for i in range(1, n + 2):
    print(A[i][i-1:])
print("R = ")
for i in range(1, n + 2):
    print(R[i][i-1:])
print("minavg = ", minavg)

root = tree(1, n, K, R)
path = [] 
root.preorder(path)
print(path)
path = []
root.inorder(path)
print(path)
