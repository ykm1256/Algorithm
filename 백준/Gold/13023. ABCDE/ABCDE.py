import sys
si = sys.stdin.readline

# dfs 구현
# 모든 노드에서 탐색
# 방문 노드 체크하면서 탐색
# 돌아오면 체크해제
# ABCDE이므로 5개의 이상의 정점을 방문했는지 체크

n, m = map(int, si().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)


chk = [0 for _ in range(n)]

def dfs(node, cnt):
    if cnt >= 5:
        return 1

    res = 0
    for next in graph[node]:
        if chk[next] == 0:
            chk[next] = 1
            res = dfs(next, cnt+1)
            chk[next] = 0
            if res == 1:
                break

    return res

res = 0
for i in range(n):
    chk[i] = 1
    res = dfs(i, 1)
    chk[i] = 0
    if res == 1:
        break

print(res)