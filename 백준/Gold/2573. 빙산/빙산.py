import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

n, m = map(int, si().split())

sea = []

for _ in range(n):
	sea.append(list(map(int, si().split())))
chk = [arr[:] for arr in sea]

offset = [[0,1],[0,-1],[-1,0],[1,0]]

def fill(n, m):
	tmp = [arr[:] for arr in sea]
	flag = False
	for i in range(1, n-1):
		for j in range(1, m-1):
			if sea[i][j] != 0:
				flag = True
				for idx in range(4):
					di = i + offset[idx][0]
					dj = j + offset[idx][1]
					if sea[di][dj] == 0 and tmp[i][j] > 0:
						tmp[i][j] -= 1
	if flag:
		return tmp
	else:
		return None

def dfs(x, y):
	for i in range(4):
		dx = x + offset[i][1]
		dy = y + offset[i][0]
		if dx < 1 or dx >= m-1 or dy < 1 or dy >= n-1 or chk[dy][dx] == 0:
			continue
		chk[dy][dx] = 0
		dfs(dx, dy)

def check(n, m):
	global chk
	cnt = 1
	chk = [arr[:] for arr in sea]

	for i in range(1,n-1):
		for j in range(1, m-1):
			if chk[i][j] != 0:
				chk[i][j] = 0
				if cnt > 1:
					return True
				dfs(j, i)
				cnt += 1
	return False

ans = 0
while True:
	ans += 1
	sea = fill(n, m)
	if sea == None:
		ans = 0
		break

	if check(n, m):
		break

print(ans)