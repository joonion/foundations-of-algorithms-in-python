from heapq import heappush, heappop

class Node:

    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        
    def preorder(self, path):
        path.append((self.symbol, self.freq))
        if self.left != None:
            self.left.preorder(path)
        if self.right != None:
            self.right.preorder(path)

    def inorder(self, path):
        if self.left != None:
            self.left.inorder(path)
        path.append((self.symbol, self.freq))
        if self.right != None:
            self.right.inorder(path)

def huffman(n, s, f):
    heap = []
    for i in range(n):
        heappush(heap, (f[i], Node(s[i], f[i])))
    while len(heap) > 1:
        p = heappop(heap)[1]
        q = heappop(heap)[1]
        r = Node('+', p.freq + q.freq)
        r.left = p
        r.right = q
        heappush(heap, (r.freq, r))
    return heappop(heap)[1]

n = int(input())
s = input().split()
f = list(map(int, input().split()))
print(n, s, f)
root = huffman(n, s, f)
path = []
root.preorder(path)
print(path)
path = []
root.inorder(path)
print(path)
