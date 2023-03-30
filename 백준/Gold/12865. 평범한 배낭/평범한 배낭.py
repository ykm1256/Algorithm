import sys
si = sys.stdin.readline

n, k = map(int, si().split())

things = [0]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for _ in range(n):
	w, v = map(int, si().split())
	things.append((w,v))

for i in range(1, n+1):
	w, v = things[i]
	for j in range(1, k+1):
		if j < w:
			dp[i][j] = dp[i-1][j]
		elif j == w:
			dp[i][j] = max(dp[i-1][j], v)
		else:
			dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[-1][-1])