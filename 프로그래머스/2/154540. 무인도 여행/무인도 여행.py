import sys
sys.setrecursionlimit(10**9)

def recur(y, x, maps, chk):
    ret = int(maps[y][x])
    offset = [[0,1],[1,0],[-1,0],[0,-1]]
    
    for idx in range(4):
        dy = y + offset[idx][0]
        dx = x + offset[idx][1]
        if dy < 0 or dy >= len(maps) or dx < 0 or dx >= len(maps[0]) or chk[dy][dx] or maps[dy][dx] =='X':
            continue
        chk[dy][dx] = True
        ret += recur(dy, dx, maps, chk)
    
    
    return ret

def solution(maps):
    answer = []
    chk = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not chk[i][j] and maps[i][j] != 'X':
                chk[i][j] = True
                res = recur(i, j, maps, chk)
                answer.append(res)
    
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer