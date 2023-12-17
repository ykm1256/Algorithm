import sys
sys.setrecursionlimit(10**9)

si = sys.stdin.readline

N = int(si().rstrip())
popul = list(map(int, si().split()))

graph = [[] for _ in range(N)]

dp = [[0 for _ in range(2)] for _ in range(N)]
chk = [False for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, si().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def recur(node):
    chk[node] = True
    dp[node][0] = 0
    dp[node][1] = popul[node]

    for next in graph[node]:
        if chk[next]:
            continue
        recur(next)
        dp[node][0] += max(dp[next][0], dp[next][1])
        dp[node][1] += dp[next][0]

recur(0)
print(max(dp[0][0], dp[0][1]))