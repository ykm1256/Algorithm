import sys
si = sys.stdin.readline

tc = 1
while True:
    n = int(si().rstrip())
    if n == 0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, si().split())))
    dp = [[float('inf'), graph[0][1], graph[0][1] + graph[0][2]]]
    for i in range(1, n):
        tmp = []
        for j in range(3):
            if j == 0:
                val = min(dp[i-1][0], dp[i-1][1])
            elif j == 1:
                val = min(dp[i-1][0], dp[i-1][1], dp[i-1][2])
            else:
                val = min(dp[i-1][1], dp[i-1][2])
            val += graph[i][j]
            tmp.append(val)
        tmp[1] = min(tmp[1], tmp[0] + graph[i][1])
        tmp[2] = min(tmp[2], tmp[1] + graph[i][2])
        dp.append(tmp)
    print(str(tc) + ".", dp[-1][1])
    tc += 1