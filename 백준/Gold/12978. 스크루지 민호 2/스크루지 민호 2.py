import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(si().rstrip())

city = [[] for _ in range(n+1)]

for _ in range(n-1):
	a,b = map(int,si().split())
	city[a].append(b)
	city[b].append(a)

dp = [[0,0] for _ in range(1000001)]
chk = [0 for _ in range(1000001)]

def find(node):
	chk[node] = 1
	dp[node][0] = 1
	for child in city[node]:
		if chk[child] == 1:
			continue
		find(child)
		dp[node][1] += dp[child][0]
		dp[node][0] += min(dp[child][1], dp[child][0])

find(1)

print(min(dp[1][0], dp[1][1]))