import sys
from collections import defaultdict
si = sys.stdin.readline

n = int(si().rstrip())

H = list(map(int,si().split()))
A = list(map(int,si().split()))

chk = defaultdict()


A.sort()
ans = 0
ans += sum(H)
for i in range(n):
    ans += A[i] * i
print(ans)