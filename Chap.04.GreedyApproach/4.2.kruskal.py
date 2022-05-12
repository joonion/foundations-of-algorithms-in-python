from heapq import heappush, heappop
from re import I

class DisjointSet:
    
    def __init__(self, n):
        self.U = [i for i in range(n + 1)]
        
    def find(self, i):
        j = i
        while self.U[j] != j:
            j = self.U[j]
        return j  
    
    def merge(self, p, q):
        if p < q:
            self.U[q] = p
        else:
            self.U[p] = q 
    
def kruskal(n, m, E):
    heap = []
    for i in range(m):
        heappush(heap, (E[i][2], E[i]))
    dset = DisjointSet(n)
    F = []
    while len(F) < n - 1:
        e = heappop(heap)[1]
        p = dset.find(e[0])
        q = dset.find(e[1])
        if p != q:
            dset.merge(p, q)
            F.append(e)
    return F

n, m = map(int, input().split())
E = []
for _ in range(m):
    u, v, w = map(int, input().split())
    E.append((u, v, w))
    
F = kruskal(n, m, E)
print(F)
