import sys

si = sys.stdin.readline

str = list(si().rstrip())


cnt = 0
for i in range(len(str)):
    if str[i] == 'b':
        cnt += 1


b = 0
for i in range(0, cnt):
    if str[i] == 'b':
        b += 1

maxB = b
for s in range(1, len(str)):
    if str[s-1] == 'b':
        b -= 1
    if str[(s + cnt - 1)%len(str)] == 'b':
        b += 1
    
    maxB = max(maxB, b)

print(cnt - maxB)