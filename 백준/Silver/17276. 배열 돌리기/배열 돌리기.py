import sys
si = sys.stdin.readline

T = int(si().rstrip())

def clockWise(n):
    d = n // 2
    for o in range(d):
        tmp = arr[o][o]

        for j in range(d, n-o, d-o):
            arr[o][j], tmp = tmp, arr[o][j]
        
        for i in range(d, n-o, d-o):
            arr[i][n-o-1], tmp = tmp, arr[i][n-o-1]
        
        for j in range(n-1-d, o-1, -(d-o)):
            arr[n-o-1][j], tmp = tmp, arr[n-o-1][j]
        
        for i in range(n-1-d, o-1, -(d-o)):
            arr[i][o], tmp = tmp, arr[i][o]

def reverse(n):
    d = n // 2
    for o in range(d):
        tmp = arr[o][o]

        for i in range(d, n-o, d-o):
            arr[i][o], tmp = tmp, arr[i][o]

        for j in range(d, n-o, d-o):
            arr[n-o-1][j], tmp = tmp, arr[n-o-1][j]
        
        for i in range(n-d-1, o-1, -(d-o)):
            arr[i][n-o-1], tmp = tmp, arr[i][n-o-1]
        
        for j in range(n-d-1, o-1, -(d-o)):
            arr[o][j], tmp = tmp, arr[o][j]

for _ in range(T):
    n, d = map(int, si().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, si().split())))
    flag = 1
    if d < 0:
        flag = -1
        d *= -1
    if d >= 360:
        d %= 360

    if d > 180:
        d = 360 - d
        flag *= -1
    
    if flag == -1:
        for i in range(d//45):
            reverse(n)
    else:
        for i in range(d//45):
            clockWise(n)
    
    for i in range(n):
        print(*(arr[i]))