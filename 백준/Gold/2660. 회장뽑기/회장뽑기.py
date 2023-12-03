import sys, heapq
si = sys.stdin.readline

n = int(si().rstrip())

graph = [[] for _ in range(n)]
d = [[float('inf') for _ in range(n)] for _ in range(n)]

while True:
    a, b = map(int, si().split())
    if a == -1:
        break
    
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    d[a][b] = 1
    d[b][a] = 1
for start in range(n):
    queue = []
    heapq.heappush(queue, (start, 0))

    while queue:
        node, cnt = heapq.heappop(queue)
        if d[start][node] < cnt:
            continue
        for next in graph[node]:
            if d[start][next] >= cnt + 1:
                heapq.heappush(queue, (next, cnt+1))
                d[start][next] = cnt+1

score = float('inf')
answer = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        cnt = max(cnt, d[i][j])
    if score > cnt:
        score = cnt
        answer = [i+1]
    elif score == cnt:
        answer.append(i+1)

print(score, len(answer))
print(*answer)