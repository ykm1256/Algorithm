import sys
si = sys.stdin.readline

N = int(si().rstrip())

snack = []
dp = []

for _ in range(N):
    num = int(si().rstrip())
    snack.append(num)
    dp.append(num)

ans = 0

for i in range(N):
    for j in range(i):
        if snack[i] > snack[j] and dp[j] + snack[i] > dp[i]:
            dp[i] = dp[j] + snack[i]
    ans = max(ans, dp[i])

print(ans)