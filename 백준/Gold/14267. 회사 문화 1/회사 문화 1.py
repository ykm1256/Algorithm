import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int, si().split())

parents = list(map(int, si().split()))
children = [[] for _ in range(n)]
cnt = [0 for _ in range(n)]
for i in range(n):
    if parents[i] == -1:
        continue
    children[parents[i]-1].append(i)

for _ in range(m):
    i, w = map(int, si().split())
    i -= 1
    cnt[i] += w

def recur(node):
    for child in children[node]:
        cnt[child] += cnt[node]
        recur(child)

recur(0)
print(*cnt)