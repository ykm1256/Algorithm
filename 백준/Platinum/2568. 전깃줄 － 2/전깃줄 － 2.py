import sys, bisect
from collections import deque

si = sys.stdin.readline

n = int(si().rstrip())
lines = []
tmp = []
idx = []
l = 0
answer = deque()
for _ in range(n):
	s, e = map(int, si().split())
	lines.append((s, e))

lines.sort()

for i in range(n):
	if not tmp or tmp[-1] < lines[i][1]:
		tmp.append(lines[i][1])
		idx.append(l)
		l += 1
	else:
		pos = bisect.bisect_left(tmp, lines[i][1])
		tmp[pos] = lines[i][1]
		idx.append(pos)

l = len(tmp)-1
for i in range(n-1, -1, -1):
	if idx[i] == l:
		l -= 1
	else:
		answer.appendleft(lines[i][0])

print(n-len(tmp))
for i in range(len(answer)):
	print(answer[i])