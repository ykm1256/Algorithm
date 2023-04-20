import sys
si = sys.stdin.readline

n = int(si().rstrip())

time = [0 for _ in range(n)]
degree = [0 for _ in range(n)]
graph = [[] for _ in range(n)]

for i in range(n):
    work = list(map(int, si().split()))
    
    time[i] = work[0]
    for j in range(work[1]):
        degree[i] += 1
        graph[work[j+2]-1].append(i)

queue = []
end = [0 for _ in range(n)]

for i in range(n):
    if degree[i] == 0:
        queue.append(i)
        end[i] = time[i]


ans = 0
while queue:
    now= queue.pop(0)
    ans = max(ans, end[now])

    for next in graph[now]:
        degree[next] -= 1
        end[next] = max(end[next], end[now] + time[next])
        if degree[next] == 0:
            queue.append(next)

print(ans)