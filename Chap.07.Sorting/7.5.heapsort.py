class Heap:
    
    def __init__(self, n, S):
        self.heapsize = n
        self.S = S[:]

def siftdown(H, i):
    siftkey = H.S[i]
    parent = i
    spotfound = False
    while 2*parent <= H.heapsize and not spotfound:
        if 2*parent < H.heapsize and H.S[2*parent] < H.S[2*parent + 1]:
            largerchild = 2*parent + 1
        else:
            largerchild = 2*parent
        if siftkey < H.S[largerchild]:
            H.S[parent] = H.S[largerchild]
            parent = largerchild
        else:
            spotfound = True
    H.S[parent] = siftkey
        
def root(H):
    keyout = H.S[1]
    H.S[1] = H.S[H.heapsize]
    H.heapsize -= 1
    siftdown(H, 1)
    return keyout

def removekeys(n, H, S):
    for i in range(n, 0, -1):
        S[i] = root(H)

def makeheap(n, H):
    heap.heapsize = n
    for i in range(n // 2, 0, -1):
        siftdown(H, i)

def heapsort(n, H, S):
    makeheap(n, H)
    print("makeheap:", H.S)
    removekeys(n, H, S)
    print("removekeys:", H.S)
    
from random import sample
n = 10
S = [0] + sample(range(10, 100), n)
heap = Heap(n, S)
heapsort(n, heap, S)
print(S)
