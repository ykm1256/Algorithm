import sys
si = sys.stdin.readline

n = int(si().rstrip())
m = int(si().rstrip())

graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
cnt = [[0 for _ in range(n+1)] for _ in range(n+1)]
isMiddle = [0 for _ in range(n+1)]

order = []
for _ in range(m):
	x, y, z = map(int, si().split())
	
	graph[y].append((x, z))
	isMiddle[x] = 1
	degree[x] += 1

queue = []
for i in range(1, n+1):
	if degree[i] == 0:
		queue.append(i)


while queue:
	now = queue.pop(0)
	for x, z in graph[now]:
		if isMiddle[now] == 0:
			cnt[x][now] += z
		else:
			for i in range(1, n+1):
				cnt[x][i] += z*cnt[now][i]
		degree[x] -= 1

		if degree[x] == 0:
			queue.append(x)

for i in range(1, n+1):
	if cnt[n][i] > 0:
		print(i, cnt[n][i])