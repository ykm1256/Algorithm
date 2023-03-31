import sys
si = sys.stdin.readline

n = int(si().strip())

a = list(map(int, si().split()))
dp = [1 for _ in range(n)]

dp[0] = 1
for i in range(1, n):
	cnt = 0
	for j in range(i):
		if a[j] < a[i]:
			if cnt < dp[j]:
				cnt = dp[j]
	dp[i] = cnt + 1
print(max(dp))