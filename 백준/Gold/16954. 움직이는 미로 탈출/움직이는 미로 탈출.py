import sys
si = sys.stdin.readline

graph = []

for _ in range(8):
	graph.append(list(si().rstrip()))

queue = []
# 좌표, 시간
chk = [[[0 for _ in range(8)] for _ in range(8)] for _ in range(10)]
offset = [[0,1], [0,-1], [1,0], [-1,0], [1, 1], [-1, -1], [1, -1], [-1, 1], [0,0]]

queue.append((7, 0, 0))
chk[0][7][0] = 1
ans = 0

while queue:
	y, x, t = queue.pop(0)
	if y - t >= 0 and graph[y-t][x] == '#':
		continue
	if y - t < 0:
		ans = 1
		break


	for i in range(9):
		dy = y + offset[i][0]
		dx = x + offset[i][1]
		if dy < 0 or dy >= 8 or dx < 0 or dx >= 8 or chk[t+1][dy][dx] == 1:
			continue

		if dy - t >= 0 and graph[dy-t][dx] == '#':
			continue
		if dy == 0 and dx == 7:
			ans = 1
			queue.clear()
		chk[t+1][dy][dx] = 1
		queue.append((dy, dx, t+1))

print(ans)