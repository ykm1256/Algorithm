import sys, bisect
si = sys.stdin.readline

n, m = map(int, si().split())

a = []
for _ in range(n):
    a.append(int(si().rstrip()))

b = sorted(a)
answer = []

for _ in range(m):
    ans = -1
    num = int(si().rstrip())
    idx = bisect.bisect_left(b, num)
    if idx < n and b[idx] == num:
        ans = idx
    answer.append(ans)

print(*answer, sep="\n")