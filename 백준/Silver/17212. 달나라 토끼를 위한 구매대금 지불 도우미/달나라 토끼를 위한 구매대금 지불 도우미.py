import sys
si = sys.stdin.readline

money = int(si().rstrip())

dp = [float('inf') for _ in range(money+1 if money+1 >= 8 else 8)]

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1

for i in range(8, money+1):
        dp[i] = min(dp[i], dp[i-7] + 1, dp[i-5]+1, dp[i-2] + 1, dp[i-1] + 1)

print(dp[money])