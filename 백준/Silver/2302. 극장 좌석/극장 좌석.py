import sys
si = sys.stdin.readline

dp = [0 for _ in range(41)]

dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, 41):
    dp[i] = dp[i-1] + dp[i-2]

chk = [0 for _ in range(41)]
n = int(si().rstrip())
m = int(si().rstrip())
for _ in range(m):
    num = int(si().rstrip())
    chk[num] = 1

ans = 1
cnt = 0
for i in range(1, n+1):
    if chk[i] == 0:
        cnt += 1
    else:
        if cnt > 0:
            ans *= dp[cnt]
        cnt = 0
if cnt > 0:
    ans *= dp[cnt]

print(ans)