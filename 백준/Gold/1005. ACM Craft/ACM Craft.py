import sys
si = sys.stdin.readline
from collections import deque

T = int(si().rstrip())

for _ in range(T):
    n, k = map(int, si().split())
    building = list(map(int, si().split()))
    degree = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]
    dp = [0 for _ in range(n)]

    for _ in range(k):
        x, y = map(int, si().split())
        x -= 1
        y -= 1
        graph[x].append(y)
        degree[y] += 1
    
    q = deque()
    w = int(si().rstrip())

    for i in range(n):
        if degree[i] == 0:
            q.append(i)
            dp[i] = building[i]
        
    while q:
        a = q.popleft()
        for i in graph[a]:
            degree[i] -= 1
            dp[i] = max(dp[a] + building[i], dp[i])
            if degree[i] == 0:
                q.append(i)

    print(dp[w-1])