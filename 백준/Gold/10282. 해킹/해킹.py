import sys, heapq

si = sys.stdin.readline

T = int(si().rstrip())
for _ in range(T):
	n, d, c = map(int, si().split())
	graph = [[] for _ in range(n+1)]
	queue = []
	# 현재노드, 시간
	heapq.heappush(queue, (0, c))
	ans = 0
	cnt = 0
	chk = [float('inf') for _ in range(n+1)]
	chk[c] = 0
	cnt += 1
	for _ in range(d):
		a, b, s = map(int, si().split())
		graph[b].append((a,s))
	
	while queue:
		t, now = heapq.heappop(queue)
		if chk[now] < t:
			continue

		ans = max(t, ans)
		for next, time in graph[now]:
			if chk[next] <= t + time:
				continue
			if chk[next] == float('inf'):
				cnt += 1
			chk[next] = t + time
			heapq.heappush(queue, (chk[next], next))
	
	print(cnt, ans)