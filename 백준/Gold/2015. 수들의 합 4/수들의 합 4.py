import sys
from collections import defaultdict
si = sys.stdin.readline

N, K = map(int, si().split())
sums = [0 for _ in range(N)]

A = list(map(int, si().split()))

dic = defaultdict(int)
sums[0] = A[0]
answer = 0
for i in range(N):
    sums[i] = sums[i-1] + A[i]

for i in range(N):
    if sums[i] == K:
        answer += 1
    answer += dic[sums[i] - K]
    dic[sums[i]] += 1

print(answer)