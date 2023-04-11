import sys

si = sys.stdin.readline
n = int(si().rstrip())
x = []
y = []
answer = 0

for _ in range(n):
	a, b = map(int, si().split())
	x.append(a)
	y.append(b)
x.append(x[0])
y.append(y[0])

for i in range(n):
	answer += x[i] * y[i+1]
	answer -= y[i] * x[i+1]
print(round(abs(answer) / 2, 1))