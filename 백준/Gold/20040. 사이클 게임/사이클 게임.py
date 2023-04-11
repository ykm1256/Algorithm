import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, si().split())

parents = [i for i in range(n)]

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return True

    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    
    return False

answer = 0
for i in range(m):
    a, b = map(int, si().split())
    if union(a, b):
        answer = i+1
        break

print(answer)