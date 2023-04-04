import sys, heapq
si = sys.stdin.readline

T = int(si().rstrip())
for _ in range(T):
    k = int(si().rstrip())

    novel = list(map(int,si().split()))
    heapq.heapify(novel)

    ans = 0
    while novel:
        res = heapq.heappop(novel)
        if not novel:
            break
        res += heapq.heappop(novel)
        ans += res
        heapq.heappush(novel, res)
    print(ans)