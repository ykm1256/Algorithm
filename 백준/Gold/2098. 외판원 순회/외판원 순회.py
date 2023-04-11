import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(si().rstrip())

w = []
dp = [[-1 for _ in range(1 << n)] for _ in range(n)]
for _ in range(n):
    w.append(list(map(int, si().split())))


def dfs(now, flag):
    if flag == ((1 << n) - 1):
        if w[now][0] == 0:
            return float('inf')
        return w[now][0]

    if dp[now][flag] != -1:
        return dp[now][flag]
    
    dp[now][flag] = float('inf')
    for i in range(n):
        if (flag & (1 << i)) == 0 and w[now][i] > 0:
            dp[now][flag] = min(dp[now][flag], w[now][i] + dfs(i, flag | 1 << i))

    return dp[now][flag]

print(dfs(0, 1))