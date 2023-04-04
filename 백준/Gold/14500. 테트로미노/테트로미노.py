import sys
si = sys.stdin.readline

n, m = map(int, si().split())

offset = [[0,1],[1,0],[-1,0],[0,-1]]
chk = [[0 for _ in range(m)] for _ in range(n)]
board = []


for _ in range(n):
    board.append(list(map(int, si().split())))

maxValue = max(map(max, board))
ans = 0

def dfs(x, y, res, cnt):
    global ans, n, m, maxValue
    if ans > res + maxValue * (4 - cnt):
        return
    if cnt == 4:
        ans = max(ans, res)
    
    for i in range(4):
        dx, dy = x + offset[i][1], y + offset[i][0]
        
        if dx < 0 or dx >= m or dy < 0 or dy >= n or chk[dy][dx] == 1:
            continue

        if cnt == 2:
            chk[dy][dx] = 1
            dfs(x, y, res+board[dy][dx], cnt+1)
            chk[dy][dx] = 1
        chk[dy][dx] = 1
        dfs(dx, dy, res+board[dy][dx], cnt+1)
        chk[dy][dx] = 0

for i in range(n):
    for j in range(m):
        chk[i][j] = 1
        dfs(j, i, board[i][j], 1)
        chk[i][j] = 0

print(ans)