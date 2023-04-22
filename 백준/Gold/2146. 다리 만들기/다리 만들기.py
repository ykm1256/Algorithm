import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(si().rstrip())
graph = []

for _ in range(n):
    graph.append(list(map(int, si().split())))
offset = [[0,1],[0,-1],[1,0],[-1,0]]

def is_boundary(y, x):
    global n
    for i in range(4):
        dy = y + offset[i][0]
        dx = x + offset[i][1]

        if dy < 0 or dy >= n or dx < 0 or dx >= n:
            continue
        if graph[dy][dx] == 0:
            return True

    return False

queue = []
chk = [[0 for _ in range(n)] for _ in range(n)]


def dfs(y, x, value):
    global n
    for i in range(4):
        dy = y + offset[i][0]
        dx = x + offset[i][1]

        if dy < 0 or dy >= n or dx < 0 or dx >= n:
            continue

        if graph[dy][dx] != 1:
            if graph[dy][dx] == 0 and chk[y][x] == 0:
                queue[value-2].append((y, x, 0))
                chk[y][x] = 1
            continue

        graph[dy][dx] = value
        dfs(dy, dx, value)

cnt = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append([])
            graph[i][j] = cnt
            dfs(i, j, cnt)
            cnt += 1

ans = float('inf')
idx = 2
while len(queue) > 1:
    tmp = queue.pop(0)
    chk = [[0 for _ in range(n)] for _ in range(n)]
    while tmp:
        y, x, cnt = tmp.pop(0)
        if cnt >= ans:
            continue

        for i in range(4):
            dy = y + offset[i][0]
            dx = x + offset[i][1]
            if dy < 0 or dy >= n or dx < 0 or dx >= n:
                continue

            if graph[dy][dx] == 0 and chk[dy][dx] == 0:
                chk[dy][dx] = 1
                tmp.append((dy, dx, cnt + 1))
            elif graph[dy][dx] != 0 and graph[dy][dx] != idx:
                tmp.clear()
                ans = min(ans, cnt)
                break
    idx += 1

print(ans)