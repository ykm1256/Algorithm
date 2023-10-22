import sys
si = sys.stdin.readline

N = int(si().rstrip())

now = list(si().rstrip())
goal = list(si().rstrip())

def push(arr):
    cnt = 0

    for i in range(1, len(arr)):
        if arr[i-1] != goal[i-1]:
            arr[i-1] = goal[i-1]
            arr[i] = '0' if arr[i] == '1' else '1'
            if i < len(arr)-1:
                arr[i+1] = '0' if arr[i+1] == '1' else '1'
            cnt += 1
    
    if arr == goal:
        return cnt
    else:
        return float('inf')

ans = float('inf')
ans = min(ans, push(now[:]))

now[0] = '0' if now[0] == '1' else '1'
now[1] = '0' if now[1] == '1' else '1'
ans = min(ans, push(now[:]) + 1)

if ans == float('inf'):
    ans = -1
print(ans)