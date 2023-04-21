import sys
si = sys.stdin.readline

n = int(si().rstrip())
negative = []
positive = []

for _ in range(n):
    num = int(si().rstrip())
    if num <= 0:
        negative.append(num)
    elif num > 0:
        positive.append(num)


negative.sort()
positive.sort(reverse=True)
ans = 0

res = 0
idx = 1
while idx < len(negative):
    if negative[idx] * negative[idx-1] >= 0:
        res += negative[idx] * negative[idx-1]
        idx += 2
if len(negative) % 2 == 1:
    res += negative[len(negative) - 1]
ans += res

res = 0
idx = 1
while idx < len(positive):
    if positive[idx] != 1 and  positive[idx-1] != 1:
        res += positive[idx] * positive[idx-1]
    else:
        res += positive[idx] + positive[idx-1]
    idx += 2
if len(positive) % 2 == 1:
    res += positive[len(positive) - 1]
ans += res

print(ans)