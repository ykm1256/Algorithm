import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int,si().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, si().split())
    graph[b-1].append(a-1)



ans = 0
def bfs(node):
    queue = deque()
    chk = [False] * n
    chk[node] = True
    queue.append(node)
    cnt = 1

    while queue:
        now = queue.popleft()

        for next in graph[now]:
            if chk[next]:
                continue
            cnt += 1
            chk[next] = True
            queue.append(next)
    
    return cnt

l = []

for i in range(n):
    cnt = bfs(i)
    if cnt > ans:
        l = []
        l.append(i+1)
        ans = cnt
    elif cnt == ans:
        l.append(i+1)

for n in l:
    print(n, end=" ")