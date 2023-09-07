import sys
from itertools import product, combinations
from collections import deque
si = sys.stdin.readline

board = [list(si().rstrip()) for _ in range(5)]
arry = [i for i in range(5)]
arrx = [i for i in range(5)]
positions = list(product(arry, arrx))
routes = combinations(positions, 7)

def count(route):
    ret = 0
    for y, x in route:
        if board[y][x] == 'S':
            ret += 1
    return ret

def isValid(route):
    queue = deque()
    queue.append(route[0])
    chk = [[0 for _ in range(5)] for _ in range(5)]
    chk[route[0][0]][route[0][1]] = 1

    offset = [[0,1],[1,0],[0,-1],[-1,0]]

    cnt = 1
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            dy = y + offset[i][0]
            dx = x + offset[i][1]
            if  (dy,dx) in route and chk[dy][dx] == 0:
                chk[dy][dx] = 1
                queue.append((dy,dx))
                cnt += 1
    if cnt == 7:
        return True
    else:
        return False

ans = 0
for route in routes:
    if count(route) >= 4 and isValid(route):
        ans += 1

print(ans)