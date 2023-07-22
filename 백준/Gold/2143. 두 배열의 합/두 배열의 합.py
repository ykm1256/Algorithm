import sys
from bisect import bisect_left, bisect_right

si = sys.stdin.readline

ans = 0
t = int(si().rstrip())

n = int(si().rstrip())
a = list(map(int,si().split()))
m = int(si().rstrip())
b = list(map(int,si().split()))

dpa = []
dpb = []

for i in range(n):
    res = a[i]
    dpa.append(res)
    for j in range(i+1, n):
        res += a[j]
        dpa.append(res)

for i in range(m):
    res = b[i]
    dpb.append(res)
    for j in range(i+1, m):
        res += b[j]
        dpb.append(res)

dpa.sort()
dpb.sort()

idx = 0
while idx < len(dpa):
    o = t - dpa[idx]
    s, e = bisect_left(dpa, dpa[idx]), bisect_right(dpa, dpa[idx])
    ans += (bisect_right(dpb, o) - bisect_left(dpb, o)) * (e-s)
    idx = e


print(ans)

