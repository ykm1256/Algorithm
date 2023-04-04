import sys
si = sys.stdin.readline

n = int(si().rstrip())

lines = []
stars = []
parents = [i for i in range(n)]
for i in range(n):
    stars.append(list(map(float, si().split())))

def calLength(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

for i in range(n-1):
    for j in range(i,n):
        length = calLength(stars[i][0], stars[i][1], stars[j][0], stars[j][1])
        lines.append((length, i, j))

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa < pb:
        parents[pb] = pa
    else:
        parents[pa] = pb

lines.sort()

ans = 0
for l, a, b in lines:
    if find(a) != find(b):
        ans += l
        union(a,b)
print(round(ans,2))