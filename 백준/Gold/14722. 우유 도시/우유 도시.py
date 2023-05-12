import sys
input = sys.stdin.readline
 
n = int(input())
# dp와 동일한 모양을 맞춰주기 위함
graph = [[-1] * n]  + [list(map(int, input().split())) for _ in range(n)]
for i in range(n+1):
    graph[i].insert(0, -1)
 
dp = [[0] * (n+1) for _ in range(n+1)]
 
for i in range(1, n+1):
    for j in range(1, n+1):
        # 위쪽과 좌측 중에서, 가장 높은 값을 가져가기
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
 
        # 현재 쌓인 우유 % 3이라면. 즉, 다음에 마셔야 할 우유라면 하나를 증가
        if dp[i][j] % 3 == graph[i][j]:
            dp[i][j] += 1
 
print(dp[-1][-1])