import sys
si = sys.stdin.readline

s = int(si().rstrip())
num = 0
cnt = 0
ans = 1
for i in range(1, s):
    cnt += 1
    num += i
    if s - num > i:
        ans = cnt + 1
    else:
        break
print(ans)