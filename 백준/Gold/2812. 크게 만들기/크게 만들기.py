import sys
si = sys.stdin.readline

N, K = map(int, si().split())

num = list(map(int, si().rstrip()))

ans = []

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