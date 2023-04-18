import sys
from bisect import bisect_left
from collections import deque

si = sys.stdin.readline
n = int(si().rstrip())
a = list(map(int, si().split()))

tmp = []
idx = []
answer = deque()
l = 0


for i in range(n):
	if not tmp or tmp[-1] < a[i]:
		tmp.append(a[i])
		idx.append(l)
		l += 1
	else:
		pos = bisect_left(tmp, a[i])
		tmp[pos] = a[i]
		idx.append(pos)

l = len(tmp)-1
for i in range(n-1, -1, -1):
	if idx[i] == l:
		answer.appendleft(a[i])
		l -= 1

print(len(tmp))
print(*answer)