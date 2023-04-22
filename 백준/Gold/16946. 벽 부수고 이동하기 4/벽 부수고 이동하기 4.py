import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, si().split())
graph = []
ans = [[0 for _ in range(m)]for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, si().rstrip())))

queue = set()

def dfs(x, y, sx, sy):
    global n, m
    offset = [[0,1], [0,-1], [1,0], [-1,0]]
    cnt = 1

    for i in range(4):
        if x == sx and y == sy:
            queue.clear()
        dx = x + offset[i][1]
        dy = y + offset[i][0]
        if dx < 0 or dx >= m or dy < 0 or dy >= n or chk[dy][dx] == 1:
            continue
        if graph[dy][dx] == 1:
            queue.add((dy, dx))
            continue
        chk[dy][dx] = 1
        res = dfs(dx,dy, sx, sy)
        cnt += res
        if x == sx and y == sy:
            while queue:
                dy, dx = queue.pop()
                ans[dy][dx] += res
                ans[dy][dx] %= 10


    return cnt

chk = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            chk[i][j] = 1
            res = dfs(j, i, j ,i)
            ans[i][j] += res
            ans[i][j] %= 10

for i in range(n):
    print(*(ans[i]), sep="")