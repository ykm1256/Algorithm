import sys
si = sys.stdin.readline

m,n,l = map(int, si().split())
pos = list(map(int,si().split()))

animals = []
ans = 0

for _ in range(n):
	x, y = map(int, si().split())
	if y <= l:
		animals.append((x,y))


for i in range(m):
	cnt = 0
	length = len(animals)

	while cnt < length:
		x, y = animals.pop(0)
		if abs(pos[i] - x) + y <= l:
			ans += 1
		else:
			animals.append((x,y))
		
		cnt += 1

print(ans)