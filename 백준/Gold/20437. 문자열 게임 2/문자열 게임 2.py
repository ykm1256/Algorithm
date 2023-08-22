import sys
si = sys.stdin.readline

T = int(si().rstrip())

for _ in range(T):
	s = si().rstrip()
	w = int(si().rstrip())
	
	cnts = [0 for _ in range(26)]
	indexes = [[] for _ in range(26)]
	for i in range(len(s)):
		idx = ord(s[i]) - ord('a')
		
		cnts[idx] += 1
		indexes[idx].append(i)
	
	max_l = 0
	min_l = float('inf')


	for i in range(26):
		if cnts[i] < w:
			continue
		for j in range(cnts[i] - w + 1):
			cnt = indexes[i][j+w-1] - indexes[i][j] + 1
			max_l = max(max_l, cnt)
			min_l = min(min_l, cnt)
	
	if max_l == 0:
		print(-1)
	else:
		print(min_l, max_l)