import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
graph = [[] for _ in range(n)]

# 0번 노드와의 거리
distance = [float('inf') for _ in range(n)]

for _ in range(m):
    a, b = map(int, si().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

distance[0] = 0
queue = deque()
queue.append((0,0))

while queue:
    now, cnt = queue.popleft()

    for next in graph[now]:
        # 거리배열에 저장된 값보다 작으면 계속 탐색
        if distance[next] > cnt+1:
            distance[next] = cnt+1
            queue.append((next, cnt+1))

node = 0
cnt = 0
maxValue = 0
for i in range(n):
    if distance[i] > maxValue:
        node = i+1
        maxValue = distance[i]
        cnt = 1
    elif distance[i] == maxValue:
        cnt += 1

print(node, maxValue, cnt)