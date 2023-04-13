import sys
sys.setrecursionlimit(10**9)
T = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(T)]

for i in range(T-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1,c))

check = [0 for _ in range(T)]
maxlen = 0
maxidx = 0

def recur(sum, idx):
    global maxlen, maxidx, check
    check[idx] = 1
    if maxlen < sum:
        maxlen = sum
        maxidx = idx

    for n,d in graph[idx]:
        if check[n] == 0:
            recur(sum+d, n)
    check[idx] = 0

recur(0, 0)
maxlen = 0
recur(0, maxidx)
print(maxlen)