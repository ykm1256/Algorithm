import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

w, h = map(int, si().split())
board = []
for _ in range(h):
	board.append(list(map(int, si().split())))

# 위, 아랫줄 건물 끝은 2개 고정

# -1,-1 0,-1
#홀
offset_odd = [[-1,-1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]
#짝
offset_even = [[1,1], [1,0], [0,-1], [-1,0], [-1, 1], [0, 1]]
ans = 0

def dfs(i, j):
	for idx in range(6):
		if i % 2 == 0:
			di = i + offset_even[idx][0]
			dj = j + offset_even[idx][1]
		else:
			di = i + offset_odd[idx][0]
			dj = j + offset_odd[idx][1]

		if di < 0 or di >= h or dj < 0 or dj >= w:
			continue
		if board[di][dj] == 0:
			board[di][dj] = 2
			dfs(di,dj)

		
for i in range(h):
	for j in range(w):
		if board[i][j] == 0:
			for idx in range(6):
				if i % 2 == 0:
					di = i + offset_even[idx][0]
					dj = j + offset_even[idx][1]
				else:
					di = i + offset_odd[idx][0]
					dj = j + offset_odd[idx][1]
				if di < 0 or di >= h or dj < 0 or dj >= w:
					board[i][j] = 2
					dfs(i, j)
					break



for i in range(h):
	for j in range(w):
		if board[i][j] == 1:
			cnt = 0
			for idx in range(6):
				if i % 2 == 0:
					di = i + offset_even[idx][0]
					dj = j + offset_even[idx][1]
				else:
					di = i + offset_odd[idx][0]
					dj = j + offset_odd[idx][1]
				
				# 왼쪽 or 오른쪽 끝이면 홀 
				if di < 0 or di >= h or dj < 0 or dj >= w:
					cnt += 1
				elif board[di][dj] == 2:
					cnt += 1
			# print('(' + str(j+1) + ',' + str(i+1) + ')' + '결과 : ' + str(cnt))
			ans += cnt
print(ans)