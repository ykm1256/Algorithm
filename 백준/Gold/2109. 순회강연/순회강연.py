import sys, heapq
si = sys.stdin.readline

n = int(si().rstrip())
l = []
parents = [i for i in range(10001)]

for _ in range(n):
    money, d = map(int, si().split())
    heapq.heappush(l, (-money, d))

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

ans = 0
while l:
    money, d = heapq.heappop(l)
    p = find(d)
    if p == 0:
        continue
    elif p == d:
        parents[d] = d-1
    else:
        parents[p] = p-1
    ans -= money

print(ans)