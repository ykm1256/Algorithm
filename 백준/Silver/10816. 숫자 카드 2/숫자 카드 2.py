import sys
from bisect import bisect_left, bisect_right

si = sys.stdin.readline
N = int(si().rstrip())
a = list(map(int, si().split()))
a.sort()
M = int(si().rstrip())
m = list(map(int, si().split()))
answer = []

for num in m:
	start = bisect_left(a, num)
	end = bisect_right(a, num)
	cnt = 0
	if start < N and a[start] == num:
		cnt += end - start
	answer.append(cnt)

print(*answer)