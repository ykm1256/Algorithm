import sys, heapq
from collections import deque
si = sys.stdin.readline

def recur(now, n, money):
	global ans
	if now == n:
		ans = "Yes"
		return
	
	idx = 2
	while True:
		next = int(room[now][idx])
		if next == 0:
			break
		if chk[next] == 1:
			idx += 1
			continue

		if room[next][0] == 'T':
			if int(room[next][1]) <= money:
				chk[next] = 1
				recur(next, n, int(room[next][1]) - money)
				chk[next] = 0
		elif room[next][0] == 'L':
			chk[next] = 1
			if int(room[next][1]) > money:
				recur(next, n, int(room[next][1]))
			else:
				recur(next, n, money)
			chk[next] = 0
		else:
			chk[next] = 1
			recur(next, n, money)
			chk[next] = 0
		idx += 1
		if ans == "Yes":
			return



while True:
	n = int(si().rstrip())
	if n == 0:
		break
		
	room = [[]]
	for _ in range(n):
		room.append(list(si().split()))
	ans = "No"
	
	chk = [0 for _ in range(n+1)]
	recur(1, n, 0)	

	print(ans)