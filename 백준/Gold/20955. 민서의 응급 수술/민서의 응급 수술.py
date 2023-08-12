import sys
si = sys.stdin.readline

n, m = map(int, si().split())

parents = list(range(n+1))

def find(x):
	if x != parents[x]:
		parents[x] = find(parents[x])
	return parents[x]

def union(a, b):
	pa = find(a)
	pb = find(b)
	if pa == pb:
		return True
	if pa < pb:
		parents[pb] = pa
	elif pa > pb:
		parents[pa] = pb
	return False

cnt = 0
for _ in range(m):
	u, v = map(int, si().split())
	if union(u, v):
		cnt += 1

for i in range(1, n+1):
	if find(i) == i:
		cnt += 1

print(cnt - 1)