import sys

si = sys.stdin.readline

n, m = map(int, si().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, si().split())))

offset = [[0, 1], [1, 0], [-1, 0], [0, -1]]
lines = []

def chk_island(x, y, num):
    global n, m

    for i in range(4):
        dx = x + offset[i][1]
        dy = y + offset[i][0]

        if dx < 0 or dx >= m or dy < 0 or dy >= n or arr[dy][dx] != 1:
            continue

        arr[dy][dx] = num
        chk_island(dx, dy, num)


def is_inBoundary(x, y):
    global n, m
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    return True

def connect_bridge(x, y, i, cnt, start):
    global n, m
    dx = x + offset[i][1]
    dy = y + offset[i][0]
    res = False

    if not is_inBoundary(dx, dy):
        return False
    elif arr[dy][dx] > 1:
        if start == arr[dy][dx]-2 or cnt < 2 or (graph[start][arr[dy][dx]- 2] != 0 and graph[start][arr[dy][dx]-2] < cnt):
            return False
        graph[start][arr[dy][dx]-2] = cnt
        lines.append((cnt, start, arr[dy][dx] - 2))
        return True
    elif arr[dy][dx] == -1:
        res = connect_bridge(dx, dy, i, cnt+1, start)
    elif arr[dy][dx] == 0:
        arr[dy][dx] = -1
        res = connect_bridge(dx, dy, i, cnt+1, start)
        if not res:
            arr[dy][dx] = 0
    return res

def make_bridge():
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                for idx in range(4):
                    di = i + offset[idx][0]
                    dj = j + offset[idx][1]
                    if is_inBoundary(dj, di) and (arr[di][dj] == 0 or arr[di][dj] == -1):
                        connect_bridge(j, i, idx, 0, arr[i][j]-2)

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa < pb:
        parents[pb] = pa
    else:
        parents[pa] = pb


cnt_island = 0


idx = 2
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = idx
            cnt_island += 1
            chk_island(j, i, idx)
            idx += 1

parents = [i for i in range(cnt_island)]
graph = [[0 for _ in range(cnt_island)] for _ in range(cnt_island)]
make_bridge()
chk = [0 for _ in range(cnt_island)]

lines.sort()
answer = 0
for c, a, b in lines:
    if find(a) != find(b):
        answer += c
        union(a, b)



for i in range(cnt_island):
    if find(i) != 0:
        answer = 0
        break
print(answer if answer > 0 else -1)
