import sys

si = sys.stdin.readline

N,M,K = map(int, si().split())

dp = [[1 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[N][M] < K:
    print(-1)
else:
    answer = ""

    while N > 0 and M > 0:
        idx = dp[N-1][M]

        if K <= idx:
            N -= 1
            answer += 'a'
        else:
            M -= 1
            K -= idx
            answer += 'z'
    answer += ('a' * N) + ('z' * M)
    print(answer)