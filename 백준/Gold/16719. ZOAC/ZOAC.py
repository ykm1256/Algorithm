import sys
from collections import deque
si = sys.stdin.readline


alpha = list(si().rstrip())

chk = [0 for _ in range(len(alpha))]

def dfs(l, r):
	minAlpha = float('inf')
	idx = 0
	for i in range(l, r+1):
		if chk[i] == 0 and minAlpha > ord(alpha[i]):
			minAlpha = ord(alpha[i])
			idx = i
	
	if minAlpha == float('inf'):
		return
	
	chk[idx] = 1
	for i in range(len(alpha)):
		if chk[i] == 1:
			print(alpha[i], end="")
	
	print("")
	dfs(idx+1, r)
	dfs(l, idx-1)

dfs(0, len(alpha)-1)