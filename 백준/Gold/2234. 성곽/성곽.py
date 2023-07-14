import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

M, N  = map(int, si().split())

castle = []

for _ in range(N):
	castle.append(list(map(int, si().split())))

cnts = []
chk = [[0 for _ in range(M)] for _ in range(N)]

def dfs(x, y, no):
	global N, M

	cnts[no-1] += 1
	for i in range(4):
		flag = 2**i
		if castle[y][x] & flag == 0:
			dy = y
			dx = x
			if flag == 1:
				dx = x - 1
			elif flag == 2:
				dy = y - 1
			elif flag == 4:
				dx = x + 1
			else:
				dy = y + 1
			
			if dx < 0 or dx >= M or dy < 0 or dy >= N or chk[dy][dx] == 1:
				continue
			chk[dy][dx] = 1
			dfs(dx, dy, no)

	castle[y][x] = no * -1

no = 0

for i in range(N):
	for j in range(M):
		if castle[i][j] > 0 and chk[i][j] == 0:
			cnts.append(0)
			no += 1
			chk[i][j] = 1
			dfs(j, i, no)

ans = max(cnts)
offset = [[0,1],[1,0], [-1,0] ,[0,-1]]
for i in range(N):
	for j in range(M):
		for idx in range(4):
			di = i + offset[idx][0]
			dj = j + offset[idx][1]

			if di < 0 or di >= N or dj < 0 or dj >= M:
				continue
			if castle[i][j] != castle[di][dj]:
				ans = max(ans, cnts[castle[i][j]*-1 - 1] + cnts[castle[di][dj]*-1 - 1])

print(no)
print(max(cnts))
print(ans)