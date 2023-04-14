import sys, heapq
from collections import deque
si = sys.stdin.readline

s = int(si().rstrip())

# 화면에 1개있음
# 화면 -> 클립보드
# 클립보드 -> 화면 +1

ans = float('inf')
queue = []
# 화면에 있는 이모티콘
# time, num, clipboard
queue.append((0, 1, 0))

dp = [[float('inf') for _ in range(1001)] for _ in range(1001)]
dp[0][0] = 0
dp[1][0] = 0
ans = 0

while queue:
    time, num, clip = heapq.heappop(queue)

    # 클립보드에 있는 거 그대로 붙여넣기
    tmp = num + clip
    if tmp <= 1000 and dp[tmp][clip] > time + 1:
        dp[tmp][clip] = time + 1
        if tmp == s:
            ans = time+1
            break
        queue.append((time+1, tmp, clip))
    # 하나 삭제
    tmp = num - 1
    if dp[tmp][clip] > time+1:
        dp[tmp][clip] = time+1
        queue.append((time+1, tmp, clip))

    # 클립보드로 복사
    if num > clip and dp[num][num] > time + 1:
        queue.append((time+1, num, num))

print(ans)