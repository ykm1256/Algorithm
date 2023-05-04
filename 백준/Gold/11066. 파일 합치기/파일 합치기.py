import sys
si = sys.stdin.readline

T = int(si().rstrip())

for _ in range(T):
	k = int(si().rstrip())
	a = list(map(int, si().split()))
	s = [0 for _ in range(k+1)]
	for i in range(1, k+1):
		s[i] = s[i-1] + a[i-1]
	dp = [[0 for _ in range(k+1)] for _ in range(k+1)]

	for i in range(2, k+1):
		for j in range(1, k+2-i):
			dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (s[j+i-1] - s[j-1])
	
	print(dp[1][-1])