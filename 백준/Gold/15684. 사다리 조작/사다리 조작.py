import sys
si = sys.stdin.readline


N, M, H = map(int, si().split())
cntHorizon = [0 for _ in range(N)]

board = [[0 for _ in range(N)] for _ in range(H)]
answer = -1

for _ in range(M):
    a, b = map(int, si().split())
    board[a-1][b-1] = 1
    board[a-1][b-1+1] = 2

def check():
    offset = [[1,0], [0,1],[0,-1]]
    for start in range(N):
        y = 0
        x = start
        flag = True
        while y < H:
            idx = board[y][x]
            if flag and idx != 0:
                y += offset[idx][0]
                x += offset[idx][1]
                flag = False
            else:
                y += 1
                flag = True
        if x != start:
            return False
    return True

def recur(y, x, cnt, N, H):
    global answer, M
    if check():
        if answer == -1:
            answer = cnt
        else:
            answer = min(answer, cnt)
        return
    elif cnt == 3+M or (answer != -1 and cnt >= answer):
        return

    for i in range(y, H):
        if i == y:
            sx = x
        else:
            sx = 0
        for j in range(sx, N-1):
            if board[i][j] == 0 and board[i][j+1] == 0:
                board[i][j] = 1
                board[i][j+1] = 2
                recur(i, j+2, cnt+1, N, H)
                board[i][j] = 0
                board[i][j+1] = 0

recur(0,0,M,N,H)
if answer >= 0:
    answer -= M
print(answer)