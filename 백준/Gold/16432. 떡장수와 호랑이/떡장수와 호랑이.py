import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

n = int(si().rstrip())


graph = []
for _ in range(n):
	tmp = list(map(int, si().split()))
	graph.append(tmp[1:])

ans = [0 for _ in range(n)]
visited = [[0 for _ in range(10)] for _ in range(n)]

def dfs(cnt, prev):
	global n
	if cnt == n:
		for n in ans:
			print(n)
		exit()

	for next in graph[cnt]:
		if cnt == 0 or (visited[cnt][next] == 0 and prev != next):
			ans[cnt] = next
			visited[cnt][next] = 1
			dfs(cnt+1, next)

dfs(0, 0)
print(-1)