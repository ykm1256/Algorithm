import sys
si = sys.stdin.readline

N, K = map(int, si().split())

board = []

for _ in range(N):
    board.append(list(map(int, si().split())))

S, Y, X = map(int, si().split())

queue = []
offset = [[0,1],[1,0],[0,-1],[-1,0]]

for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            queue.append((board[i][j], i, j, 0))

if S == 0:
    queue = []
queue.sort()
while queue:
    virus, y, x, t = queue.pop(0)
    
    for idx in range(4):
        dy = y + offset[idx][0]
        dx = x + offset[idx][1]
        if dy < 0 or dy >= N or dx < 0 or dx >= N or board[dy][dx] != 0:
            continue
        board[dy][dx] = virus
        if t+1 < S:
            queue.append((virus, dy, dx, t+1))

print(board[Y-1][X-1])