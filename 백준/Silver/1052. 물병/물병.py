import sys
si = sys.stdin.readline

n, k = map(int, si().split())
num = bin(n)[2:]

cnt = 0

ans = 0
for i in range(len(num)):
    if num[i] == '1':
        cnt += 1
    
    if cnt == k:
        d = n % (2**(len(num) - i - 1))
        if d != 0:
            ans = 2**(len(num) - i - 1) - d
        break

print(ans)