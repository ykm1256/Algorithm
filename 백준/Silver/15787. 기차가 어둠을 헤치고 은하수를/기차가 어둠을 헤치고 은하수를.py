import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())

order = []
for _ in range(m):
	order.append(list(map(int, si().split())))

ans = set()

train = [deque([0 for _ in range(20)]) for _ in range(n)]

for o in order:
	if o[0] == 1:
		train[o[1]-1][o[2]-1] = 1
	elif o[0] == 2:
		train[o[1]-1][o[2]-1] = 0
	elif o[0] == 3:
		train[o[1]-1].appendleft(0)
		train[o[1]-1].pop()
	else:
		train[o[1]-1].append(0)
		train[o[1]-1].popleft()

for i in range(n):
	flag = 0
	for j in range(20):
		if train[i][j] == 1:
			flag = flag | (1 << j)
	ans.add(flag)

print(len(ans))