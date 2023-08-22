import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())

distances = [float('inf') for _ in range(n)]
distances[0] = 0
graph = [[] for _ in range(n)]
for _ in range(m):
	a,b,c = map(int, si().split())
	graph[a-1].append((b-1, c))
	graph[b-1].append((a-1, c))
	
# node, distance
queue = deque([(0, 0)])

while queue:
	node, cnt = queue.popleft()
	if cnt > distances[node]:
		continue

	for next, d in graph[node]:
		if distances[next] > d + cnt:
			distances[next] = d + cnt
			queue.append((next, d + cnt))

print(distances[n-1])
