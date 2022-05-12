from heapq import heappush, heappop

class Node:
    def __init__(self, level, path):
        self.level = level
        self.path = path[:]
        self.bound = 0

def remainder(path, n):
    return n * (n + 1) // 2 - sum(path)

def pathlength(path, W):
    length = 0
    for i in range(len(path) - 1):
        length += W[path[i]][path[i+1]]
    return length

def hasOutgoing(v, path):
    return v in path[:len(path)-1]

def hasIncoming(v, path):
    return v in path[1:]

def boundof(v, n, W):
    global INF
    lower = pathlength(v.path, W)
    for i in range(1, n + 1):
        if hasOutgoing(i, v.path): continue
        minimum = INF
        for j in range(1, n + 1):
            if i == j: continue
            if j == 1 and i == v.path[len(v.path) - 1]: continue
            if hasIncoming(j, v.path): continue
            minimum = min(minimum, W[i][j])
        lower += minimum
    return lower

def travel2(n, W):
    global INF
    heap = [] # Initialize Priority Queue
    v = Node(0, [1])
    v.bound = boundof(v, n, W)
    minlength, opttour = INF, []
    heappush(heap, (v.bound, v))
    print(v.level, v.bound, v.path, minlength, True)
    while len(heap) != 0:
        v = heappop(heap)[1]
        # print(v.level, v.bound, v.path, minlength, True)
        if v.bound < minlength:
            for i in range(2, n + 1):
                if i in v.path: continue
                u = Node(v.level + 1, v.path)
                u.path.append(i)
                if u.level == n - 2:
                    u.path.append(remainder(u.path, n))
                    u.path.append(1)
                    pathlen = pathlength(u.path, W)
                    if pathlen < minlength:
                        minlength = pathlen
                        opttour = u.path[:]
                else:
                    u.bound = boundof(u, n, W)
                    if u.bound < minlength:
                        heappush(heap, (u.bound, u))
                print(u.level, u.bound, u.path, minlength, True)
    return minlength, opttour
    
INF = 999
n, m = map(int, input().split())
W = [[INF] * (n + 1) for _ in range(n + 1)]
for v in range(1, n + 1):
    W[v][v] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w
for i in range(1, n + 1):
    print(W[i][1:])
    
minlength, opttour = travel2(n, W)
print(minlength)
print(opttour)