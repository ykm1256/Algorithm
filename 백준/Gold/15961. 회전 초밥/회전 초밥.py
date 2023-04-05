import sys
si = sys.stdin.readline

n, d, k, c = map(int, si().split())
sushi = []
for _ in range(n):
    sushi.append(int(si().rstrip()))

chk = [0 for _ in range(3001)]

cnt = 0
for i in range(k):
    if chk[sushi[i]] == 0:
        cnt += 1
    chk[sushi[i]] += 1

ans = cnt
if chk[c] == 0:
    ans += 1

for i in range(1, n):
    e = i + k - 1

    if e >= n:
        e %= n

    chk[sushi[i-1]] -= 1
    if chk[sushi[i-1]] == 0:
        cnt -= 1
    
    if chk[sushi[e]] == 0:
        cnt += 1
    chk[sushi[e]] += 1

    if cnt >= ans:
        if chk[c] == 0:
            ans = cnt + 1
        else:
            ans = cnt

print(ans)