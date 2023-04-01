import sys
si = sys.stdin.readline

G = int(si().rstrip())
P = int(si().rstrip())
g = []
for _ in range(P):
    g.append(int(si().rstrip()))

parents = [i for i in range(G+1)]
ans = 0

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    parents[parent_a] = parent_b

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

for plane in g:
    d = find(plane)
    if d == 0:
        break
    union(d, d-1)
    ans += 1

print(ans)