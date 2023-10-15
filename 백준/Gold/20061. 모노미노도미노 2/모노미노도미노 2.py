import sys
si = sys.stdin.readline


board = [[0 for _ in range(10)] for _ in range(10)]

for i in range(4,10):
    for j in range(4, 10):
        board[i][j] = -1

N = int(si().rstrip())

def move_blue(sx):
    for j in range(sx, 4, -1):
        for i in range(4):
            board[i][j] = board[i][j-1]
            if j == 5:
                board[i][4] = 0

def move_green(sy):
    for i in range(sy, 4, -1):
        for j in range(4):
            board[i][j] = board[i-1][j]
            if i == 5:
                board[4][j] = 0
    

def check_light_blue():
    cnt = 0

    for j in range(4, 6):
        for i in range(4):
            if board[i][j] == 1:
                cnt += 1
                break
    for _ in range(cnt):
        move_blue(9)

def check_light_green():
    cnt = 0

    for i in range(4, 6):
        for j in range(4):
            if board[i][j] == 1:
                cnt += 1
                break
    for _ in range(cnt):
        move_green(9)


# 부술 수 있는 것 확인
def check_blue():

    cnt = 0
    j = 9
    while j >= 4:
        flag = True
        for i in range(4):
            if board[i][j] != 1:
                flag = False
                break
        if flag:
            move_blue(j)
            cnt += 1
        else:
            j -= 1
    
    return cnt

def check_green():
    i = 9
    cnt = 0
    while i >= 4:
        flag = True
        for j in range(4):
            if board[i][j] != 1:
                flag = False
                break
        if flag:
            move_green(i)
            cnt += 1
        else:
            i -= 1
    return cnt

def blue(t, x, y):
    
    while True:
        dx = x + 1

        if dx >= 10 or board[y][dx] != 0:
            break

        if t == 2:
            if dx+1 >= 10 or board[y][dx+1] != 0:
                break
        elif t == 3:
            if board[y+1][dx] != 0:
                break
        x = dx

    board[y][x] = 1
    if t == 2:
        board[y][x+1] = 1
    elif t == 3:
        board[y+1][x] = 1
    
    ret = check_blue()
    check_light_blue()
    return ret

def green(t, x, y):
    while True:
        dy = y + 1

        if dy >= 10 or board[dy][x] != 0:
            break

        if t == 2:
            if board[dy][x+1] != 0:
                break
        elif t == 3:
            if dy+1 >= 10 or board[dy+1][x] != 0:
                break
        y = dy
    
    board[y][x] = 1
    if t == 2:
        board[y][x+1] = 1
    elif t == 3:
        board[y+1][x] = 1
    
    ret = check_green()
    check_light_green()
    return ret

score = 0

for _ in range(N):
    t, x, y = map(int, si().split())
    x, y = y, x
    score += blue(t, x, y)
    score += green(t, x, y)

ans = 0
for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            ans += 1

print(score)
print(ans)