import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m,r = map(int,input().split())

x = [[]*(n+1) for _ in range(n+1)]
visisted = [False] * (n+1)

y = [0] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    x[a].append(b)
    x[b].append(a)


for i in range(n+1):
    x[i].sort()

idx = 1

def dfs(start):
    global idx
    
    visisted[start] = True
    y[start] = idx
    for next in x[start]:
        if visisted[next] == False:
            idx += 1
            dfs(next)

dfs(r)

for i in range(1,n+1):
    print(y[i])