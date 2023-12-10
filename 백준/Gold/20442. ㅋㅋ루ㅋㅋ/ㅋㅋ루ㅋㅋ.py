import sys
si = sys.stdin.readline

s = si().rstrip()

l = len(s)
cntK = 0
leftK = []
rightK = []
for i in range(l):
    if s[i] == 'K':
        cntK += 1
    else:
        leftK.append(cntK)

cntK = 0
for i in range(l-1, -1, -1):
    if s[i] == 'K':
        cntK += 1
    else:
        rightK.append(cntK)
rightK.sort(reverse=True)

s = 0
e = len(rightK) - 1
answer = 0

while s <= e:
    answer = max(answer, (e-s+1) + (2*min(leftK[s], rightK[e])))

    if leftK[s] < rightK[e]:
        s += 1
    else:
        e -= 1

print(answer)