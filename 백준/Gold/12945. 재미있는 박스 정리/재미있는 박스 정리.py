import sys
from collections import deque
from bisect import bisect_left, bisect_right
si = sys.stdin.readline

n = int(si().rstrip())

boxes = []
for _ in range(n):
	boxes.append(int(si().rstrip()))


ans = 0
boxes.sort()
l = 0
r = n // 2
while l < n // 2 and r < n:
	if boxes[l] * 2 <= boxes[r]:
		ans += 1
		l += 1
	r += 1
print(n - ans)