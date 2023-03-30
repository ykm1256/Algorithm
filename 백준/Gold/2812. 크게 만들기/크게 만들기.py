import sys
si = sys.stdin.readline


N, K = map(int, si().split())

num = list(map(int, si().rstrip()))

ans = []

def search(s, e, m):
	maxValue = m
	index = 0
	for i in range(s, e):
		if num[i] > maxValue:
			maxValue = num[i]
			index = i
	
	return index

for i in range(N):
	if not ans:
		ans.append(num[i])
		continue
	while K > 0:
		if ans and ans[-1] < num[i]:
			ans.pop()
			K -= 1
		else:
			break
	ans.append(num[i])
while K > 0:
	ans.pop()
	K -= 1
print(*ans, sep="")