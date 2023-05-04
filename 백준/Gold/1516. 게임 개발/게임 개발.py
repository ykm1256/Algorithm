import sys
from collections import deque

si = sys.stdin.readline

n = int(si().rstrip())
times = [0] * n
indegree = [0] * n
graph = [[] for _ in range(n)]

for i in range(n):
    data = list(map(int, si().split()))
    times[i] = data[0]  # 시간 정보
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x - 1].append(i)

def topology_sort():
    q = deque()
    result = times[:]  # 현재까지 걸린 시간을 저장할 리스트
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for next in graph[now]:
            indegree[next] -= 1
            result[next] = max(result[next], result[now] + times[next])  # 다음 건물의 완성 시간 갱신
            if indegree[next] == 0:
                q.append(next)

    return result

answer = topology_sort()
for ans in answer:
    print(ans)