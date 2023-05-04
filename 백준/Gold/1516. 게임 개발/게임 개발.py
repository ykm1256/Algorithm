import sys, heapq
si = sys.stdin.readline

N = int(si().rstrip())
times = [0 for _ in range(N)]
degree = [0 for _ in range(N)]
graph = [[] for _ in range(N)]
answer = [0 for _ in range(N)]

for i in range(N):
    tmp = list(map(int, si().split()))
    times[i] = tmp[0]
    for j in range(1, len(tmp)):
        if tmp[j] == -1:
            break
        degree[i] += 1
        graph[tmp[j]-1].append(i)


queue = []
for i in range(N):
    if degree[i] == 0:
        heapq.heappush(queue, (times[i], i))
        answer[i] = times[i]


while queue:
    t, now = queue.pop(0)

    for next in graph[now]:
        degree[next] -= 1
        answer[next] = max(answer[next], t)
        if degree[next] == 0:
            heapq.heappush(queue, (answer[next] + times[next], next))
            answer[next] += times[next]

for ans in answer:
    print(ans)