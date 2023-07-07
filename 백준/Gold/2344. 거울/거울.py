import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

n, m = map(int, si().split())

box = [[0 for _ in range(m+2)] for _ in range(n+2)]

for i in range(1, n+1):
	tmp = list(map(int, si().split()))
	for j in range(1, m+1):
		box[i][j] = tmp[j-1]

cnt = 1

for i in range(1, n+1):
	box[i][0] = cnt
	cnt += 1
for j in range(1, m+1):
	box[n+1][j] = cnt
	cnt += 1
for i in range(n, 0, -1):
	box[i][m+1] = cnt
	cnt += 1
for j in range(m, 0, -1):
	box[0][j] = cnt
	cnt += 1

offset = [[0,1],[-1,0],[0,-1],[1,0]]

def direction(d):
	if d == 0:
		return d+1
	elif d == 1:
		return d-1
	elif d == 2:
		return d+1
	else:
		return d-1

# 좌표, 방향
def dfs(x, y, d):
	global n
	if x == 0 or y == 0 or x == m+1 or y == n+1:
		return box[y][x]
	
	if box[y][x] == 1:
		d = direction(d)
	
	dx = x + offset[d][1]
	dy = y + offset[d][0]
	return dfs(dx, dy, d)

ans = []
for i in range(1, n+1):
	ans.append(dfs(1, i, 0))

for j in range(1, m+1):
	ans.append(dfs(j, n, 1))

for i in range(n, 0, -1):
	ans.append(dfs(m, i, 2))

for j in range(m, 0, -1):
	ans.append(dfs(j, 1, 3))

print(*ans)