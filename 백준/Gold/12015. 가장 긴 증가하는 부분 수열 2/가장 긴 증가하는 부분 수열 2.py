import sys
from bisect import bisect_left

si = sys.stdin.readline
n = int(si().rstrip())
a = list(map(int, si().split()))
answer = []

for i in range(n):
	if not answer or answer[-1] < a[i]:
		answer.append(a[i])
	elif a[i] < answer[-1]:
		answer[bisect_left(answer, a[i])] = a[i]

print(len(answer))