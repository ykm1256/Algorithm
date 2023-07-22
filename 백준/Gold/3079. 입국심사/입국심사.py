import sys
si = sys.stdin.readline

n,m = map(int, si().split())
times = [0 for _ in range(n)]

for i in range(n):
	times[i] = int(si().rstrip())

l = min(times)
r = max(times) * m
ans = r

while l <= r:
	people = 0
	mid = (l+r) // 2

	for i in range(n):
		people += mid // times[i]
	
	if people >= m:
		r = mid - 1
		ans = min(mid, ans)
	else:
		l = mid + 1

print(ans)