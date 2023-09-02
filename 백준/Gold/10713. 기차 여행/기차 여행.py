import sys
si = sys.stdin.readline

n, m = map(int, si().split())

plan = list(map(int, si().split()))

cost = [list(map(int, si().split())) for _ in range(n-1)]

cnt = [0 for _ in range(n+1)]

for i in range(m-1):
	if plan[i] < plan[i+1]:
		cnt[plan[i]] += 1
		cnt[plan[i+1]] -= 1
	else:
		cnt[plan[i+1]] += 1
		cnt[plan[i]] -= 1
	
s = 0
ans = 0

for i in range(n-1):
	s += cnt[i+1]
	ans += min(cost[i][0] * s, cost[i][1] * s + cost[i][2])
print(ans)