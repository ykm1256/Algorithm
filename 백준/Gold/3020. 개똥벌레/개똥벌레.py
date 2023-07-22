import sys
si = sys.stdin.readline

n, h = map(int, si().split())

bottom = [0 for _ in range(h+1)]
top = [0 for _ in range(h+1)]

for i in range(n):
	o = int(si().rstrip())
	if i % 2 == 0:
		bottom[o] += 1
	else:
		top[o] += 1

for i in range(h-1, 0, -1):
	bottom[i] += bottom[i+1]
	top[i] += top[i+1]

minValue = n
answer = 0

for i in range(1, h+1):
	if minValue > bottom[i] + top[h-i+1]:
		minValue = bottom[i] + top[h-i+1]
		answer = 1
	elif minValue == bottom[i] + top[h-i+1]:
		answer += 1

print(minValue, answer)