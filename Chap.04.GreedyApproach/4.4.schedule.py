def insert(seq, job, deadline):
    j = 0
    while j < len(seq) and deadline[seq[j]] <= deadline[job]:
        j += 1
    return seq[:j] + [job] + seq[j:]
    
def feasible(seq, deadline):
    for i in range(len(seq)):
        if (i + 1) > deadline[seq[i]]:
            return False
    return True

def schedule(n, deadline):
    seq = [1]
    for job in range(2, n + 1):
        K = insert(seq, job, deadline)
        print("K =", K)
        if feasible(K, deadline):
            seq = K[:]
        print("  J = ", seq)
    return seq

n = int(input())
deadline = [0] + list(map(int, input().split()))
profit = [0] + list(map(int, input().split()))
jobs = schedule(n, deadline)
print(jobs)
