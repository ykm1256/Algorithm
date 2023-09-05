import sys
si = sys.stdin.readline

input = list(map(int, si().split()))

ans = 0

board = [[0 for _ in range(29)] for _ in range(29)]

start = [14, 14]
offset = [[0,1],[0,-1],[1,0],[-1,0]]
board[14][14] = 1

def recur(x, y, p, cnt):
    global ans
    if cnt == input[0]:
        ans += p
        return
    
    for idx in range(4):
        if input[idx+1] == 0:
            continue
        nx = x + offset[idx][0]
        ny = y + offset[idx][1]
        if nx < 0 or nx >= 29 or ny < 0 or ny >= 29 or board[ny][nx] == 1:
            continue
        board[ny][nx] = 1
        recur(nx, ny, p*(input[idx+1]/100), cnt+1)
        board[ny][nx] = 0

recur(14,14,1,0)

print(ans)