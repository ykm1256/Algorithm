import sys
si = sys.stdin.readline

characters = list(si().rstrip())
goal = list(si().rstrip())

cnt = len(characters)
MOD = 900528
l = len(goal)
ans = 0

dic = dict()
for idx in range(len(characters)):
    dic[characters[idx]] = idx+1

g = 1
for i in range(l-1, -1, -1):
    num = dic[goal[i]]
    ans = (ans + g*num) % MOD
    g = (g*cnt) % MOD

print(ans)