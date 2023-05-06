import sys, bisect
from collections import deque
from bisect import bisect_left

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
	if not answer or answer[-1] < lines[i][1]:
		answer.append(lines[i][1])
	elif lines[i][1] < answer[-1]:
		answer[bisect_left(answer, lines[i][1])] = lines[i][1]

print(n-len(answer))