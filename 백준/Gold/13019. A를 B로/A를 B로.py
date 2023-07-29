import sys
si = sys.stdin.readline

A = si().rstrip()
B = si().rstrip()

flag = True
ans = 0
if sorted(A) != sorted(B):
	ans = -1
	flag = False

idx = len(A) - 1
if idx == 0:
	if A == B:
		ans = 0
		flag = False
	else:
		ans = -1
		flag = False

if flag:
	for i in range(len(A)-1,-1,-1):
		if A[i] != B[idx]:
			ans += 1
		else:
			idx -= 1
print(ans)